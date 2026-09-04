#!/usr/bin/env python3
"""Markdown Readability and Life-Examples Evaluator with Golden Profile Benchmarks.

Uses the Antigravity CLI (`agy`), static analysis, and ground-truth golden profiles
(from `research/case-studies/detailed-typology-*.md` and `wiki/concepts/composite-profile-*.md`)
to verify that Markdown documents are clear, pleasant to read, avoid dry jargon,
and include concrete real-life examples of how latent processes manifest.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Sequence

EXAMPLE_HEADER_PATTERNS = [
    re.compile(
        r"^#+\s+.*(пример|жизнен|приклад|example|case\s+study|scenario|dialog|диалог|діалог).*",
        re.IGNORECASE,
    ),
]

SECTION_SHARED_EXAMPLE_RE = re.compile(
    r"<!--\s*section:(shared-example|example[a-z0-9_-]*)\s*-->", re.IGNORECASE
)


@dataclass
class GoldenProfileCase:
    subject_name: str
    doc_path: str
    socionics_code: str
    psychosophy_code: str
    temporistics_code: str
    value_moral_summary: str
    process_manifestations: list[dict[str, str]] = field(default_factory=list)
    search_keywords: list[str] = field(default_factory=list)


class GoldenProfileRegistry:
    """Registry of canonical benchmark ground-truth profiles from docs/ and wiki/."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path(__file__).resolve().parents[1]
        self.cases: list[GoldenProfileCase] = []
        self._load_ground_truth_profiles()

    def _load_ground_truth_profiles(self) -> None:
        """Load and structure ground-truth profiles of real investigated cases."""
        # 1. Юрий Дудь (ЛИЭ + ФВЛЭ + НПБВ)
        self.cases.append(
            GoldenProfileCase(
                subject_name="Юрий Дудь",
                doc_path="research/case-studies/detailed-typology-dud.md",
                socionics_code="ЛИЭ (Джек Лондон / Предприниматель)",
                psychosophy_code="ФВЛЭ (Гёте)",
                temporistics_code="НПБВ (Звезда, Старожилы)",
                value_moral_summary="Защита свободы слова, прав человека, личной автономии, уважение к честному труду и профессионализму.",
                process_manifestations=[
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "3Л (Логика)",
                        "process": "Скептический аудит тезисов, поиск доказательств и проверка смет.",
                        "example": "В интервью с бизнесменами и чиновниками дотошно разбирает цифры: «Откуда эта сумма? Покажи выписку и доказательства», реагируя на логическую непоследовательность.",
                    },
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "1Ф (Физика)",
                        "process": "Витальная выносливость, высокая спортивная активность и спартанская неприхотливость.",
                        "example": "Регулярный триатлон и футбол; спокойное отношение к тяжелым экспедициям и спартанским условиям съемок документалок на Колыме.",
                    },
                    {
                        "level": "Strategic (Temporistics)",
                        "aspect_position": "2П (Прошлое / Летописец)",
                        "process": "Исследование прецедентов, архивов и исторической памяти поколений.",
                        "example": "Авторские документальные фильмы («Колыма», «Беслан», «Балабанов», 90-е), где современные проблемы объясняются через исследование исторических первопричин.",
                    },
                    {
                        "level": "Strategic (Temporistics)",
                        "aspect_position": "3Б (Будущее / Безбилетник)",
                        "process": "Уязвимость и тревога перед неопределенностью долгосрочного будущего.",
                        "example": "Повторяющийся вопрос в финале почти каждого интервью: «Что будет через 5–10 лет?», «Окажемся ли мы там?», отражающий ощущение хрупкости планов.",
                    },
                    {
                        "level": "Tactical (Socionics)",
                        "aspect_position": "1Te (Деловая логика)",
                        "process": "Оптимизация процессов, интерес к практической отдаче, монетизации и продуктивности.",
                        "example": "Построение эффективной медиа-редакции Sports.ru, развитие независимого YouTube-продакшена с жесткой ориентацией на тайминг и отдачу.",
                    },
                ],
                search_keywords=["дудь", "dud", "лиэ", "lie", "фвлэ", "нпбв", "3л", "1ф", "2п", "3б", "1te"],
            )
        )

        # 2. Алишер Моргенштерн (СЭЭ + ФЭВЛ + НВПБ)
        self.cases.append(
            GoldenProfileCase(
                subject_name="Алишер Моргенштерн",
                doc_path="research/case-studies/detailed-typology-morgenshtern.md",
                socionics_code="СЭЭ (Наполеон / Политик)",
                psychosophy_code="ФЭВЛ (Дюма)",
                temporistics_code="НВПБ (Серый Кардинал, Лазутчики)",
                value_moral_summary="Радикальный гедонизм, приоритет личной автономии и трансгрессия социальных табу при периодической благотворительности.",
                process_manifestations=[
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "3В (Воля)",
                        "process": "Гиперкомпенсация статуса, острая фиксация на личном первенстве и аллергия на запреты.",
                        "example": "Публичные заявления «Я номер один», демонстрация пачек денег и эпатажное доминирование как защитная реакция на попытки институтов власти ограничить его автономию.",
                    },
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "1Ф (Физика)",
                        "process": "Материально-сенсорный гедонизм, опора на физические блага.",
                        "example": "Культ материального изобилия, дорогих машин, ресторанов и одежды как базовой опоры самоощущения.",
                    },
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "2Э (Эмоция)",
                        "process": "Процессионная эмоциональная драматургия и пластичность настроения.",
                        "example": "Мгновенное переключение эмоционального тона на стримах и концертах, зажигание зала смехом и провокацией.",
                    },
                    {
                        "level": "Strategic (Temporistics)",
                        "aspect_position": "1Н (Настоящее / Хозяин)",
                        "process": "Извлечение максимального драйва и ресурса 'здесь и сейчас'.",
                        "example": "Спонтанные решения о покупках и релизах треков за 24 часа; отказ от долгосрочного накопления ради немедленного проживания момента.",
                    },
                    {
                        "level": "Tactical (Socionics)",
                        "aspect_position": "1Se (Силовая сенсорика)",
                        "process": "Мгновенный силовой захват пространства и удержание внимания.",
                        "example": "Физическая уверенность на публике, прямое столкновение с критиками, агрессивный захват трендов.",
                    },
                ],
                search_keywords=["моргенштерн", "morgenshtern", "сээ", "see", "фэвл", "нвпб", "3в", "1ф", "2э", "1н", "1se"],
            )
        )

        # 3. Валерий Залужный (СЛЭ + ФВЛЭ + БНПВ)
        self.cases.append(
            GoldenProfileCase(
                subject_name="Валерий Залужный",
                doc_path="research/case-studies/detailed-typology-zaluzhnyi.md",
                socionics_code="СЛЭ (Жуков / Маршал)",
                psychosophy_code="ФВЛЭ (Гёте)",
                temporistics_code="БНПВ (Колонист)",
                value_moral_summary="Служение, сохранение жизни людей, личная ответственность и человеческое достоинство подчиненных.",
                process_manifestations=[
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "2В (Воля)",
                        "process": "Процессионное неавторитарное делегирование и уважение к субъектности командиров на местах.",
                        "example": "Отказ от жесткой советской командной вертикали; предоставление офицерам на передовой права принимать самостоятельные тактические решения без страха наказания.",
                    },
                    {
                        "level": "Strategic (Temporistics)",
                        "aspect_position": "1Б (Будущее / Колонист)",
                        "process": "Стратегическая проработка траектории и подготовка к неизбежным вызовам.",
                        "example": "Системная перестройка армейских практик и подготовка оборонительных рубежей за годы до полномасштабного вторжения.",
                    },
                    {
                        "level": "Tactical (Socionics)",
                        "aspect_position": "1Se + 2Ti (Силовая сенсорика + Структурная логика)",
                        "process": "Оценка реального баланса сил и распределение ресурсов в жесткой иерархической системе.",
                        "example": "Управление крупномасштабной обороной через четкий учет боеприпасов, логистики и маневра резервами.",
                    },
                ],
                search_keywords=["залужный", "zaluzhnyi", "слэ", "sle", "фвлэ", "бнпв", "2в", "1б", "1se", "2ti"],
            )
        )

        # 4. Светлана Тарабарова (ИЭЭ + ЭВФЛ + БНПВ)
        self.cases.append(
            GoldenProfileCase(
                subject_name="Светлана Тарабарова",
                doc_path="research/case-studies/detailed-typology-tarabarova.md",
                socionics_code="ИЭЭ (Гексли / Советчик)",
                psychosophy_code="ЭВФЛ (Пастернак)",
                temporistics_code="БНПВ (Колонист)",
                value_moral_summary="Семейная поддержка, ненасильственная коммуникация, созидательное творчество («Світла музика»).",
                process_manifestations=[
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "1Э (Эмоция)",
                        "process": "Автономный источник эмоциональной мобилизации и вдохновения.",
                        "example": "Создание авторского проекта 'Світла музика', трансляция искреннего тепла и жизнеутверждающего посыла даже в кризисные периоды.",
                    },
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "3Ф (Физика)",
                        "process": "Уязвимость в материально-бытовой сфере при столкновении с финансовыми перегрузками.",
                        "example": "Тяжелый стресс и открытое обсуждение кризиса с выплатой ипотеки и ремонтом дома в Дмитровке во время пандемии и войны.",
                    },
                ],
                search_keywords=["тарабарова", "tarabarova", "иээ", "iee", "эвфл", "бнпв", "1э", "3ф"],
            )
        )

        # 5. Владимир Зеленский (ЭИЭ + ЭФВЛ + НПБВ)
        self.cases.append(
            GoldenProfileCase(
                subject_name="Владимир Зеленский",
                doc_path="research/case-studies/detailed-typology-zelenskyi.md",
                socionics_code="ЭИЭ (Гамлет / Наставник)",
                psychosophy_code="ЭФВЛ (Пушкин)",
                temporistics_code="НПБВ (Звезда, Старожилы)",
                value_moral_summary="Защита суверенитета, публичное лидерство, дипломатическая мобилизация союзников.",
                process_manifestations=[
                    {
                        "level": "Tactical (Socionics)",
                        "aspect_position": "1Fe + 2Ni (Этика эмоций + Интуиция времени)",
                        "process": "Публичная эмоциональная мобилизация и драматургия исторического момента.",
                        "example": "Ежедневные обращения к мировым парламентам и гражданам, точная подстройка риторики под культурный код каждой страны для получения военной помощи.",
                    },
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "3В (Воля)",
                        "process": "Чувствительность к признанию и вызов внешнему давлению.",
                        "example": "Решительный отказ от эвакуации («Мне нужно оружие, а не эвакуация») как ответ на попытку навязать сценарий капитуляции.",
                    },
                ],
                search_keywords=["зеленский", "zelenskyi", "эиэ", "eie", "эфвл", "нпбв", "1fe", "2ni", "3в"],
            )
        )

        # 6. Референсный композитный DevOps-профиль (СЛИ + ЭЛВФ + ВПНБ)
        self.cases.append(
            GoldenProfileCase(
                subject_name="Композитный DevOps-эталон (СЛИ + ЭЛВФ + ВПНБ)",
                doc_path="wiki/concepts/composite-profile-sli-elvf-vpnb-ru.md",
                socionics_code="СЛИ (Габен / Мастер)",
                psychosophy_code="ЭЛВФ (Пастернак)",
                temporistics_code="ВПНБ (Идеолог / Проводники)",
                value_moral_summary="Осмысленная надёжность, отказ от токсичных статусных игр, взаимная ответственность и прозрачность.",
                process_manifestations=[
                    {
                        "level": "Tactical (Socionics)",
                        "aspect_position": "1Si + 2Te",
                        "process": "Интеграция условий среды и гибкая отладка инструментов по логам.",
                        "example": "Инженер автоматизирует рутину, пишет самовосстанавливающиеся скрипты и устраняет причину сбоя в инфраструктуре без лишней суеты.",
                    },
                    {
                        "level": "Strategic (Temporistics)",
                        "aspect_position": "1В + 2П",
                        "process": "Поиск глубинного 'зачем' и анализ прошлых инцидентов.",
                        "example": "При старте проекта первым делом поднимает постмортемы прошлых аварий и требует ясного ответа, какую реальную пользу продукт принесет пользователям.",
                    },
                    {
                        "level": "Operational (Psychosophy)",
                        "aspect_position": "3В (Воля)",
                        "process": "Аллергия на бессмысленную бюрократию и самодурство начальства.",
                        "example": "При попытке навязать бессмысленные совещания или иерархическое давление требует перехода к конструктивным техническим аргументам.",
                    },
                ],
                search_keywords=["сли", "sli", "элвф", "elvf", "впнб", "vpnb", "девопс", "devops", "габен"],
            )
        )

    def find_relevant_cases(self, text: str) -> list[tuple[GoldenProfileCase, list[dict[str, str]]]]:
        """Find matching cases and their relevant process manifestations based on text keywords."""
        lowered = text.lower()
        results = []

        for case in self.cases:
            matched_manifestations = []
            case_matched = False
            for kw in case.search_keywords:
                kw_lowered = kw.lower()
                if len(kw_lowered) <= 3:
                    if re.search(rf"\b{re.escape(kw_lowered)}\b", lowered):
                        case_matched = True
                        break
                else:
                    stem = kw_lowered.rstrip("ьяеиоуы")
                    if stem in lowered:
                        case_matched = True
                        break

            for m in case.process_manifestations:
                pos = m["aspect_position"].lower()
                code = pos.split()[0]
                if re.search(rf"\b{re.escape(code)}\b", lowered) or case_matched:
                    matched_manifestations.append(m)

            if matched_manifestations:
                results.append((case, matched_manifestations))
            elif case_matched:
                results.append((case, case.process_manifestations))

        return results


@dataclass
class StaticCheckResult:
    has_example_section: bool
    has_example_heading: bool
    word_count: int
    matched_markers: list[str]


@dataclass
class EvaluationResult:
    filepath: str
    readability_score: int  # 1 to 10
    has_life_examples: bool
    clarity_verdict: str  # PASS, NEEDS_WORK, FAIL
    summary: str
    life_examples_found: list[str]
    unclear_jargon_or_passages: list[str]
    suggestions: list[str]
    is_valid: bool
    golden_profile_references: list[dict[str, str]] = field(default_factory=list)
    error: str | None = None


def get_git_files(mode: str, root: Path) -> list[Path]:
    """Retrieve markdown files from Git based on mode."""
    files: list[Path] = []
    try:
        if mode == "staged":
            cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
        elif mode == "modified":
            cmd = ["git", "diff", "HEAD", "--name-only", "--diff-filter=ACMR"]
        elif mode == "untracked":
            cmd = ["git", "ls-files", "--others", "--exclude-standard"]
        elif mode == "staged_or_modified":
            proc1 = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"], capture_output=True, text=True, cwd=root)
            proc2 = subprocess.run(["git", "diff", "HEAD", "--name-only", "--diff-filter=ACMR"], capture_output=True, text=True, cwd=root)
            proc3 = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True, cwd=root)
            all_lines = set(proc1.stdout.splitlines() + proc2.stdout.splitlines() + proc3.stdout.splitlines())
            return sorted([root / p for p in all_lines if p.endswith((".md", ".markdown")) and (root / p).is_file()])
        else:
            return []

        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=root)
        if proc.returncode == 0:
            for line in proc.stdout.splitlines():
                line = line.strip()
                if line.endswith((".md", ".markdown")):
                    p = root / line
                    if p.is_file():
                        files.append(p)
    except Exception as exc:
        print(f"Warning: git command failed ({exc})", file=sys.stderr)
    return sorted(files)


def static_analyze_markdown(content: str) -> StaticCheckResult:
    """Analyze static structure for example markers and headings."""
    has_section = bool(SECTION_SHARED_EXAMPLE_RE.search(content))
    matched_markers = []
    has_heading = False

    for line in content.splitlines():
        for pat in EXAMPLE_HEADER_PATTERNS:
            if pat.match(line.strip()):
                has_heading = True
                matched_markers.append(line.strip())

    words = len(re.findall(r"\w+", content))
    return StaticCheckResult(
        has_example_section=has_section,
        has_example_heading=has_heading,
        word_count=words,
        matched_markers=matched_markers,
    )


def build_evaluation_prompt(
    content: str,
    filepath: str,
    matched_cases: list[tuple[GoldenProfileCase, list[dict[str, str]]]] | None = None,
) -> str:
    """Build the evaluation prompt for agy CLI including ground-truth case examples."""
    golden_context = ""
    if matched_cases:
        golden_context = "\n### ЭТАЛОННЫЕ КЕЙСЫ ИЗ ЗОЛОТЫХ ПРОФИЛЕЙ (РЕАЛЬНЫЕ ПРОЯВЛЕНИЯ В ЖИЗНИ):\n"
        for case, items in matched_cases[:3]:
            golden_context += f"• **{case.subject_name}** ({case.socionics_code} | {case.psychosophy_code} | {case.temporistics_code}):\n"
            for it in items[:2]:
                golden_context += f"   - [{it['aspect_position']}]: {it['process']} -> *Пример*: «{it['example']}»\n"

    return f"""Ты — строгий, но практичный рецензент читаемости текстов (в духе 'Vanka the Layman' и 'Plain Language Translator').
Твоя задача — проверить Markdown-документ на понятность, приятность чтения обычному человеку и обязательное наличие жизненных/бытовых примеров.

Файл: `{filepath}`

Текст для проверки:
```markdown
{content[:8000]}
```
{golden_context}
Критерии проверки:
1. **Приятность и понятность чтения (1-10)**: Легко ли обычному человеку читать текст? Нет ли заумного псевдонаучного «птичьего языка», нераспакованного абстрактного жаргона или тяжеловесных канцеляризмов?
2. **Жизненные примеры (ОБЯЗАТЕЛЬНО)**: Есть ли в тексте конкретные бытовые, человеческие примеры, диалоги, сценарии из реальной жизни или работы, иллюстрирующие абстрактные тезисы? (Простое упоминание абстрактных терминов примером не считается).
3. **Практическая ясность**: Понятно ли, о чем речь и зачем это нужно?
4. **Опора на золотые профили**: Если в тексте не хватает живых примеров, используй приведенные выше реальные кейсы (поступки, реакции в интервью, споры) из золотых профилей как образец и порекомендуй, как добавить похожую жизненную иллюстрацию.

Верни ответ СТРОГО в формате валидного JSON-объекта (без лишнего текста вокруг):
{{
  "readability_score": <число от 1 до 10>,
  "has_life_examples": <true/false>,
  "clarity_verdict": <"PASS" | "NEEDS_WORK" | "FAIL">,
  "summary": "<краткий вердикт на русском языке в 1-2 предложения>",
  "life_examples_found": ["<найденный пример 1>", "<найденный пример 2>"],
  "unclear_jargon_or_passages": ["<фрагмент или термин без пояснения>"],
  "suggestions": ["<конкретная рекомендация, где добавить пример или что упростить>"]
}}
"""


def evaluate_with_agy(
    content: str,
    filepath: str,
    *,
    matched_cases: list[tuple[GoldenProfileCase, list[dict[str, str]]]] | None = None,
    model: str | None = None,
    timeout_seconds: int = 120,
) -> EvaluationResult:
    """Invoke agy CLI to evaluate markdown content."""
    agy_path = shutil.which("agy")
    if not agy_path:
        local_bin_agy = Path.home() / ".local" / "bin" / "agy"
        if local_bin_agy.is_file():
            agy_path = str(local_bin_agy)

    golden_refs = []
    if matched_cases:
        for case, items in matched_cases:
            for it in items:
                golden_refs.append({
                    "subject": case.subject_name,
                    "doc": case.doc_path,
                    "aspect_position": it["aspect_position"],
                    "process": it["process"],
                    "example": it["example"],
                })

    if not agy_path:
        return EvaluationResult(
            filepath=filepath,
            readability_score=0,
            has_life_examples=False,
            clarity_verdict="FAIL",
            summary="agy CLI not found in PATH or ~/.local/bin",
            life_examples_found=[],
            unclear_jargon_or_passages=[],
            suggestions=["Install agy CLI or make it accessible in PATH."],
            is_valid=False,
            golden_profile_references=golden_refs,
            error="agy CLI binary not found",
        )

    prompt = build_evaluation_prompt(content, filepath, matched_cases)
    cmd = [agy_path, "-p", prompt, "--effort", "low"]
    if model:
        cmd.extend(["--model", model])

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        if proc.returncode != 0:
            err_msg = proc.stderr.strip() or f"Process exited with code {proc.returncode}"
            return EvaluationResult(
                filepath=filepath,
                readability_score=0,
                has_life_examples=False,
                clarity_verdict="FAIL",
                summary=f"agy error: {err_msg}",
                life_examples_found=[],
                unclear_jargon_or_passages=[],
                suggestions=[],
                is_valid=False,
                golden_profile_references=golden_refs,
                error=err_msg,
            )

        output = proc.stdout.strip()
        json_str = output
        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", output, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        elif "{" in output and "}" in output:
            start = output.find("{")
            end = output.rfind("}") + 1
            json_str = output[start:end]

        data = json.loads(json_str)
        score = int(data.get("readability_score", 5))
        has_examples = bool(data.get("has_life_examples", False))
        verdict = str(data.get("clarity_verdict", "NEEDS_WORK")).upper()
        summary = str(data.get("summary", ""))
        examples_found = list(data.get("life_examples_found", []))
        jargon = list(data.get("unclear_jargon_or_passages", []))
        suggestions = list(data.get("suggestions", []))

        return EvaluationResult(
            filepath=filepath,
            readability_score=score,
            has_life_examples=has_examples,
            clarity_verdict=verdict,
            summary=summary,
            life_examples_found=examples_found,
            unclear_jargon_or_passages=jargon,
            suggestions=suggestions,
            is_valid=True,
            golden_profile_references=golden_refs,
        )
    except subprocess.TimeoutExpired:
        return EvaluationResult(
            filepath=filepath,
            readability_score=0,
            has_life_examples=False,
            clarity_verdict="FAIL",
            summary=f"agy timed out after {timeout_seconds}s",
            life_examples_found=[],
            unclear_jargon_or_passages=[],
            suggestions=[],
            is_valid=False,
            golden_profile_references=golden_refs,
            error="Execution timed out",
        )
    except Exception as exc:
        return EvaluationResult(
            filepath=filepath,
            readability_score=0,
            has_life_examples=False,
            clarity_verdict="FAIL",
            summary=f"Failed to parse agy response: {exc}",
            life_examples_found=[],
            unclear_jargon_or_passages=[],
            suggestions=[],
            is_valid=False,
            golden_profile_references=golden_refs,
            error=str(exc),
        )


def check_file(
    filepath: Path,
    *,
    registry: GoldenProfileRegistry | None = None,
    min_score: int = 7,
    require_examples: bool = True,
    static_only: bool = False,
    model: str | None = None,
) -> tuple[bool, dict[str, Any]]:
    """Check a single markdown file with golden profile enrichment."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as exc:
        return False, {"filepath": str(filepath), "error": f"Cannot read file: {exc}"}

    static_res = static_analyze_markdown(content)
    matched_cases = registry.find_relevant_cases(content) if registry else []
    golden_refs = []
    for case, items in matched_cases:
        for it in items:
            golden_refs.append({
                "subject": case.subject_name,
                "doc": case.doc_path,
                "aspect_position": it["aspect_position"],
                "process": it["process"],
                "example": it["example"],
            })

    if static_only:
        has_examples = static_res.has_example_section or static_res.has_example_heading
        passed = (not require_examples) or has_examples
        return passed, {
            "filepath": str(filepath),
            "passed": passed,
            "static_check": asdict(static_res),
            "has_life_examples": has_examples,
            "readability_score": 8 if passed else 4,
            "clarity_verdict": "PASS" if passed else "NEEDS_WORK",
            "summary": "Static check completed." if passed else "No example section or heading found.",
            "suggestions": [] if passed else ["Add a shared-example section or real-life example heading."],
            "failure_reasons": [] if passed else ["Missing example section or heading"],
            "golden_profile_references": golden_refs,
        }

    eval_res = evaluate_with_agy(
        content,
        str(filepath),
        matched_cases=matched_cases,
        model=model,
    )

    passed = True
    reasons = []

    if not eval_res.is_valid:
        passed = False
        reasons.append(f"Evaluation error: {eval_res.error}")
    else:
        if eval_res.readability_score < min_score:
            passed = False
            reasons.append(f"Readability score {eval_res.readability_score} < min required {min_score}")
        if require_examples and not eval_res.has_life_examples and not (static_res.has_example_section or static_res.has_example_heading):
            passed = False
            reasons.append("Missing concrete real-life examples")
        if eval_res.clarity_verdict == "FAIL":
            passed = False
            reasons.append("Verdict is FAIL")

    result_data = asdict(eval_res)
    result_data["static_check"] = asdict(static_res)
    result_data["passed"] = passed
    result_data["failure_reasons"] = reasons
    return passed, result_data


def format_report_console(results: list[dict[str, Any]]) -> str:
    """Format evaluation results for human-readable terminal output."""
    lines = []
    lines.append("=" * 70)
    lines.append("Markdown Readability & Life-Examples Report")
    lines.append("=" * 70)

    for item in results:
        path = item.get("filepath", "unknown")
        passed = item.get("passed", False)
        status_str = "\033[92m[PASS]\033[0m" if passed else "\033[91m[FAIL]\033[0m"
        score = item.get("readability_score", 0)
        has_ex = item.get("has_life_examples", False)
        verdict = item.get("clarity_verdict", "UNKNOWN")

        lines.append(f"\n{status_str} {path}")
        lines.append(f"  • Readability Score: {score}/10 | Verdict: {verdict} | Life Examples: {'Yes' if has_ex else 'No'}")
        
        summary = item.get("summary")
        if summary:
            lines.append(f"  • Summary: {summary}")

        examples = item.get("life_examples_found") or []
        if examples:
            lines.append("  • Found examples in document:")
            for ex in examples[:3]:
                lines.append(f"    - {ex}")

        jargon = item.get("unclear_jargon_or_passages") or []
        if jargon:
            lines.append("  • Unclear terms/passages:")
            for j in jargon[:3]:
                lines.append(f"    - {j}")

        suggestions = item.get("suggestions") or []
        if suggestions:
            lines.append("  • Recommendations:")
            for s in suggestions[:3]:
                lines.append(f"    - {s}")

        golden_refs = item.get("golden_profile_references") or []
        if golden_refs:
            lines.append("  • 🌟 Golden Profile Ground-Truth Reference (как процесс проявляется в реальном кейсе):")
            for g in golden_refs[:3]:
                lines.append(f"    - [{g.get('subject')}] {g.get('aspect_position')}: «{g.get('example')}»")

        reasons = item.get("failure_reasons") or []
        if reasons:
            lines.append(f"  • Failure reasons: {'; '.join(reasons)}")

    lines.append("\n" + "=" * 70)
    total = len(results)
    passed_count = sum(1 for r in results if r.get("passed", False))
    lines.append(f"Total files checked: {total} | Passed: {passed_count} | Failed: {total - passed_count}")
    lines.append("=" * 70)
    return "\n".join(lines)


def show_golden_benchmarks(query: str | None, registry: GoldenProfileRegistry) -> int:
    """Print golden profile cases matching the query."""
    cases_with_items = []
    if query:
        cases_with_items = registry.find_relevant_cases(query)
    else:
        cases_with_items = [(c, c.process_manifestations) for c in registry.cases]

    print("=" * 70)
    print("🌟 Before We Build — Золотые Профили Реальных Людей и Проявления Процессов")
    print("=" * 70)
    if not cases_with_items:
        print(f"По запросу '{query}' золотых профилей не найдено.")
        return 0

    for idx, (case, items) in enumerate(cases_with_items, 1):
        print(f"\n{idx}. 👤 {case.subject_name} ({case.doc_path})")
        print(f"   • Соционика: {case.socionics_code}")
        print(f"   • Психософия: {case.psychosophy_code}")
        print(f"   • Темпористика: {case.temporistics_code}")
        print(f"   • Ценностная основа: {case.value_moral_summary}")
        print(f"   • Реальные поведенческие проявления процессов:")
        for it in items:
            print(f"     - [{it['level']}] {it['aspect_position']}: {it['process']}")
            print(f"       👉 Пример из жизни: «{it['example']}»")

    print("\n" + "=" * 70)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-staged", action="store_true", help="Check staged markdown files in Git (default for pre-commit)")
    parser.add_argument("--git-modified", action="store_true", help="Check modified markdown files in Git")
    parser.add_argument("--git-all", action="store_true", help="Check all uncommitted (staged + unstaged + untracked) markdown files")
    parser.add_argument("--files", nargs="*", help="Specific markdown files to check")
    parser.add_argument("--all-wiki", action="store_true", help="Check all wiki/*.md files")
    parser.add_argument("--min-score", type=int, default=7, help="Minimum readability score to pass (1-10, default: 7)")
    parser.add_argument("--no-require-examples", action="store_true", help="Do not require life examples to pass")
    parser.add_argument("--static-only", action="store_true", help="Run static heuristic check only (no agy CLI LLM calls)")
    parser.add_argument("--model", type=str, default=None, help="Specific model to pass to agy CLI")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--show-golden", nargs="?", const="", type=str, help="Show golden profile benchmark examples for a query (e.g., dud, 3В, morgenshtern, zaluzhnyi)")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Repository root directory")

    args = parser.parse_args(argv)
    root = args.root.resolve()
    registry = GoldenProfileRegistry(root)

    if args.show_golden is not None:
        return show_golden_benchmarks(args.show_golden or None, registry)

    target_files: list[Path] = []

    if args.files:
        for f in args.files:
            p = Path(f)
            if not p.is_absolute():
                p = root / p
            if p.is_file() and p.suffix.lower() in (".md", ".markdown"):
                target_files.append(p)
            else:
                print(f"Warning: File '{f}' not found or not a markdown file", file=sys.stderr)
    elif args.git_staged:
        target_files = get_git_files("staged", root)
    elif args.git_modified:
        target_files = get_git_files("modified", root)
    elif args.git_all:
        target_files = get_git_files("staged_or_modified", root)
    elif args.all_wiki:
        target_files = sorted((root / "wiki").rglob("*.md"))
    else:
        target_files = get_git_files("staged", root)
        if not target_files:
            target_files = get_git_files("modified", root)

    if not target_files:
        if args.json:
            print(json.dumps({"status": "ok", "message": "No markdown files found to check", "results": []}))
        else:
            print("No matching markdown files found to check.")
        return 0

    results = []
    all_passed = True

    for filepath in target_files:
        passed, data = check_file(
            filepath,
            registry=registry,
            min_score=args.min_score,
            require_examples=not args.no_require_examples,
            static_only=args.static_only,
            model=args.model,
        )
        results.append(data)
        if not passed:
            all_passed = False

    if args.json:
        print(json.dumps({"passed": all_passed, "results": results}, indent=2, ensure_ascii=False))
    else:
        print(format_report_console(results))

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
