# PersonalPreparationMap Report Template

**Project:** Before We Build  
**Path:** Start Alone / personal preparation before serious relationship decisions  
**Status:** Draft report template for review  
**Created:** 2026-05-13  
**Inputs:** `wiki/concepts/report-caveat-standard.md`, `docs/start-alone-question-library-v0.md`, `docs/mvp-data-entities.md`, `docs/answer-normalization-rules.md`

## 1. Purpose

`PersonalPreparationMap` is the first generated report for a Christian brother or sister who begins alone before a serious relationship decision.

The report should help the user:

- remember what they already named honestly;
- notice hopes, fears, and expectations;
- see what is still unclear;
- choose topics for prayer, Scripture reflection, church community, and wise counsel;
- prepare future conversation questions;
- take one wise next step without haste.

It must not give a verdict, score, diagnosis, spouse promise, match recommendation, prophecy, readiness judgment, or pastoral decision.

## 2. Public-facing report name options

Use localized plain language in the product. The internal object may remain `PersonalPreparationMap`, but ordinary users should not see that name.

### Ukrainian options

1. `Карта підготовки до мудрої розмови`
2. `Карта особистої підготовки`
3. `Питання і теми перед серйозним кроком`

Recommended first option: `Карта підготовки до мудрої розмови`.

### Russian options

1. `Карта подготовки к мудрому разговору`
2. `Карта личной подготовки`
3. `Вопросы и темы перед серьёзным шагом`

Recommended first option: `Карта подготовки к мудрому разговору`.

**Reviewer note:** localized titles should be checked by a native speaker and theological/safety reviewer before publication.

## 3. Required caveat block

Place this near the beginning of every generated map, before any interpretive summary.

```text
This report is not a verdict, a pastoral authority, or a promise of marriage, family, agreement, calling, or any guaranteed outcome.

It is a conversation aid: a way to pause, name what is clear, notice what is still unclear, and prepare for honest discussion before God.

Please read it in the light of Scripture, prayer, your church community, wise counsel, and personal responsibility. If the report touches painful, serious, or spiritually weighty matters, bring those questions to trusted mature believers, a pastor, or another appropriate counselor rather than carrying them alone.

Before We Build does not decide for you. It helps you ask better questions so that the next step can be taken humbly, truthfully, and responsibly.
```

Compact localized meaning to preserve:

```text
This is not a verdict, pastoral authority, or promise. It is help for prayerful conversation: to see what is clear, name what is not yet clear, and bring the next step before God with Scripture, prayer, church, wise counsel, and personal responsibility.
```

## 4. Data inputs

The report composer should use only traceable MVP objects.

| Report input | Source object | Use in report |
|---|---|---|
| User's raw answers | `QuestionResponse` | Optional user quotes or answer review, under user control |
| Cautious summaries | `NormalizedAnswer` | Short plain-language summaries with attribution and uncertainty |
| Clear or unclear clusters | `ConversationTheme` | Section summaries |
| Suggested questions | `OpenQuestion` | Prayer, counsel, and future conversation questions |
| Sensitive cautions | `ReviewFlag` | Gentle human-help routing or suppressed ordinary sections |
| One next action | `WiseNextStep` | Final wise next step |
| Caveat | `ConversationMap.caveat_text` | Required boundary statement |

Implementation rule: do not compose a report directly from raw answers without normalized, attributed, uncertainty-labeled objects.

## 5. Report structure

### Section 0 — Title and short introduction

Purpose: explain what the map is in one warm paragraph.

Template:

```text
This map gathers what you have named while preparing before God for a serious relationship decision. It is meant to help you slow down, see what is clear, notice what still needs prayer or counsel, and prepare for honest conversation when the time is right.
```

Ukrainian direction:

```text
Ця карта збирає те, що ви назвали, готуючись перед Богом до серйозного кроку у стосунках. Вона допомагає зупинитися, побачити, що вже зрозуміло, помітити, що ще потребує молитви чи поради, і підготуватися до чесної розмови, коли настане час.
```

Russian direction:

```text
Эта карта собирает то, что вы назвали, готовясь перед Богом к серьёзному шагу в отношениях. Она помогает остановиться, увидеть, что уже ясно, заметить, что ещё нуждается в молитве или совете, и подготовиться к честному разговору, когда придёт время.
```

### Section 1 — Important caveat

Use the standard caveat block from section 3.

### Section 2 — What you already named clearly

Purpose: affirm clear user-stated material without judging readiness.

Allowed content:

- Scripture convictions the user named;
- responsibilities the user recognizes;
- hopes and fears stated honestly;
- counsel or church support the user already identified;
- practical topics already named: work, money, family, conflict, service, boundaries.

Template:

```text
From your answers, these areas appear clearer:

- You named: [user-stated or clearly summarized theme].
- You described: [self-description with attribution].
- Several answers point to: [clear summary].

Hold these as starting points for prayer, counsel, and future conversation, not as proof that every decision is settled.
```

Safe phrasing rules:

- Say `you named`, `you wrote`, `you described`, `several answers point to`.
- Do not say `you are ready`, `God is leading you to`, `this proves`, or `the right person will`.

### Section 3 — Hopes, fears, and expectations to examine

Purpose: make hopes visible without shaming loneliness or promising fulfillment.

Expected sources:

- question group B: motives, hopes, fears, loneliness;
- question group E: marriage expectations and daily life;
- question group I: children, family, future direction.

Template:

```text
These hopes and expectations may be worth examining carefully:

- Hope named: [hope], held before God without turning it into a demand.
- Fear named: [fear], which may need prayer, Scripture, and wise counsel.
- Expectation to clarify: [expectation], especially before making promises.

A good hope can still need patience. A real fear can still need truth and counsel. This map does not tell you whether marriage or family will happen; it helps you bring your hopes and fears into the light before God.
```

Localized wording direction:

- Ukrainian: `надія`, `страх`, `очікування`, `терпіння`, `мудра порада`.
- Russian: `надежда`, `страх`, `ожидание`, `терпение`, `мудрый совет`.

Avoid:

- `Your future spouse...`
- `This shows you are ready/not ready.`
- `You will build a family if...`
- shame-based wording about loneliness.

### Section 4 — What is still unclear

Purpose: name missing, thin, vague, or contradictory areas without accusation.

Expected sources:

- `ConversationTheme.theme_type = still_unclear`;
- `NormalizedAnswer.uncertainty_label = partly_clear` or `unclear_or_missing`;
- skipped or thin answers.

Template:

```text
These areas are not yet clear from your answers:

- [Topic] — this may need more reflection before serious promises.
- [Topic] — your answers mention it, but not enough to know what you mean in daily life.
- [Topic] — this may be a good question for prayer or counsel.

Unclear does not mean wrong. It means this topic should not be rushed past.
```

Good topics to surface:

- Scripture convictions and church life;
- family expectations and parental involvement;
- money, work, time, debt, giving, saving;
- conflict, forgiveness, apology, reconciliation;
- children, household life, service, and shared direction;
- boundaries, consent, privacy, and safety.

### Section 5 — Topics for prayer, Scripture, church, and wise counsel

Purpose: turn unclear or weighty areas toward prayer and human wisdom.

Template:

```text
These topics may be worth bringing before God with Scripture, prayer, and wise counsel:

1. [Topic] — because [short cautious reason tied to answers].
   Question for prayer or counsel: [OpenQuestion]

2. [Topic] — because [short cautious reason tied to answers].
   Question for prayer or counsel: [OpenQuestion]

3. [Topic] — because [short cautious reason tied to answers].
   Question for prayer or counsel: [OpenQuestion]
```

Safe question examples:

- `Which Scripture truths should shape this decision before emotion, pressure, or fear?`
- `Who could help you examine this wisely without gossip, pressure, or control?`
- `What would need to become clearer before you make serious promises?`
- `Where might you need patience, repentance, apology, or a change of direction with counsel?`
- `What should remain private until you freely choose to share it?`

**Reviewer/theological safety note:** questions involving repentance, husband/wife roles, church discipline, abuse, coercion, self-harm, or unsafe family context need review before public release.

### Section 6 — Future conversation questions

Purpose: prepare questions that may later be discussed with a future serious relationship prospect, mentor, pastor, or trusted believer. The report must not assume that such a person already exists.

Template:

```text
If the time comes for a serious and respectful conversation, these questions may help:

- What do we each believe must be built on Scripture rather than only emotion or pressure?
- How do we understand marriage, faithfulness, service, and responsibility before God?
- What expectations about daily life, church rhythm, money, work, family, children, and rest should be discussed early?
- How should hard topics be handled before they become silence, bitterness, or repeated conflict?
- Who could give wise counsel without gossip, pressure, or control?
```

Generated question rule:

- Prefer 3–7 questions.
- Use questions, not conclusions.
- Do not include private raw answer details unless the user chooses to export them.
- Do not phrase questions as accusations against the user or another person.

### Section 7 — Gentle cautions or safety note, if needed

Purpose: handle sensitive material without turning the report into ordinary advice.

Show this section only when `ReviewFlag` requires user-facing caution.

Ordinary caution template:

```text
One area may need careful human wisdom rather than quick decisions: [topic]. It may be better to discuss this with a trusted mature believer, pastor, or appropriate counselor before taking a serious step.
```

High-risk safety template:

```text
Some answers touch matters that should be handled with safe human help rather than an automated report. If there is coercion, abuse, fear for safety, self-harm, severe distress, or spiritual pressure, please seek help from trusted mature believers, a pastor, appropriate local support, or emergency help where needed. Do not carry this alone.
```

Forbidden:

- giving step-by-step advice for abuse, self-harm, coercion, or legal danger;
- validating spiritual manipulation claims;
- telling the user to confront, submit, disclose, reconcile, pursue, or break off without human wisdom and safety.

### Section 8 — One wise next step

Purpose: end with one concrete, humble step, not a life plan.

Allowed next-step categories:

- continue reflection;
- pray and read Scripture around one named topic;
- seek wise counsel from a trusted mature believer;
- speak with a pastor or church leader;
- prepare one future conversation question;
- pause before promises;
- repair, apology, repentance, or changed responsibility with counsel;
- seek safe human help;
- review privacy and consent before sharing.

Template:

```text
A wise next step may be:

[one concise next step]

Why this step: [short explanation tied to clear or unclear themes, using cautious language].

Take this step humbly and without haste. This map does not decide for you; it helps you bring the next step before God with Scripture, prayer, church, wise counsel, and personal responsibility.
```

Examples:

```text
A wise next step may be to choose one unclear topic and speak about it with a trusted mature believer before making serious promises.
```

```text
A wise next step may be to write one future conversation question about daily life, money, church rhythm, or family expectations, and keep it for the right time.
```

```text
A wise next step may be to pause before pursuing a relationship while you bring loneliness, fear, or pressure into prayer and wise counsel.
```

### Section 9 — Footer reminder

Use when the map includes strong cautions, sensitive topics, or important next steps.

```text
Treat this map as an invitation to prayerful conversation and wise counsel, not as a decision made for you.
```

## 6. Example report skeleton

```text
# [Localized report title]

This map gathers what you have named while preparing before God for a serious relationship decision...

## Important caveat
[standard caveat block]

## What you already named clearly
- You named...
- You described...
- Several answers point to...

## Hopes, fears, and expectations to examine
- Hope named...
- Fear named...
- Expectation to clarify...

## What is still unclear
- [Topic] is not yet clear from your answers...
- [Topic] may need more reflection...

## Topics for prayer, Scripture, church, and wise counsel
1. [Topic]
   Question: [OpenQuestion]
2. [Topic]
   Question: [OpenQuestion]

## Future conversation questions
- [Question]
- [Question]
- [Question]

## Gentle caution, if needed
[Only if ReviewFlag permits or requires user-facing caution]

## One wise next step
A wise next step may be...

## Footer reminder
Treat this map as an invitation to prayerful conversation and wise counsel, not as a decision made for you.
```

## 7. JSON-like composer contract

This is not a database schema; it is a report-composer contract for card 13 implementation.

```json
{
  "report_type": "PersonalPreparationMap",
  "public_title": "localized string",
  "locale": "uk | ru | en",
  "intro": "localized string",
  "caveat_text": "required localized caveat",
  "already_clear": [
    {
      "text": "plain-language summary",
      "source_kind": "user_stated_fact | user_self_description | clear_from_answers",
      "source_ids": ["norm_..."],
      "uncertainty_label": "user_stated_fact | user_self_description | clear_from_answers"
    }
  ],
  "hopes_fears_expectations": [
    {
      "text": "plain-language summary",
      "source_ids": ["norm_..."],
      "uncertainty_label": "user_self_description | clear_from_answers | partly_clear"
    }
  ],
  "still_unclear": [
    {
      "topic": "plain-language topic",
      "why_it_matters": "cautious explanation",
      "source_ids": ["norm_..."],
      "uncertainty_label": "partly_clear | unclear_or_missing"
    }
  ],
  "prayer_and_counsel_topics": [
    {
      "topic": "plain-language topic",
      "question": "suggested question",
      "source_ids": ["openq_..."],
      "uncertainty_label": "suggested_question | possible_concern"
    }
  ],
  "future_conversation_questions": [
    {
      "question": "plain-language question",
      "source_ids": ["openq_..."],
      "privacy_note": "optional; avoid raw private details by default"
    }
  ],
  "visible_review_flags": [
    {
      "message": "gentle caution or safe-human-help message",
      "source_ids": ["flag_..."],
      "uncertainty_label": "possible_concern | needs_human_review"
    }
  ],
  "wise_next_step": {
    "category": "continue_reflection | pray_and_read_scripture | seek_wise_counsel | prepare_future_conversation | pause_before_pursuing | repair_or_repentance | seek_safety_support | privacy_and_consent_review",
    "text": "one concise next step",
    "rationale": "short cautious explanation",
    "uncertainty_label": "wise_next_step"
  },
  "footer_reminder": "optional localized footer reminder",
  "suppressed_sections": ["section names suppressed because of safety flags"],
  "generated_at": "timestamp",
  "stale": false
}
```

## 8. Plain-language wording bank

### Prefer

- `what you named`
- `what is still unclear`
- `a topic for prayer and counsel`
- `a question for future conversation`
- `a wise next step may be`
- `before God`
- `with Scripture, prayer, church, wise counsel, and personal responsibility`
- `without haste`
- `not as a decision made for you`

### Avoid

- `score`
- `verdict`
- `match`
- `ideal spouse`
- `readiness level`
- `compatibility percentage`
- `diagnosis`
- `profile`
- `type`
- `the system knows`
- `God wants you to...`
- `you must...`
- `this proves...`

### Ukrainian-ready public terms

- `що вже зрозуміло`
- `що ще не ясно`
- `тема для молитви й поради`
- `питання для майбутньої розмови`
- `наступний мудрий крок може бути...`
- `перед Богом`
- `зі Святим Письмом, молитвою, церквою, мудрою порадою та особистою відповідальністю`
- `без поспіху`

### Russian-ready public terms

- `что уже ясно`
- `что ещё не ясно`
- `тема для молитвы и совета`
- `вопрос для будущего разговора`
- `следующий мудрый шаг может быть...`
- `перед Богом`
- `с Писанием, молитвой, церковью, мудрым советом и личной ответственностью`
- `без спешки`

## 9. Review checklist

Before this template is implemented or localized publicly, verify:

- [x] includes hopes and expectations;
- [x] includes unclear areas;
- [x] includes topics for prayer, Scripture, church, and wise counsel;
- [x] includes future conversation questions;
- [x] includes one wise next step;
- [x] includes the report caveat standard;
- [x] avoids verdict, score, promise, spouse guarantee, readiness judgment, and hidden match language;
- [x] uses plain-language wording ready for Ukrainian/Russian localization;
- [x] separates user-stated material from system-suggested questions and next steps;
- [x] routes sensitive or unsafe material toward human help instead of ordinary automated advice.

## 10. Reviewer/theological safety flags

These parts need reviewer/theological safety review before publication:

1. any localized caveat wording;
2. repentance, apology, and change-of-direction language;
3. husband/wife role and shared-decision wording;
4. children/family expectation wording, to avoid promising children or shaming childlessness;
5. counsel language where family or church contexts may be unsafe, controlling, or non-Christian;
6. safety, consent, abuse, coercion, severe distress, and self-harm routing;
7. any implementation that chooses a next step from sensitive user answers.
