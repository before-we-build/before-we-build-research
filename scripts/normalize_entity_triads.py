#!/usr/bin/env python3
"""Normalize formulaic entity triads to equal, non-deterministic summaries.

The legacy English entity pages contained far more deterministic material than
their Russian and Ukrainian peers. This one-time, repeatable migration keeps
codes and attributed aliases while replacing unsupported portraits, celebrity
lists, and good/bad relation rankings with the same compact contract in all
three languages.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LANG_RE = re.compile(r"-(en|ru|uk)$")
PSY_ASPECTS = {
    "en": {"e": "Emotion", "l": "Logic", "v": "Will", "f": "Physics"},
    "ru": {"e": "Эмоция", "l": "Логика", "v": "Воля", "f": "Физика"},
    "uk": {"e": "Емоція", "l": "Логіка", "v": "Воля", "f": "Фізика"},
}
TEMP_ASPECTS = {
    "en": {"e": "Eternity", "n": "Present", "p": "Past", "f": "Future"},
    "ru": {"e": "Вечность", "n": "Настоящее", "p": "Прошлое", "f": "Будущее"},
    "uk": {"e": "Вічність", "n": "Теперішнє", "p": "Минуле", "f": "Майбутнє"},
}
ARCHETYPE_NAMES = {
    "avtor-author": "Author",
    "captain-kapitan": "Captain",
    "chronicler-letopisets": "Chronicler",
    "exile-izgnannik": "Exile",
    "guest-gost": "Guest",
    "guru": "Guru",
    "host-khozyain": "Host",
    "kritik-critic": "Critic",
    "local-mestnyi": "Local",
    "passenger-passazhir": "Passenger",
    "philistine-obyvatel": "Philistine",
    "philosopher-filosof": "Philosopher",
    "reader-chitatel": "Reader",
    "stewersman-rulevoi": "Steersman",
    "stowaway-bezbiletnik": "Stowaway",
    "student-uchenik": "Student",
}
POSITION_MEANING = {
    "en": {
        1: "an autonomous organizing frame",
        2: "a collaborative and adaptive process",
        3: "a sensitive error-monitoring and revision zone",
        4: "a receptive or externally supported frame",
    },
    "ru": {
        1: "автономная организующая рамка",
        2: "совместный и адаптивный процесс",
        3: "чувствительная зона проверки ошибок и пересмотра",
        4: "принимающая или поддерживаемая извне рамка",
    },
    "uk": {
        1: "автономна організувальна рамка",
        2: "спільний та адаптивний процес",
        3: "чутлива зона перевірки помилок і перегляду",
        4: "приймальна або підтримувана ззовні рамка",
    },
}


def language(path: Path) -> str:
    match = LANG_RE.search(path.stem)
    return match.group(1) if match else "en"


def group_name(path: Path) -> str:
    return LANG_RE.sub("", path.stem)


def split_document(text: str) -> tuple[str, str]:
    end = text.find("\n---\n", 4)
    if not text.startswith("---\n") or end == -1:
        raise ValueError("entity page must have frontmatter")
    return text[: end + 5], text[end + 5 :]


def field(frontmatter: str, name: str) -> str:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*(.+)$", frontmatter)
    return match.group(1).strip().strip('"') if match else ""


def update_frontmatter(frontmatter: str, sources: list[str]) -> str:
    frontmatter = re.sub(r"(?m)^updated:.*$", "updated: 2026-08-30", frontmatter)
    source_line = "sources: " + json.dumps(sources, ensure_ascii=False)
    frontmatter = re.sub(r"(?m)^sources:.*$", source_line, frontmatter)
    return frontmatter


def local_slug(base: str, lang: str) -> str:
    return f"{base}-{lang}"


def language_switch(group: str, lang: str) -> str:
    labels = {"en": "English", "ru": "Русский", "uk": "Українська"}
    parts = []
    for locale in ("en", "ru", "uk"):
        if locale == lang:
            parts.append(labels[locale])
        else:
            parts.append(f"[[{local_slug(group, locale)}|{labels[locale]}]]")
    return " · ".join(parts)


def title_from_body(body: str) -> str:
    match = re.search(r"(?m)^#\s+(.+)$", body)
    return match.group(1).strip() if match else "Entity"


def type_body(group: str, title: str, lang: str, system: str, code: str) -> str:
    switcher = language_switch(group, lang)
    aspect_map = PSY_ASPECTS[lang] if system == "psychosophy" else TEMP_ASPECTS[lang]
    rows = "\n".join(f"- {index}{letter.upper()} — {aspect_map[letter]}" for index, letter in enumerate(code, 1))
    position_rows = "\n".join(
        f"- {index}: {POSITION_MEANING[lang][index]}" for index in range(1, 5)
    )
    if lang == "en":
        layer = "operational joint-action" if system == "psychosophy" else "strategic temporal-existential"
        system_name = "Psychosophy" if system == "psychosophy" else "Temporistics"
        return f"""# {title}

{switcher}

<!-- section:definition -->
This page records a **{system_name} type hypothesis** at the {layer} level. The code is a compact model of a possible pattern of perceiving or organizing experience. It is not an observable entity, a complete person, a diagnosis, or a deterministic verdict.

<!-- section:code -->
## Code decomposition

{rows}

<!-- section:reading -->
## How to read the positions

{position_rows}

<!-- section:caveat -->
## Important

A result is provisional. Check it against repeated situations, counterexamples, alternative results, role, skill, stress, health, culture, and context. The code does not determine character, morality, dignity, safety, profession, or relationship outcome.

<!-- section:questions -->
## Questions for verification

- Which repeated observations support this ordering?
- Which situations contradict it or suggest another code?
- Could role, learning, pressure, or circumstance explain the pattern better?

<!-- section:see-also -->
## See also

- [[{local_slug(system + '-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""
    if lang == "ru":
        layer = "операционном уровне совместного действия" if system == "psychosophy" else "стратегическом временно-смысловом уровне"
        system_name = "Психософии" if system == "psychosophy" else "Темпористики"
        return f"""# {title}

{switcher}

<!-- section:definition -->
Страница фиксирует **гипотезу типа {system_name}** на {layer}. Код — это компактная модель возможного паттерна восприятия или организации опыта. Он не является наблюдаемым объектом, полным описанием человека, диагнозом или детерминированным вердиктом.

<!-- section:code -->
## Разбор кода

{rows}

<!-- section:reading -->
## Как читать позиции

{position_rows}

<!-- section:caveat -->
## Важно

Результат предварителен. Проверяйте его по повторяющимся ситуациям, контрпримерам, альтернативным результатам, роли, навыкам, стрессу, здоровью, культуре и контексту. Код не определяет характер, нравственность, достоинство, безопасность, профессию или исход отношений.

<!-- section:questions -->
## Вопросы для проверки

- Какие повторяющиеся наблюдения поддерживают этот порядок?
- Какие ситуации ему противоречат или указывают на другой код?
- Не объясняют ли паттерн лучше роль, обучение, давление или обстоятельства?

<!-- section:see-also -->
## См. также

- [[{local_slug(system + '-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""
    layer = "операційному рівні спільної дії" if system == "psychosophy" else "стратегічному часово-смисловому рівні"
    system_name = "Психософії" if system == "psychosophy" else "Темпористики"
    return f"""# {title}

{switcher}

<!-- section:definition -->
Сторінка фіксує **гіпотезу типу {system_name}** на {layer}. Код — це компактна модель можливого патерну сприйняття або організації досвіду. Він не є спостережуваним об'єктом, повним описом людини, діагнозом або детермінованим вердиктом.

<!-- section:code -->
## Розбір коду

{rows}

<!-- section:reading -->
## Як читати позиції

{position_rows}

<!-- section:caveat -->
## Важливо

Результат попередній. Перевіряйте його за повторюваними ситуаціями, контрприкладами, альтернативними результатами, роллю, навичками, стресом, здоров'ям, культурою та контекстом. Код не визначає характер, моральність, гідність, безпеку, професію або результат стосунків.

<!-- section:questions -->
## Питання для перевірки

- Які повторювані спостереження підтримують цей порядок?
- Які ситуації йому суперечать або вказують на інший код?
- Чи не пояснюють патерн краще роль, навчання, тиск або обставини?

<!-- section:see-also -->
## Див. також

- [[{local_slug(system + '-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""


def socionics_body(group: str, title: str, lang: str, code: str, stack: str, alias: str) -> str:
    switcher = language_switch(group, lang)
    if lang == "en":
        return f"""# {title}

{switcher}

<!-- section:definition -->
This page records a **Socionics tactical-level hypothesis** about information modeling and exchange. It is not an MBTI type, diagnosis, full personality portrait, or deterministic relation verdict.

<!-- section:code -->
## Compact reference

- Code: **{code}**
- Traditionally attributed alias: **{alias}**
- Model A notation used in this repository: **{stack}**

<!-- section:reading -->
## How to read it

Use the page as a comparison prompt, not an identity label. Ask which repeated information tasks fit, which alternatives remain plausible, and where role, expertise, language, stress, or context gives a better explanation.

<!-- section:caveat -->
## Important

The hypothesis does not determine morality, dignity, spiritual maturity, profession, safety, or relationship outcome. Relation names are structural mnemonics, not a scale from best to worst.

<!-- section:questions -->
## Questions for verification

- Which information does the person repeatedly notice, request, or omit?
- Which kinds of correction help or hinder in comparable tasks?
- What evidence distinguishes this code from its nearest alternatives?

<!-- section:see-also -->
## See also

- [[{local_slug('socionics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""
    if lang == "ru":
        return f"""# {title}

{switcher}

<!-- section:definition -->
Страница фиксирует **гипотезу тактического уровня Соционики** об информационном моделировании и обмене. Это не MBTI-тип, диагноз, полный портрет личности или детерминированный вердикт об отношениях.

<!-- section:code -->
## Краткая справка

- Код: **{code}**
- Традиционно приписываемый псевдоним: **{alias}**
- Обозначение Модели A, используемое в репозитории: **{stack}**

<!-- section:reading -->
## Как читать

Используйте страницу как повод для сравнения, а не ярлык идентичности. Проверяйте, какие повторяющиеся информационные задачи совпадают, какие альтернативы остаются правдоподобными и где роль, опыт, язык, стресс или контекст объясняют наблюдение лучше.

<!-- section:caveat -->
## Важно

Гипотеза не определяет нравственность, достоинство, духовную зрелость, профессию, безопасность или исход отношений. Названия отношений — структурные мнемоники, а не шкала от лучшего к худшему.

<!-- section:questions -->
## Вопросы для проверки

- Какую информацию человек повторяющимся образом замечает, запрашивает или пропускает?
- Какие виды исправления помогают или мешают в сопоставимых задачах?
- Какие данные отличают этот код от ближайших альтернатив?

<!-- section:see-also -->
## См. также

- [[{local_slug('socionics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""
    return f"""# {title}

{switcher}

<!-- section:definition -->
Сторінка фіксує **гіпотезу тактичного рівня Соціоніки** про інформаційне моделювання й обмін. Це не MBTI-тип, діагноз, повний портрет особистості або детермінований вердикт про стосунки.

<!-- section:code -->
## Коротка довідка

- Код: **{code}**
- Традиційно приписуваний псевдонім: **{alias}**
- Позначення Моделі A, використане в репозиторії: **{stack}**

<!-- section:reading -->
## Як читати

Використовуйте сторінку як привід для порівняння, а не ярлик ідентичності. Перевіряйте, які повторювані інформаційні завдання збігаються, які альтернативи лишаються правдоподібними та де роль, досвід, мова, стрес або контекст пояснюють спостереження краще.

<!-- section:caveat -->
## Важливо

Гіпотеза не визначає моральність, гідність, духовну зрілість, професію, безпеку або результат стосунків. Назви відносин — структурні мнемоніки, а не шкала від найкращого до найгіршого.

<!-- section:questions -->
## Питання для перевірки

- Яку інформацію людина повторювано помічає, запитує або пропускає?
- Які види виправлення допомагають або заважають у порівнюваних завданнях?
- Які дані відрізняють цей код від найближчих альтернатив?

<!-- section:see-also -->
## Див. також

- [[{local_slug('socionics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""


def archetype_body(group: str, title: str, lang: str, code: str, alias: str) -> str:
    position = int(code[0])
    aspect = TEMP_ASPECTS[lang][code[1].lower()]
    switcher = language_switch(group, lang)
    if lang == "en":
        return f"""# {title}

{switcher}

<!-- section:definition -->
**{code}** places **{aspect}** in position {position} of Temporistics. This is a strategic temporal-existential hypothesis, not a diagnosis, spiritual status, personality essence, or prediction.

<!-- section:meaning -->
## Compact meaning

**{alias}** is a traditional working alias for **{code} / {aspect}**. The position is modeled as {POSITION_MEANING[lang][position]}. The alias is a mnemonic, not an observable kind of person.

<!-- section:reading -->
## How to read it

Compare the hypothesis with repeated decisions and stories, counterexamples, and alternative codes. Separate a stable pattern from role, crisis, culture, skill, health, and circumstance.

<!-- section:caveat -->
## Important

The archetype does not determine morality, dignity, calling, profession, safety, or relationship outcome.

<!-- section:questions -->
## Questions for verification

- How does this temporal theme appear across different contexts?
- What observation would favor another position?
- Is the pattern stable outside pressure or a particular role?

<!-- section:see-also -->
## See also

- [[{local_slug('temporistics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""
    if lang == "ru":
        return f"""# {title}

{switcher}

<!-- section:definition -->
**{code}** помещает аспект **{aspect}** в {position}-ю позицию Темпористики. Это стратегическая временно-смысловая гипотеза, а не диагноз, духовный статус, сущность личности или предсказание.

<!-- section:meaning -->
## Краткий смысл

**{alias}** — традиционное рабочее название для **{code} / {aspect}**. Позиция моделируется как {POSITION_MEANING[lang][position]}. Название служит мнемоникой, а не обозначением наблюдаемого типа человека.

<!-- section:reading -->
## Как читать

Сравнивайте гипотезу с повторяющимися решениями и историями, контрпримерами и альтернативными кодами. Отделяйте устойчивый паттерн от роли, кризиса, культуры, навыков, здоровья и обстоятельств.

<!-- section:caveat -->
## Важно

Архетип не определяет нравственность, достоинство, призвание, профессию, безопасность или исход отношений.

<!-- section:questions -->
## Вопросы для проверки

- Как эта временная тема проявляется в разных контекстах?
- Какое наблюдение поддержало бы другую позицию?
- Сохраняется ли паттерн вне давления или конкретной роли?

<!-- section:see-also -->
## См. также

- [[{local_slug('temporistics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""
    return f"""# {title}

{switcher}

<!-- section:definition -->
**{code}** розміщує аспект **{aspect}** у {position}-й позиції Темпористики. Це стратегічна часово-смислова гіпотеза, а не діагноз, духовний статус, сутність особистості або передбачення.

<!-- section:meaning -->
## Короткий зміст

**{alias}** — традиційна робоча назва для **{code} / {aspect}**. Позиція моделюється як {POSITION_MEANING[lang][position]}. Назва слугує мнемонікою, а не позначенням спостережуваного типу людини.

<!-- section:reading -->
## Як читати

Порівнюйте гіпотезу з повторюваними рішеннями й історіями, контрприкладами та альтернативними кодами. Відокремлюйте стійкий патерн від ролі, кризи, культури, навичок, здоров'я й обставин.

<!-- section:caveat -->
## Важливо

Архетип не визначає моральність, гідність, покликання, професію, безпеку або результат стосунків.

<!-- section:questions -->
## Питання для перевірки

- Як ця часова тема проявляється в різних контекстах?
- Яке спостереження підтримало б іншу позицію?
- Чи зберігається патерн поза тиском або конкретною роллю?

<!-- section:see-also -->
## Див. також

- [[{local_slug('temporistics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    entities = args.root.resolve() / "wiki" / "entities"
    paths = sorted(entities.glob("*.md"))
    groups: dict[str, dict[str, Path]] = {}
    for path in paths:
        groups.setdefault(group_name(path), {})[language(path)] = path

    changes: list[tuple[Path, str]] = []
    for group, peers in sorted(groups.items()):
        if set(peers) != {"en", "ru", "uk"}:
            continue
        for lang, path in peers.items():
            text = path.read_text(encoding="utf-8")
            frontmatter, old_body = split_document(text)
            title = title_from_body(old_body)
            if group.startswith("psychosophy-type-"):
                code = group.removeprefix("psychosophy-type-")
                body = type_body(group, title, lang, "psychosophy", code)
                sources = [
                    f"wiki/entities/{local_slug('psychosophy-overview', lang)}.md",
                    f"wiki/concepts/{local_slug('compatibility-level-boundaries', lang)}.md",
                    f"wiki/concepts/{local_slug('test-result-reading-guide', lang)}.md",
                ]
            elif group.startswith("temporistics-type-"):
                code = group.removeprefix("temporistics-type-")
                body = type_body(group, title, lang, "temporistics", code)
                sources = [
                    f"wiki/entities/{local_slug('temporistics-overview', lang)}.md",
                    f"wiki/concepts/{local_slug('compatibility-level-boundaries', lang)}.md",
                    f"wiki/concepts/{local_slug('test-result-reading-guide', lang)}.md",
                ]
            elif group in ARCHETYPE_NAMES:
                ru_text = peers["ru"].read_text(encoding="utf-8")
                code_match = re.search(r"\*\*([1-4][PNEF])\*\*", ru_text)
                if not code_match:
                    raise ValueError(f"cannot find archetype code for {group}")
                code = code_match.group(1)
                alias = ARCHETYPE_NAMES[group] if lang == "en" else title.split("—")[-1].strip()
                body = archetype_body(group, title, lang, code, alias)
                sources = [
                    "raw/temporistics",
                    f"wiki/entities/{local_slug('temporistics-overview', lang)}.md",
                    f"wiki/concepts/{local_slug('compatibility-level-boundaries', lang)}.md",
                    f"wiki/concepts/{local_slug('test-result-reading-guide', lang)}.md",
                ]
            elif re.match(r"^[a-z]{3}-.+-(?:extrovert|introvert)$", group):
                code = group.split("-", 1)[0].upper()
                en_text = peers["en"].read_text(encoding="utf-8")
                stack_match = re.search(
                    r"(?:Function Stack|стек функций|стек функцій|"
                    r"Model A notation used in this repository|"
                    r"Обозначение Модели A, используемое в репозитории|"
                    r"Позначення Моделі A, використане в репозиторії):\s*\*\*?([^*\n]+)",
                    en_text,
                    re.IGNORECASE,
                )
                if not stack_match:
                    stack_match = re.search(r"Function Stack:\s*([^\n]+)", en_text)
                stack = (stack_match.group(1).strip() if stack_match else "see Model A reference")
                alias_match = re.search(r"\(([^)]+)\)", title)
                if lang == "en":
                    alias = alias_match.group(1) if alias_match else group
                else:
                    alias = title.split("—")[-1].strip()
                body = socionics_body(group, title, lang, code, stack, alias)
                sources = [
                    "raw/socionics/what-is-socionics.md",
                    "raw/socionics/model-a.md",
                    f"wiki/entities/{local_slug('socionics-overview', lang)}.md",
                    f"wiki/concepts/{local_slug('compatibility-level-boundaries', lang)}.md",
                    f"wiki/concepts/{local_slug('test-result-reading-guide', lang)}.md",
                ]
            else:
                continue
            new_text = update_frontmatter(frontmatter, sources) + body.rstrip() + "\n"
            if new_text != text:
                changes.append((path, new_text))

    if args.write:
        for path, text in changes:
            path.write_text(text, encoding="utf-8")
    print(f"Entity files requiring normalization: {len(changes)}")
    for path, _ in changes[:20]:
        print(path.relative_to(args.root.resolve()))
    if len(changes) > 20:
        print(f"... {len(changes) - 20} more")
    return 1 if args.check and changes else 0


if __name__ == "__main__":
    raise SystemExit(main())
