from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_wiki_site import build_site, render_markdown_to_html


class WikiSiteReadabilityTests(unittest.TestCase):
    def render(self, text):
        return render_markdown_to_html(text, "ru", {}, title_map={})[0]

    def test_source_wrapping_does_not_fragment_paragraphs(self):
        rendered = self.render("Первая часть\nпродолжение мысли.\n\nНовый абзац.\n## Раздел\nТекст")
        self.assertIn("<p>Первая часть продолжение мысли.</p>", rendered)
        self.assertEqual(rendered.count("<p>"), 3)
        self.assertIn("<h2", rendered)

    def test_lists_keep_sequence_and_wrapped_item_text(self):
        rendered = self.render("3. Обсудить\n   решение.\n4. Проверить\n\n- Первый\n  пункт\n- Второй")
        self.assertIn('<ol start="3"><li>', rendered.replace("\n", ""))
        self.assertIn("<li>Обсудить решение.</li>", rendered)
        self.assertIn("<li>Первый пункт</li>", rendered)
        self.assertEqual(rendered.count("<li>"), 4)

    def test_plain_links_use_titles_and_explicit_labels_are_preserved(self):
        rendered, _ = render_markdown_to_html(
            "[[sample-ru]] и [[sample-ru|свой текст]]", "ru",
            {"sample-ru": "concepts/sample-ru.html"}, wiki_root_prefix="../", title_map={"sample-ru": "Понятное название"},
        )
        self.assertIn('href="../concepts/sample-ru.html">Понятное название</a>', rendered)
        self.assertIn('>свой текст</a>', rendered)

    def test_code_and_table_remain_separate_from_paragraphs(self):
        rendered = self.render("Введение\n```text\nпервая\nвторая\n```\n\n| A | B |\n|---|---|\n| 1 | 2 |")
        self.assertIn("<p>Введение</p>", rendered)
        self.assertIn("первая\nвторая</code></pre>", rendered)
        self.assertIn("<td>2</td>", rendered)

    def test_built_root_and_nested_pages_have_readable_working_navigation(self):
        with tempfile.TemporaryDirectory() as directory:
            with redirect_stdout(io.StringIO()):
                build_site(Path(directory))
            root = Path(directory)
            start = (root / "start-here-ru.html").read_text()
            article = (root / "concepts/main-idea-ru.html").read_text()
            self.assertEqual(start.count("<h1"), 1)
            self.assertEqual(article.count("<h1"), 1)
            self.assertIn('href="./start-here-en.html"', start)
            self.assertIn('href="../concepts/main-idea-en.html"', article)
            self.assertIn('href="./concepts/main-idea-ru.html"', start)
            self.assertIn('href="../concepts/four-level-compatibility-architecture-ru.html"', article)
            self.assertNotIn(">Latent Process</a>", article)
            self.assertNotIn("four-levels-of-compatibility-", article)


if __name__ == "__main__":
    unittest.main()
