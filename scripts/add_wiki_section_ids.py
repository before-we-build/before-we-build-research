#!/usr/bin/env python3
"""Add equal stable section markers to headings in every active wiki triad.

The English peer supplies an existing marker or a stable slug for each level
2-6 heading. Russian and Ukrainian peers receive the same IDs by heading
position. A structural mismatch is reported instead of guessed.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from check_wikilinks import _mask_code
from wiki_quality_common import LOCALES, SECTION_MARKER_RE, WikiPage, load_wiki_pages


HEADING_RE = re.compile(r"^(#{2,6})[ \t]+(.+?)\s*$")
MARKER_LINE_RE = re.compile(
    r"^\s*<!--\s*section:([a-z0-9][a-z0-9._-]*)\s*-->\s*$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class HeadingSlot:
    line_index: int
    level: int
    title: str
    marker: str | None


def heading_slots(body: str) -> list[HeadingSlot]:
    original = body.splitlines(keepends=True)
    masked = _mask_code(body).splitlines(keepends=True)
    slots: list[HeadingSlot] = []
    for index, masked_line in enumerate(masked):
        match = HEADING_RE.match(masked_line.rstrip("\r\n"))
        if not match:
            continue
        original_match = HEADING_RE.match(original[index].rstrip("\r\n"))
        previous = index - 1
        while previous >= 0 and not original[previous].strip():
            previous -= 1
        marker_match = (
            MARKER_LINE_RE.match(original[previous].rstrip("\r\n"))
            if previous >= 0
            else None
        )
        slots.append(
            HeadingSlot(
                line_index=index,
                level=len(match.group(1)),
                title=(original_match.group(2) if original_match else match.group(2)).strip(),
                marker=marker_match.group(1).lower() if marker_match else None,
            )
        )
    return slots


def _slug(title: str, index: int, used: set[str]) -> str:
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
    plain = re.sub(r"<[^>]+>|[*_~`]", "", plain)
    plain = unicodedata.normalize("NFKD", plain).encode("ascii", "ignore").decode()
    base = re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")
    if not base:
        base = f"section-{index:02d}"
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def desired_ids(reference: list[HeadingSlot], reserved: set[str] | None = None) -> list[str]:
    used: set[str] = set(reserved or set())
    result: list[str] = []
    for index, slot in enumerate(reference, start=1):
        if slot.marker:
            marker = slot.marker
            if marker in used:
                # The validator will report duplicate pre-existing markers.
                marker = _slug(slot.title, index, used)
            else:
                used.add(marker)
            result.append(marker)
        else:
            result.append(_slug(slot.title, index, used))
    return result


def _insert_markers(body: str, slots: list[HeadingSlot], ids: list[str]) -> str:
    lines = body.splitlines(keepends=True)
    for slot, section_id in reversed(list(zip(slots, ids))):
        if slot.marker is None:
            lines.insert(slot.line_index, f"<!-- section:{section_id} -->\n")
    return "".join(lines)


def _insert_content_marker(body: str) -> str:
    lines = body.splitlines(keepends=True)
    index = next(
        (i + 1 for i, line in enumerate(lines) if re.match(r"^#\s+", line)),
        0,
    )
    lines.insert(index, "\n<!-- section:content -->\n")
    return "".join(lines)


def synchronize_section_ids(root: Path, *, write: bool) -> tuple[list[str], list[Path]]:
    pages = load_wiki_pages(root)
    groups: dict[str, list[WikiPage]] = defaultdict(list)
    for page in pages:
        if page.status == "active":
            groups[page.translation_group].append(page)

    issues: list[str] = []
    changed: list[Path] = []
    for group_name, members in sorted(groups.items()):
        by_language: dict[str, list[WikiPage]] = defaultdict(list)
        for page in members:
            by_language[page.language or "unknown"].append(page)
        if set(by_language) != set(LOCALES) or any(len(items) != 1 for items in by_language.values()):
            issues.append(f"{group_name}: expected exactly one EN/RU/UK page")
            continue

        reference_page = by_language["en"][0]
        reference_slots = heading_slots(reference_page.body)
        attached = {slot.marker for slot in reference_slots if slot.marker}
        reserved = set(reference_page.section_ids) - attached
        ids = desired_ids(reference_slots, reserved)
        structures = [[slot.level for slot in reference_slots]]
        group_slots: dict[str, list[HeadingSlot]] = {"en": reference_slots}
        blocked = False
        for language in ("ru", "uk"):
            slots = heading_slots(by_language[language][0].body)
            group_slots[language] = slots
            structures.append([slot.level for slot in slots])
        structure_lists = structures
        if any(items != structure_lists[0] for items in structure_lists[1:]):
            issues.append(
                f"{group_name}: heading level/count drift EN={structure_lists[0]} "
                f"RU={structure_lists[1]} UK={structure_lists[2]}"
            )
            continue

        for language in LOCALES:
            for slot, expected in zip(group_slots[language], ids):
                if slot.marker is not None and slot.marker != expected:
                    issues.append(
                        f"{group_name}/{language}: marker '{slot.marker}' must be '{expected}' "
                        f"before heading '{slot.title}'"
                    )
                    blocked = True
        if blocked:
            continue

        if not reference_slots:
            for language in LOCALES:
                page = by_language[language][0]
                if page.section_ids:
                    continue
                if not write:
                    issues.append(f"{group_name}/{language}: page has no stable section marker")
                    continue
                before = page.path.read_text(encoding="utf-8")
                frontmatter_length = len(before) - len(page.body)
                page.path.write_text(
                    before[:frontmatter_length] + _insert_content_marker(page.body),
                    encoding="utf-8",
                )
                changed.append(page.path)
            continue

        for language in LOCALES:
            page = by_language[language][0]
            slots = group_slots[language]
            if not any(slot.marker is None for slot in slots):
                continue
            if not write:
                missing = sum(slot.marker is None for slot in slots)
                issues.append(
                    f"{group_name}/{language}: {missing} heading(s) lack section markers"
                )
                continue
            before = page.path.read_text(encoding="utf-8")
            frontmatter_length = len(before) - len(page.body)
            after_body = _insert_markers(page.body, slots, ids)
            page.path.write_text(before[:frontmatter_length] + after_body, encoding="utf-8")
            changed.append(page.path)

    return issues, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    issues, changed = synchronize_section_ids(args.root.resolve(), write=args.write)
    for issue in issues:
        print(f"ERROR: {issue}")
    if changed:
        print(f"Updated {len(changed)} wiki page(s)")
    elif not issues:
        print("OK: all active headings have synchronized section IDs")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
