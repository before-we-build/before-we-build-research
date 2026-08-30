from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from check_wikilinks import check_links  # noqa: E402
from migrate_wiki_language_paths import rewrite_links  # noqa: E402


class MigrationLinkHardeningTests(unittest.TestCase):
    def test_two_writes_preserve_discovered_migration_history(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            page = root / "wiki" / "sample.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "---\ntitle: Sample\nlang: en\n---\n# Sample\n",
                encoding="utf-8",
            )
            command = [
                sys.executable,
                str(REPOSITORY_ROOT / "scripts" / "migrate_wiki_language_paths.py"),
                "--write",
                "--root",
                str(root),
            ]

            subprocess.run(command, check=True, capture_output=True, text=True)
            manifest_path = root / "wiki" / "slug-migrations.json"
            first = manifest_path.read_bytes()
            first_manifest = json.loads(first)
            self.assertEqual(
                first_manifest["migrations"]["wiki/sample.md"],
                "wiki/sample-en.md",
            )

            subprocess.run(command, check=True, capture_output=True, text=True)
            self.assertEqual(manifest_path.read_bytes(), first)

            check_command = command.copy()
            check_command[2] = "--check"
            subprocess.run(
                check_command, check=True, capture_output=True, text=True
            )
            self.assertEqual(manifest_path.read_bytes(), first)

    def test_localizes_anchored_and_path_qualified_wikilinks(self) -> None:
        groups = {
            "sample": {
                lang: Path(f"/repo/wiki/concepts/sample-{lang}.md")
                for lang in ("en", "ru", "uk")
            },
            "project-positioning": {
                lang: Path(f"/repo/wiki/concepts/project-positioning-{lang}.md")
                for lang in ("en", "ru", "uk")
            },
        }
        migrated = rewrite_links(
            "[[concepts/sample#overview|Читать]]\n"
            "[[wiki/concepts/sample.md#details|Подробнее]]\n"
            "[[concepts/sample-en#explicit|English]]\n"
            "[[concepts/project-main-goal#scope|Позиционирование]]\n",
            "ru",
            groups,
            {
                "wiki/concepts/sample.md": "wiki/concepts/sample-en.md",
                "wiki/concepts/project-main-goal.md": (
                    "wiki/concepts/project-positioning-en.md"
                ),
            },
        )

        self.assertIn("[[concepts/sample-ru#overview|Читать]]", migrated)
        self.assertIn(
            "[[wiki/concepts/sample-ru.md#details|Подробнее]]", migrated
        )
        self.assertIn("[[concepts/sample-en#explicit|English]]", migrated)
        self.assertIn(
            "[[concepts/project-positioning-ru#scope|Позиционирование]]",
            migrated,
        )

    def test_markdown_rewrite_distinguishes_raw_and_wiki_basename_collision(self) -> None:
        groups = {
            "guru": {
                lang: Path(f"/repo/wiki/entities/guru-{lang}.md")
                for lang in ("en", "ru", "uk")
            }
        }
        source = (
            '[raw](../raw/temporistics/guru.md#source "Raw source")\n'
            '[wiki](../wiki/entities/guru.md#meaning "Wiki page")\n'
            "[ambiguous](guru.md)\n"
            "sources: [raw/temporistics/guru.md]\n"
            "wiki/entities/guru.md\n"
        )
        migrated = rewrite_links(
            source,
            "ru",
            groups,
            {"wiki/entities/guru.md": "wiki/entities/guru-en.md"},
            {"guru.md"},
        )

        self.assertIn(
            '[raw](../raw/temporistics/guru.md#source "Raw source")', migrated
        )
        self.assertIn(
            '[wiki](../wiki/entities/guru-ru.md#meaning "Wiki page")', migrated
        )
        self.assertIn("[ambiguous](guru.md)", migrated)
        self.assertIn("sources: [raw/temporistics/guru.md]", migrated)
        self.assertIn("wiki/entities/guru-ru.md", migrated)


class LinkCheckerHardeningTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_path_qualified_raw_reference_is_not_an_old_wiki_slug(self) -> None:
        self.write("README.md", "[preserved source](raw/general/research-program.md)\n")
        self.write("raw/general/research-program.md", "# Preserved raw source\n")
        self.write(
            "wiki/slug-migrations.json",
            json.dumps(
                {
                    "schema_version": 1,
                    "migrations": {
                        "wiki/sources/research-program.md": (
                            "wiki/concepts/validation-program-en.md"
                        )
                    },
                }
            ),
        )

        diagnostics = check_links(self.root, strict=True, check_orphans=False)
        self.assertNotIn("old-slug", {item.code for item in diagnostics})
        self.assertEqual(diagnostics, [])

    def test_default_scan_covers_instruments_and_opencode_documentation(self) -> None:
        self.write("instruments/pilot.md", "[missing](instrument-missing.md)\n")
        self.write(".opencode/agents/reviewer.md", "[missing](agent-missing.md)\n")
        self.write(".opencode/ORGANIZATION.md", "[missing](organization-missing.md)\n")

        diagnostics = check_links(self.root, strict=True, check_orphans=False)
        missing_paths = {
            item.path for item in diagnostics if item.code == "missing-link"
        }
        self.assertEqual(
            missing_paths,
            {
                "instruments/pilot.md",
                ".opencode/agents/reviewer.md",
                ".opencode/ORGANIZATION.md",
            },
        )


if __name__ == "__main__":
    unittest.main()
