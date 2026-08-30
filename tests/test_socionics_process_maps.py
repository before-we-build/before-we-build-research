from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from normalize_entity_triads import (  # noqa: E402
    SOCIONICS_ASPECT_OPERATIONS,
    SOCIONICS_POSITION_MODES,
    SOCIONICS_STACKS,
)


STACK_ITEM_RE = re.compile(r"([1-8])(Ne|Se|Te|Fe|Ni|Si|Ti|Fi)")
PROCESS_ROW_RE = re.compile(
    r"^\|\s*([1-8])\s*\|\s*(Ne|Se|Te|Fe|Ni|Si|Ti|Fi)\s*\|",
    re.MULTILINE,
)
TYPE_FILE_RE = re.compile(r"^([a-z]{3})-.+-(?:extrovert|introvert)-(en|ru|uk)\.md$")


class SocionicsCanonicalStackTests(unittest.TestCase):
    def test_all_sixteen_stacks_have_unique_positions_and_aspects(self) -> None:
        self.assertEqual(len(SOCIONICS_STACKS), 16)
        for code, notation in SOCIONICS_STACKS.items():
            entries = [(int(position), aspect) for position, aspect in STACK_ITEM_RE.findall(notation)]
            with self.subTest(code=code):
                self.assertEqual(len(entries), 8)
                self.assertEqual({position for position, _ in entries}, set(range(1, 9)))
                self.assertEqual(
                    {aspect for _, aspect in entries},
                    {"Ne", "Se", "Te", "Fe", "Ni", "Si", "Ti", "Fi"},
                )

    def test_all_type_triads_match_the_canonical_stack(self) -> None:
        entity_dir = REPOSITORY_ROOT / "wiki" / "entities"
        found: dict[str, dict[str, list[tuple[int, str, str, str]]]] = {}

        for path in sorted(entity_dir.glob("*.md")):
            match = TYPE_FILE_RE.match(path.name)
            if not match:
                continue
            code, lang = match.groups()
            code = code.upper()
            self.assertIn(code, SOCIONICS_STACKS, path.name)
            text = path.read_text(encoding="utf-8")
            rows: list[tuple[int, str, str, str]] = []
            for line in text.splitlines():
                if not PROCESS_ROW_RE.match(line):
                    continue
                fields = [field.strip() for field in line.strip().split("|")[1:-1]]
                rows.append((int(fields[0]), fields[1], fields[2], fields[3]))
            found.setdefault(code, {})[lang] = rows

        self.assertEqual(set(found), set(SOCIONICS_STACKS))
        self.assertEqual(sum(len(peers) for peers in found.values()), 48)

        for code, peers in found.items():
            with self.subTest(code=code):
                self.assertEqual(set(peers), {"en", "ru", "uk"})
                for lang in ("en", "ru", "uk"):
                    expected = [
                        (
                            int(position),
                            aspect,
                            SOCIONICS_ASPECT_OPERATIONS[lang][aspect],
                            SOCIONICS_POSITION_MODES[lang][int(position)],
                        )
                        for position, aspect in STACK_ITEM_RE.findall(SOCIONICS_STACKS[code])
                    ]
                    self.assertEqual(peers[lang], expected)


if __name__ == "__main__":
    unittest.main()
