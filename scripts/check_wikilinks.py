#!/usr/bin/env python3
"""Check repository Markdown links, localized targets, anchors, and orphans.

Default invocation is a non-blocking migration report. Use ``--strict`` for the
final repository contract.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Set, Tuple
from urllib.parse import unquote

from wiki_quality_common import (
    LOCALE_SUFFIX_RE,
    Diagnostic,
    WikiPage,
    exit_code,
    line_number,
    load_wiki_pages,
    markdown_files,
    parse_frontmatter,
    print_report,
    read_migration_map,
    repo_relative,
    severity,
)


DEFAULT_SCAN_ENTRIES = (
    "README.md",
    "index.md",
    "wiki",
    "docs",
    "skills",
    "instruments",
    "biblical-compatibility",
    ".opencode/agents",
    ".opencode/ORGANIZATION.md",
)
WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]\n]*)\]\(([^)\n]+)\)")
FENCE_RE = re.compile(r"(^|\n)([ \t]*)(`{3,}|~{3,}).*?\n.*?\n\2\3[ \t]*(?=\n|$)", re.DOTALL)
INLINE_CODE_RE = re.compile(r"(`+)(?!`)(.+?)\1", re.DOTALL)
SECTION_RE = re.compile(r"<!--\s*section:([a-z0-9][a-z0-9._-]*)\s*-->", re.IGNORECASE)
EXPLICIT_ANCHOR_RE = re.compile(r"<(?:a|[^>]+\sid)\s+[^>]*?id=[\"']([^\"']+)[\"'][^>]*>", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)

DELETED_SLUGS = {
    "scientific-contribution-statement",
    "common-projects",
    "llm-psychological-simulators-methodology",
    "s-researcher-llm-social-scientists",
    "ai-agents-psychometric-approach",
    "llm-emulate-personality-nature-2025",
    "ai-experiment-participants",
    "project-main-goal",
    "research-layer-vs-practical-guidance",
    "hypothesis-status-of-before-we-build",
    "limits-of-typological-inference",
    "typology-full-description",
    "weight-calibration",
    "research-program",
    "music-style-catalog-and-psychosophy-emotion",
    "psychosophy-model",
}


@dataclass(frozen=True)
class Link:
    raw: str
    target: str
    anchor: str | None
    label: str | None
    line: int
    kind: str
    cross_language_allowed: bool = False


def _mask_code(text: str) -> str:
    def blank(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group(0))

    return INLINE_CODE_RE.sub(blank, FENCE_RE.sub(blank, text))


def _split_target(value: str) -> tuple[str, str | None]:
    value = unquote(value.strip())
    if value.startswith("<") and ">" in value:
        value = value[1 : value.index(">")]
    elif " " in value:
        value = value.split(None, 1)[0]
    if "#" in value:
        target, anchor = value.split("#", 1)
        return target, anchor or None
    return value, None


def extract_links(text: str) -> list[Link]:
    masked = _mask_code(text)
    links: list[Link] = []
    lines = text.splitlines()
    for match in WIKILINK_RE.finditer(masked):
        inside = match.group(1).strip()
        if "|" in inside:
            target_part, label = inside.split("|", 1)
        else:
            target_part, label = inside, None
        target, anchor = _split_target(target_part)
        number = line_number(masked, match.start())
        source_line = lines[number - 1] if number <= len(lines) else ""
        allowed = _cross_language_allowed(label, source_line)
        links.append(Link(match.group(0), target, anchor, label, number, "wikilink", allowed))
    for match in MARKDOWN_LINK_RE.finditer(masked):
        label, raw_target = match.group(1), match.group(2)
        target, anchor = _split_target(raw_target)
        number = line_number(masked, match.start())
        source_line = lines[number - 1] if number <= len(lines) else ""
        allowed = _cross_language_allowed(label, source_line)
        links.append(Link(match.group(0), target, anchor, label, number, "markdown", allowed))
    return sorted(links, key=lambda item: (item.line, item.raw))


def extract_wikilinks(content: str) -> Set[str]:
    """Backward-compatible helper used by earlier local tooling."""
    return {match.group(1) for match in WIKILINK_RE.finditer(_mask_code(content))}


def wikilink_to_filename(wikilink: str) -> str:
    target = wikilink.split("|", 1)[0].split("#", 1)[0]
    return target.lower().replace(" ", "-") + ("" if target.endswith(".md") else ".md")


def _cross_language_allowed(label: str | None, line: str) -> bool:
    if "allow-cross-language" in line or "language-switcher" in line:
        return True
    if re.match(r"^\s*(?:Languages?|Языки|Мови|Мови сторінки)\s*:", line, re.IGNORECASE):
        return True
    normalized = (label or "").strip().lower()
    return normalized in {
        "en",
        "english",
        "английский",
        "англійська",
        "ru",
        "русский",
        "російська",
        "uk",
        "ua",
        "українська",
        "украинский",
    }


def _github_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"[*_~`]", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", heading).strip("-")


def anchors_for(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    anchors = {item.lower() for item in SECTION_RE.findall(text)}
    anchors.update(item.lower() for item in EXPLICIT_ANCHOR_RE.findall(text))
    counts: dict[str, int] = defaultdict(int)
    for heading in HEADING_RE.findall(_mask_code(text)):
        base = _github_slug(heading)
        if not base:
            continue
        count = counts[base]
        anchors.add(base if count == 0 else f"{base}-{count}")
        counts[base] += 1
    return anchors


def _page_language(path: Path, page_by_path: dict[Path, WikiPage]) -> str | None:
    page = page_by_path.get(path.resolve())
    if page:
        return page.language
    match = LOCALE_SUFFIX_RE.match(path.stem)
    if match:
        return match.group("lang").lower()
    try:
        metadata, _, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        value = metadata.get("lang")
        return str(value).lower() if value else None
    except OSError:
        return None


def _migration_lookup(migrations: dict[str, str]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for old, new in migrations.items():
        old_clean = old.removeprefix("./").removesuffix(".md").lower()
        variants = {old_clean, Path(old_clean).name}
        if old_clean.startswith("wiki/"):
            variants.add(old_clean[5:])
        for variant in variants:
            lookup[variant] = new
    return lookup


def _old_slug(link: Link, lookup: dict[str, str]) -> tuple[str, str] | None:
    normalized_target = link.target.replace("\\", "/")
    path_parts = [part for part in normalized_target.split("/") if part not in {"", ".", ".."}]
    if any(part.lower() == "raw" for part in path_parts):
        return None
    clean = normalized_target.removeprefix("./").removesuffix(".md").lower()
    variants = (clean, clean.removeprefix("wiki/"), Path(clean).name)
    for variant in variants:
        if variant in lookup:
            return variant, lookup[variant]
    stem = Path(clean).name
    match = LOCALE_SUFFIX_RE.match(stem)
    base_stem = match.group("group") if match else stem
    if base_stem in DELETED_SLUGS:
        return stem, "deleted/consolidated page"
    return None


def _resolve_link(
    source: Path,
    link: Link,
    root: Path,
    wiki_files: list[Path],
    all_files: list[Path],
) -> tuple[Path | None, list[Path]]:
    target = link.target.strip().replace("\\", "/")
    if not target:
        return source, []
    lowered = target.lower()
    if lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None, []
    if target.startswith("/") and not target.startswith("/wiki/"):
        return None, []

    target_path = Path(target.removeprefix("/"))
    if target_path.suffix and target_path.suffix.lower() not in {".md", ".markdown"}:
        return None, []
    if not target_path.suffix:
        target_path = target_path.with_suffix(".md")

    direct_candidates: list[Path] = []
    if target.startswith("wiki/") or target.startswith("/wiki/"):
        direct_candidates.append(root / target.removeprefix("/"))
    elif "/" in target or link.kind == "markdown":
        direct_candidates.extend((source.parent / target_path, root / target_path, root / "wiki" / target_path))
    else:
        direct_candidates.append(source.parent / target_path)
    for candidate in direct_candidates:
        if candidate.exists() and candidate.is_file():
            return candidate.resolve(), []

    pool = wiki_files if link.kind == "wikilink" else all_files
    expected_name = target_path.name.lower()
    matches = sorted({path.resolve() for path in pool if path.name.lower() == expected_name})
    if len(matches) == 1:
        return matches[0], []
    return None, matches


def check_links(
    root: Path,
    *,
    strict: bool = False,
    check_orphans: bool = True,
    scan_entries: Iterable[str] = DEFAULT_SCAN_ENTRIES,
) -> list[Diagnostic]:
    root = root.resolve()
    files = markdown_files(root, tuple(scan_entries))
    wiki_files = sorted((root / "wiki").rglob("*.md")) if (root / "wiki").exists() else []
    pages = load_wiki_pages(root)
    page_by_path = {page.path.resolve(): page for page in pages}
    migration_lookup = _migration_lookup(read_migration_map(root))
    diagnostics: list[Diagnostic] = []
    inbound_groups: dict[str, set[str]] = defaultdict(set)

    anchor_cache: dict[Path, set[str]] = {}
    for source in files:
        text = source.read_text(encoding="utf-8")
        source_relative = repo_relative(source, root)
        source_page = page_by_path.get(source.resolve())
        source_group = source_page.translation_group if source_page else f"outside:{source_relative}"
        for link in extract_links(text):
            old = _old_slug(link, migration_lookup)
            if old:
                diagnostics.append(
                    Diagnostic(
                        severity(strict),
                        "old-slug",
                        f"link uses retired target '{link.target}'; replacement: {old[1]}",
                        source_relative,
                        link.line,
                    )
                )
                continue

            resolved, ambiguous = _resolve_link(source, link, root, wiki_files, files)
            if ambiguous:
                diagnostics.append(
                    Diagnostic(
                        severity(strict),
                        "ambiguous-link",
                        f"'{link.target}' matches multiple files: "
                        + ", ".join(repo_relative(path, root) for path in ambiguous),
                        source_relative,
                        link.line,
                    )
                )
                continue
            if resolved is None:
                if link.target.lower().startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                    continue
                target_suffix = Path(link.target).suffix.lower()
                if link.kind == "markdown" and target_suffix not in {"", ".md", ".markdown"}:
                    continue
                diagnostics.append(
                    Diagnostic(
                        severity(strict),
                        "missing-link",
                        f"cannot resolve '{link.target}'",
                        source_relative,
                        link.line,
                    )
                )
                continue

            target_page = page_by_path.get(resolved)
            if target_page:
                inbound_groups[target_page.translation_group].add(source_group)

            if link.anchor:
                anchors = anchor_cache.setdefault(resolved, anchors_for(resolved))
                normalized_anchor = unquote(link.anchor).strip().lower()
                if normalized_anchor not in anchors:
                    diagnostics.append(
                        Diagnostic(
                            severity(strict),
                            "missing-anchor",
                            f"target '{repo_relative(resolved, root)}' has no anchor '#{link.anchor}'",
                            source_relative,
                            link.line,
                        )
                    )

            source_language = _page_language(source.resolve(), page_by_path)
            target_language = _page_language(resolved, page_by_path)
            if (
                source_language in {"en", "ru", "uk"}
                and target_language in {"en", "ru", "uk"}
                and source_language != target_language
                and not link.cross_language_allowed
            ):
                diagnostics.append(
                    Diagnostic(
                        severity(strict),
                        "cross-language-link",
                        f"{source_language} page links to {target_language} target without an explicit language-switch marker",
                        source_relative,
                        link.line,
                    )
                )

    if check_orphans:
        active_groups: dict[str, list[WikiPage]] = defaultdict(list)
        for page in pages:
            if page.status == "active":
                active_groups[page.translation_group].append(page)
        for group_name, members in sorted(active_groups.items()):
            external_sources = {source for source in inbound_groups[group_name] if source != group_name}
            if not external_sources:
                diagnostics.append(
                    Diagnostic(
                        severity(strict),
                        "orphan-group",
                        f"active translation group '{group_name}' has no inbound link from another group or repository entrypoint",
                        members[0].relative_path.as_posix(),
                    )
                )

    return sorted(diagnostics, key=lambda item: (item.path or "", item.line or 0, item.code))


def check_wikilinks(verbose: bool = False) -> Tuple[list[str], list[str]]:
    """Compatibility wrapper for callers of the original checker."""
    diagnostics = check_links(Path(__file__).resolve().parents[1], strict=True, check_orphans=False)
    errors = [item.format() for item in diagnostics if item.severity == "error"]
    warnings = [item.format() for item in diagnostics if item.severity == "warning"]
    return errors, warnings if verbose else []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true", help="fail on final-state violations")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--no-orphans", action="store_true", help="skip active-group orphan detection")
    parser.add_argument("--fail-on-warnings", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true", help="retained for compatibility")
    args = parser.parse_args()

    diagnostics = check_links(
        args.root,
        strict=args.strict,
        check_orphans=not args.no_orphans,
    )
    print_report(diagnostics, json_output=args.json)
    return exit_code(diagnostics, fail_on_warnings=args.fail_on_warnings)


if __name__ == "__main__":
    raise SystemExit(main())
