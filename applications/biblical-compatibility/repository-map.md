# Карта репозиторію Before We Build

Ця карта показує чинну інформаційну архітектуру репозиторію після мовної та змістової міграції. **Before We Build** має універсальне дослідницьке ядро для вивчення взаємодії будь-яких двох людей. **Christian Before We Build** є першим спеціалізованим застосуванням цього ядра, але не визначає його повністю і не перетворює типології на біблійну антропологію.

## Точки входу

- `README.md` — короткий мовний навігатор і межі проєкту.
- `index.md` — автоматично згенерований повний каталог wiki.
- `wiki/start-here-en.md`, `wiki/start-here-ru.md`, `wiki/start-here-uk.md` — рівноправні стартові сторінки для огляду, дослідницького маршруту, Christian application і типологічного довідника.

Кожна активна wiki-група має три рівноправні файли: `slug-en.md`, `slug-ru.md` і `slug-uk.md`. Несуфіксовані мовні wiki-сторінки не є частиною чинної архітектури.

## Універсальне дослідницьке ядро

Основне позиціювання і межі ядра описані в:

- `wiki/concepts/project-positioning-en.md`, `wiki/concepts/project-positioning-ru.md`, `wiki/concepts/project-positioning-uk.md`;
- `wiki/concepts/main-idea-en.md`, `wiki/concepts/main-idea-ru.md`, `wiki/concepts/main-idea-uk.md`;
- `wiki/concepts/typology-reconceptualization-en.md`, `wiki/concepts/typology-reconceptualization-ru.md`, `wiki/concepts/typology-reconceptualization-uk.md`;
- `wiki/concepts/latent-process-en.md`, `wiki/concepts/latent-process-ru.md`, `wiki/concepts/latent-process-uk.md`;
- `wiki/concepts/epistemic-status-and-inference-limits-en.md`, `wiki/concepts/epistemic-status-and-inference-limits-ru.md`, `wiki/concepts/epistemic-status-and-inference-limits-uk.md`.

Чинна архітектура має чотири рівні:

| Рівень | Що досліджується | Основна сторінка українською |
|---|---|---|
| Ціннісно-моральна основа | Цінності, моральні зобов’язання, спостережувана поведінка, згода, безпека, відповідальність, взаємність і відновлення після шкоди | `wiki/concepts/value-moral-compatibility-uk.md` |
| Стратегічний | Часова та екзистенційна організація напряму; Temporistics як евристична модель | `wiki/concepts/strategic-compatibility-uk.md` |
| Операційний | Організація спільної дії; Psychosophy як евристична модель | `wiki/concepts/operational-compatibility-uk.md` |
| Тактичний | Моделювання та обмін інформацією; Socionics як евристична модель | `wiki/concepts/tactical-compatibility-uk.md` |

Зведення рівнів і правила їх розмежування містять `wiki/concepts/four-level-compatibility-architecture-uk.md` і `wiki/concepts/compatibility-level-boundaries-uk.md`. Відповідні EN і RU сторінки мають ті самі slug, версію, структуру та ідентифікатори тверджень.

Контекст є наскрізною умовою, а безпека — обов’язковим обмеженням. Вони не додають нових рівнів. Типологічний тип тут означає модельну гіпотезу, а не сутність людини, моральний рейтинг або прогноз долі стосунків.

## Christian Before We Build

Межу спеціалізації задають:

- `wiki/concepts/christian-application-overview-en.md`;
- `wiki/concepts/christian-application-overview-ru.md`;
- `wiki/concepts/christian-application-overview-uk.md`.

Каталог `applications/biblical-compatibility/` розвиває Scripture-first герменевтичний, етичний і пастирський шар: реєстр тверджень, біблійні теми, огляди застосування типологій і застереження. Він може уточнювати нормативні джерела Christian application, але не переписує універсальні визначення ядра і не надає типологічним гіпотезам біблійного авторитету.

`Cognitive Matchmaker` залишається майбутнім прикладним дослідницьким треком, а не поточним ядром чи Christian MVP.

## Дослідницькі додатки

Окремий маршрут для дослідника починається з:

- `wiki/concepts/validation-program-en.md`, `wiki/concepts/validation-program-ru.md`, `wiki/concepts/validation-program-uk.md`;
- `wiki/concepts/compatibility-measurement-roadmap-en.md`, `wiki/concepts/compatibility-measurement-roadmap-ru.md`, `wiki/concepts/compatibility-measurement-roadmap-uk.md`;
- `wiki/concepts/compatibility-measurement-methods-en.md`, `wiki/concepts/compatibility-measurement-methods-ru.md`, `wiki/concepts/compatibility-measurement-methods-uk.md`;
- `wiki/concepts/evidence-workflow-and-walkthrough-en.md`, `wiki/concepts/evidence-workflow-and-walkthrough-ru.md`, `wiki/concepts/evidence-workflow-and-walkthrough-uk.md`.

Цей шар охоплює перевірюваність конструктів, психометрику, оцінку джерел, невизначеність, альтернативні пояснення та умови спростування. Дорожня карта вимірювання описує лише передумови майбутньої валідованої моделі. У репозиторії немає чинного BWB score, ваг, відсотків сумісності чи формули вердикту для пари.

## Довідники, сутності та відносини

- `wiki/glossary-core-en.md`, `wiki/glossary-core-ru.md`, `wiki/glossary-core-uk.md` — основні визначення і розмежування термінів.
- `wiki/glossary-extended-en.md`, `wiki/glossary-extended-ru.md`, `wiki/glossary-extended-uk.md` — розширений технічний довідник.
- `wiki/entities/` — типологічні коди й сутності з обов’язковими застереженнями щодо висновків.
- `wiki/relations/` — якісні гіпотези про можливі ресурси, напруження, альтернативні пояснення і те, що слід перевірити в реальній взаємодії.

## Джерела і межа `raw/`

`raw/` є незмінюваним архівом отриманих матеріалів. Наявність тексту в цьому каталозі не означає, що Before We Build погоджується з його формулами, відсотками, типологічними узагальненнями або іншими висновками. Цю межу паралельно пояснює `raw/README.md`.

Чинна оцінка використаного джерела розміщується у відповідній тріаді `wiki/sources/*-en.md`, `wiki/sources/*-ru.md`, `wiki/sources/*-uk.md`. Source-summary окремо фіксує:

- що стверджує автор;
- які дані наведено;
- які обмеження виявлено;
- що BWB приймає;
- що залишається спірним;
- що відхилено або збережено лише історично.

## Автоматизація і контроль якості

Основні перевірки:

- `scripts/validate_wiki.py` — frontmatter, мовні тріади, версії, структури, claims, caveats, sources і заборонена термінологія;
- `scripts/check_wikilinks.py` — шляхи, якорі, старі slug, мовна узгодженість, неоднозначні посилання й сироти;
- `scripts/audit_claim_language.py` — надмірні наукові, детерміністичні та кількісні формулювання;
- `scripts/add_wiki_section_ids.py` — однакові стабільні ідентифікатори розділів у мовних партнерах;
- `scripts/generate_wiki_index.py` — генерація і перевірка `index.md`;
- `scripts/generate_wiki_inventory.py` — підсумковий машинний звіт про міграцію;
- `scripts/lint-agents.py` — статична перевірка інструкцій агентів;
- `tests/test_wiki_quality.py` — регресійні сценарії на стандартному `unittest`.

`.github/workflows/wiki-quality.yml` запускає ці quality gates у CI. `wiki/slug-migrations.json` є однозначним маніфестом старих і нових шляхів; перенаправляючі заглушки не використовуються, історію зберігає Git.

## Як користуватися картою

Новому читачеві слід почати зі Start Here своєю мовою. Для практичного християнського застосування після огляду універсального ядра перейти до Christian application. Для перевірки доказовості перейти до validation program і source summaries. Архівні `raw/` матеріали слід читати лише як джерела, а не як чинну позицію проєкту.
