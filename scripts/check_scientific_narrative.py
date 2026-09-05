#!/usr/bin/env python3
"""Deterministic Scientific Narrative & Readability Quality Checker for Before We Build.

Evaluates narrative flow, cognitive fatigue hazards, AI/bureaucratic clichés,
sentence complexity, and epistemic boundaries across Russian, English, and Ukrainian texts.
Works statically without external LLM dependencies for instantaneous CI verification.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

from wiki_quality_common import (
    Diagnostic,
    REPO_ROOT,
    exit_code,
    line_number,
    markdown_files,
    parse_frontmatter,
    print_report,
    repo_relative,
    severity,
)


# Language-specific thresholds
THRESHOLDS = {
    "ru": {
        "max_sentence_words": 35,
        "extreme_sentence_words": 60,
        "max_paragraph_words": 170,
    },
    "uk": {
        "max_sentence_words": 35,
        "extreme_sentence_words": 60,
        "max_paragraph_words": 170,
    },
    "en": {
        "max_sentence_words": 30,
        "extreme_sentence_words": 50,
        "max_paragraph_words": 150,
    },
}

# Empty clichés, robotic phrasing, and bureaucratic filler
CLICHE_PATTERNS: dict[str, list[tuple[str, re.Pattern[str]]]] = {
    "ru": [
        ("cliche-modern-world", re.compile(r"\bв\s+современном(?:\s+стремительно\s+меняющемся)?\s+мире\b", re.IGNORECASE)),
        ("cliche-no-secret", re.compile(r"\bни\s+для\s+кого\s+не\s+секрет\b", re.IGNORECASE)),
        ("cliche-lets-dive", re.compile(r"\bдавайте\s+(?:погрузимся|разберемся|взглянем\s+поближе)\b", re.IGNORECASE)),
        ("cliche-plays-role", re.compile(r"\bиграет\s+(?:важную|ключевую|решающую)\s+роль\b", re.IGNORECASE)),
        ("cliche-integral-part", re.compile(r"\bявляется\s+неотъемлемой\s+частью\b", re.IGNORECASE)),
        ("cliche-cannot-not-note", re.compile(r"\bнельзя\s+не\s+(?:отметить|упомянуть|подчеркнуть)\b", re.IGNORECASE)),
        ("cliche-worth-stressing", re.compile(r"\bстоит\s+(?:подчеркнуть|отметить|сказать|заметить)\b", re.IGNORECASE)),
        ("cliche-as-known", re.compile(r"\bкак\s+известно\b", re.IGNORECASE)),
        ("cliche-must-understand", re.compile(r"\bнеобходимо\s+понимать\b", re.IGNORECASE)),
        ("cliche-central-place", re.compile(r"\bзанимает\s+центральное\s+место\b", re.IGNORECASE)),
        ("cliche-nothing-else-than", re.compile(r"\bпредставляет\s+собой\s+не\s+что\s+иное,\s+как\b", re.IGNORECASE)),
        ("cliche-today-day", re.compile(r"\bна\s+сегодняшний\s+день\b", re.IGNORECASE)),
    ],
    "en": [
        ("cliche-today-world", re.compile(r"\bin\s+today'?s\s+(?:fast-paced\s+)?world\b", re.IGNORECASE)),
        ("cliche-goes-without-saying", re.compile(r"\bit\s+goes\s+without\s+saying\b", re.IGNORECASE)),
        ("cliche-delve-into", re.compile(r"\b(?:let'?s\s+)?delve\s+into\b", re.IGNORECASE)),
        ("cliche-plays-role", re.compile(r"\bplays\s+a\s+(?:crucial|vital|key|pivotal)\s+role\b", re.IGNORECASE)),
        ("cliche-testament-to", re.compile(r"\bserves\s+as\s+a\s+testament\s+to\b", re.IGNORECASE)),
        ("cliche-important-note", re.compile(r"\bit\s+is\s+important\s+to\s+note\b", re.IGNORECASE)),
        ("cliche-worth-mentioning", re.compile(r"\bit\s+is\s+worth\s+mentioning\b", re.IGNORECASE)),
        ("cliche-tapestry", re.compile(r"\ba\s+rich\s+tapestry\s+of\b", re.IGNORECASE)),
        ("cliche-at-end-of-day", re.compile(r"\bat\s+the\s+end\s+of\s+the\s+day\b", re.IGNORECASE)),
    ],
    "uk": [
        ("cliche-modern-world", re.compile(r"\bу\s+сучасному(?:\s+світі,\s+що\s+стрімко\s+змінюється|\s+світі)\b", re.IGNORECASE)),
        ("cliche-no-secret", re.compile(r"\bні\s+для\s+кого\s+не\s+секрет\b", re.IGNORECASE)),
        ("cliche-plays-role", re.compile(r"\bвідіграє\s+(?:важливу|ключову|вирішальну)\s+роль\b", re.IGNORECASE)),
        ("cliche-worth-stressing", re.compile(r"\bварто\s+(?:підкреслити|зазначити|наголосити)\b", re.IGNORECASE)),
        ("cliche-cannot-not-note", re.compile(r"\bне\s+можна\s+не\s+(?:зазначити|відзначити|згадати)\b", re.IGNORECASE)),
        ("cliche-must-understand", re.compile(r"\bнеобхідно\s+розуміти\b", re.IGNORECASE)),
        ("cliche-as-known", re.compile(r"\bяк\s+відомо\b", re.IGNORECASE)),
        ("cliche-central-place", re.compile(r"\bпосідає\s+центральне\s+місце\b", re.IGNORECASE)),
        ("cliche-nothing-else-than", re.compile(r"\bє\s+не\s+чим\s+іншим,\s+як\b", re.IGNORECASE)),
        ("cliche-today-day", re.compile(r"\bна\s+сьогоднішній\s+день\b", re.IGNORECASE)),
    ],
}

# Negation detection to avoid false positives on cautions and caveats
NEGATED_RE = re.compile(
    r"(?:\bnot\b|\bnever\b|\bcannot\b|\bcan't\b|\bdoes\s+not\b|\bdo\s+not\b|"
    r"\bno\b|\brather\s+than\b|\binstead\s+of\b|\bwithout\b|"
    r"\bне\b|\bни\b|\bні\b|\bне\s+може\b|\bне\s+є\b|\bне\s+является\b).{0,120}$",
    re.IGNORECASE,
)


def is_negated(text: str, start: int, end: int) -> bool:
    """Check if the matched segment is preceded by a qualifying negation within window."""
    context = text[max(0, start - 80) : end]
    return bool(NEGATED_RE.search(context))


# Epistemic inflation patterns: overconfident certainty, premature claims, biological fatalism
EPISTEMIC_PATTERNS: dict[str, list[tuple[str, re.Pattern[str]]]] = {
    "ru": [
        (
            "epistemic-guarantee-outcome",
            re.compile(
                r"\b(?:тип|типологи\w*|модель)\b.{0,60}\bгарантир\w+\b|"
                r"\bгарантир\w+\b.{0,60}\b(?:совместимост\w*|отношен\w*|брак\w*|исход\w*)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-fatal-determinism",
            re.compile(
                r"\b(?:фатально|жестко|генетически)\s+(?:предопределя\w+|детерминир\w+)\b|"
                r"\bна\s+100%\s+(?:определя\w+|предсказыва\w+)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-proven-typology",
            re.compile(
                r"\bнаучно\s+(?:доказан\w*|подтвержден\w*)\s+(?:совместимост\w*|тип\w*|соционик\w*|психософи\w*|темпористик\w*)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-innate-essence",
            re.compile(
                r"\bявляется\s+(?:врожденным|биологическим)\s+(?:модулем|свойством|каналом)\b",
                re.IGNORECASE,
            ),
        ),
    ],
    "en": [
        (
            "epistemic-guarantee-outcome",
            re.compile(
                r"\b(?:type|typology|model)\b.{0,60}\bguarantee(?:s|d)?\b|"
                r"\bguarantee(?:s|d)?\b.{0,60}\b(?:compatibility|relationship|outcome|success)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-fatal-determinism",
            re.compile(
                r"\b(?:fatally|genetically|strictly)\s+determines?\b|"
                r"\b100%\s+(?:determines?|predicts?)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-proven-typology",
            re.compile(
                r"\bscientifically\s+proven\s+(?:compatibility|typology|socionics|psychosophy|temporistics)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-innate-essence",
            re.compile(
                r"\bis\s+an?\s+(?:innate|hardwired|biological)\s+(?:brain\s+module|essence)\b",
                re.IGNORECASE,
            ),
        ),
    ],
    "uk": [
        (
            "epistemic-guarantee-outcome",
            re.compile(
                r"\b(?:тип|типологі\w*|модель)\b.{0,60}\bгаранту\w+\b|"
                r"\bгаранту\w+\b.{0,60}\b(?:сумісн\w*|стосунк\w*|шлюб\w*|результат\w*)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-fatal-determinism",
            re.compile(
                r"\b(?:фатально|жорстко|генетично)\s+(?:зумовлю\w+|детерміну\w+)\b|"
                r"\bна\s+100%\s+(?:визнача\w+|передбача\w+)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-proven-typology",
            re.compile(
                r"\bнауково\s+(?:доведен\w*|підтверджен\w*)\s+(?:сумісн\w*|тип\w*|соціонік\w*|психософі\w*|темпористик\w*)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "epistemic-innate-essence",
            re.compile(
                r"\bє\s+(?:вродженим|біологічним)\s+(?:модулем|каналом)\b",
                re.IGNORECASE,
            ),
        ),
    ],
}

LIST_ITEM_START_RE = re.compile(r"^(?:[-*+]\s+|\d+\.\s+)")


@dataclass
class SentenceInfo:
    text: str
    word_count: int
    line: int
    is_question: bool
    parenthesis_depth: int
    parenthesis_ratio: float


@dataclass
class ParagraphInfo:
    index: int
    start_line: int
    end_line: int
    text: str
    word_count: int
    sentences: list[SentenceInfo]
    cliches: list[tuple[str, str, int]]  # code, match_text, line
    epistemic_issues: list[tuple[str, str, int]]  # code, match_text, line
    is_blockquote: bool
    cognitive_hazard_score: int = 0  # C_j index


@dataclass
class DocumentAnalysis:
    path: str
    language: str
    word_count: int
    sentence_count: int
    paragraph_count: int
    citation_word_count: int
    paragraphs: list[ParagraphInfo]
    diagnostics: list[Diagnostic] = field(default_factory=list)
    score: float = 100.0
    questions_count: int = 0
    dialogue_or_example_markers_count: int = 0
    sustained_fatigue_zones: list[tuple[int, int]] = field(default_factory=list)


def detect_language(text: str, filepath: Path, metadata: dict[str, Any]) -> str:
    """Infer document language from metadata, filename, or text content."""
    meta_lang = str(metadata.get("lang") or "").lower().strip()
    if meta_lang in {"en", "ru", "uk"}:
        return meta_lang

    stem = filepath.stem.lower()
    if stem.endswith("-en"):
        return "en"
    if stem.endswith("-uk"):
        return "uk"
    if stem.endswith("-ru"):
        return "ru"

    # Character frequency fallback
    cyrillic_ukrainian_chars = set("іїєґІЇЄҐ")
    cyrillic_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

    text_chars = set(text)
    if text_chars & cyrillic_ukrainian_chars:
        return "uk"
    cyr_count = sum(ch in cyrillic_chars for ch in text)
    if cyr_count > len(text) * 0.15:
        return "ru"
    return "en"


TABLE_SEP_RE = re.compile(r"^\|(?:\s*[-:]+\s*\|)+$")
TABLE_ROW_RE = re.compile(r"^\|.*\|$")


def _split_into_sentences(text: str, start_line: int) -> list[SentenceInfo]:
    """Split paragraph text into sentences with word counts and parenthesis metrics.

    Treats bullet/numbered list items and table cells as distinct semantic units to avoid
    falsely conjoining semicolon-separated lists or table cells into massive run-on sentences.
    """
    sentence_re = re.compile(r"(?<=[.!?])\s+(?=[A-ZА-ЯІЇЄҐ\d—])")

    # Pre-split on list items and table cells if present
    raw_units: list[tuple[str, int]] = []
    lines = text.splitlines()
    cur_unit_lines: list[str] = []
    cur_unit_start = start_line

    for idx, line in enumerate(lines):
        line_num = start_line + idx
        stripped = line.strip()
        if TABLE_SEP_RE.match(stripped):
            continue
        if TABLE_ROW_RE.match(stripped):
            if cur_unit_lines:
                raw_units.append(("\n".join(cur_unit_lines), cur_unit_start))
                cur_unit_lines = []
            cells = [c.strip() for c in stripped.split("|") if c.strip()]
            for cell in cells:
                raw_units.append((cell, line_num))
            continue

        if LIST_ITEM_START_RE.match(stripped):
            if cur_unit_lines:
                raw_units.append(("\n".join(cur_unit_lines), cur_unit_start))
                cur_unit_lines = []
            cur_unit_start = line_num
            # strip the list item prefix
            cleaned = LIST_ITEM_START_RE.sub("", stripped)
            cur_unit_lines.append(cleaned)
        else:
            cur_unit_lines.append(line)

    if cur_unit_lines:
        raw_units.append(("\n".join(cur_unit_lines), cur_unit_start))

    result: list[SentenceInfo] = []

    for unit_text, unit_line in raw_units:
        raw_sentences = [s.strip() for s in sentence_re.split(unit_text) if s.strip()]
        s_line = unit_line
        for s in raw_sentences:
            words = re.findall(r"\b[\w'-]+\b", s)
            w_count = len(words)
            is_q = s.endswith("?") or "?" in s

            # Calculate parenthesis depth and ratio
            max_depth = 0
            cur_depth = 0
            paren_chars = 0
            for ch in s:
                if ch == "(":
                    cur_depth += 1
                    max_depth = max(max_depth, cur_depth)
                elif ch == ")":
                    cur_depth = max(0, cur_depth - 1)
                elif cur_depth > 0:
                    paren_chars += 1

            paren_ratio = paren_chars / max(1, len(s))

            result.append(
                SentenceInfo(
                    text=s,
                    word_count=w_count,
                    line=s_line,
                    is_question=is_q,
                    parenthesis_depth=max_depth,
                    parenthesis_ratio=paren_ratio,
                )
            )
            s_line += s.count("\n")

    return result


def parse_markdown_paragraphs(body: str) -> list[tuple[int, int, str, bool]]:
    """Parse body text into (start_line, end_line, raw_text, is_blockquote)."""
    lines = body.splitlines()
    paragraphs: list[tuple[int, int, str, bool]] = []

    current_para: list[str] = []
    start_line = 1
    in_code_block = False
    in_blockquote = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Handle code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Blank line delimits paragraph
        if not stripped:
            if current_para:
                raw_text = "\n".join(current_para).strip()
                if raw_text:
                    paragraphs.append((start_line, idx - 1, raw_text, in_blockquote))
                current_para = []
                in_blockquote = False
            start_line = idx + 1
            continue

        # Markdown headings are separate structural elements
        if stripped.startswith("#"):
            if current_para:
                raw_text = "\n".join(current_para).strip()
                if raw_text:
                    paragraphs.append((start_line, idx - 1, raw_text, in_blockquote))
                current_para = []
                in_blockquote = False
            start_line = idx + 1
            continue

        # Track blockquotes
        if stripped.startswith(">"):
            if not current_para:
                in_blockquote = True
            cleaned = re.sub(r"^>\s*", "", stripped)
            current_para.append(cleaned)
        else:
            current_para.append(line)

    if current_para:
        raw_text = "\n".join(current_para).strip()
        if raw_text:
            paragraphs.append((start_line, len(lines), raw_text, in_blockquote))

    return paragraphs


def analyze_document(
    filepath: Path,
    content: str | None = None,
    *,
    strict: bool = False,
    min_score: float = 75.0,
) -> DocumentAnalysis:
    """Analyze a single markdown document for narrative clarity and epistemic precision."""
    if content is None:
        try:
            content = filepath.read_text(encoding="utf-8")
        except Exception as exc:
            doc = DocumentAnalysis(
                path=str(filepath),
                language="unknown",
                word_count=0,
                sentence_count=0,
                paragraph_count=0,
                citation_word_count=0,
                paragraphs=[],
                diagnostics=[
                    Diagnostic(
                        severity="error",
                        code="io-error",
                        message=f"Cannot read file: {exc}",
                        path=str(filepath),
                    )
                ],
                score=0.0,
            )
            return doc

    diagnostics: list[Diagnostic] = []
    metadata: dict[str, Any] = {}
    body = content

    # Only parse frontmatter if file starts with --- or is inside wiki/
    is_wiki = "wiki" in filepath.parts
    if content.startswith("---") or is_wiki:
        metadata, body, fm_error = parse_frontmatter(content)
        if fm_error and is_wiki:
            diagnostics.append(
                Diagnostic(
                    severity="warning",
                    code="frontmatter-parse",
                    message=fm_error,
                    path=str(filepath),
                    line=1,
                )
            )

    lang = detect_language(content, filepath, metadata)
    thresholds = THRESHOLDS.get(lang, THRESHOLDS["en"])
    cliche_list = CLICHE_PATTERNS.get(lang, CLICHE_PATTERNS["en"])
    epistemic_list = EPISTEMIC_PATTERNS.get(lang, EPISTEMIC_PATTERNS["en"])

    raw_paras = parse_markdown_paragraphs(body)
    parsed_paras: list[ParagraphInfo] = []

    total_words = 0
    total_sentences = 0
    citation_words = 0
    total_questions = 0
    dialogue_markers = 0

    cliche_hits_count = 0
    epistemic_hits_count = 0
    overlong_sentences_count = 0
    extreme_sentences_count = 0
    overlong_paras_count = 0

    for p_idx, (s_line, e_line, p_text, is_bq) in enumerate(raw_paras, start=1):
        words = re.findall(r"\b[\w'-]+\b", p_text)
        p_word_count = len(words)
        total_words += p_word_count

        if is_bq:
            citation_words += p_word_count

        sentences = _split_into_sentences(p_text, s_line)
        total_sentences += len(sentences)

        if any("—" in s.text or " – " in s.text or "«" in s.text for s in sentences):
            dialogue_markers += 1

        p_cliches: list[tuple[str, str, int]] = []
        p_epistemic: list[tuple[str, str, int]] = []

        # Blockquotes with citations are exempted from stylistic / cliché penalties
        if not is_bq:
            for code, pattern in cliche_list:
                for match in pattern.finditer(p_text):
                    m_text = match.group(0)
                    m_line = s_line + p_text.count("\n", 0, match.start())
                    p_cliches.append((code, m_text, m_line))
                    cliche_hits_count += 1
                    diagnostics.append(
                        Diagnostic(
                            severity="warning",
                            code=code,
                            message=f"Detected cliché or robotic phrase: «{m_text}». Rephrase in direct, vivid voice.",
                            path=str(filepath),
                            line=m_line,
                        )
                    )

            for code, pattern in epistemic_list:
                for match in pattern.finditer(p_text):
                    if is_negated(p_text, match.start(), match.end()):
                        continue
                    m_text = match.group(0)
                    m_line = s_line + p_text.count("\n", 0, match.start())
                    p_epistemic.append((code, m_text, m_line))
                    epistemic_hits_count += 1
                    diagnostics.append(
                        Diagnostic(
                            severity=severity(strict, always_error=strict),
                            code=code,
                            message=f"Epistemic certainty inflation: «{m_text}». Typology and latent models must not guarantee outcomes or assert unverified fatalism.",
                            path=str(filepath),
                            line=m_line,
                        )
                    )

        max_s_words = 0
        for s in sentences:
            if s.is_question:
                total_questions += 1
            max_s_words = max(max_s_words, s.word_count)

            if not is_bq:
                if s.word_count > thresholds["extreme_sentence_words"]:
                    extreme_sentences_count += 1
                    diagnostics.append(
                        Diagnostic(
                            severity=severity(strict, always_error=False),
                            code="extreme-sentence-overload",
                            message=f"Overloaded run-on sentence ({s.word_count} words > {thresholds['extreme_sentence_words']}). Split into 2-3 shorter sentences.",
                            path=str(filepath),
                            line=s.line,
                        )
                    )
                elif s.word_count > thresholds["max_sentence_words"]:
                    overlong_sentences_count += 1
                    diagnostics.append(
                        Diagnostic(
                            severity="warning",
                            code="overlong-sentence",
                            message=f"Sentence exceeds recommended length ({s.word_count} words > {thresholds['max_sentence_words']}).",
                            path=str(filepath),
                            line=s.line,
                        )
                    )

                if s.parenthesis_depth >= 3:
                    diagnostics.append(
                        Diagnostic(
                            severity="warning",
                            code="deep-parentheses",
                            message=f"Nested parentheses depth {s.parenthesis_depth} >= 3 increases cognitive parsing fatigue.",
                            path=str(filepath),
                            line=s.line,
                        )
                    )

        if not is_bq and p_word_count > thresholds["max_paragraph_words"]:
            overlong_paras_count += 1
            diagnostics.append(
                Diagnostic(
                    severity="warning",
                    code="overlong-paragraph",
                    message=f"Paragraph is too long ({p_word_count} words > {thresholds['max_paragraph_words']}). Break into digestible chunks.",
                    path=str(filepath),
                    line=s_line,
                )
            )

        # Compute Editorial Attention / Cognitive Hazard Index: C_j
        c_j = 0
        if max_s_words > thresholds["max_sentence_words"]:
            c_j += 1
        if p_word_count > thresholds["max_paragraph_words"]:
            c_j += 1
        if len(p_cliches) >= 1:
            c_j += 1
        if any(s.parenthesis_depth >= 3 or s.parenthesis_ratio > 0.25 for s in sentences):
            c_j += 1

        parsed_p = ParagraphInfo(
            index=p_idx,
            start_line=s_line,
            end_line=e_line,
            text=p_text,
            word_count=p_word_count,
            sentences=sentences,
            cliches=p_cliches,
            epistemic_issues=p_epistemic,
            is_blockquote=is_bq,
            cognitive_hazard_score=c_j,
        )
        parsed_paras.append(parsed_p)

        if c_j >= 2 and not is_bq:
            diagnostics.append(
                Diagnostic(
                    severity="warning",
                    code="cognitive-hazard-paragraph",
                    message=f"Paragraph attention hazard index C_{p_idx} = {c_j} >= 2 (dense sentences/clichés/parentheses). Reader drop-off risk elevated.",
                    path=str(filepath),
                    line=s_line,
                )
            )

    # Detect sustained cognitive fatigue zones (3+ consecutive paragraphs with C_j >= 2)
    sustained_zones: list[tuple[int, int]] = []
    current_zone_start = None
    count_in_row = 0

    for p in parsed_paras:
        if not p.is_blockquote and p.cognitive_hazard_score >= 2:
            count_in_row += 1
            if count_in_row == 3:
                current_zone_start = p.index - 2
        else:
            if count_in_row >= 3 and current_zone_start is not None:
                sustained_zones.append((current_zone_start, p.index - 1))
            count_in_row = 0
            current_zone_start = None

    if count_in_row >= 3 and current_zone_start is not None:
        sustained_zones.append((current_zone_start, len(parsed_paras)))

    for z_start, z_end in sustained_zones:
        start_p = parsed_paras[z_start - 1]
        diagnostics.append(
            Diagnostic(
                severity=severity(strict, always_error=False),
                code="sustained-cognitive-fatigue",
                message=f"Sustained cognitive fatigue zone detected (paragraphs {z_start} to {z_end}). High reader abandonment risk. Introduce dialogue, inquiry question, or scenario.",
                path=str(filepath),
                line=start_p.start_line,
            )
        )

    if total_words > 400 and total_questions == 0:
        diagnostics.append(
            Diagnostic(
                severity="warning",
                code="missing-curiosity-hooks",
                message="Text has 0 question hooks across > 400 words. Reader engagement requires periodic micro-discovery questions.",
                path=str(filepath),
                line=1,
            )
        )

    # Calculate deterministic Scientific Narrative Score (SNS, 0-100)
    score = 100.0
    score -= overlong_sentences_count * 2.5
    score -= extreme_sentences_count * 6.0
    score -= overlong_paras_count * 4.0
    score -= cliche_hits_count * 5.0
    score -= epistemic_hits_count * 12.0
    score -= len(sustained_zones) * 10.0

    if total_words > 400 and total_questions == 0:
        score -= 8.0

    # Pacing and engagement bonuses
    if total_words > 300:
        q_ratio = total_questions / max(1, len(parsed_paras))
        if 0.15 <= q_ratio <= 0.6:
            score += 5.0
        if dialogue_markers >= 2:
            score += 5.0

    score = max(0.0, min(100.0, round(score, 1)))

    if score < min_score:
        diagnostics.append(
            Diagnostic(
                severity=severity(strict, always_error=strict),
                code="readability-score-below-threshold",
                message=f"Overall Scientific Narrative Score ({score:.1f}/100) is below minimum required threshold ({min_score:.1f}/100).",
                path=str(filepath),
            )
        )

    return DocumentAnalysis(
        path=str(filepath),
        language=lang,
        word_count=total_words,
        sentence_count=total_sentences,
        paragraph_count=len(parsed_paras),
        citation_word_count=citation_words,
        paragraphs=parsed_paras,
        diagnostics=diagnostics,
        score=score,
        questions_count=total_questions,
        dialogue_or_example_markers_count=dialogue_markers,
        sustained_fatigue_zones=sustained_zones,
    )


EXCLUDED_NON_NARRATIVE_FILENAMES = {
    "log.md",
    "index.md",
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
}


def check_paths(
    paths: Sequence[Path],
    *,
    strict: bool = False,
    min_score: float = 75.0,
    json_output: bool = False,
) -> int:
    """Run narrative readability and quality checks on a sequence of files."""
    valid_paths = [p for p in paths if p.name not in EXCLUDED_NON_NARRATIVE_FILENAMES]
    if not valid_paths:
        if json_output:
            print(json.dumps({"summary": [], "diagnostics": []}))
        else:
            print("No narrative documents to check.")
        return 0

    all_diagnostics: list[Diagnostic] = []
    summaries: list[dict[str, Any]] = []

    for path in valid_paths:
        analysis = analyze_document(path, strict=strict, min_score=min_score)
        all_diagnostics.extend(analysis.diagnostics)
        summaries.append({
            "path": repo_relative(path),
            "language": analysis.language,
            "word_count": analysis.word_count,
            "score": analysis.score,
            "questions": analysis.questions_count,
            "fatigue_zones": len(analysis.sustained_fatigue_zones),
            "diagnostics_count": len(analysis.diagnostics),
        })

    if json_output:
        out = {
            "summary": summaries,
            "diagnostics": [d.as_dict() for d in all_diagnostics],
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print_report(all_diagnostics)
        print("\n--- Scientific Narrative Readability Summary ---")
        for s in summaries:
            status = "PASS" if s["score"] >= min_score else "FAIL"
            print(f"[{status}] {s['path']} ({s['language'].upper()}): Score {s['score']:.1f}/100 | {s['word_count']} words | {s['questions']} questions | {s['fatigue_zones']} fatigue zones")

    return exit_code(all_diagnostics, fail_on_warnings=False)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic Scientific Narrative & Readability Quality Checker."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Files or directories to audit (defaults to narrative expositions in raw/ and docs/).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat readability score drops below threshold and epistemic inflation as blocking errors.",
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=75.0,
        help="Minimum required Scientific Narrative Score (0-100, default: 75.0).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format.",
    )

    args = parser.parse_args()

    if args.paths:
        target_files = markdown_files(REPO_ROOT, [str(p) for p in args.paths])
    else:
        target_files = markdown_files(
            REPO_ROOT,
            [
                "raw/general/latent-process-narrative-exposition.md",
            ],
        )

    return check_paths(
        target_files,
        strict=args.strict,
        min_score=args.min_score,
        json_output=args.json,
    )


if __name__ == "__main__":
    sys.exit(main())
