#!/usr/bin/env python3
"""Migrate wiki pages to symmetric language-suffixed paths.

The migration is deliberately mechanical: it renames unsuffixed wiki pages
to their declared or inferred language suffix, adds common governance frontmatter when it is
missing, updates repository-local wiki links, and writes a machine-readable
old-to-new path map. It never reads or writes ``raw/`` or historical
``log.md``.

Run with ``--check`` to preview and ``--write`` to apply.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


LANG_SUFFIX = re.compile(r"-(en|ru|uk)$")
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".toml"}
EXCLUDED_PARTS = {".git", "raw", "__pycache__"}
EXCLUDED_FILES = {"log.md"}
LINK_UPDATE_ENTRIES = (
    "README.md",
    "index.md",
    "docs",
    "skills",
    "instruments",
    "biblical-compatibility",
    ".opencode/agents",
    ".opencode/ORGANIZATION.md",
)
MANUAL_MIGRATIONS = {
    "wiki/concepts/main-idea.md": "wiki/concepts/main-idea-en.md",
    "wiki/concepts/project-positioning.md": "wiki/concepts/project-positioning-en.md",
    "wiki/concepts/four-level-compatibility-architecture.md": "wiki/concepts/four-level-compatibility-architecture-en.md",
    "wiki/concepts/value-moral-compatibility.md": "wiki/concepts/value-moral-compatibility-en.md",
    "wiki/concepts/latent-process.md": "wiki/concepts/latent-process-en.md",
    "wiki/concepts/compatibility-level-boundaries.md": "wiki/concepts/compatibility-level-boundaries-en.md",
    "wiki/concepts/project-main-goal.md": "wiki/concepts/project-positioning-en.md",
    "wiki/concepts/research-layer-vs-practical-guidance.md": "wiki/concepts/project-positioning-en.md",
    "wiki/concepts/research-layer-vs-practical-guidance-ru.md": "wiki/concepts/project-positioning-ru.md",
    "wiki/concepts/research-layer-vs-practical-guidance-uk.md": "wiki/concepts/project-positioning-uk.md",
    "wiki/concepts/hypothesis-status-of-before-we-build.md": "wiki/concepts/epistemic-status-and-inference-limits-en.md",
    "wiki/concepts/hypothesis-status-of-before-we-build-ru.md": "wiki/concepts/epistemic-status-and-inference-limits-ru.md",
    "wiki/concepts/hypothesis-status-of-before-we-build-uk.md": "wiki/concepts/epistemic-status-and-inference-limits-uk.md",
    "wiki/concepts/limits-of-typological-inference.md": "wiki/concepts/epistemic-status-and-inference-limits-en.md",
    "wiki/concepts/limits-of-typological-inference-ru.md": "wiki/concepts/epistemic-status-and-inference-limits-ru.md",
    "wiki/concepts/limits-of-typological-inference-uk.md": "wiki/concepts/epistemic-status-and-inference-limits-uk.md",
    "wiki/concepts/weight-calibration.md": "wiki/concepts/compatibility-measurement-roadmap-en.md",
    "wiki/concepts/multilingual-translation-policy.md": "wiki/concepts/multilingual-translation-policy-en.md",
    "wiki/concepts/music-style-catalog-and-psychosophy-emotion.md": "wiki/concepts/music-styles-and-psychosophy-emotion-en.md",
    "wiki/concepts/music-style-catalog-and-psychosophy-emotion-ru.md": "wiki/concepts/music-styles-and-psychosophy-emotion-ru.md",
    "wiki/concepts/music-style-catalog-and-psychosophy-emotion-uk.md": "wiki/concepts/music-styles-and-psychosophy-emotion-uk.md",
    "wiki/concepts/psychosophy-model.md": "wiki/concepts/afanasyev-model-en.md",
    "wiki/concepts/psychosophy-model-ru.md": "wiki/concepts/afanasyev-model-ru.md",
    "wiki/concepts/psychosophy-model-uk.md": "wiki/concepts/afanasyev-model-uk.md",
    "wiki/sources/typology-full-description.md": "wiki/concepts/typology-reconceptualization-en.md",
    "wiki/sources/research-program.md": "wiki/concepts/validation-program-en.md",
    "wiki/glossary-core.md": "wiki/glossary-core-en.md",
    "wiki/glossary-extended.md": "wiki/glossary-extended-en.md",
}
REMOVED_PATHS = {
    "wiki/scientific-contribution-statement.md": "retired simulation track",
    "wiki/sources/common-projects.md": "retired simulation track",
    "wiki/sources/llm-psychological-simulators-methodology.md": "retired simulation track",
    "wiki/sources/s-researcher-llm-social-scientists.md": "retired simulation track",
    "wiki/sources/ai-agents-psychometric-approach.md": "retired simulation track",
    "wiki/sources/llm-emulate-personality-nature-2025.md": "retired simulation track",
    "wiki/sources/ai-experiment-participants.md": "retired simulation track",
}
MANUAL_SLUG_MIGRATIONS = {
    "project-main-goal": "project-positioning",
    "research-layer-vs-practical-guidance": "project-positioning",
    "hypothesis-status-of-before-we-build": "epistemic-status-and-inference-limits",
    "limits-of-typological-inference": "epistemic-status-and-inference-limits",
    "weight-calibration": "compatibility-measurement-roadmap",
    "typology-full-description": "typology-reconceptualization",
    "research-program": "validation-program",
    "music-style-catalog-and-psychosophy-emotion": "music-styles-and-psychosophy-emotion",
    "psychosophy-model": "afanasyev-model",
}


def page_language(path: Path, text: str | None = None) -> tuple[str, str]:
    match = LANG_SUFFIX.search(path.stem)
    if match:
        return match.group(1), LANG_SUFFIX.sub("", path.stem)
    if text is None and path.exists():
        text = path.read_text(encoding="utf-8")
    text = text or ""
    declared = re.search(r"(?m)^lang:\s*(en|ru|uk)\s*$", text)
    if declared:
        return declared.group(1), path.stem
    # Some legacy pages predate the lang field. Infer a language only when
    # Cyrillic clearly dominates; otherwise retain the historical EN default.
    cyrillic = len(re.findall(r"[А-Яа-яЁёІіЇїЄєҐґ]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    if cyrillic > latin:
        ukrainian = len(re.findall(r"[ІіЇїЄєҐґ]", text))
        return ("uk" if ukrainian > max(4, cyrillic // 100) else "ru"), path.stem
    return "en", path.stem


def infer_role(path: Path, page_type: str | None) -> str:
    parts = set(path.parts)
    group = LANG_SUFFIX.sub("", path.stem)
    if "sources" in parts or page_type == "source":
        return "source-summary"
    if "entities" in parts or page_type == "entity":
        return "entity"
    if "relations" in parts or page_type == "relation":
        return "relation"
    if group == "start-here":
        return "hub"
    if any(
        token in group
        for token in ("christian", "biblical", "family-formation", "spiritual")
    ):
        return "application"
    if any(
        token in group
        for token in (
            "test-specification",
            "test-design",
            "mapping",
            "research",
            "validation",
            "measurement",
            "neural",
            "neuroscience",
            "sociological",
            "analysis",
            "synthesis",
            "evidence",
            "public-figure",
            "combinatorics",
            "big-five",
            "resource-distribution",
            "cognitive-resource",
            "music-style",
        )
    ):
        return "research-appendix"
    return "explanation"


def default_claim_status(role: str) -> str:
    return {
        "source-summary": "[source-attribution]",
        "entity": "[source-attribution, research-hypothesis]",
        "relation": "[research-hypothesis]",
        "application": "[application-guidance, normative-rule]",
        "research-appendix": "[research-hypothesis]",
        "hub": "[project-definition]",
    }.get(role, "[project-definition, research-hypothesis]")


def split_frontmatter(text: str) -> tuple[list[str], str]:
    if not text.startswith("---\n"):
        return [], text
    end = text.find("\n---\n", 4)
    if end == -1:
        return [], text
    return text[4:end].splitlines(), text[end + 5 :]


def scalar_value(lines: list[str], key: str) -> str | None:
    prefix = f"{key}:"
    for line in lines:
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return None


def normalize_frontmatter(path: Path, text: str) -> str:
    lines, body = split_frontmatter(text)
    lang, group = page_language(path, text)
    page_type = scalar_value(lines, "type")
    role = scalar_value(lines, "page_role") or infer_role(path, page_type)
    heading_match = re.search(r"(?m)^#\s+(.+?)\s*$", body)
    inferred_title = (
        heading_match.group(1).strip()
        if heading_match
        else group.replace("-", " ").title()
    )

    # Remove only the retired language-hierarchy keys. Existing claim and
    # caveat blocks are content-bearing governance and must be preserved.
    preserved: list[str] = []
    for line in lines:
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
        if key_match and key_match.group(1) in {"canonical", "translation_of"}:
            continue
        if line.startswith("lang:"):
            preserved.append(f"lang: {lang}")
        elif line.startswith("translation_group:"):
            preserved.append(f"translation_group: {group}")
        else:
            preserved.append(line)

    present = {
        match.group(1)
        for line in preserved
        if (match := re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line))
    }
    semantic_version = scalar_value(preserved, "semantic_version") or "1"
    additions: list[str] = []
    defaults = [
        ("title", json.dumps(inferred_title, ensure_ascii=False)),
        ("lang", lang),
        ("translation_group", group),
        ("semantic_version", semantic_version),
        ("reviewed_semantic_version", semantic_version),
        ("document_status", "active"),
        ("page_role", role),
        ("claim_status", default_claim_status(role)),
        ("claims", "[]"),
        ("caveat_ids", "[]"),
        ("sources", "[]"),
    ]
    for key, value in defaults:
        if key not in present:
            additions.append(f"{key}: {value}")
    return "---\n" + "\n".join(preserved + additions) + "\n---\n" + body


def collect_pages(root: Path) -> tuple[dict[Path, Path], dict[str, dict[str, Path]]]:
    renames: dict[Path, Path] = {}
    groups: dict[str, dict[str, Path]] = defaultdict(dict)
    wiki = root / "wiki"
    for path in sorted(wiki.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        lang, group = page_language(path, text)
        target = path if LANG_SUFFIX.search(path.stem) else path.with_name(f"{path.stem}-{lang}.md")
        renames[path] = target
        groups[group][lang] = target
    return renames, groups


def wikilink_target(slug: str, source_lang: str, groups: dict[str, dict[str, Path]]) -> str:
    suffix_match = LANG_SUFFIX.search(slug)
    group = LANG_SUFFIX.sub("", slug)
    group = MANUAL_SLUG_MIGRATIONS.get(group, group)
    if group not in groups:
        return slug
    requested = suffix_match.group(1) if suffix_match else source_lang
    if requested in groups[group]:
        return f"{group}-{requested}"
    if "en" in groups[group]:
        return f"{group}-en"
    return slug


def language_from_link_label(label: str | None) -> str | None:
    """Return an explicitly named language used by a language switcher."""
    normalized = (label or "").strip().lower()
    aliases = {
        "en": "en",
        "english": "en",
        "английский": "en",
        "англійська": "en",
        "ru": "ru",
        "русский": "ru",
        "російська": "ru",
        "uk": "uk",
        "ua": "uk",
        "українська": "uk",
        "украинский": "uk",
    }
    return aliases.get(normalized)


def _is_explicit_raw_path(target: str) -> bool:
    """Return whether a repository-local target explicitly traverses ``raw/``.

    Raw sources may share a basename with a generated wiki page.  The path
    segment, rather than the basename, is therefore the authority here.
    """

    normalized = target.replace("\\", "/").strip()
    return any(part.lower() == "raw" for part in normalized.split("/") if part)


def _mapped_link_path(target: str, path_map: dict[str, str]) -> str | None:
    """Map a repository path while retaining its relative-path spelling."""

    normalized = target.replace("\\", "/")
    parent_prefix = ""
    while normalized.startswith("../"):
        parent_prefix += "../"
        normalized = normalized[3:]
    current_prefix = ""
    while normalized.startswith("./"):
        current_prefix += "./"
        normalized = normalized[2:]
    root_relative = normalized.startswith("/")
    normalized = normalized.lstrip("/")

    candidates = [(normalized, False)]
    if normalized and not normalized.startswith("wiki/"):
        candidates.append((f"wiki/{normalized}", True))
    for candidate, added_wiki_prefix in candidates:
        migrated = path_map.get(candidate)
        if migrated is None:
            continue
        if added_wiki_prefix and migrated.startswith("wiki/"):
            migrated = migrated[5:]
        leading = "/" if root_relative else parent_prefix + current_prefix
        return leading + migrated
    return None


def _localized_path_target(
    target: str,
    source_lang: str,
    groups: dict[str, dict[str, Path]],
    path_map: dict[str, str],
    *,
    requested_language: str | None = None,
    protected_basenames: set[str] | None = None,
    basename_collision_is_ambiguous: bool = False,
) -> str:
    """Localize one path-like wiki target without changing its anchor."""

    if not target or _is_explicit_raw_path(target):
        return target
    lowered = target.lower()
    if lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return target

    path_part, separator, anchor = target.partition("#")
    path_part = path_part.strip()
    name = Path(path_part.replace("\\", "/")).name
    has_markdown_extension = name.lower().endswith(".md")
    stem = name[:-3] if has_markdown_extension else name
    suffix_match = LANG_SUFFIX.search(stem)
    source_group = LANG_SUFFIX.sub("", stem)
    target_group = MANUAL_SLUG_MIGRATIONS.get(source_group, source_group)
    if target_group not in groups:
        return target

    if (
        basename_collision_is_ambiguous
        and "/" not in path_part.replace("\\", "/")
        and name in (protected_basenames or set())
    ):
        return target

    requested = suffix_match.group(1) if suffix_match else requested_language or source_lang
    available = groups[target_group]
    if requested not in available:
        requested = "en" if "en" in available else ""
    if not requested:
        return target
    selected = available[requested]
    selected_name = selected.name if has_markdown_extension else selected.stem

    mapped = _mapped_link_path(path_part, path_map)
    if mapped is not None:
        mapped_path = Path(mapped)
        localized = str(mapped_path.with_name(selected.name if has_markdown_extension else selected.stem))
        # Path() normalizes a leading ``./`` away. Restore it for stable diffs.
        if mapped.startswith("./") and not localized.startswith("./"):
            localized = "./" + localized
    else:
        slash_index = max(path_part.rfind("/"), path_part.rfind("\\"))
        localized = path_part[: slash_index + 1] + selected_name

    return localized + (separator + anchor if separator else "")


def _rewrite_markdown_destination(
    payload: str,
    source_lang: str,
    groups: dict[str, dict[str, Path]],
    path_map: dict[str, str],
    protected_basenames: set[str],
) -> str:
    """Rewrite only the destination token inside ``](...)``."""

    leading_length = len(payload) - len(payload.lstrip())
    leading = payload[:leading_length]
    remainder = payload[leading_length:]
    if not remainder:
        return payload

    if remainder.startswith("<") and ">" in remainder:
        end = remainder.index(">")
        destination = remainder[1:end]
        suffix = remainder[end + 1 :]
        wrapper = ("<", ">")
    else:
        match = re.match(r"(\S+)(.*)", remainder, re.DOTALL)
        if match is None:
            return payload
        destination, suffix = match.groups()
        wrapper = ("", "")

    path_without_anchor = destination.split("#", 1)[0]
    if not path_without_anchor.lower().endswith(".md"):
        return payload
    localized = _localized_path_target(
        destination,
        source_lang,
        groups,
        path_map,
        protected_basenames=protected_basenames,
        basename_collision_is_ambiguous=True,
    )
    return leading + wrapper[0] + localized + wrapper[1] + suffix


def rewrite_links(
    text: str,
    source_lang: str,
    groups: dict[str, dict[str, Path]],
    path_map: dict[str, str],
    protected_basenames: set[str] | None = None,
) -> str:
    def replace_wikilink(match: re.Match[str]) -> str:
        inside = match.group(1)
        if "|" in inside:
            target, label = inside.split("|", 1)
        else:
            target, label = inside, None
        requested_language = language_from_link_label(label) or source_lang
        updated = _localized_path_target(
            target.strip(),
            source_lang,
            groups,
            path_map,
            requested_language=requested_language,
        )
        return "[[" + updated + ("|" + label if label is not None else "") + "]]"

    protected_basenames = protected_basenames or set()
    text = re.sub(r"(?<!!)\[\[([^\]\n]+)\]\]", replace_wikilink, text)

    def replace_markdown_link(match: re.Match[str]) -> str:
        return (
            match.group(1)
            + _rewrite_markdown_destination(
                match.group(2), source_lang, groups, path_map, protected_basenames
            )
            + match.group(3)
        )

    text = re.sub(
        r"(?<!!)(\[[^\]\n]*\]\()([^\)\n]+)(\))",
        replace_markdown_link,
        text,
    )

    # Some repository maps and frontmatter fields contain an explicit full
    # wiki path without Markdown syntax. Keep supporting those exact paths,
    # but never do basename-wide replacement: a raw source can legitimately
    # have the same filename.
    for old, new in sorted(path_map.items(), key=lambda item: len(item[0]), reverse=True):
        localized_new = new
        new_path = Path(new)
        suffix_match = LANG_SUFFIX.search(new_path.stem)
        target_group = LANG_SUFFIX.sub("", new_path.stem)
        if suffix_match and target_group in groups and source_lang in groups[target_group]:
            localized_new = str(
                new_path.with_name(groups[target_group][source_lang].name)
            )
        exact_path = re.compile(
            rf"(?<![A-Za-z0-9_./-]){re.escape(old)}(?![A-Za-z0-9_./-])"
        )
        text = exact_path.sub(localized_new, text)
    return text


def iter_text_files(root: Path):
    for entry in LINK_UPDATE_ENTRIES:
        candidate = root / entry
        paths = [candidate] if candidate.is_file() else candidate.rglob("*") if candidate.is_dir() else []
        for path in paths:
            if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
                continue
            if path.name in EXCLUDED_FILES or any(
                part in EXCLUDED_PARTS for part in path.relative_to(root).parts
            ):
                continue
            yield path


def load_existing_manifest(path: Path) -> dict[str, object]:
    """Load an existing migration manifest without silently discarding history."""

    if not path.exists():
        return {}
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read existing migration manifest {path}: {error}") from error
    if not isinstance(manifest, dict):
        raise ValueError(f"existing migration manifest {path} must be a JSON object")
    for field in ("migrations", "english_entrypoints", "removed"):
        value = manifest.get(field, {})
        if not isinstance(value, dict) or not all(
            isinstance(key, str) and isinstance(item, str)
            for key, item in value.items()
        ):
            raise ValueError(
                f"existing migration manifest field {field!r} must be a string map"
            )
    return manifest


def merge_migration_manifest(
    existing: dict[str, object],
    migrations: dict[str, str],
    english_entrypoints: dict[str, str],
    removed: dict[str, str],
) -> dict[str, object]:
    """Merge new facts into the append-only migration history.

    Newly computed and manually declared values take precedence, so an explicit
    correction can replace a stale destination without losing unrelated entries
    accumulated by earlier migration runs.
    """

    def merged_field(field: str, current: dict[str, str]) -> dict[str, str]:
        previous = existing.get(field, {})
        if not isinstance(previous, dict):
            raise ValueError(f"existing manifest field {field!r} must be an object")
        combined = dict(previous)
        combined.update(current)
        return dict(sorted(combined.items()))

    return {
        "schema_version": 1,
        "migrations": merged_field("migrations", migrations),
        "english_entrypoints": merged_field(
            "english_entrypoints", english_entrypoints
        ),
        "removed": merged_field("removed", removed),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    renames, groups = collect_pages(root)
    collisions: list[tuple[Path, Path]] = []
    target_owners: dict[Path, Path] = {}
    for old, new in renames.items():
        owner = target_owners.get(new)
        if owner is not None and owner != old:
            collisions.append((old, new))
        else:
            target_owners[new] = old
        if old != new and new.exists():
            collisions.append((old, new))
    if collisions:
        print("ERROR: migration target collision(s):")
        for old, new in sorted(set(collisions)):
            print(f"  {old.relative_to(root)} -> {new.relative_to(root)}")
        return 1
    path_map = {
        str(old.relative_to(root)): str(new.relative_to(root))
        for old, new in renames.items()
        if old != new
    }
    path_map.update(MANUAL_MIGRATIONS)
    protected_basenames = {
        path.name for path in (root / "raw").rglob("*") if path.is_file()
    }
    english_entrypoints: dict[str, str] = {}
    for old, migrated in path_map.items():
        migrated_path = Path(migrated)
        match = LANG_SUFFIX.search(migrated_path.stem)
        group = LANG_SUFFIX.sub("", migrated_path.stem) if match else None
        if group and group in groups and "en" in groups[group]:
            english_entrypoints[old] = str(groups[group]["en"].relative_to(root))
        elif migrated.endswith("-en.md"):
            english_entrypoints[old] = migrated

    migration_file = root / "wiki" / "slug-migrations.json"
    try:
        existing_manifest = load_existing_manifest(migration_file)
        migration_manifest = merge_migration_manifest(
            existing_manifest,
            path_map,
            english_entrypoints,
            REMOVED_PATHS,
        )
    except ValueError as error:
        print(f"ERROR: {error}")
        return 1

    changed_files = 0
    if args.write:
        for old, new in renames.items():
            if old != new:
                new.parent.mkdir(parents=True, exist_ok=True)
                old.rename(new)

        for path in sorted((root / "wiki").rglob("*.md")):
            before = path.read_text(encoding="utf-8")
            after = normalize_frontmatter(path, before)
            lang, _ = page_language(path)
            after = rewrite_links(
                after, lang, groups, path_map, protected_basenames
            )
            if after != before:
                path.write_text(after, encoding="utf-8")
                changed_files += 1

        for path in iter_text_files(root):
            if path.is_relative_to(root / "wiki"):
                continue
            before = path.read_text(encoding="utf-8")
            after = rewrite_links(
                before, "en", groups, path_map, protected_basenames
            )
            if after != before:
                path.write_text(after, encoding="utf-8")
                changed_files += 1

        migration_file.write_text(
            json.dumps(migration_manifest, indent=2, ensure_ascii=False)
            + "\n",
            encoding="utf-8",
        )

    print(f"wiki pages: {len(renames)}")
    pending_renames = sum(old != new for old, new in renames.items())
    print(f"Unsuffixed paths to rename: {pending_renames}")
    manifest_migrations = migration_manifest["migrations"]
    assert isinstance(manifest_migrations, dict)
    print(f"Migration manifest entries: {len(manifest_migrations)}")
    print(f"text files changed: {changed_files}")
    if args.check:
        for old, new in list(sorted(path_map.items()))[:20]:
            print(f"  {old} -> {new}")
        if len(path_map) > 20:
            print(f"  ... {len(path_map) - 20} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
