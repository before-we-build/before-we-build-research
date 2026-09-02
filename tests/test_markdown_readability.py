from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import MagicMock, patch

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from check_markdown_readability import (  # noqa: E402
    EvaluationResult,
    GoldenProfileCase,
    GoldenProfileRegistry,
    build_evaluation_prompt,
    check_file,
    evaluate_with_agy,
    format_report_console,
    get_git_files,
    show_golden_benchmarks,
    static_analyze_markdown,
)


class GoldenProfileRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = GoldenProfileRegistry(REPOSITORY_ROOT)

    def test_registry_contains_real_ground_truth_cases(self) -> None:
        self.assertGreaterEqual(len(self.registry.cases), 5)
        names = {c.subject_name for c in self.registry.cases}
        self.assertIn("Юрий Дудь", names)
        self.assertIn("Алишер Моргенштерн", names)
        self.assertIn("Валерий Залужный", names)

    def test_find_relevant_cases_by_person_name(self) -> None:
        matches = self.registry.find_relevant_cases("Здесь анализируется стиль интервью Юрия Дудя")
        self.assertTrue(any(case.subject_name == "Юрий Дудь" for case, _ in matches))

    def test_find_relevant_cases_by_latent_process_3v(self) -> None:
        matches = self.registry.find_relevant_cases("Чувствительность к статусу и 3В (третья воля)")
        subjects = {case.subject_name for case, _ in matches}
        self.assertTrue("Алишер Моргенштерн" in subjects or "Композитный DevOps-эталон (СЛИ + ЭЛВФ + ВПНБ)" in subjects)

    def test_show_golden_benchmarks_outputs_person_and_example(self) -> None:
        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = show_golden_benchmarks("дудь", self.registry)
        self.assertEqual(ret, 0)
        output = buf.getvalue()
        self.assertIn("Юрий Дудь", output)
        self.assertIn("Пример из жизни", output)
        self.assertIn("Колыма", output)


class MarkdownReadabilityStaticTests(unittest.TestCase):
    def test_static_analysis_detects_shared_example_section(self) -> None:
        content = """# Concept

<!-- section:in-90-seconds -->
## Summary

<!-- section:shared-example -->
## Shared Example

Two colleagues, Alice and Bob, are discussing project deadlines.
"""
        result = static_analyze_markdown(content)
        self.assertTrue(result.has_example_section)
        self.assertTrue(result.has_example_heading)
        self.assertGreater(result.word_count, 10)

    def test_static_analysis_detects_russian_example_heading(self) -> None:
        content = """# Концепция

## Жизненный пример

Муж и жена планируют отпуск и спорят о билетах.
"""
        result = static_analyze_markdown(content)
        self.assertFalse(result.has_example_section)
        self.assertTrue(result.has_example_heading)

    def test_static_analysis_detects_ukrainian_example_heading(self) -> None:
        content = """# Концепція

## Спільний приклад

Колеги обговорюють розподіл завдань у команді.
"""
        result = static_analyze_markdown(content)
        self.assertTrue(result.has_example_heading)

    def test_static_analysis_detects_lack_of_examples(self) -> None:
        content = """# Pure Theory

Here is an abstract mathematical representation of categorical morphisms.
No humans or situations are mentioned.
"""
        result = static_analyze_markdown(content)
        self.assertFalse(result.has_example_section)
        self.assertFalse(result.has_example_heading)


class PromptAndParserTests(unittest.TestCase):
    def test_prompt_generation_contains_golden_cases(self) -> None:
        matched_cases = [
            (
                GoldenProfileCase(
                    subject_name="Юрий Дудь",
                    doc_path="docs/detailed-typology-dud.md",
                    socionics_code="ЛИЭ",
                    psychosophy_code="ФВЛЭ",
                    temporistics_code="НПБВ",
                    value_moral_summary="Свобода слова",
                    process_manifestations=[
                        {
                            "level": "Operational",
                            "aspect_position": "3Л (Логика)",
                            "process": "Скептический аудит смет",
                            "example": "Откуда эта сумма?",
                        }
                    ],
                ),
                [
                    {
                        "level": "Operational",
                        "aspect_position": "3Л (Логика)",
                        "process": "Скептический аудит смет",
                        "example": "Откуда эта сумма?",
                    }
                ],
            )
        ]
        prompt = build_evaluation_prompt("# Title\nBody text", "wiki/sample.md", matched_cases)
        self.assertIn("Vanka the Layman", prompt)
        self.assertIn("ЭТАЛОННЫЕ КЕЙСЫ ИЗ ЗОЛОТЫХ ПРОФИЛЕЙ", prompt)
        self.assertIn("Юрий Дудь", prompt)
        self.assertIn("Откуда эта сумма?", prompt)

    @patch("shutil.which", return_value="/usr/local/bin/agy")
    @patch("subprocess.run")
    def test_evaluate_with_agy_parses_json_output(
        self, mock_run: MagicMock, mock_which: MagicMock
    ) -> None:
        mock_output = json.dumps({
            "readability_score": 9,
            "has_life_examples": True,
            "clarity_verdict": "PASS",
            "summary": "Текст написан понятно и живо.",
            "life_examples_found": ["Диалог двух коллег на кухне"],
            "unclear_jargon_or_passages": [],
            "suggestions": ["Добавить еще один подзаголовок"],
        })
        mock_run.return_value = subprocess.CompletedProcess(
            args=["agy", "-p", "..."],
            returncode=0,
            stdout=f"```json\n{mock_output}\n```",
            stderr="",
        )

        res = evaluate_with_agy("Sample text", "test.md")
        self.assertTrue(res.is_valid)
        self.assertEqual(res.readability_score, 9)
        self.assertTrue(res.has_life_examples)
        self.assertEqual(res.clarity_verdict, "PASS")
        self.assertEqual(len(res.life_examples_found), 1)

    @patch("shutil.which", return_value="/usr/local/bin/agy")
    @patch("subprocess.run")
    def test_evaluate_with_agy_handles_error(
        self, mock_run: MagicMock, mock_which: MagicMock
    ) -> None:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["agy", "-p", "..."],
            returncode=1,
            stdout="",
            stderr="Authentication required",
        )

        res = evaluate_with_agy("Sample text", "test.md")
        self.assertFalse(res.is_valid)
        self.assertEqual(res.clarity_verdict, "FAIL")
        self.assertIn("Authentication required", res.error or "")


class CheckFileEndToEndTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.registry = GoldenProfileRegistry(self.root)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_check_file_static_only_pass(self) -> None:
        file_path = self.root / "sample.md"
        file_path.write_text(
            "# Idea\n\n## Жизненный пример\n\nПример взаимодействия.\n",
            encoding="utf-8",
        )
        passed, data = check_file(file_path, registry=self.registry, static_only=True, require_examples=True)
        self.assertTrue(passed)
        self.assertEqual(data["clarity_verdict"], "PASS")

    def test_check_file_static_only_fail_missing_examples(self) -> None:
        file_path = self.root / "abstract.md"
        file_path.write_text("# Abstract Formula\n\nA + B = C\n", encoding="utf-8")
        passed, data = check_file(file_path, registry=self.registry, static_only=True, require_examples=True)
        self.assertFalse(passed)
        self.assertEqual(data["clarity_verdict"], "NEEDS_WORK")

    def test_format_report_console(self) -> None:
        results = [
            {
                "filepath": "wiki/good.md",
                "passed": True,
                "readability_score": 9,
                "has_life_examples": True,
                "clarity_verdict": "PASS",
                "summary": "Отличный понятный текст.",
                "life_examples_found": ["Пример с ремонтом"],
                "golden_profile_references": [
                    {
                        "subject": "Юрий Дудь",
                        "aspect_position": "3Л",
                        "example": "Откуда эта сумма?",
                    }
                ],
                "suggestions": [],
            },
            {
                "filepath": "wiki/bad.md",
                "passed": False,
                "readability_score": 4,
                "has_life_examples": False,
                "clarity_verdict": "FAIL",
                "summary": "Слишком много абстракций.",
                "failure_reasons": ["Missing concrete real-life examples"],
            },
        ]
        report = format_report_console(results)
        self.assertIn("wiki/good.md", report)
        self.assertIn("wiki/bad.md", report)
        self.assertIn("Golden Profile Ground-Truth Reference", report)
        self.assertIn("Total files checked: 2", report)
        self.assertIn("Passed: 1", report)
        self.assertIn("Failed: 1", report)


if __name__ == "__main__":
    unittest.main()
