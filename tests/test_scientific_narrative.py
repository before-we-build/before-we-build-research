from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from check_scientific_narrative import (
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


if __name__ == "__main__":
    unittest.main()
