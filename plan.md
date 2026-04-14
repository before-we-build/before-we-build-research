Ниже дам план так, как это стоило бы строить в реальном продукте, а не как красивую идею в промпте.

Сразу главное: этот проект нельзя начинать с мысли “сделаем умную сваху на LLM и она сама все поймет”. Правильный путь другой: сначала строится строгий multi-agent pipeline, потом ограниченный MVP с человеком в контуре, потом проверка, предсказывает ли симуляция реальную совместимость, и только после этого — частичная автономия.

Я бы строил это как систему из 4 слоев:

1. orchestration layer — кто запускает пайплайн и следит за состоянием
2. cognition layer — агенты, которые интервьюируют, моделируют, симулируют, оценивают
3. evidence layer — где хранятся факты, гипотезы, транскрипты, риски и объяснения
4. action layer — что видит пользователь: shortlist, объяснение, вопросы на свидание, логистика

Ниже детальный план.

1. Цель проекта

Что именно должен делать продукт:

не показывать пользователю 300 анкет, а выдавать 1–5 сильных кандидатов в неделю с понятным объяснением, почему именно они;
оценивать не только интересы и био, а то, как пара потенциально ведет себя в напряженных и значимых сценариях;
давать не “магический verdict”, а гипотезу с evidence packet: что именно модель увидела, где риски, что проверить вживую;
снижать когнитивную нагрузку и усталость от свайпов.

Что продукт не должен делать:

не должен делать жесткие исключения только по типологиям;
не должен выдавать симуляцию за истину о человеке;
не должен сразу сам писать людям, договариваться и принимать решения без прозрачного согласия;
не должен строиться на непрозрачном scraping без consent.

2. Базовый принцип архитектуры

Нужен не один “суперагент”, а оркестр специализированных агентов с четкими контрактами.

Правильная схема такая:

User / Candidate Data
→ Intake Agents
→ Profiling Agents
→ Twin Builder
→ Scenario Planner
→ Simulation Agents
→ Observer / Judge Ensemble
→ Risk & Compliance Agent
→ Shortlist Composer
→ Human Review / Optional Concierge Actions
→ Feedback Loop / Retraining

Ключевая идея: каждый агент отвечает только за одну стадию. Никаких “один LLM все делает сам”.

3. Набор агентов

Я бы сделал 12 основных агентов.

3.1 Orchestrator Agent

Это главный workflow manager.

Что делает:
принимает новый onboarding, нового кандидата, weekly run, feedback event;
запускает правильные подагенты;
следит за статусами, retries, версионностью профиля;
останавливает pipeline, если confidence низкий или есть red flags.

Вход:
event type + entity id

Выход:
state transition + список задач для других агентов

По сути это control plane всей системы.

3.2 Onboarding Interview Agent

Это агент глубинного интервью с пользователем.

Задача:
не просто собрать анкету, а вытащить реальные relationship-relevant patterns:
ценности,
границы,
страхи,
типичные конфликты,
стиль коммуникации,
ожидания от брака/отношений,
отношение к деньгам, детям, карьере, переезду, вере, семье.

Он должен работать по адаптивному дереву интервью:
если видит важный сигнал — углубляется;
если ответ поверхностный — переформулирует;
если область критична — просит пример из прошлого.

Выход не текст “пользователь такой-то”, а структурированный объект:
UserEvidenceProfile v1

Пример полей:
identity_constraints
relationship_goals
non_negotiables
conflict_patterns
attachment_signals
decision_style
stress_response
faith_values
family_model
time_horizon
money_norms
relocation_attitude
child_preferences
communication_style
self_reported_typology
confidence_per_field

3.3 Evidence Normalizer Agent

Этот агент превращает сырые ответы в нормализованные факты и гипотезы.

Почему он нужен:
люди отвечают длинно, противоречиво, эмоционально;
LLM любит делать слишком уверенные выводы;
нужно отделять “факт”, “самоописание”, “гипотеза”, “непонятно”.

Он разбивает данные на 4 слоя:
observed facts
self-claims
model inferences
unknowns

Это критично для безопасности и explainability.

3.4 Typology Mapping Agent

Этот агент отдельно работает с темпористикой, психософией, соционикой.

Но очень важно: он не должен быть источником истины.
Он должен выдавать не тип как догму, а распределение гипотез.

Например:
socionics_hypotheses = [typeA: 0.41, typeB: 0.27, typeC: 0.13...]
psychosophy_hypotheses = [...]
temporistics_hypotheses = [...]

И рядом:
which statements support this
which statements contradict this
confidence
what should be validated in reality

Так эти типологии становятся feature generators, а не “оракулом”.

3.5 Candidate Intake Agent

Этот агент принимает кандидатов из любого источника:
анкета в приложении,
приглашенный пул,
ручной импорт,
партнерский matchmaking pool,
human curator input.

Он должен:
нормализовать профили;
проверять наличие consent;
удалять мусор;
отмечать missing fields;
создавать CandidateEvidenceProfile.

Для MVP я бы вообще не трогал массовые dating apps.
Лучше начать с закрытого consent-based пула, иначе утонете в этике, платформах и плохих данных.

3.6 Twin Builder Agent

Это один из главных агентов.

Его задача:
собрать из evidence-профиля управляемого digital twin.

Twin — это не просто prompt.
Это structured simulation policy.

Он строит:
core motives
decision heuristics
emotional triggers
style constraints
red lines
preferred repair strategies
uncertainty zones

То есть twin должен уметь отвечать не “красиво”, а консистентно.

На выходе:
UserTwinSpec
CandidateTwinSpec

Важно: twin spec должен быть machine-readable, а не только narrative text.

Например:
{
"conflict_style": {"mode": "withdraw_then_return", "confidence": 0.72},
"money_decision_style": {"mode": "conservative_budgeting", "confidence": 0.81},
"relocation_priority": {"mode": "relationship_over_career", "confidence": 0.49},
"strategic_values": [...]
}

3.7 Scenario Planner Agent

Этот агент выбирает, какие именно сценарии гонять для пары.

Не надо гонять 50 одинаковых диалогов.
Нужны sparse high-information scenarios.

Он должен подбирать сценарии по матрице:

stakes:
low / medium / high

domains:
money
career
faith
family
children
location
sexual boundaries
social life
caregiving
failure
illness
jealousy
time allocation
conflict recovery

axes:
ambiguity
time pressure
value clash
role asymmetry
external stress

На пару нужно не 3 случайных сценария, а сценарный пакет:
ScenarioPack v1

Например:

1. career relocation under time pressure
2. family budget after unexpected loss
3. conflict about weekly routine / church / relatives
4. response to partner burnout
5. long-term vision alignment

3.8 Simulation Director Agent

Этот агент запускает симуляции и следит, чтобы они были качественные.

Его работа:
делать multiple runs;
менять seeds;
пробовать role reversal;
усиливать стресс;
гонять counterfactual branches;
останавливать явно невалидные симуляции;
маркировать unstable outputs.

То есть одна симуляция = мусор.
Нужен ensemble.

Я бы делал минимум так:
на одну пару 5–10 сценариев
на каждый сценарий 3–5 прогонов
итого 15–50 transcripts на пару

Потому что один диалог LLM легко уедет в случайность.

3.9 Pair Simulation Agents

Технически это два агента:
User Twin Agent
Candidate Twin Agent

Они играют не “умного ассистента”, а конкретного человека внутри ограничений twin spec.

Правила:
не иметь доступа к итоговому score;
не знать желаемый outcome;
не подстраиваться специально ради совместимости;
следовать internal policy, а не pleasing mode.

Иначе все превратится в синтетическую вежливость.

3.10 Observer / Judge Ensemble Agent

Это самый важный аналитический слой.

Я бы не делал одного judge.
Нужен ensemble из 3–4 оценочных ролей:

1. Strategic Judge
   Смотрит на ценности, мотивы, жизненный вектор.

2. Operational Judge
   Смотрит на распределение ролей, совместное решение задач, complementarity.

3. Tactical Judge
   Смотрит на микродинамику общения:
   эскалация,
   repair attempts,
   слушание,
   перебивание,
   дефенсивность,
   withdrawal,
   co-regulation.

4. Skeptic / Red-Team Judge
   Пытается доказать, что match плохой, и ищет слабые места модели.

Это критично, потому что без red-team judge система будет галлюцинировать compatibility.

На выходе:
CompatibilityAssessment
RiskFlags
EvidenceMoments
ConfidenceScore
Contradictions

3.11 Explanation Composer Agent

Этот агент превращает технический вывод в человеческий.

Он делает:
match card,
plain-language explanation,
why this candidate,
why not others,
what to validate offline,
questions for first date,
what could go wrong.

Пример хорошего объяснения:
“В сценариях про деньги и стресс вы оба не уходили в contempt или silent withdrawal. У вас разный стиль принятия решений: один быстрее закрывает неопределенность, другой дольше исследует варианты. Но в 4 из 5 прогонов вы находили рабочий компромисс. Основной риск — разная срочность в теме переезда.”

Это и есть evidence packet.

3.12 Feedback & Learning Agent

После реального контакта или свидания он собирает реальность.

Что надо собирать:
был ли mutual interest;
было ли ощущение “модель промахнулась”;
совпали ли конфликтные паттерны;
появилось ли желание продолжить;
что оказалось критичным, но модель не заметила.

Без этого проекта не существует.
Иначе это просто красивая симуляция без ground truth.

4. Какие сущности и артефакты должны быть в системе

Нужна строгая data model.

Минимальный набор сущностей:

UserProfile
CandidateProfile
EvidenceClaim
TypologyHypothesis
TwinSpec
ScenarioTemplate
ScenarioPack
SimulationRun
Transcript
JudgeAssessment
RiskFlag
MatchCard
ShortlistDigest
FeedbackEvent
ModelVersion
ConsentRecord
AuditLog

Это важно потому, что без структурированных сущностей нельзя:
делать explainability,
пересчитывать score,
версионировать профили,
строить offline evaluation,
проводить A/B.

5. Как должен выглядеть end-to-end pipeline

Шаг 1. Onboarding пользователя
Пользователь проходит интервью.
Система собирает evidence, а не просто анкету.

Шаг 2. Normalization
Ответы очищаются, превращаются в факты, гипотезы, unknowns.

Шаг 3. Typology feature extraction
Типологии используются как дополнительный словарь признаков, а не как ядро истины.

Шаг 4. User twin build
Собирается версия цифрового двойника пользователя.

Шаг 5. Candidate intake
Кандидаты импортируются, проходят ту же нормализацию.

Шаг 6. Candidate twin build
Для каждого кандидата строится twin.

Шаг 7. Pair pre-filtering
Быстрый фильтр по hard constraints:
возрастной диапазон,
география,
статус отношений,
дети / брак / вера / non-negotiables,
consent,
критичные несовместимости.

Шаг 8. Scenario planning
Для каждой пары подбирается индивидуальный пакет высокоинформативных сценариев.

Шаг 9. Multi-run simulation
Пара прогоняется через много сценариев и повторов.

Шаг 10. Judge ensemble scoring
Судьи выдают layer-by-layer оценку и риски.

Шаг 11. Explanation synthesis
Собирается human-readable объяснение.

Шаг 12. Weekly ranking
Пользователь получает shortlist 1–5 кандидатов.

Шаг 13. Real-world validation
После общения / свидания собирается обратная связь.

Шаг 14. Recalibration
Модель, веса, сценарии, twin-building улучшаются на реальных outcome data.

6. Как считать score

Я бы не делал один score “87/100”.
Это слишком фальшиво.

Нужно минимум 5 чисел:

1. strategic alignment
2. operational complementarity
3. tactical interaction stability
4. risk severity
5. confidence / evidence sufficiency

Итоговая логика должна быть такой:

final_match_score =
0.40 strategic_alignment

* 0.30 operational_complementarity
* 0.20 tactical_stability
* 0.10 reciprocal_interest_prior

- risk_penalty

Но отдельно обязательно:
confidence_score
hard_stop_flags

Пример hard stop:
противоречие по детям,
несовместимость по вере,
критичное расхождение в брачных ожиданиях,
опасные признаки контроля / агрессии / манипуляции.

То есть высокая “химия” не должна перекрывать hard incompatibility.

7. Как сделать симуляции не игрушечными

Вот здесь чаще всего все ломается.

Чтобы симуляция не была красивой болтовней, нужны 7 правил:

1. Structured world state
   Сценарий должен иметь состояние мира:
   доход,
   срок,
   ограничения,
   родственники,
   здоровье,
   время,
   варианты решения.

2. Goal tension
   У каждого twin в сценарии должны быть реальные competing priorities.

3. Memory continuity
   Если в начале был конфликт, его последствия должны оставаться в следующих репликах.

4. Stress modulation
   Нужно уметь усиливать стресс и смотреть, как меняется динамика.

5. Multi-run variance tracking
   Если outcome слишком скачет, confidence должен падать.

6. Counterfactual probes
   Нужно прогонять “а что если условия хуже”, “а что если у одного меньше ресурсов”.

7. Anti-pleasing constraints
   Агенты не должны искусственно сглаживать конфликт ради красивого результата.

8. Какой MVP реально делать первым

Правильный MVP очень узкий.

Не надо сразу:
full autonomy,
calendar booking,
venue search,
outreach,
массовый пул,
автопереписка с кандидатами.

Первый MVP должен быть таким:

MVP-1
deep onboarding
candidate intake from curated consent-based pool
twin builder
5–7 сценариев
judge ensemble
manual human review
1–3 recommendations per week
feedback collection after date

Цель MVP:
не “заработать вау”, а проверить 3 вещи:

1. пользователю вообще полезно такое объяснение?

2. shortlist реально лучше случайного или обычного выбора?

3. simulation outputs хоть как-то коррелируют с реальностью?

4. План по фазам

Фаза 0. Research & problem framing
Срок: 2–4 недели

Что делаем:
фиксируем продуктовую гипотезу;
описываем outcomes;
определяем sensitive domains;
фиксируем legal boundaries;
делаем data contracts;
решаем, какие типологии optional, а какие вообще не используем в ядре.

Артефакты:
PRD
risk register
ontology of compatibility
scenario taxonomy
data schema draft
evaluation plan v1

Фаза 1. Human-in-the-loop concierge prototype
Срок: 4–8 недель

Что делаем:
онбординг-агент;
candidate intake;
ручной или semi-automatic twin building;
5 базовых сценариев;
judge ensemble;
ручная сборка shortlist.

Цель:
понять, какие объяснения полезны, и где модель несет чушь.

Фаза 2. Simulation platform MVP
Срок: 6–10 недель

Что делаем:
scenario compiler;
simulation runner;
logging of transcripts;
variance tracking;
confidence computation;
explanation composer.

Цель:
получить стабильный simulation pipeline.

Фаза 3. Evaluation loop
Срок: 8–12 недель

Что делаем:
сбор реального feedback;
post-date surveys;
сравнение predicted vs actual;
ablation tests:
без типологий,
только hard constraints,
с типологиями,
с симуляцией,
без симуляции.

Цель:
доказать, что хоть какой-то кусок системы реально дает signal.

Фаза 4. Partial automation
Срок: 6–8 недель

Что делаем:
оркестратор;
автоматический weekly digest;
лучшие сценарии по сегментам;
базовый risk gate;
versioned twin specs.

Фаза 5. Concierge action layer
Срок: 4–6 недель

Что делаем:
вопросы на первое свидание;
scheduling assist;
venue suggestions;
consent workflows.

Фаза 6. Scaling & personalization
Срок: дальше постоянно

Что делаем:
segment-specific models;
personalized scenario selection;
bandit-style scenario prioritization;
retrieval of similar past outcomes;
human coach escalation for edge cases.

10. Какой стек я бы выбрал

Не буду привязываться к хайпу, дам практичную схему.

Backend:
Python + FastAPI

Workflow orchestration:
Temporal или Prefect
Я бы скорее взял Temporal, если проект реально станет event-driven и stateful.

Database:
PostgreSQL
потому что нужна строгая relational model, auditability и versioning

Vector store:
pgvector на старте
не надо тащить отдельный векторный зоопарк слишком рано

Cache / queue:
Redis

LLM layer:
абстракция над несколькими моделями
нельзя завязывать весь продукт на одну модель

Observability:
OpenTelemetry
structured logs
trace per workflow
prompt/version tracing

Evaluation storage:
отдельные таблицы под runs, judges, outcomes, confidence drift

Policy / guardrails:
отдельный rule engine, не внутри промпта

Frontend:
в начале web dashboard для operator + user digest UI

11. Как должна выглядеть память агентов

Нельзя просто давать всем агентам всю историю.
Нужна многослойная память.

1. Raw memory
   сырые интервью, анкеты, заметки

2. Structured memory
   факты, признаки, гипотезы

3. Working memory
   то, что нужно агенту в конкретной задаче

4. Audit memory
   какая версия модели, какой prompt, какие входы, какой output

Очень важно:
агенты должны видеть только нужный минимум.
Иначе будет leakage, bias и ненужное hallucination coupling.

12. Какие проверки должны быть у каждого агента

У каждого output должны быть обязательные поля:

claim
evidence span
confidence
alternative interpretation
missing information
safe-to-use flag

Тогда система будет не просто “умничать”, а реально держать epistemic discipline.

13. Как валидировать научно, а не на ощущениях

Тут нужен почти research-grade подход.

13.1 Offline validation
Берете исторические кейсы или пилотные пары и смотрите:
предсказывает ли система:
первое свидание,
второе свидание,
mutual interest,
продолжение общения,
расхождение модели и реальности.

13.2 Online pilot
Маленькая группа пользователей.
Сравниваете:
обычный поиск
vs
concierge shortlist

13.3 Ablation
Проверяете вклад каждого слоя:
только анкета
анкета + hard filters
анкета + типологии
анкета + симуляции
анкета + симуляции + judge ensemble

13.4 Calibration
Если система ставит 0.8 compatibility, это реально чаще приводит к позитивному outcome, чем 0.4?
Если нет — score мусор.

13.5 Human qualitative review
Независимый reviewer читает transcript и говорит:
это правдоподобно или synthetic nonsense?

14. Главные риски проекта

14.1 LLM twins будут правдоподобны, но не предиктивны
Это риск номер один.

14.2 Типологии дадут красивый narrative, но слабый signal
Поэтому они должны быть optional features, а не foundation truth.

14.3 Судьи будут усиливать bias
Поэтому нужен skeptical judge и human review.

14.4 Пользователь начнет воспринимать систему как “читает души”
Нужно очень жестко формулировать output как hypothesis, not diagnosis.

14.5 Автоматические исключения будут юридически и этически опасны
Нужен human override и понятный consent.

14.6 Модель начнет советовать слишком “удобные”, а не лучшие пары
Потому что LLM любит социальную гладкость.
Нужны stress scenarios и red-team probing.

15. Privacy, ethics, compliance

Это не “потом добавим”. Это в ядре.

Нужно сразу:

явный informed consent;
понятный список, какие данные используются;
право удалить профиль;
retention policy;
не хранить лишнее;
audit log на automated decisions;
объяснение, как формируется shortlist;
запрет на hidden scraping без согласия;
запрет на чувствительные выводы без достаточных оснований;
human-in-the-loop для спорных кейсов.

Особенно важно:
если система кого-то исключает, должно быть ясно почему.
И причина должна звучать как product reason, а не “AI решил”.

16. Как я бы спроектировал weekly product output

Пользователь должен видеть не кашу, а компактный digest.

Для каждого кандидата:

1. Почему вы попали в shortlist
2. Где у вас сильная совместимость
3. Где у вас возможный риск
4. Что нужно проверить вживую
5. 3–5 вопросов на первое свидание
6. Общий confidence
7. Что система пока не знает

Пример структуры card:
match summary
top strengths
top risks
key simulation moments
validation questions
suggested date style
confidence level

17. Где нужен человек в контуре

На старте почти везде.

Human operator нужен:
после онбординга — проверить profile coherence;
после twin build — проверить, не уехала ли модель;
после scoring — проверить red flags и nonsense;
перед выдачей shortlist — финальный sanity check;
после feedback — размечать ошибки модели.

Только потом можно убирать человека из части шагов.

18. Какая команда нужна

Минимально:

1 product lead
1 research / behavioral design lead
1 LLM engineer
1 backend engineer
1 frontend engineer
1 data / evaluation engineer
1 privacy / policy advisor part-time
1 human concierge / operator на пилот

Если делать серьезно, еще нужен:
conversation designer
safety evaluator
qa for prompts and workflows

19. Что бы я сделал в первые 30 дней

Неделя 1
зафиксировать продуктовую гипотезу;
собрать ontology совместимости;
описать data model;
решить, какие данные вообще допустимы.

Неделя 2
собрать interview framework;
собрать 20–30 high-information questions;
описать 15–20 сценариев;
сделать формат evidence profile.

Неделя 3
сделать twin spec schema;
сделать judge rubric;
сделать transcript format;
сделать explanation format.

Неделя 4
поднять прототип pipeline:
onboarding
normalization
twin build
3 сценария
judge ensemble
manual digest

Цель первого месяца:
получить 5–10 тестовых кейсов end-to-end.

20. Что бы я точно не делал

Не строил бы сразу “универсальную любовь-машину”.
Не делал бы hard ranking только на типологиях.
Не делал бы fully autonomous messaging.
Не делал бы black-box final score без evidence.
Не лез бы сразу в большой dating marketplace.
Не верил бы первому красивому demo.

21. Самая правильная формула продукта

Если совсем сжать:

ядро проекта = не match by profile, а match by simulated joint behavior under constraint

но practically:

value only exists if
simulation → shortlist quality → real-world positive outcomes

Иначе это просто интересная интеллектуальная игрушка.

22. Рекомендуемая первая версия архитектуры

Самая здравая v1:

Orchestrator
→ Onboarding Interview Agent
→ Evidence Normalizer
→ Typology Mapping Agent
→ Twin Builder
→ Candidate Intake Agent
→ Scenario Planner
→ Simulation Director
→ Twin A / Twin B
→ Judge Ensemble
→ Explanation Composer
→ Human Reviewer
→ Weekly Digest
→ Feedback Agent

Это уже достаточно серьезно, чтобы проверить идею, и еще не настолько безумно, чтобы утонуть.

23. Мой честный вывод

Идея сильная, но реальная ценность проекта не в “типологиях + агентах”, а в трех вещах:

1. хорошая ontology совместимости
2. качественные high-stakes scenarios
3. жесткая валидация against real-world outcomes

Если это сделать слабо, получится псевдонаучный dating oracle.
Если сделать сильно, может получиться новый класс agentic matchmaking systems.

Дальше я могу сразу развернуть это в следующем виде:
или как техническую архитектуру с сервисами и API,
или как roadmap на 3–6 месяцев с задачами по спринтам,
или как полный список агентов с prompt contracts и JSON-схемами входов/выходов.
