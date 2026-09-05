from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from build_wiki_site import build_site, render_markdown_to_html  # noqa: E402
from check_generated_wiki_links import check_generated_links  # noqa: E402


class GeneratedWikiLinkTests(unittest.TestCase):
    def test_nested_wikilink_is_relative_to_wiki_root(self) -> None:
        rendered, _ = render_markdown_to_html(
            "See [[target-en|Target]].",
            "en",
            {"target-en": "concepts/target-en.html"},
            "../",
        )

        self.assertIn('href="../concepts/target-en.html"', rendered)

    def test_checker_accepts_existing_wiki_and_site_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            site_root = Path(temporary_directory)
            wiki_root = site_root / "wiki"
            concepts = wiki_root / "concepts"
            concepts.mkdir(parents=True)
            (site_root / "index.html").write_text("site", encoding="utf-8")
            (wiki_root / "index.html").write_text("wiki", encoding="utf-8")
            (concepts / "target.html").write_text("target", encoding="utf-8")
            (concepts / "source.html").write_text(
                '<a href="../concepts/target.html">Target</a>'
                '<a href="../../index.html">Site</a>',
                encoding="utf-8",
            )

            self.assertEqual(check_generated_links(wiki_root, site_root), [])

    def test_checker_reports_missing_and_escaping_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            site_root = Path(temporary_directory) / "site"
            wiki_root = site_root / "wiki"
            wiki_root.mkdir(parents=True)
            (wiki_root / "source.html").write_text(
                '<a href="missing.html">Missing</a>'
                '<a href="../../outside.html">Outside</a>',
                encoding="utf-8",
            )

            broken = check_generated_links(wiki_root, site_root)

            self.assertEqual(len(broken), 2)
            self.assertIn("target does not exist", broken[0].reason)
            self.assertEqual(broken[1].reason, "reference escapes the site root")

    def test_complete_generated_wiki_has_no_broken_local_references(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            site_root = Path(temporary_directory)
            wiki_root = site_root / "wiki"
            assets = site_root / "assets"
            assets.mkdir()
            for relative_path in (
                "index.html",
                "relations-calculator.html",
                "manifest.webmanifest",
                "assets/icon.svg",
                "assets/site.css",
            ):
                target = site_root / relative_path
                target.write_text("placeholder", encoding="utf-8")

            build_site(wiki_root)

            self.assertEqual(check_generated_links(wiki_root, site_root), [])


if __name__ == "__main__":
    unittest.main()
