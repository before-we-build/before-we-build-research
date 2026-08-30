#!/usr/bin/env python3
"""Normalize formulaic entity triads to equal, non-deterministic summaries.

The legacy English entity pages contained far more deterministic material than
their Russian and Ukrainian peers. This one-time, repeatable migration keeps
codes and attributed aliases while replacing unsupported portraits, celebrity
lists, and good/bad relation rankings with the same compact contract in all
three languages. Socionics type pages additionally derive an eight-row
aspect-operation × position-mode map from the canonical Model A stack.
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

SOCIONICS_ASPECT_OPERATIONS = {
    "en": {
        "Ne": "infer hidden properties and possible realizations of an object while preserving unrealized potential",
        "Se": "estimate present force, form, boundaries, resistance, and direct impact",
        "Te": "link actions and methods to observable changes and results, updating procedure from feedback",
        "Fe": "track internal dynamics of activation and state through expressed reactions and their spread",
        "Ni": "organize sequential processes into trajectory, temporal relations, pace, and transitions",
        "Si": "integrate simultaneous conditions and their effects on state, quality, and environmental fit",
        "Ti": "construct objective structural relations, comparisons, classifications, constraints, and invariants",
        "Fi": "represent stable subjective relations: attraction, significance, need, distance, and acceptability",
    },
    "ru": {
        "Ne": "выводить скрытые свойства и возможные реализации объекта, сохраняя нереализованный потенциал",
        "Se": "оценивать наличную силу, форму, границы, сопротивление и прямое воздействие",
        "Te": "связывать действия и методы с наблюдаемыми изменениями и результатами, обновляя процедуру по обратной связи",
        "Fe": "отслеживать внутреннюю динамику возбуждения и состояния через выраженные реакции и их распространение",
        "Ni": "организовывать последовательные процессы в траекторию, временные отношения, темп и переходы",
        "Si": "интегрировать одновременные условия и их влияние на состояние, качество и соответствие среды",
        "Ti": "строить объективные структурные отношения, сравнения, классификации, ограничения и инварианты",
        "Fi": "представлять устойчивые субъективные отношения: притяжение, значимость, потребность, дистанцию и приемлемость",
    },
    "uk": {
        "Ne": "виводити приховані властивості й можливі реалізації об'єкта, зберігаючи нереалізований потенціал",
        "Se": "оцінювати наявну силу, форму, межі, опір і прямий вплив",
        "Te": "пов'язувати дії та методи зі спостережуваними змінами й результатами, оновлюючи процедуру за зворотним зв'язком",
        "Fe": "відстежувати внутрішню динаміку збудження і стану через виражені реакції та їх поширення",
        "Ni": "організовувати послідовні процеси у траєкторію, часові відношення, темп і переходи",
        "Si": "інтегрувати одночасні умови та їхній вплив на стан, якість і відповідність середовища",
        "Ti": "будувати об'єктивні структурні відношення, порівняння, класифікації, обмеження та інваріанти",
        "Fi": "представляти стійкі суб'єктивні відношення: тяжіння, значущість, потребу, дистанцію і прийнятність",
    },
}

SOCIONICS_POSITION_MODES = {
    "en": {
        1: "stable foreground framing",
        2: "flexible situational production",
        3: "norm-guided, effortful application",
        4: "least stable modeling under pressure",
        5: "valued, externally scaffolded intake",
        6: "supported or activated development",
        7: "background monitoring",
        8: "automatic background production",
    },
    "ru": {
        1: "устойчивая рамка переднего плана",
        2: "гибкое ситуативное порождение",
        3: "нормативное применение с усилием",
        4: "наименее устойчивое моделирование под давлением",
        5: "ценностное восприятие с внешним каркасом",
        6: "поддерживаемое или активируемое развитие",
        7: "фоновое отслеживание",
        8: "автоматическое фоновое порождение",
    },
    "uk": {
        1: "стійка рамка переднього плану",
        2: "гнучке ситуативне породження",
        3: "нормативне застосування із зусиллям",
        4: "найменш стійке моделювання під тиском",
        5: "ціннісне сприйняття із зовнішнім каркасом",
        6: "підтримуваний або активований розвиток",
        7: "фонове відстеження",
        8: "автоматичне фонове породження",
    },
}

SOCIONICS_VERIFICATION_QUESTIONS = {
    "en": {
        "Ne": "Which viable property or alternative was preserved or excluded?",
        "Se": "What evidence changes the estimate of capacity, boundary, or resistance?",
        "Te": "Does the method reproduce the result after feedback changes?",
        "Fe": "Which expressed-state transition or propagation was detected or missed?",
        "Ni": "Does the inferred timing and direction still fit the sequence?",
        "Si": "Does the represented condition match experienced or observed state?",
        "Ti": "Does the structure preserve its rules without contradiction?",
        "Fi": "Does later interaction fit the represented significance and distance?",
    },
    "ru": {
        "Ne": "Какое жизнеспособное свойство или вариант сохранены либо исключены?",
        "Se": "Какие данные меняют оценку возможности непосредственного воздействия, границы или сопротивления?",
        "Te": "Воспроизводит ли метод результат после изменения обратной связи?",
        "Fe": "Какой переход или распространение выраженного состояния замечены либо пропущены?",
        "Ni": "Соответствуют ли предполагаемые время и направление последовательности?",
        "Si": "Совпадает ли представленное состояние с переживаемым или наблюдаемым?",
        "Ti": "Сохраняет ли структура свои правила без противоречий?",
        "Fi": "Соответствует ли последующее взаимодействие представленной значимости и дистанции?",
    },
    "uk": {
        "Ne": "Яку життєздатну властивість або варіант збережено чи виключено?",
        "Se": "Які дані змінюють оцінку можливості безпосереднього впливу, межі або опору?",
        "Te": "Чи відтворює метод результат після зміни зворотного зв'язку?",
        "Fe": "Який перехід або поширення вираженого стану помічено чи пропущено?",
        "Ni": "Чи відповідають припущені час і напрям послідовності?",
        "Si": "Чи збігається представлене становище з пережитим або спостережуваним станом?",
        "Ti": "Чи зберігає структура свої правила без суперечностей?",
        "Fi": "Чи відповідає подальша взаємодія представленій значущості й дистанції?",
    },
}

SOCIONICS_RIVAL = {
    "en": "expertise, task cues, role, language, health, stress, or familiarity",
    "ru": "экспертность, подсказки задачи, роль, язык, здоровье, стресс или знакомство",
    "uk": "експертність, підказки завдання, роль, мова, здоров'я, стрес або знайомство",
}

SOCIONICS_STACKS = {
    "ILE": "1Ne 2Ti 3Se 4Fi 5Si 6Fe 7Ni 8Te",
    "SEI": "1Si 2Fe 3Ni 4Te 5Ne 6Ti 7Se 8Fi",
    "ESE": "1Fe 2Si 3Te 4Ni 5Ti 6Ne 7Fi 8Se",
    "LII": "1Ti 2Ne 3Fi 4Se 5Fe 6Si 7Te 8Ni",
    "EIE": "1Fe 2Ni 3Te 4Si 5Ti 6Se 7Fi 8Ne",
    "LSI": "1Ti 2Se 3Fi 4Ne 5Fe 6Ni 7Te 8Si",
    "SLE": "1Se 2Ti 3Ne 4Fi 5Ni 6Fe 7Si 8Te",
    "IEI": "1Ni 2Fe 3Si 4Te 5Se 6Ti 7Ne 8Fi",
    "SEE": "1Se 2Fi 3Ne 4Ti 5Ni 6Te 7Si 8Fe",
    "ILI": "1Ni 2Te 3Si 4Fe 5Se 6Fi 7Ne 8Ti",
    "LIE": "1Te 2Ni 3Fe 4Si 5Fi 6Se 7Ti 8Ne",
    "ESI": "1Fi 2Se 3Ti 4Ne 5Te 6Ni 7Fe 8Si",
    "IEE": "1Ne 2Fi 3Se 4Ti 5Si 6Te 7Ni 8Fe",
    "SLI": "1Si 2Te 3Ni 4Fe 5Ne 6Fi 7Se 8Ti",
    "LSE": "1Te 2Si 3Fe 4Ni 5Fi 6Ne 7Ti 8Se",
    "EII": "1Fi 2Ne 3Ti 4Se 5Te 6Si 7Fe 8Ni",
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


def update_socionics_frontmatter(frontmatter: str, sources: list[str]) -> str:
    frontmatter = update_frontmatter(frontmatter, sources)
    frontmatter = re.sub(r"(?m)^semantic_version:.*$", "semantic_version: 2", frontmatter)
    frontmatter = re.sub(
        r"(?m)^reviewed_semantic_version:.*$",
        "reviewed_semantic_version: 2",
        frontmatter,
    )
    claims = """claims:
  - id: socionics-type-code-is-model-a-arrangement
    status: source-attribution
  - id: socionics-type-code-may-model-positioned-operations
    status: research-hypothesis
"""
    frontmatter = re.sub(r"(?ms)^claims:.*?(?=^caveat_ids:)", claims, frontmatter)
    frontmatter = re.sub(
        r"(?m)^caveat_ids:.*$",
        "caveat_ids: [not-personality-type, not-ability-profile, context-required, innateness-not-established]",
        frontmatter,
    )
    return frontmatter


def socionics_stack_entries(stack: str) -> list[tuple[int, str]]:
    entries = [(int(position), aspect) for position, aspect in re.findall(
        r"([1-8])(Ne|Ni|Se|Si|Te|Ti|Fe|Fi)", stack
    )]
    if len(entries) != 8 or {position for position, _ in entries} != set(range(1, 9)):
        raise ValueError(f"invalid Socionics stack: {stack}")
    return sorted(entries)


def socionics_process_rows(stack: str, lang: str) -> str:
    rows = []
    for position, aspect in socionics_stack_entries(stack):
        rows.append(
            f"| {position} | {aspect} | {SOCIONICS_ASPECT_OPERATIONS[lang][aspect]} | "
            f"{SOCIONICS_POSITION_MODES[lang][position]} | "
            f"{SOCIONICS_VERIFICATION_QUESTIONS[lang][aspect]} | {SOCIONICS_RIVAL[lang]} |"
        )
    return "\n".join(rows)


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
    process_rows = socionics_process_rows(stack, lang)
    if lang == "en":
        return f"""# {title}

{switcher}

<!-- section:definition -->
This page records a **Socionics tactical-level hypothesis** about positioned operations for building partial, correctable representations of one shared world. It is not an MBTI type, diagnosis, ability profile, full personality portrait, or deterministic relation verdict.

<!-- section:code -->
## Compact reference

- Code: **{code}**
- Traditionally attributed alias: **{alias}**
- Model A notation used in this repository: **{stack}**

<!-- section:process-map -->
## Eight-position process map

| Position | Aspect | Proposed aspect operation | Proposed position mode | Verification question | Rival explanations |
|---:|---|---|---|---|---|
{process_rows}

<!-- section:reading -->
## How to read it

Read each row as aspect operation × position mode. Use the page as a comparison prompt, not an identity label. Aspect evidence and position evidence must be gathered separately before the whole stack is preferred.

<!-- section:caveat -->
## Important

The hypothesis does not determine ability, innateness, morality, dignity, spiritual maturity, profession, safety, or relationship outcome. Positions 1/2/7/8 are not guaranteed strengths, and 3/4/5/6 are not diagnosed deficits.

<!-- section:questions -->
## Questions for verification

- What is selected, preserved after compression, inferred, and updated after feedback?
- Does the proposed position mode recur across comparable tasks?
- What evidence distinguishes this code from its nearest alternatives and rival explanations?

<!-- section:see-also -->
## See also

- [[{local_slug('socionics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
- [[{local_slug('socionics-reality-modeling', lang)}]]
"""
    if lang == "ru":
        return f"""# {title}

{switcher}

<!-- section:definition -->
Страница фиксирует **гипотезу тактического уровня Соционики** о позиционированных операциях построения частичных исправимых представлений одного общего мира. Это не MBTI-тип, диагноз, профиль способностей, полный портрет личности или детерминированный вердикт об отношениях.

<!-- section:code -->
## Краткая справка

- Код: **{code}**
- Традиционно приписываемый псевдоним: **{alias}**
- Обозначение Модели A, используемое в репозитории: **{stack}**

<!-- section:process-map -->
## Процессная карта восьми позиций

| Позиция | Аспект | Предлагаемая аспектная операция | Предлагаемый позиционный режим | Вопрос проверки | Конкурирующие объяснения |
|---:|---|---|---|---|---|
{process_rows}

<!-- section:reading -->
## Как читать

Читайте каждую строку как аспектная операция × позиционный режим. Используйте страницу как повод для сравнения, а не ярлык идентичности. До предпочтения всего стека аспектные и позиционные свидетельства собираются раздельно.

<!-- section:caveat -->
## Важно

Гипотеза не определяет способность, врождённость, нравственность, достоинство, духовную зрелость, профессию, безопасность или исход отношений. Позиции 1/2/7/8 не являются гарантированными сильными сторонами, а 3/4/5/6 — диагностированными дефицитами.

<!-- section:questions -->
## Вопросы для проверки

- Что отбирается, сохраняется после сжатия, выводится и обновляется после обратной связи?
- Повторяется ли предлагаемый позиционный режим в сопоставимых задачах?
- Какие данные отличают этот код от ближайших альтернатив и конкурирующих объяснений?

<!-- section:see-also -->
## См. также

- [[{local_slug('socionics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
- [[{local_slug('socionics-reality-modeling', lang)}]]
"""
    return f"""# {title}

{switcher}

<!-- section:definition -->
Сторінка фіксує **гіпотезу тактичного рівня Соціоніки** про позиціоновані операції побудови часткових виправних представлень одного спільного світу. Це не MBTI-тип, діагноз, профіль здібностей, повний портрет особистості або детермінований вердикт про стосунки.

<!-- section:code -->
## Коротка довідка

- Код: **{code}**
- Традиційно приписуваний псевдонім: **{alias}**
- Позначення Моделі A, використане в репозиторії: **{stack}**

<!-- section:process-map -->
## Процесна карта восьми позицій

| Позиція | Аспект | Запропонована аспектна операція | Запропонований позиційний режим | Питання перевірки | Конкурентні пояснення |
|---:|---|---|---|---|---|
{process_rows}

<!-- section:reading -->
## Як читати

Читайте кожен рядок як аспектна операція × позиційний режим. Використовуйте сторінку як привід для порівняння, а не ярлик ідентичності. До надання переваги всьому стеку аспектні та позиційні свідчення збирають окремо.

<!-- section:caveat -->
## Важливо

Гіпотеза не визначає здібність, уродженість, моральність, гідність, духовну зрілість, професію, безпеку або результат стосунків. Позиції 1/2/7/8 не є гарантованими сильними сторонами, а 3/4/5/6 — діагностованими дефіцитами.

<!-- section:questions -->
## Питання для перевірки

- Що відбирається, зберігається після стиснення, виводиться й оновлюється після зворотного зв'язку?
- Чи повторюється запропонований позиційний режим у порівнюваних завданнях?
- Які дані відрізняють цей код від найближчих альтернатив і конкурентних пояснень?

<!-- section:see-also -->
## Див. також

- [[{local_slug('socionics-overview', lang)}]]
- [[{local_slug('compatibility-level-boundaries', lang)}]]
- [[{local_slug('test-result-reading-guide', lang)}]]
- [[{local_slug('socionics-reality-modeling', lang)}]]
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
                if code not in SOCIONICS_STACKS:
                    raise ValueError(f"missing canonical Socionics stack for {code}")
                stack = SOCIONICS_STACKS[code]
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
                    f"wiki/concepts/{local_slug('socionics-reality-modeling', lang)}.md",
                    f"wiki/concepts/{local_slug('compatibility-level-boundaries', lang)}.md",
                    f"wiki/concepts/{local_slug('test-result-reading-guide', lang)}.md",
                ]
                frontmatter = update_socionics_frontmatter(frontmatter, sources)
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
