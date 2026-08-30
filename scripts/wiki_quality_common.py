#!/usr/bin/env python3
"""Shared, dependency-free helpers for the Before We Build wiki checks."""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = REPO_ROOT / "wiki"
LOCALES = ("en", "ru", "uk")
LOCALE_SUFFIX_RE = re.compile(r"^(?P<group>.+)-(?P<lang>en|ru|uk)$", re.IGNORECASE)
SECTION_MARKER_RE = re.compile(r"<!--\s*section:([a-z0-9][a-z0-9._-]*)\s*-->", re.IGNORECASE)
CLAIM_MARKER_RE = re.compile(r"<!--\s*claim:([a-z0-9][a-z0-9._-]*)\s*-->", re.IGNORECASE)


@dataclass(frozen=True)
class Diagnostic:
    severity: str
    code: str
    message: str
    path: str | None = None
    line: int | None = None

    def format(self) -> str:
        location = self.path or "repository"
        if self.line is not None:
            location += f":{self.line}"
        return f"{self.severity.upper()} [{self.code}] {location}: {self.message}"

    def as_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
        }
        if self.path is not None:
            result["path"] = self.path
        if self.line is not None:
            result["line"] = self.line
        return result


@dataclass
class WikiPage:
    path: Path
    relative_path: Path
    metadata: dict[str, Any]
    body: str
    frontmatter_error: str | None = None
    section_ids: tuple[str, ...] = field(default_factory=tuple)

    @property
    def filename_language(self) -> str | None:
        match = LOCALE_SUFFIX_RE.match(self.path.stem)
        return match.group("lang").lower() if match else None

    @property
    def language(self) -> str | None:
        value = self.metadata.get("lang")
        return str(value).lower() if value else self.filename_language

    @property
    def inferred_group(self) -> str:
        match = LOCALE_SUFFIX_RE.match(self.path.stem)
        return match.group("group") if match else self.path.stem

    @property
    def translation_group(self) -> str:
        return str(self.metadata.get("translation_group") or self.inferred_group)

    @property
    def status(self) -> str:
        # Legacy pages predate the status field and are reader-visible, so they
        # must be audited as active until migration explicitly classifies them.
        return str(self.metadata.get("document_status") or "active")

    @property
    def title(self) -> str:
        return str(self.metadata.get("title") or self.path.stem)


def repo_relative(path: Path, root: Path = REPO_ROOT) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _strip_comment(value: str) -> str:
    """Strip a YAML-style comment while preserving hashes in quoted strings."""
    quote: str | None = None
    for index, char in enumerate(value):
        if char in {"'", '"'}:
            if quote is None:
                quote = char
            elif quote == char:
                quote = None
        elif char == "#" and quote is None and (index == 0 or value[index - 1].isspace()):
            return value[:index].rstrip()
    return value.strip()


def parse_scalar(value: str) -> Any:
    value = _strip_comment(value.strip())
    if value == "":
        return None
    if value in {"[]", "{}"}:
        return [] if value == "[]" else {}
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        try:
            parsed = ast.literal_eval(value)
            if isinstance(parsed, list):
                return parsed
        except (ValueError, SyntaxError):
            pass
        return [parse_scalar(item) for item in re.split(r",\s*", inner)]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if value.lower() in {"null", "none", "~"}:
        return None
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, str | None]:
    """Parse the small YAML subset used by this repository.

    The project intentionally keeps quality tooling dependency-free. This parser
    supports top-level scalars, inline lists, block lists, and lists of shallow
    mappings (the shape used by ``claims``). Unsupported YAML is reported rather
    than guessed.
    """

    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text, "missing opening frontmatter delimiter"

    lines = text.splitlines(keepends=True)
    closing_index: int | None = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break
    if closing_index is None:
        return {}, text, "missing closing frontmatter delimiter"

    raw_lines = [line.rstrip("\r\n") for line in lines[1:closing_index]]
    body = "".join(lines[closing_index + 1 :])
    result: dict[str, Any] = {}
    index = 0
    try:
        while index < len(raw_lines):
            raw = raw_lines[index]
            index += 1
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            if raw[:1].isspace():
                raise ValueError(f"unexpected indentation on line {index}")
            match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", raw)
            if not match:
                raise ValueError(f"unsupported frontmatter syntax on line {index}")
            key, raw_value = match.group(1), match.group(2) or ""
            if raw_value.strip():
                result[key] = parse_scalar(raw_value)
                continue

            block: list[Any] = []
            current_mapping: dict[str, Any] | None = None
            while index < len(raw_lines):
                child = raw_lines[index]
                if not child.strip():
                    index += 1
                    continue
                indent = len(child) - len(child.lstrip(" "))
                if indent == 0:
                    break
                if indent < 2:
                    raise ValueError(f"invalid indentation on line {index + 1}")
                stripped = child.strip()
                if stripped.startswith("-"):
                    item = stripped[1:].strip()
                    mapping_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", item)
                    if mapping_match:
                        current_mapping = {
                            mapping_match.group(1): parse_scalar(mapping_match.group(2))
                        }
                        block.append(current_mapping)
                    else:
                        current_mapping = None
                        block.append(parse_scalar(item))
                else:
                    mapping_match = re.match(
                        r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", stripped
                    )
                    if current_mapping is None or not mapping_match:
                        raise ValueError(
                            f"unsupported nested frontmatter syntax on line {index + 1}"
                        )
                    current_mapping[mapping_match.group(1)] = parse_scalar(
                        mapping_match.group(2)
                    )
                index += 1
            result[key] = block
    except ValueError as exc:
        return result, body, str(exc)

    return result, body, None


def load_wiki_pages(root: Path = REPO_ROOT) -> list[WikiPage]:
    wiki_dir = root / "wiki"
    if not wiki_dir.exists():
        return []
    pages: list[WikiPage] = []
    for path in sorted(wiki_dir.rglob("*.md")):
        metadata, body, error = parse_frontmatter(path.read_text(encoding="utf-8"))
        pages.append(
            WikiPage(
                path=path,
                relative_path=path.relative_to(root),
                metadata=metadata,
                body=body,
                frontmatter_error=error,
                section_ids=tuple(SECTION_MARKER_RE.findall(body)),
            )
        )
    return pages


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def claim_map(metadata: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for claim in as_list(metadata.get("claims")):
        if isinstance(claim, dict) and claim.get("id"):
            result[str(claim["id"])] = str(claim.get("status") or "")
    return result


def normalize_reference_id(value: Any) -> str:
    """Normalize a localized wiki reference to a language-neutral identity."""
    text = str(value).strip().replace("\\", "/")
    suffix = ""
    if "#" in text:
        text, suffix = text.split("#", 1)
        suffix = "#" + suffix
    extension = ".md" if text.lower().endswith(".md") else ""
    if extension:
        text = text[:-3]
    parts = text.split("/")
    match = LOCALE_SUFFIX_RE.match(parts[-1])
    if match:
        parts[-1] = match.group("group")
    return "/".join(parts).lower() + suffix.lower()


def normalized_sources(metadata: dict[str, Any]) -> tuple[str, ...]:
    return tuple(sorted(normalize_reference_id(item) for item in as_list(metadata.get("sources"))))


def markdown_files(root: Path, entries: Sequence[str]) -> list[Path]:
    files: set[Path] = set()
    for entry in entries:
        candidate = root / entry
        if candidate.is_file() and candidate.suffix.lower() in {".md", ".markdown"}:
            files.add(candidate)
        elif candidate.is_dir():
            files.update(candidate.rglob("*.md"))
            files.update(candidate.rglob("*.markdown"))
    return sorted(files)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def severity(strict: bool, *, always_error: bool = False) -> str:
    return "error" if strict or always_error else "warning"


def print_report(diagnostics: Iterable[Diagnostic], *, json_output: bool = False) -> None:
    items = list(diagnostics)
    if json_output:
        print(json.dumps([item.as_dict() for item in items], ensure_ascii=False, indent=2))
        return
    if not items:
        print("OK: no issues found")
        return
    for item in items:
        print(item.format())
    errors = sum(item.severity == "error" for item in items)
    warnings = sum(item.severity == "warning" for item in items)
    print(f"\nSummary: {errors} error(s), {warnings} warning(s)")


def exit_code(diagnostics: Iterable[Diagnostic], *, fail_on_warnings: bool = False) -> int:
    items = list(diagnostics)
    if any(item.severity == "error" for item in items):
        return 1
    if fail_on_warnings and any(item.severity == "warning" for item in items):
        return 1
    return 0


def read_migration_map(root: Path = REPO_ROOT) -> dict[str, str]:
    path = root / "wiki" / "slug-migrations.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if isinstance(data, dict) and isinstance(data.get("migrations"), dict):
        data = data["migrations"]
    if not isinstance(data, dict):
        return {}
    return {str(key).replace("\\", "/"): str(value).replace("\\", "/") for key, value in data.items()}


def iter_lines(text: str) -> Iterator[tuple[int, str]]:
    for number, line in enumerate(text.splitlines(), start=1):
        yield number, line
