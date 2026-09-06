from __future__ import annotations

import sys
import contextlib
import io
import json
import tempfile
from unittest.mock import patch
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from check_scientific_narrative import (
    main,
    analyze_document,
    detect_language,
    parse_markdown_paragraphs,
)


class ClicheDetectorTests(unittest.TestCase):
    def test_russian_cliches_detected(self) -> None:
        text = "В современном мире ни для кого не секрет, что эта идея играет ключевую роль."
        doc = analyze_document(Path("test-ru.md"), text)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("cliche-modern-world", codes)
        self.assertIn("cliche-no-secret", codes)
        self.assertIn("cliche-plays-role", codes)

    def test_english_cliches_detected(self) -> None:
        text = "In today's fast-paced world, it goes without saying that let's delve into this topic."
        doc = analyze_document(Path("test-en.md"), text)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("cliche-today-world", codes)
        self.assertIn("cliche-goes-without-saying", codes)
        self.assertIn("cliche-delve-into", codes)

    def test_ukrainian_cliches_detected(self) -> None:
        text = "У сучасному світі ні для кого не секрет, що цей фактор відіграє ключову роль."
        doc = analyze_document(Path("test-uk.md"), text)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("cliche-modern-world", codes)
        self.assertIn("cliche-no-secret", codes)
        self.assertIn("cliche-plays-role", codes)

    def test_clean_text_has_no_cliche_flags(self) -> None:
        text = "Мы сидели на кухне и наблюдали за тем, как закипает медный чайник с узким носиком."
        doc = analyze_document(Path("test-clean.md"), text)
        cliche_codes = [d.code for d in doc.diagnostics if d.code.startswith("cliche-")]
        self.assertEqual(len(cliche_codes), 0)


class EpistemicInflationTests(unittest.TestCase):
    def test_flags_unsupported_guarantees(self) -> None:
        text = "Этот соционический тип на 100% определяет поведение человека и гарантирует совместимость в браке."
        doc = analyze_document(Path("test-epistemic-ru.md"), text, strict=True)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("epistemic-fatal-determinism", codes)
        self.assertIn("epistemic-guarantee-outcome", codes)

    def test_allows_negated_and_qualified_cautions(self) -> None:
        text = "Важно подчеркнуть, что типологическая модель не гарантирует совместимость и не определяет судьбу."
        # Negated claims ("не гарантирует", "не определяет") must not trigger epistemic inflation
        doc = analyze_document(Path("test-negated-ru.md"), text)
        epistemic_codes = [d.code for d in doc.diagnostics if d.code.startswith("epistemic-")]
        self.assertEqual(len(epistemic_codes), 0)

    def test_english_epistemic_inflation(self) -> None:
        text = "This type model is scientifically proven typology and guarantees compatibility between partners."
        doc = analyze_document(Path("test-epistemic-en.md"), text, strict=True)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("epistemic-proven-typology", codes)
        self.assertIn("epistemic-guarantee-outcome", codes)


class SentenceAndParagraphComplexityTests(unittest.TestCase):
    def test_flags_overlong_sentence(self) -> None:
        # Sentence with 40 words
        long_sentence = " ".join(["слово"] * 40) + "."
        doc = analyze_document(Path("test-len-ru.md"), long_sentence)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("overlong-sentence", codes)

    def test_flags_extreme_sentence_overload(self) -> None:
        # Sentence with 65 words
        huge_sentence = " ".join(["термин"] * 65) + "."
        doc = analyze_document(Path("test-extreme-ru.md"), huge_sentence)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("extreme-sentence-overload", codes)

    def test_flags_overlong_paragraph(self) -> None:
        # Paragraph with 180 words in short sentences
        paragraph = " ".join(["Короткая фраза здесь."] * 60)
        doc = analyze_document(Path("test-para-ru.md"), paragraph)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("overlong-paragraph", codes)

    def test_detects_nested_parentheses(self) -> None:
        text = "Это простое утверждение (с уточнением (которое содержит еще одно (вложенное) примечание)) требует внимания."
        doc = analyze_document(Path("test-paren.md"), text)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("deep-parentheses", codes)


class CognitiveHazardAndCitationTests(unittest.TestCase):
    def test_citation_blockquotes_are_exempted_from_stylistic_penalties(self) -> None:
        quote = "> В современном мире ни для кого не секрет, что эта цитата из старого трактата очень длинная и многословная.\n\nАвторский чистый текст идет следом."
        doc = analyze_document(Path("test-cite.md"), quote)
        cliche_codes = [d.code for d in doc.diagnostics if d.code.startswith("cliche-")]
        self.assertEqual(len(cliche_codes), 0)
        self.assertGreater(doc.citation_word_count, 0)

    def test_sustained_fatigue_zone_detected(self) -> None:
        # Create 3 consecutive paragraphs each with C_j >= 2
        bad_p1 = "В современном мире " + " ".join(["слово"] * 40) + "."
        bad_p2 = "Ни для кого не секрет, что " + " ".join(["факт"] * 40) + "."
        bad_p3 = "Как известно, " + " ".join(["наблюдение"] * 40) + "."
        text = f"{bad_p1}\n\n{bad_p2}\n\n{bad_p3}"

        doc = analyze_document(Path("test-fatigue.md"), text)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("sustained-cognitive-fatigue", codes)
        self.assertGreaterEqual(len(doc.sustained_fatigue_zones), 1)


class GroundTruthBenchmarkTests(unittest.TestCase):
    def test_canonical_exposition_achieves_high_score(self) -> None:
        expo_path = REPOSITORY_ROOT / "raw" / "general" / "latent-process-narrative-exposition.md"
        self.assertTrue(expo_path.exists())
        doc = analyze_document(expo_path)
        self.assertGreaterEqual(doc.score, 85.0)
        self.assertGreaterEqual(doc.questions_count, 15)
        self.assertEqual(len(doc.sustained_fatigue_zones), 0)

    def test_bad_synthetic_text_fails_threshold(self) -> None:
        bad_text = (
            "В современном мире ни для кого не секрет, что типологическая модель жестко детерминирует "
            + " ".join(["и фатально предопределяет судьбу"] * 10)
            + " и гарантирует совместимость.\n\n"
            "Давайте погрузимся в этот вопрос (хотя это (очевидно (всем))), ведь это играет ключевую роль "
            + " ".join(["в бесконечно длинном потоке канцелярита"] * 8)
            + ".\n\n"
            "Стоит подчеркнуть, что научно доказанная типология на 100% определяет характер "
            + " ".join(["без всяких сомнений и без единого вопроса читателя"] * 6)
            + "."
        )
        doc = analyze_document(Path("synthetic-bad.md"), bad_text, strict=True, min_score=75.0)
        self.assertLess(doc.score, 60.0)
        codes = {d.code for d in doc.diagnostics}
        self.assertIn("readability-score-below-threshold", codes)



class PublicWikiAuditTests(unittest.TestCase):
    def test_default_audits_every_published_markdown_including_nested_and_readme(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = ["wiki/start-here-en.md", "wiki/concepts/example-ru.md", "wiki/README.md"]
            for name in paths:
                page = root / name
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text("A clear explanation.", encoding="utf-8")
            # An unpublished raw source must not replace or join the default corpus.
            (root / "raw").mkdir()
            (root / "raw/source.md").write_text("Source text.", encoding="utf-8")
            output = io.StringIO()
            with patch("check_scientific_narrative.REPO_ROOT", root), patch.object(
                sys, "argv", ["checker", "--strict", "--json"]
            ), contextlib.redirect_stdout(output):
                self.assertEqual(main(), 0)
            summaries = json.loads(output.getvalue())["summary"]
            self.assertEqual({Path(row["path"]).name for row in summaries},
                             {Path(name).name for name in paths})

    def test_empty_default_corpus_fails(self):
        with tempfile.TemporaryDirectory() as directory, patch(
            "check_scientific_narrative.REPO_ROOT", Path(directory)
        ), patch.object(sys, "argv", ["checker", "--strict"]), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main()
            self.assertEqual(raised.exception.code, 2)

    def test_explicit_source_path_still_blocks_bad_text(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "source-en.md"
            page.write_text("This model guarantees compatibility.", encoding="utf-8")
            output = io.StringIO()
            with patch.object(sys, "argv", ["checker", str(page), "--strict", "--json"]), contextlib.redirect_stdout(output):
                self.assertEqual(main(), 1)
            self.assertEqual(len(json.loads(output.getvalue())["summary"]), 1)

    def test_bold_sentence_start_does_not_merge_sentences(self):
        text = " ".join(["word"] * 28) + ". **Another " + " ".join(["word"] * 27) + ".**"
        doc = analyze_document(Path("example-en.md"), text, strict=True)
        self.assertEqual(doc.sentence_count, 2)
        self.assertFalse(any(d.code == "extreme-sentence-overload" for d in doc.diagnostics))

    def test_avoid_claims_caution_does_not_hide_next_sentence_guarantee(self):
        caution = "Avoid claims about a chosen spouse, guaranteed family outcome, ideal pair, or a type-based decision."
        doc = analyze_document(Path("example-en.md"), caution, strict=True)
        self.assertFalse(any(d.code.startswith("epistemic-") for d in doc.diagnostics))
        doc = analyze_document(Path("example-en.md"), caution + " This model guarantees compatibility.", strict=True)
        self.assertTrue(any(d.code == "epistemic-guarantee-outcome" for d in doc.diagnostics))

if __name__ == "__main__":
    unittest.main()
