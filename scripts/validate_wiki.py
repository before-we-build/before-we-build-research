#!/usr/bin/env python3
"""Validate the multilingual Before We Build wiki contract.

Default invocation is a non-blocking migration report. ``--strict`` turns every
contract violation into an error and is the mode used by CI after migration.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from wiki_quality_common import (
    CLAIM_MARKER_RE,
    LOCALES,
    Diagnostic,
    WikiPage,
    as_list,
    claim_map,
    exit_code,
    load_wiki_pages,
    normalized_sources,
    print_report,
    read_migration_map,
    repo_relative,
    severity,
)


REQUIRED_FIELDS = {
    "title",
    "lang",
    "translation_group",
    "semantic_version",
    "reviewed_semantic_version",
    "document_status",
    "page_role",
    "claim_status",
    "claims",
    "caveat_ids",
    "sources",
}

DOCUMENT_STATUSES = {"active", "draft", "historical"}
PAGE_ROLES = {
    "hub",
    "explanation",
    "application",
    "research-appendix",
    "source-summary",
    "entity",
    "relation",
}
CLAIM_STATUSES = {
    "project-definition",
    "normative-rule",
    "source-attribution",
    "research-hypothesis",
    "evidence-informed",
    "empirically-supported",
    "contested",
    "rejected",
    "application-guidance",
    "historical-proposal",
}
DEPRECATED_FIELDS = {"canonical", "translation_of"}

CENTRAL_GROUPS = {
    "start-here",
    "main-idea",
    "project-positioning",
    "typology-reconceptualization",
    "four-level-compatibility-architecture",
    "value-moral-compatibility",
    "strategic-compatibility",
    "operational-compatibility",
    "tactical-compatibility",
    "latent-process",
    "compatibility-level-boundaries",
    "epistemic-status-and-inference-limits",
    "evidence-workflow-and-walkthrough",
    "glossary-core",
    "christian-application-overview",
}

CENTRAL_SECTION_IDS = (
    "in-90-seconds",
    "definition-and-scope",
    "shared-example",
    "observations",
    "hypotheses",
    "alternatives",
    "non-inferences",
    "conversation-questions",
    "researcher-route",
    "next-reading",
)

LEVEL_GROUPS = {
    "value-moral-compatibility",
    "strategic-compatibility",
    "operational-compatibility",
    "tactical-compatibility",
}

LEVEL_SECTION_IDS = (
    "inclusion-exclusion",
    "latent-construct",
    "observable-indicators",
    "interaction-mechanism",
    "counterexamples",
    "falsification",
    "evidence-status",
)

SOURCE_SUMMARY_SECTION_IDS = (
    "source-claims",
    "source-evidence",
    "source-limitations",
    "bwb-accepts",
    "bwb-contested",
    "bwb-rejected-or-historical",
)

RETIRED_TERMS = (
    "digital twin",
    "user twin",
    "candidate twin",
    "simulation engine",
    "text world engine",
    "simulation transcript",
    "love observer",
    "scenario compiler",
    "digital twin builder",
    "inner parliament",
)

SOURCE_REPOSITORY_PREFIXES = (
    "raw/",
    "wiki/",
    "docs/",
    "skills/",
    "protocols/",
    "applications/",
    "research/",
    "governance/",
    ".opencode/",
    ".agent-learning/",
    "biblical-compatibility/",
    "instruments/",
    "./",
    "../",
)
SOURCE_EXTERNAL_PREFIXES = ("web:", "doi:", "arxiv:")
SOURCE_URL_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.IGNORECASE)
MARKDOWN_SUFFIXES = {".md", ".markdown"}


def _path(page: WikiPage) -> str:
    return page.relative_path.as_posix()


def _list_of_strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def _source_path_text(reference: str) -> str:
    """Return the local-path part of a source reference."""

    # Network references are filtered before this helper is called, so a URL
    # fragment cannot be damaged here.
    return reference.split("#", 1)[0].strip().replace("\\", "/")


def _ignored_source_reference(reference: str) -> bool:
    lowered = reference.strip().lower()
    return bool(SOURCE_URL_RE.match(lowered)) or lowered.startswith(
        SOURCE_EXTERNAL_PREFIXES + ("www.",)
    )


def _inside_repository(candidate: Path, root: Path) -> tuple[Path | None, str | None]:
    resolved = candidate.resolve(strict=False)
    try:
        relative = resolved.relative_to(root)
    except ValueError:
        return None, None
    return resolved, relative.as_posix()


def _markdown_source_index(root: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for candidate in root.rglob("*"):
        try:
            relative = candidate.relative_to(root)
        except ValueError:
            continue
        resolved, _ = _inside_repository(candidate, root)
        if ".git" in relative.parts or resolved is None or not resolved.is_file():
            continue
        if candidate.suffix.lower() in MARKDOWN_SUFFIXES:
            index[candidate.name.lower()].append(resolved)
    return {name: sorted(set(paths)) for name, paths in index.items()}


def _migration_indexes(
    root: Path,
) -> tuple[dict[str, str], dict[str, list[tuple[str, str]]]]:
    exact: dict[str, str] = {}
    by_basename: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for old, new in read_migration_map(root).items():
        old_path = old.strip().replace("\\", "/").removeprefix("./").lstrip("/")
        new_path = new.strip().replace("\\", "/").removeprefix("./").lstrip("/")
        if not old_path.lower().startswith("wiki/"):
            continue
        if old_path.lower() == new_path.lower():
            continue
        exact[old_path.lower()] = new_path
        by_basename[Path(old_path).name.lower()].append((old_path, new_path))
    return exact, dict(by_basename)


def _old_wiki_source(
    *,
    relative_target: str | None,
    bare_name: str | None,
    exact_migrations: dict[str, str],
    basename_migrations: dict[str, list[tuple[str, str]]],
) -> tuple[str, str] | None:
    if relative_target:
        normalized = relative_target.removeprefix("./").lstrip("/").lower()
        variants = [normalized]
        if not Path(normalized).suffix:
            variants.append(normalized + ".md")
        for variant in variants:
            replacement = exact_migrations.get(variant)
            if replacement:
                return variant, replacement
    if bare_name:
        matches = basename_migrations.get(bare_name.lower(), [])
        if len(matches) == 1:
            return matches[0]
    return None


def _localized_source_diagnostic(
    source_page: WikiPage,
    target: Path,
    *,
    page_by_path: dict[Path, WikiPage],
    peers: dict[str, dict[str, list[WikiPage]]],
    strict: bool,
    root: Path,
) -> Diagnostic | None:
    target_page = page_by_path.get(target.resolve())
    source_language = source_page.language
    if not target_page or source_language not in LOCALES or target_page.language not in LOCALES:
        return None
    if source_language == target_page.language:
        return None
    localized = peers.get(target_page.translation_group, {}).get(source_language, [])
    if not localized:
        return None
    suggestions = ", ".join(repo_relative(item.path, root) for item in localized)
    return Diagnostic(
        severity(strict),
        "cross-language-source",
        f"{source_language} page cites {target_page.language} wiki source while a localized peer exists: {suggestions}",
        _path(source_page),
    )


def validate_source_references(
    pages: list[WikiPage], root: Path, strict: bool
) -> list[Diagnostic]:
    """Validate local provenance references without touching the network.

    Free-form bibliography labels remain valid. A value is treated as a local
    repository reference only when it has an explicit repository prefix, is a
    bare Markdown filename, or exactly names an existing translation group.
    This intentionally leaves mixed labels such as
    ``before-we-build/Psyche-Yoga`` alone.
    """

    root = root.resolve()
    diagnostics: list[Diagnostic] = []
    level = severity(strict)
    markdown_index = _markdown_source_index(root)
    exact_migrations, basename_migrations = _migration_indexes(root)
    page_by_path = {page.path.resolve(): page for page in pages}
    peers: dict[str, dict[str, list[WikiPage]]] = defaultdict(lambda: defaultdict(list))
    groups: dict[str, list[WikiPage]] = defaultdict(list)
    for page in pages:
        groups[page.translation_group.lower()].append(page)
        if page.language:
            peers[page.translation_group][page.language].append(page)

    def report_resolved_source(source_page: WikiPage, target: Path) -> None:
        _, relative_target = _inside_repository(target, root)
        old = _old_wiki_source(
            relative_target=relative_target,
            bare_name=None,
            exact_migrations=exact_migrations,
            basename_migrations=basename_migrations,
        )
        if old:
            diagnostics.append(
                Diagnostic(
                    level,
                    "old-source-slug",
                    f"source uses retired wiki path '{old[0]}'; replacement: {old[1]}",
                    _path(source_page),
                )
            )
            return
        localized = _localized_source_diagnostic(
            source_page,
            target,
            page_by_path=page_by_path,
            peers=peers,
            strict=strict,
            root=root,
        )
        if localized:
            diagnostics.append(localized)

    for page in pages:
        if page.status != "active" or not _list_of_strings(page.metadata.get("sources")):
            continue
        for raw_reference in page.metadata["sources"]:
            reference = raw_reference.strip()
            if not reference or _ignored_source_reference(reference):
                continue
            path_text = _source_path_text(reference)
            if not path_text:
                continue
            lowered = path_text.lower()

            if lowered.startswith(SOURCE_REPOSITORY_PREFIXES):
                if lowered.startswith(("./", "../")):
                    candidate = page.path.parent / Path(path_text)
                else:
                    candidate = root / Path(path_text)
                resolved, relative_target = _inside_repository(candidate, root)
                if resolved is None:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "source-outside-root",
                            f"source path escapes the repository: '{reference}'",
                            _path(page),
                        )
                    )
                    continue
                old = _old_wiki_source(
                    relative_target=relative_target,
                    bare_name=None,
                    exact_migrations=exact_migrations,
                    basename_migrations=basename_migrations,
                )
                if old:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "old-source-slug",
                            f"source uses retired wiki path '{old[0]}'; replacement: {old[1]}",
                            _path(page),
                        )
                    )
                    continue
                if not resolved.exists():
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "missing-source",
                            f"source path does not exist: '{reference}'",
                            _path(page),
                        )
                    )
                    continue
                if resolved.is_dir():
                    if relative_target == "raw" or relative_target.startswith("raw/"):
                        continue
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "invalid-source-target",
                            f"only raw/ directories may be cited as source targets: '{reference}'",
                            _path(page),
                        )
                    )
                    continue
                if not resolved.is_file():
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "invalid-source-target",
                            f"source target is not a regular file: '{reference}'",
                            _path(page),
                        )
                    )
                    continue
                report_resolved_source(page, resolved)
                continue

            bare_path = Path(path_text)
            if "/" not in path_text and bare_path.suffix.lower() in MARKDOWN_SUFFIXES:
                direct: set[Path] = set()
                for candidate in (page.path.parent / bare_path, root / bare_path):
                    resolved, _ = _inside_repository(candidate, root)
                    if resolved is not None and resolved.is_file():
                        direct.add(resolved)
                if len(direct) > 1:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "ambiguous-source",
                            f"bare source '{reference}' matches page-relative and root files: "
                            + ", ".join(repo_relative(item, root) for item in sorted(direct)),
                            _path(page),
                        )
                    )
                    continue
                if len(direct) == 1:
                    report_resolved_source(page, next(iter(direct)))
                    continue

                matches = markdown_index.get(bare_path.name.lower(), [])
                if len(matches) > 1:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "ambiguous-source",
                            f"bare source '{reference}' matches multiple files: "
                            + ", ".join(repo_relative(item, root) for item in matches),
                            _path(page),
                        )
                    )
                    continue
                if len(matches) == 1:
                    report_resolved_source(page, matches[0])
                    continue

                old = _old_wiki_source(
                    relative_target=None,
                    bare_name=bare_path.name,
                    exact_migrations=exact_migrations,
                    basename_migrations=basename_migrations,
                )
                if old:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "old-source-slug",
                            f"source uses retired wiki path '{old[0]}'; replacement: {old[1]}",
                            _path(page),
                        )
                    )
                else:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "missing-source",
                            f"bare Markdown source cannot be resolved: '{reference}'",
                            _path(page),
                        )
                    )
                continue

            # A slash is not enough to make an arbitrary bibliography label a
            # repository path. Bare slugs are checked only when they name an
            # actual translation group.
            if "/" in path_text or "." in path_text:
                continue
            group_members = groups.get(path_text.lower())
            if not group_members:
                continue
            same_language = [item for item in group_members if item.language == page.language]
            target_page = (same_language or group_members)[0]
            report_resolved_source(page, target_page.path)

    return diagnostics


def validate_page(page: WikiPage, strict: bool) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    level = severity(strict)
    path = _path(page)

    if page.frontmatter_error:
        diagnostics.append(
            Diagnostic(level, "frontmatter", page.frontmatter_error, path)
        )
        return diagnostics

    for field_name in sorted(REQUIRED_FIELDS - page.metadata.keys()):
        diagnostics.append(
            Diagnostic(level, "missing-field", f"required field '{field_name}' is missing", path)
        )

    for field_name in sorted(DEPRECATED_FIELDS & page.metadata.keys()):
        diagnostics.append(
            Diagnostic(
                level,
                "deprecated-field",
                f"remove '{field_name}'; language peers are equal",
                path,
            )
        )

    if page.filename_language is None:
        diagnostics.append(
            Diagnostic(
                level,
                "filename-language",
                "wiki filename must end in -en.md, -ru.md, or -uk.md",
                path,
            )
        )
    elif page.metadata.get("lang") != page.filename_language:
        diagnostics.append(
            Diagnostic(
                level,
                "language-mismatch",
                f"frontmatter lang={page.metadata.get('lang')!r} does not match filename suffix -{page.filename_language}",
                path,
            )
        )

    if page.metadata.get("translation_group") != page.inferred_group:
        diagnostics.append(
            Diagnostic(
                level,
                "translation-group",
                f"translation_group must be '{page.inferred_group}' for this filename",
                path,
            )
        )

    status = page.metadata.get("document_status")
    if status not in DOCUMENT_STATUSES:
        diagnostics.append(
            Diagnostic(level, "document-status", f"invalid document_status {status!r}", path)
        )

    role = page.metadata.get("page_role")
    if role not in PAGE_ROLES:
        diagnostics.append(Diagnostic(level, "page-role", f"invalid page_role {role!r}", path))

    for field_name in ("semantic_version", "reviewed_semantic_version"):
        value = page.metadata.get(field_name)
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            diagnostics.append(
                Diagnostic(level, "semantic-version", f"{field_name} must be a positive integer", path)
            )

    if (
        status == "active"
        and page.metadata.get("reviewed_semantic_version")
        != page.metadata.get("semantic_version")
    ):
        diagnostics.append(
            Diagnostic(
                level,
                "unreviewed-active-page",
                "active page must be reviewed at its current semantic_version",
                path,
            )
        )

    page_claim_statuses = as_list(page.metadata.get("claim_status"))
    if not page_claim_statuses:
        diagnostics.append(
            Diagnostic(level, "claim-status", "claim_status must contain at least one status", path)
        )
    for item in page_claim_statuses:
        if item not in CLAIM_STATUSES:
            diagnostics.append(
                Diagnostic(level, "claim-status", f"invalid claim status {item!r}", path)
            )

    claims = as_list(page.metadata.get("claims"))
    seen_claims: set[str] = set()
    for claim in claims:
        if not isinstance(claim, dict) or not claim.get("id") or not claim.get("status"):
            diagnostics.append(
                Diagnostic(
                    level,
                    "claim-shape",
                    "each claims item must contain non-empty id and status fields",
                    path,
                )
            )
            continue
        claim_id = str(claim["id"])
        if claim_id in seen_claims:
            diagnostics.append(
                Diagnostic(level, "duplicate-claim", f"claim id '{claim_id}' is duplicated", path)
            )
        seen_claims.add(claim_id)
        if claim.get("status") not in CLAIM_STATUSES:
            diagnostics.append(
                Diagnostic(
                    level,
                    "claim-status",
                    f"claim '{claim_id}' has invalid status {claim.get('status')!r}",
                    path,
                )
            )

    claim_markers = CLAIM_MARKER_RE.findall(page.body)
    if len(claim_markers) != len(set(claim_markers)):
        diagnostics.append(
            Diagnostic(level, "duplicate-claim-marker", "body contains duplicate claim markers", path)
        )
    for claim_id in sorted(set(claim_markers) - seen_claims):
        diagnostics.append(
            Diagnostic(
                level,
                "undeclared-claim-marker",
                f"body marker claim:{claim_id} is not declared in frontmatter",
                path,
            )
        )
    if not _list_of_strings(page.metadata.get("caveat_ids")):
        diagnostics.append(
            Diagnostic(level, "caveat-ids", "caveat_ids must be a list of strings", path)
        )
    if not _list_of_strings(page.metadata.get("sources")):
        diagnostics.append(Diagnostic(level, "sources", "sources must be a list", path))

    if len(page.section_ids) != len(set(page.section_ids)):
        diagnostics.append(
            Diagnostic(level, "duplicate-section", "body contains duplicate section IDs", path)
        )

    if status == "active" and not page.section_ids:
        diagnostics.append(
            Diagnostic(
                level,
                "missing-section-id",
                "active page must contain at least one stable <!-- section:id --> marker",
                path,
            )
        )

    if status == "active" and page.translation_group in CENTRAL_GROUPS:
        required = set(CENTRAL_SECTION_IDS)
        if page.translation_group in LEVEL_GROUPS:
            required.update(LEVEL_SECTION_IDS)
        missing = sorted(required - set(page.section_ids))
        if missing:
            diagnostics.append(
                Diagnostic(
                    level,
                    "central-page-contract",
                    "missing section marker(s): " + ", ".join(missing),
                    path,
                )
            )

    if status == "active" and role == "source-summary":
        missing = sorted(set(SOURCE_SUMMARY_SECTION_IDS) - set(page.section_ids))
        if missing:
            diagnostics.append(
                Diagnostic(
                    level,
                    "source-summary-contract",
                    "missing source-assessment section marker(s): "
                    + ", ".join(missing),
                    path,
                )
            )

    if status == "active":
        lowered = (str(page.metadata) + "\n" + page.body).lower()
        for term in RETIRED_TERMS:
            if term in lowered:
                diagnostics.append(
                    Diagnostic(
                        level,
                        "retired-simulation-term",
                        f"active page contains retired term '{term}'",
                        path,
                    )
                )

    return diagnostics


def _parity_value(page: WikiPage, field_name: str) -> Any:
    if field_name == "claims":
        return tuple(sorted(claim_map(page.metadata).items()))
    if field_name == "caveat_ids":
        return tuple(sorted(str(item) for item in as_list(page.metadata.get(field_name))))
    if field_name == "sources":
        return normalized_sources(page.metadata)
    if field_name == "section_ids":
        return page.section_ids
    if field_name == "claim_status":
        return tuple(sorted(str(item) for item in as_list(page.metadata.get(field_name))))
    return page.metadata.get(field_name)


def validate_groups(pages: list[WikiPage], strict: bool) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    level = severity(strict)
    groups: dict[str, list[WikiPage]] = defaultdict(list)
    for page in pages:
        groups[page.translation_group].append(page)

    parity_fields = (
        "semantic_version",
        "document_status",
        "page_role",
        "claim_status",
        "claims",
        "caveat_ids",
        "sources",
        "section_ids",
    )

    for group_name, members in sorted(groups.items()):
        by_language: dict[str, list[WikiPage]] = defaultdict(list)
        for page in members:
            by_language[page.language or "unknown"].append(page)

        for language, duplicates in sorted(by_language.items()):
            if len(duplicates) > 1:
                diagnostics.append(
                    Diagnostic(
                        level,
                        "duplicate-locale",
                        f"translation group '{group_name}' has {len(duplicates)} {language} pages: "
                        + ", ".join(_path(page) for page in duplicates),
                    )
                )

        if any(page.status == "active" for page in members):
            missing = sorted(set(LOCALES) - set(by_language))
            if missing:
                diagnostics.append(
                    Diagnostic(
                        level,
                        "incomplete-active-triad",
                        f"active translation group '{group_name}' is missing: {', '.join(missing)}",
                    )
                )

        representatives = [items[0] for lang, items in sorted(by_language.items()) if lang in LOCALES]
        if len(representatives) < 2:
            continue
        reference = representatives[0]
        for field_name in parity_fields:
            expected = _parity_value(reference, field_name)
            for page in representatives[1:]:
                actual = _parity_value(page, field_name)
                if actual != expected:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "translation-parity",
                            f"group '{group_name}' field '{field_name}' differs between "
                            f"{_path(reference)} and {_path(page)}",
                            _path(page),
                        )
                    )
    return diagnostics


def validate_wiki(root: Path, *, strict: bool = False) -> list[Diagnostic]:
    root = root.resolve()
    pages = load_wiki_pages(root)
    if not pages:
        return [
            Diagnostic(
                severity(strict),
                "missing-wiki",
                "wiki directory contains no Markdown pages",
                "wiki",
            )
        ]
    diagnostics: list[Diagnostic] = []
    for page in pages:
        diagnostics.extend(validate_page(page, strict))
    diagnostics.extend(validate_source_references(pages, root, strict))
    diagnostics.extend(validate_groups(pages, strict))
    return sorted(
        diagnostics,
        key=lambda item: (item.path or "", item.line or 0, item.code, item.message),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail on all final-schema violations (default: migration report)",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--fail-on-warnings", action="store_true")
    args = parser.parse_args()

    diagnostics = validate_wiki(args.root.resolve(), strict=args.strict)
    print_report(diagnostics, json_output=args.json)
    return exit_code(diagnostics, fail_on_warnings=args.fail_on_warnings)


if __name__ == "__main__":
    raise SystemExit(main())
