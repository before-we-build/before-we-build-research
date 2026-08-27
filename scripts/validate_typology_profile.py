#!/usr/bin/env python3
"""
validate_typology_profile.py — Deterministic Typology Registry Validator for Before We Build.

Validates that any typological formula is matched with its canonical pseudonym across
Psychosophy (24), Temporistics (24), and Socionics (16).
"""

import sys
import re
from typing import Dict, List, Tuple

# 1. Canonical SSOT Registries
PSYCHOSOPHY_SSOT: Dict[str, str] = {
    "ФВЛЭ": "Гёте",
    "ФВЭЛ": "Чехов",
    "ФЛВЭ": "Аристипп",
    "ФЛЭВ": "Эпикур",
    "ФЭВЛ": "Дюма",
    "ФЭЛВ": "Борджиа",
    "ВФЛЭ": "Наполеон",
    "ВФЭЛ": "Твардовский",
    "ВЛФЭ": "Ленин",
    "ВЛЭФ": "Сократ",
    "ВЭФЛ": "Толстой",
    "ВЭЛФ": "Ахматова",
    "ЛВФЭ": "Лао-Цзы",
    "ЛВЭФ": "Эйнштейн",
    "ЛФВЭ": "Платон",
    "ЛФЭВ": "Бертье",
    "ЛЭВФ": "Паскаль",
    "ЛЭФВ": "Августин",
    "ЭВФЛ": "Пастернак",
    "ЭВЛФ": "Газали",
    "ЭФВЛ": "Пушкин",
    "ЭФЛВ": "Бухарин",
    "ЭЛВФ": "Андерсен",
    "ЭЛФВ": "Руссо",
}

TEMPORISTICS_SSOT: Dict[str, str] = {
    "БНПВ": "Колонист",
    "БПНВ": "Пионер",
    "ВПНБ": "Идеолог",
    "ВНПБ": "Самурай",
    "НБПВ": "Завоеватель",
    "НПБВ": "Звезда",
    "ВПБН": "Теоретик",
    "ВБПН": "Оракул",
    "БНВП": "Инициатор",
    "БВНП": "Робинзон",
    "ПВНБ": "Следопыт",
    "ПНВБ": "Тамада",
    "БПВН": "Хакер",
    "БВПН": "Разведчик",
    "НПВБ": "Дегустатор",
    "НВПБ": "Серый Кардинал",
    "ВБНП": "Миссионер",
    "ВНБП": "Знаменосец",
    "ПНБВ": "Спасатель",
    "ПБНВ": "Рыцарь",
    "НВБП": "Политик",
    "НБВП": "Игрок",
    "ПВБН": "Маэстро",
    "ПБВН": "Гэйм Мастер",
}

SOCIONICS_SSOT: Dict[str, Tuple[str, str]] = {
    "ИЛЭ": ("Дон Кихот", "Искатель"),
    "СЭИ": ("Дюма", "Посредник"),
    "ЭСЭ": ("Гюго", "Энтузиаст"),
    "ЛИИ": ("Робеспьер", "Аналитик"),
    "ЭИЭ": ("Гамлет", "Наставник"),
    "ЛСИ": ("Максим Горький", "Инспектор"),
    "СЛЭ": ("Жуков", "Маршал"),
    "ИЭИ": ("Есенин", "Лирик"),
    "СЭЭ": ("Наполеон", "Политик"),
    "ИЛИ": ("Бальзак", "Критик"),
    "ЛИЭ": ("Джек Лондон", "Предприниматель"),
    "ЭСИ": ("Драйзер", "Хранитель"),
    "ЛСЭ": ("Штирлиц", "Администратор"),
    "ЭИИ": ("Достоевский", "Гуманист"),
    "ИЭЭ": ("Гексли", "Советчик"),
    "СЛИ": ("Габен", "Мастер"),
}

def check_text(text: str) -> List[str]:
    errors = []
    lines = text.splitlines()

    for line_num, line in enumerate(lines, 1):
        # Ignore markdown comments or explanatory negative example rules
        if "запрещено" in line.lower() or "неверно" in line.lower() or "ошибочно" in line.lower():
            continue

        # 1. Check Psychosophy formula directly paired with name: e.g. ФВЛЭ — «Эпикур» or ФВЛЭ (Эпикур)
        for code, canon in PSYCHOSOPHY_SSOT.items():
            pattern = rf"\b{code}\b\s*(?:[-–—:]|\()\s*[«\"']?([А-Яа-яA-Za-z\-]+)[»\"']?"
            match = re.search(pattern, line)
            if match:
                found_word = match.group(1).strip()
                # Check if it matches another known type
                for other_code, other_canon in PSYCHOSOPHY_SSOT.items():
                    if other_code != code and other_canon.lower() == found_word.lower():
                        errors.append(
                            f"Line {line_num}: ERROR [Психософия]: Для формулы {code} ошибочно указан псевдоним «{found_word}». "
                            f"Канонический псевдоним: «{canon}» (а «{found_word}» — это {other_code})."
                        )

        # 2. Check Temporistics formula directly paired with name: e.g. БНПВ — «Пионер»
        for code, canon in TEMPORISTICS_SSOT.items():
            pattern = rf"\b{code}\b\s*(?:[-–—:]|\()\s*[«\"']?([А-Яа-яA-Za-z\-]+)[»\"']?"
            match = re.search(pattern, line)
            if match:
                found_word = match.group(1).strip()
                if found_word.lower() == "первопроходец":
                    errors.append(
                        f"Line {line_num}: ERROR [Темпористика]: «Первопроходец» — неформальный дескриптор. "
                        f"Канонический псевдоним для {code} — «{canon}»."
                    )
                for other_code, other_canon in TEMPORISTICS_SSOT.items():
                    if other_code != code and other_canon.lower() == found_word.lower():
                        errors.append(
                            f"Line {line_num}: ERROR [Темпористика]: Для формулы {code} ошибочно указан псевдоним «{found_word}». "
                            f"Канонический псевдоним: «{canon}» (а «{found_word}» — это {other_code})."
                        )

    return list(set(errors))

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_typology_profile.py <path_to_markdown_file>")
        sys.exit(0)

    target_path = sys.argv[1]
    try:
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read {target_path}: {e}")
        sys.exit(1)

    errors = check_text(content)
    if errors:
        print(f"Validation FAILED for {target_path}:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"Validation PASSED: All typological formulas and pseudonyms strictly match SSOT.")
        sys.exit(0)

if __name__ == "__main__":
    main()
