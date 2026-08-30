#!/usr/bin/env python3
"""Generate a deterministic, machine-readable wiki migration inventory."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from audit_claim_language import audit_claims
from check_wikilinks import DEFAULT_SCAN_ENTRIES, _resolve_link, check_links, extract_links
from validate_wiki import RETIRED_TERMS, validate_wiki
from wiki_quality_common import (
    LOCALES,
    as_list,
    claim_map,
    load_wiki_pages,
    markdown_files,
    repo_relative,
)


# This is historical audit evidence, not a claim about the generated state.
AUDITED_BASELINE = {
    "date": "2026-08-30",
    "pages": 414,
    "translation_groups": 206,
    "complete_triads": 103,
    "missing_language_files": 204,
    "phase": "before consolidation and language-path migration",
}

OLD_MODEL_RULES = {
    "three-level-model": re.compile(
        r"\bthree[- ](?:level|layer)\s+compatibility\b|"
        r"\bтр[её]х(?:уровнев\w*|слойн\w*)\s+(?:модел\w*|совместимост\w*)\b|"
        r"\bтрирівнев\w*\s+(?:модел\w*|сумісн\w*)\b",
        re.IGNORECASE,
    ),
    "strategic-values": re.compile(
        r"\bstrategic(?:\s+(?:level|compatibility))?\s*(?::|=|->|→|—|\|)\s*(?:shared\s+)?values?\b|"
        r"\bvalues?\s+(?:are|as)\s+(?:a\s+)?strategic(?:\s+level)?\b|"
        r"\bstrategic\s+values?\b|"
        r"\bстратегическ\w*(?:\s+уров\w*)?\s*(?::|=|->|→|—|\|)\s*ценност\w*|"
        r"\bценност\w*\s+(?:являются|как)\s+стратегическ\w*|"
        r"\bстратегічн\w*(?:\s+рів\w*)?\s*(?::|=|->|→|—|\|)\s*цінност\w*|"
        r"\bцінност\w*\s+(?:є|як)\s+стратегічн\w*",
        re.IGNORECASE,
    ),
}


def _line_hits(text: str, patterns: dict[str, re.Pattern[str]], path: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for code, pattern in patterns.items():
            if pattern.search(line):
                hits.append({"path": path, "line": number, "code": code})
    return hits


def build_inventory(root: Path) -> dict[str, Any]:
    root = root.resolve()
    pages = load_wiki_pages(root)
    by_path = {page.path.resolve(): page for page in pages}
    groups: dict[str, list[Any]] = defaultdict(list)
    for page in pages:
        groups[page.translation_group].append(page)

    scan_files = markdown_files(root, DEFAULT_SCAN_ENTRIES)
    wiki_files = sorted((root / "wiki").rglob("*.md"))
    inbound: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    outbound: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    inbound_groups: dict[str, set[str]] = defaultdict(set)
    for source in scan_files:
        source_page = by_path.get(source.resolve())
        source_group = source_page.translation_group if source_page else f"outside:{repo_relative(source, root)}"
        for link in extract_links(source.read_text(encoding="utf-8")):
            resolved, ambiguous = _resolve_link(source, link, root, wiki_files, scan_files)
            record = {
                "source": repo_relative(source, root),
                "line": link.line,
                "raw_target": link.target,
                "resolved": repo_relative(resolved, root) if resolved else None,
                "ambiguous": [repo_relative(path, root) for path in ambiguous],
            }
            outbound[source.resolve()].append(record)
            if resolved in by_path:
                inbound[resolved].append(record)
                target_group = by_path[resolved].translation_group
                inbound_groups[target_group].add(source_group)

    group_records: list[dict[str, Any]] = []
    missing_language_files = 0
    complete_triads = 0
    duplicate_locale_groups = 0
    for group_name, members in sorted(groups.items()):
        locale_counts = Counter(page.language for page in members if page.language in LOCALES)
        locales = sorted(locale_counts)
        missing = sorted(set(LOCALES) - set(locales))
        duplicate_locales = {
            str(locale): count
            for locale, count in sorted(locale_counts.items())
            if count > 1
        }
        duplicate_locale_groups += int(bool(duplicate_locales))
        missing_language_files += len(missing)
        complete = not missing and len(locales) == len(LOCALES)
        complete_triads += int(complete)
        group_records.append(
            {
                "translation_group": group_name,
                "locales": locales,
                "missing_locales": missing,
                "complete_triad": complete,
                "locale_counts": dict(sorted(locale_counts.items())),
                "duplicate_locales": duplicate_locales,
                "statuses": sorted({page.status for page in members}),
                "roles": sorted({str(page.metadata.get("page_role") or "unclassified") for page in members}),
                "members": [page.relative_path.as_posix() for page in sorted(members, key=lambda item: item.relative_path.as_posix())],
            }
        )

    page_records: list[dict[str, Any]] = []
    old_model_hits: list[dict[str, Any]] = []
    simulation_hits: list[dict[str, Any]] = []
    simulation_patterns = {
        "retired-simulation-term": re.compile(
            "|".join(re.escape(term) for term in RETIRED_TERMS), re.IGNORECASE
        )
    }
    for page in sorted(pages, key=lambda item: item.relative_path.as_posix()):
        page_records.append(
            {
                "path": page.relative_path.as_posix(),
                "title": page.title,
                "lang": page.language,
                "translation_group": page.translation_group,
                "document_status": page.status,
                "page_role": page.metadata.get("page_role"),
                "semantic_version": page.metadata.get("semantic_version"),
                "reviewed_semantic_version": page.metadata.get(
                    "reviewed_semantic_version"
                ),
                "claim_status": [
                    str(item) for item in as_list(page.metadata.get("claim_status"))
                ],
                "claims": claim_map(page.metadata),
                "caveat_ids": [
                    str(item) for item in as_list(page.metadata.get("caveat_ids"))
                ],
                "sources": [str(item) for item in as_list(page.metadata.get("sources"))],
                "section_ids": list(page.section_ids),
                "inbound_links": sorted(
                    inbound.get(page.path.resolve(), []),
                    key=lambda item: (item["source"], item["line"], item["raw_target"]),
                ),
                "outbound_links": sorted(
                    outbound.get(page.path.resolve(), []),
                    key=lambda item: (item["line"], item["raw_target"]),
                ),
            }
        )
        if page.status == "active":
            relative = page.relative_path.as_posix()
            old_model_hits.extend(_line_hits(page.body, OLD_MODEL_RULES, relative))
            simulation_hits.extend(_line_hits(page.body, simulation_patterns, relative))

    link_findings = check_links(root, strict=False, check_orphans=True)
    validation_findings = validate_wiki(root, strict=False)
    claim_findings = audit_claims(root, strict=False)
    scoring_codes = {"compatibility-score", "compatibility-weights", "absolute-percentage"}
    scoring_hits = [item.as_dict() for item in claim_findings if item.code in scoring_codes]
    active_orphans = sorted(
        group_name
        for group_name, members in groups.items()
        if any(page.status == "active" for page in members)
        and not {source for source in inbound_groups[group_name] if source != group_name}
    )

    status_counts = Counter(page.status for page in pages)
    claim_status_counts = Counter(
        str(item)
        for page in pages
        for item in as_list(page.metadata.get("claim_status"))
    )
    claim_id_status_counts = Counter(
        status for page in pages for status in claim_map(page.metadata).values()
    )
    return {
        "schema_version": 1,
        "audited_baseline": AUDITED_BASELINE,
        "current_summary": {
            "pages": len(pages),
            "translation_groups": len(groups),
            "complete_triads": complete_triads,
            "missing_language_files": missing_language_files,
            "document_statuses": dict(sorted(status_counts.items())),
            "page_claim_statuses": dict(sorted(claim_status_counts.items())),
            "identified_claim_statuses": dict(sorted(claim_id_status_counts.items())),
            "groups_with_duplicate_locales": duplicate_locale_groups,
            "active_orphan_groups": len(active_orphans),
        },
        "pages": page_records,
        "language_groups": group_records,
        "orphans": active_orphans,
        "hits": {
            "simulation": sorted(simulation_hits, key=lambda item: (item["path"], item["line"])),
            "numeric_scoring": scoring_hits,
            "old_model": sorted(old_model_hits, key=lambda item: (item["path"], item["line"], item["code"])),
        },
        "link_findings": [item.as_dict() for item in link_findings],
        "validation_findings": [item.as_dict() for item in validation_findings],
    }


def render_inventory(root: Path) -> str:
    return json.dumps(build_inventory(root), ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true", help="fail when --output is stale")
    args = parser.parse_args()

    root = args.root.resolve()
    rendered = render_inventory(root)
    if args.output is None:
        print(rendered, end="")
        return 0
    output = args.output if args.output.is_absolute() else root / args.output
    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != rendered:
            print(f"ERROR: {output} is stale; regenerate without --check")
            return 1
        print(f"OK: {output} is up to date")
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
