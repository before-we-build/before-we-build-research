#!/usr/bin/env python3
"""Fail when generated wiki HTML references a missing local file."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


REFERENCE_ATTRIBUTES = {
    "a": "href",
    "audio": "src",
    "img": "src",
    "link": "href",
    "script": "src",
    "source": "src",
    "video": "src",
}


@dataclass(frozen=True)
class Reference:
    url: str
    line: int


@dataclass(frozen=True)
class BrokenReference:
    source: Path
    url: str
    line: int
    reason: str


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[Reference] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attribute = REFERENCE_ATTRIBUTES.get(tag)
        if not attribute:
            return
        values = dict(attrs)
        url = values.get(attribute)
        if url:
            self.references.append(Reference(url=url, line=self.getpos()[0]))


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def check_generated_links(
    wiki_root: Path, site_root: Path | None = None
) -> list[BrokenReference]:
    wiki_root = wiki_root.resolve()
    site_root = (site_root or wiki_root.parent).resolve()

    if not wiki_root.is_dir():
        raise ValueError(f"wiki root does not exist: {wiki_root}")
    if not site_root.is_dir():
        raise ValueError(f"site root does not exist: {site_root}")
    if not _is_within(wiki_root, site_root):
        raise ValueError(f"wiki root {wiki_root} is outside site root {site_root}")

    broken: list[BrokenReference] = []
    for source in sorted(wiki_root.rglob("*.html")):
        parser = ReferenceParser()
        parser.feed(source.read_text(encoding="utf-8"))

        for reference in parser.references:
            parsed = urlsplit(reference.url)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue

            decoded_path = unquote(parsed.path)
            if decoded_path.startswith("/"):
                target = (site_root / decoded_path.lstrip("/")).resolve()
            else:
                target = (source.parent / decoded_path).resolve()

            if not _is_within(target, site_root):
                broken.append(
                    BrokenReference(
                        source=source,
                        url=reference.url,
                        line=reference.line,
                        reason="reference escapes the site root",
                    )
                )
                continue

            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                broken.append(
                    BrokenReference(
                        source=source,
                        url=reference.url,
                        line=reference.line,
                        reason=f"target does not exist: {target}",
                    )
                )

    return broken


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check local references in generated wiki HTML"
    )
    parser.add_argument("--root", type=Path, required=True, help="Generated wiki directory")
    parser.add_argument(
        "--site-root",
        type=Path,
        help="Website root; defaults to the parent of --root",
    )
    args = parser.parse_args()

    try:
        broken = check_generated_links(args.root, args.site_root)
    except ValueError as error:
        print(f"ERROR: {error}")
        return 2

    if broken:
        for item in broken:
            print(f"ERROR {item.source}:{item.line}: {item.url!r}: {item.reason}")
        print(f"\nSummary: {len(broken)} broken generated reference(s)")
        return 1

    page_count = sum(1 for _ in args.root.rglob("*.html"))
    print(f"OK: checked local references in {page_count} generated HTML page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
