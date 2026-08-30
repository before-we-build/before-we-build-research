#!/usr/bin/env python3
"""Flag overconfident, deterministic, or premature scoring language.

The audit ignores negated cautions (for example, "does not guarantee") and can
allow an attributed/contested claim through explicit claim metadata or an
inline marker:

``<!-- claim-audit: allow reason=quoted-source -->``

Default invocation reports migration warnings. ``--strict`` makes findings
blocking.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

from check_wikilinks import _mask_code
from wiki_quality_common import (
    CLAIM_MARKER_RE,
    Diagnostic,
    claim_map,
    exit_code,
    load_wiki_pages,
    markdown_files,
    parse_frontmatter,
    print_report,
    repo_relative,
    severity,
)


DEFAULT_SCAN_ENTRIES = (
    "README.md",
    "index.md",
    "wiki",
    "docs",
    "skills",
    "instruments",
    "biblical-compatibility",
    ".opencode/agents",
)


@dataclass(frozen=True)
class Rule:
    code: str
    explanation: str
    pattern: re.Pattern[str]


RULES = (
    Rule(
        "retired-simulation-entity",
        "remove the retired human-simulation track from active repository content",
        re.compile(
            r"\bdigital[-\s]+twin(?:[-\s]+builder)?\b|\buser[-\s]+twin\b|"
            r"\bcandidate[-\s]+twin\b|\bsimulation[-\s]+engine\b|"
            r"\btext[-\s]+world[-\s]+engine\b|\bsimulation[-\s]+transcript\b|"
            r"\blove[-\s]+observer\b|\bscenario[-\s]+compiler\b|"
            r"\binner[-\s]+parliament\b|"
            r"\bцифров\w*\s+(?:двойн\w*|двійник\w*)\b|"
            r"\b(?:двойн\w*|двійник\w*)\s+(?:пользовател\w*|користувач\w*|кандидат\w*)\b",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "unsupported-certainty",
        "avoid claiming that an unqualified typological or compatibility conclusion is proven",
        re.compile(
            r"\bscientifically\s+proven\b|\bconclusively\s+(?:shows?|demonstrates?)\b|"
            r"\b(?:typolog\w*|compatibility|before\s+we\s+build|bwb|model|system)\b\s+"
            r"(?:(?:is|are|was|were|has\s+been)\s+)?(?:scientifically\s+)?proven\b|"
            r"\bproven\b.{0,55}\b(?:typolog\w*|compatibility|before\s+we\s+build|bwb|model|system)\b|"
            r"\b(?:типологи\w*|совместимост\w*|модел\w*|систем\w*)\b.{0,55}\bдоказан\w*\b|"
            r"\bнаучно\s+доказан\w*\b|\bнаучно\s+подтвержден\w*\b|"
            r"\b(?:типологі\w*|сумісн\w*|модел\w*|систем\w*)\b.{0,55}\bдоведен\w*\b|"
            r"\bнауково\s+доведен\w*\b|\bнауково\s+підтверджен\w*\b",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "guaranteed-outcome",
        "compatibility and typology must not guarantee a human outcome",
        re.compile(
            r"(?:\bguarantee(?:d|s)?\b.{0,70}\b(?:compatibility|love|marriage|relationship|partner|outcome|success|fit)\b|"
            r"\b(?:compatibility|typolog\w*|type|love|marriage|relationship|partner|outcome|success)\b.{0,70}\bguarantee(?:d|s)?\b)|"
            r"(?:\bгарантир\w*\b.{0,70}\b(?:совместимост\w*|любов\w*|брак\w*|отношен\w*|исход\w*|успех\w*)\b|"
            r"\b(?:совместимост\w*|типологи\w*|тип|любов\w*|брак\w*|отношен\w*|исход\w*|успех\w*)\b.{0,70}\bгарантир\w*\b)|"
            r"(?:\bгаранту\w*\b.{0,70}\b(?:сумісн\w*|любов\w*|шлюб\w*|стосунк\w*|результат\w*|успіх\w*)\b|"
            r"\b(?:сумісн\w*|типологі\w*|тип|любов\w*|шлюб\w*|стосунк\w*|результат\w*|успіх\w*)\b.{0,70}\bгаранту\w*\b)",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "absolute-percentage",
        "100% claims require explicit attribution or rejection status",
        re.compile(r"(?<!\d)100\s*%", re.IGNORECASE),
    ),
    Rule(
        "compatibility-score",
        "the active framework has no numeric compatibility or success score",
        re.compile(
            r"\b(?:compatibility|success)\s+(?:score|percentage|rating)\b|"
            r"\b(?:score|rate|rank)\s+(?:the\s+)?compatibility\b|"
            r"(?:оценк[аи]|балл|процент|рейтинг)\s+совместимост\w*|"
            r"(?:оцінк[аи]|бал|відсоток|рейтинг|показник)\s+сумісност\w*",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "compatibility-weights",
        "weights and coefficients must not be presented as a current BWB scoring model",
        re.compile(
            r"\b(?:compatibility\s+weights?|weighted\s+compatibility|compatibility\s+coefficients?)\b|"
            r"(?:вес(?:а|ы|ов)?|коэффициент\w*)\s+совместимост\w*|"
            r"(?:ваг(?:а|и)?|коефіцієнт\w*)\s+сумісност\w*",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "strategic-values",
        "values belong to the value-moral foundation, not the strategic level",
        re.compile(
            r"\bstrategic(?:\s+(?:level|compatibility))?\s*(?::|=|->|→|—|\|)\s*(?:shared\s+)?values?\b|"
            r"\bvalues?\s+(?:are|as)\s+(?:a\s+)?strategic(?:\s+level)?\b|"
            r"\bstrategic\s+values?\b|"
            r"\bстратегическ\w*(?:\s+уров\w*)?\s*(?::|=|->|→|—|\|)\s*ценност\w*|"
            r"\bценност\w*\s+(?:являются|как)\s+стратегическ\w*|"
            r"\bстратегічн\w*(?:\s+рів\w*)?\s*(?::|=|->|→|—|\|)\s*цінност\w*|"
            r"\bцінност\w*\s+(?:є|як)\s+стратегічн\w*",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "type-determines-person",
        "a type must not determine character, morality, dignity, destiny, safety, or outcome",
        re.compile(
            r"\btype\b.{0,80}\bdetermines?\b.{0,80}\b(?:character|morality|worth|dignity|destiny|safety|outcome)\b|"
            r"\bтип\b.{0,80}\bопределя\w*\b.{0,80}\b(?:характер|морал\w*|достоинств\w*|судьб\w*|безопасност\w*|исход\w*)\b|"
            r"\bтип\b.{0,80}\bвизнача\w*\b.{0,80}\b(?:характер|морал\w*|гідн\w*|дол\w*|безпек\w*|результат\w*)\b",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "bwb-personality-typology",
        "Before We Build models process predisposition hypotheses, not personality types",
        re.compile(
            r"\b(?:before\s+we\s+build|bwb)\b.{0,100}\b(?:"
            r"personality\s+(?:typolog(?:y|ies)|type\s+system)|"
            r"типологи\w*\s+личност\w*|систем\w*\s+тип\w*\s+личност\w*|"
            r"типологі\w*\s+особист\w*|систем\w*\s+тип\w*\s+особист\w*"
            r")\b",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "systems-proven-independent",
        "describe typology systems as non-equivalent/separately modeled, not empirically independent",
        re.compile(
            r"\b(?:empirically\s+)?independent\s+(?:typolog(?:y|ies)|systems?)\b|"
            r"\b(?:типологи\w*|систем\w*)\s+эмпирически\s+независим\w*\b|"
            r"\b(?:типологі\w*|систем\w*)\s+емпірично\s+незалежн\w*\b",
            re.IGNORECASE,
        ),
    ),
)

NEGATED_RE = re.compile(
    r"(?:\bnot\b|\bnever\b|\bcannot\b|\bcan't\b|\bdoes\s+not\b|\bdo\s+not\b|"
    r"\bno\b|\brather\s+than\b|\binstead\s+of\b|\bwithout\b|"
    r"\bне\b|\bни\b|\bні\b|\bне\s+може\b|\bне\s+є\b|\bне\s+является\b).{0,120}$",
    re.IGNORECASE,
)
ALLOW_MARKER_RE = re.compile(
    r"<!--\s*claim-audit:\s*allow\s+reason=([a-z0-9._-]+)\s*-->", re.IGNORECASE
)
PERMITTED_ATTRIBUTED_STATUSES = {
    "source-attribution",
    "contested",
    "rejected",
    "historical-proposal",
}
PROHIBITION_CONTEXT_RE = re.compile(
    r"\b(?:reject|rewrite|avoid|forbid|prohibit|block|unsafe|red\s+flags?|prohibited\s+output|"
    r"flag\s+or\s+reject|must\s+not|cannot|can't|do\s+not|does\s+not\s+claim|never|"
    r"non[- ]claims?|incorrect|has\s+no|currently\s+has\s+no|no\s+current)\b|"
    r"\b(?:нельзя|запрещ\w*|не\s+следует|не\s+должен|не\s+может|не\s+утвержда\w*|"
    r"не[- ]клейм\w*|отверг\w*)\b|"
    r"\b(?:не\s+можна|заборон\w*|не\s+слід|не\s+повинен|не\s+ствердж\w*|відхил\w*)\b|"
    r"(?:твердження|утверждения).{0,70}(?:не\s+можна|нельзя)",
    re.IGNORECASE,
)


def _load_allowlist(path: Path | None) -> dict[str, set[str]]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("allowlist must be a JSON object mapping paths to rule-code arrays")
    result: dict[str, set[str]] = {}
    for key, value in data.items():
        if not isinstance(value, list):
            raise ValueError(f"allowlist value for {key!r} must be an array")
        result[str(key)] = {str(item) for item in value}
    return result


def _negated(line: str, start: int, end: int) -> bool:
    # Include the full matched phrase: compound rules often begin at "type" or
    # "strategic" while the negation appears later ("type does not determine").
    context = line[max(0, start - 80) : end]
    return bool(NEGATED_RE.search(context))


def _inline_allowed(lines: list[str], index: int) -> bool:
    current = lines[index]
    previous = lines[index - 1] if index > 0 else ""
    return bool(ALLOW_MARKER_RE.search(current) or ALLOW_MARKER_RE.search(previous))


def _prohibited_example_context(lines: list[str], index: int) -> bool:
    start = max(0, index - 12)
    context = "\n".join(lines[start : index + 1]).replace("*", "").replace("`", "")
    if PROHIBITION_CONTEXT_RE.search(context):
        return True
    # Lists of forbidden wording can be longer than a small look-behind window.
    for prior in range(index, max(-1, index - 60), -1):
        line = lines[prior]
        if re.match(r"^#{1,6}\s+", line):
            heading = re.sub(r"[*_`]", "", line)
            return bool(PROHIBITION_CONTEXT_RE.search(heading))
    return False


def _active_claim_status(lines: list[str], index: int, claims: dict[str, str]) -> str | None:
    for prior in range(index, -1, -1):
        match = CLAIM_MARKER_RE.search(lines[prior])
        if match:
            return claims.get(match.group(1))
    return None


def audit_claims(
    root: Path,
    *,
    strict: bool = False,
    scan_entries: tuple[str, ...] = DEFAULT_SCAN_ENTRIES,
    allowlist_path: Path | None = None,
) -> list[Diagnostic]:
    root = root.resolve()
    allowlist = _load_allowlist(allowlist_path)
    pages = {page.path.resolve(): page for page in load_wiki_pages(root)}
    diagnostics: list[Diagnostic] = []

    for path in markdown_files(root, scan_entries):
        page = pages.get(path.resolve())
        if page and page.status != "active":
            continue
        text = path.read_text(encoding="utf-8")
        metadata, _, _ = parse_frontmatter(text)
        claims = claim_map(metadata)
        relative = repo_relative(path, root)
        allowed_codes = allowlist.get(relative, set()) | allowlist.get(path.name, set())
        masked_lines = _mask_code(text).splitlines()
        original_lines = text.splitlines()
        for index, line in enumerate(masked_lines):
            for rule in RULES:
                if rule.code in allowed_codes:
                    continue
                for match in rule.pattern.finditer(line):
                    if rule.code == "retired-simulation-entity":
                        if _inline_allowed(original_lines, index):
                            continue
                        excerpt = original_lines[index].strip()
                        if len(excerpt) > 180:
                            excerpt = excerpt[:177] + "..."
                        diagnostics.append(
                            Diagnostic(
                                severity(strict),
                                rule.code,
                                f"{rule.explanation}; found: {excerpt!r}",
                                relative,
                                index + 1,
                            )
                        )
                        continue
                    if (
                        _negated(line, match.start(), match.end())
                        or _inline_allowed(original_lines, index)
                        or _prohibited_example_context(original_lines, index)
                    ):
                        continue
                    status = _active_claim_status(original_lines, index, claims)
                    if status in PERMITTED_ATTRIBUTED_STATUSES:
                        continue
                    excerpt = original_lines[index].strip()
                    if len(excerpt) > 180:
                        excerpt = excerpt[:177] + "..."
                    diagnostics.append(
                        Diagnostic(
                            severity(strict),
                            rule.code,
                            f"{rule.explanation}; found: {excerpt!r}",
                            relative,
                            index + 1,
                        )
                    )
    return sorted(diagnostics, key=lambda item: (item.path or "", item.line or 0, item.code))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--allowlist", type=Path)
    parser.add_argument("--fail-on-warnings", action="store_true")
    args = parser.parse_args()

    diagnostics = audit_claims(
        args.root,
        strict=args.strict,
        allowlist_path=args.allowlist,
    )
    print_report(diagnostics, json_output=args.json)
    return exit_code(diagnostics, fail_on_warnings=args.fail_on_warnings)


if __name__ == "__main__":
    raise SystemExit(main())
