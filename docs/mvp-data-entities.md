# MVP Data Entities Spec

**Project:** Before We Build  
**Scope:** Start Alone / weak-AI Christian conversation-map MVP  
**Status:** Internal implementation spec v0  
**Created:** 2026-05-13  
**Source plan:** `docs/hermes-kanban-action-plan.md`, `docs/start-alone-audience-path-spec.md`

## 1. Purpose

This spec defines the minimal data entities needed for the first Before We Build MVP: a Scripture-first, non-oracular conversation-map flow that helps a user answer good questions, see clear differences or themes, name honest uncertainty, and choose one wise next step.

The entity model must keep the MVP humble:

- raw user answers are preserved separately from any normalized summaries;
- every system summary or inference carries an uncertainty label;
- reports remain maps for conversation and discernment, not verdicts;
- the flow avoids hidden matchmaking, compatibility scoring, automated shortlists, digital twins, or spiritual guidance automation.

## 2. Explicit exclusions

The following entities are intentionally deferred and must not be implemented in the MVP data model:

| Deferred entity | MVP decision | Reason |
|---|---|---|
| `DigitalTwin` | Excluded | The MVP must not simulate a person, future spouse, relationship, church, or conversation partner. |
| `CompatibilityScore` | Excluded | The MVP must not compute or display a percentage, rank, verdict, or match quality. |
| `AutomatedShortlist` | Excluded | The MVP must not browse, rank, recommend, or automatically select people for introduction. |

If future research needs these concepts, they belong in a later research track with separate theological, ethical, privacy, and validation review. They are not Start Alone MVP objects.

## 3. MVP flow and where each entity appears

```text
1. User opens or resumes a session
   → UserSession

2. User chooses a situation/path
   → AudiencePath

3. System loads the relevant questions
   → QuestionSet

4. User answers questions
   → QuestionResponse (raw, user-controlled)

5. System summarizes answers cautiously
   → NormalizedAnswer (derived, labeled uncertainty)

6. System groups normalized material into themes
   → ConversationTheme

7. System produces open questions for prayer, counsel, or future conversation
   → OpenQuestion

8. System composes the report/map
   → ConversationMap

9. System marks sensitive or unclear material needing careful handling
   → ReviewFlag

10. System chooses one safe next-step category
    → WiseNextStep

11. User may leave optional feedback
    → FeedbackNote
```

## 4. Shared conventions

### 4.1 Entity identifiers

Use stable IDs internally. Public copy should not expose database-like names.

Recommended ID format:

- `session_<id>` for `UserSession`;
- `path_<slug>` for `AudiencePath`;
- `qset_<slug>_<version>` for `QuestionSet`;
- `response_<id>` for `QuestionResponse`;
- `norm_<id>` for `NormalizedAnswer`;
- `theme_<id>` for `ConversationTheme`;
- `openq_<id>` for `OpenQuestion`;
- `map_<id>` for `ConversationMap`;
- `flag_<id>` for `ReviewFlag`;
- `step_<id>` for `WiseNextStep`;
- `feedback_<id>` for `FeedbackNote`.

### 4.2 Uncertainty labels

Every normalized answer, theme, open question, review flag, and wise next step must carry an uncertainty label. Do not use a single hidden confidence score.

Allowed labels:

| Label | Meaning | Example use |
|---|---|---|
| `user_stated_fact` | The user explicitly said this. | “I attend a Baptist church.” |
| `user_self_description` | The user described themself this way. | “I often rush decisions when lonely.” |
| `clear_from_answers` | The summary follows directly from multiple clear answers. | Several answers name fear of haste. |
| `partly_clear` | Some answers point in this direction, but not enough for certainty. | Money expectations are mentioned but thinly. |
| `unclear_or_missing` | The topic was skipped, vague, or contradictory. | No clear answer about church counsel. |
| `possible_concern` | A cautious, non-diagnostic concern that needs human wisdom. | Answers suggest pressure, coercion, unsafe haste, or isolation. |
| `needs_human_review` | The system should avoid generating a strong summary and should point toward safe human help. | Safety, abuse, coercion, self-harm, or severe distress language. |
| `suggested_question` | A question proposed for reflection or future conversation, not a claim. | “Who could help you examine this wisely?” |
| `wise_next_step` | A safe next action category, not a command or prophecy. | “Talk with a trusted believer before moving forward.” |

Implementation rule: if a generated object combines user words and system interpretation, it must identify which part is user-stated and which part is derived.

### 4.3 Raw vs normalized separation

Raw answers and normalized summaries must never be collapsed into one entity.

- `QuestionResponse` stores what the user wrote or selected.
- `NormalizedAnswer` stores a cautious summary derived from one or more responses.
- `ConversationTheme`, `OpenQuestion`, `ConversationMap`, `ReviewFlag`, and `WiseNextStep` must reference the normalized answers or raw responses they depend on.
- If the user edits a raw response, the related normalized answers and report objects must be regenerated or marked stale.

### 4.4 Spiritual and pastoral boundary labels

No entity may claim:

- God told the user what to do;
- the user is spiritually ready or unready for marriage;
- a relationship is approved or forbidden;
- a person is a good or bad match;
- a pastor, church, mentor, parent, or future partner has received the data unless explicit sharing exists.

Allowed output posture:

```text
This is a map for prayer, Scripture reflection, wise counsel, and honest conversation.
```

## 5. Entity definitions

## 5.1 UserSession

### Purpose

Represents one user’s private interaction with the MVP flow. It is not a permanent identity profile and not a dating profile.

### Appears in MVP flow

- Created when the user starts or resumes the Start Alone path.
- Links the selected audience path, answers, normalized summaries, generated map, flags, next step, and optional feedback.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable internal ID. |
| `created_at` | yes | Timestamp. |
| `updated_at` | yes | Timestamp. |
| `locale` | yes | Example: `uk`, `ru`, `en`. Public copy should be fully localized. |
| `selected_path_id` | yes | References `AudiencePath`. |
| `status` | yes | `started`, `in_progress`, `ready_for_review`, `map_generated`, `completed`, `abandoned`. |
| `consent_version` | yes | Version of privacy / data-use notice accepted for the session. |
| `share_state` | yes | `private`, `exported_by_user`, `shared_by_user`; default `private`. |
| `stale_after_edit` | no | True if raw answers changed after normalized objects were generated. |

### Must not contain

- spouse candidate data;
- church browsing permissions;
- compatibility scores;
- inferred permanent personality labels;
- simulated future behavior.

## 5.2 AudiencePath

### Purpose

Defines the situation-specific route the user chooses. It translates the shared Before We Build formula into a concrete path without exposing internal model terms.

### Appears in MVP flow

- Chosen before the question flow.
- Determines which `QuestionSet` is loaded and how the `ConversationMap` is worded.

### MVP instance

The first MVP path is:

```text
Start Alone — a Christian single preparing before God for serious relationship decisions.
```

Public Ukrainian label from the parent spec:

```text
Почати самому
```

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Example: `path_start_alone`. |
| `slug` | yes | Stable path slug. |
| `status` | yes | `active`, `draft`, `retired`. |
| `public_label` | yes | Localized visible label. |
| `short_description` | yes | Localized description. |
| `audience_promise` | yes | Plain-language promise for the path. |
| `allowed_question_set_ids` | yes | References approved `QuestionSet` versions. |
| `report_name` | yes | For Start Alone, public report is a preparation/conversation map; internal report can be `PersonalPreparationMap` as an instance of `ConversationMap`. |
| `boundaries` | yes | What this path does not do. |

### Boundaries

For Start Alone, `AudiencePath.boundaries` must include:

- no browsing people;
- no pair comparison;
- no matching;
- no promise of marriage;
- no pastoral replacement;
- no automatic disclosure to church, mentor, family, or future partner.

## 5.3 QuestionSet

### Purpose

A versioned set of grouped questions for one audience path. It defines what is asked before any AI-assisted summary exists.

### Appears in MVP flow

- Loaded after `AudiencePath` selection.
- Provides the prompts that generate `QuestionResponse` records.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Example: `qset_start_alone_v0`. |
| `audience_path_id` | yes | References `AudiencePath`. |
| `version` | yes | Version string or number. |
| `status` | yes | `draft`, `reviewed`, `active`, `retired`. |
| `language` | yes | Question language. |
| `theme_groups` | yes | Ordered groups such as faith, motives, church counsel, conflict, money, family, boundaries, unclear topics. |
| `questions` | yes | Ordered question definitions. |
| `review_notes` | no | Notes from spiritual/language safety review. |

### Question definition fields

| Field | Required | Notes |
|---|---:|---|
| `question_id` | yes | Stable ID inside the set. |
| `theme_group_id` | yes | The group this question belongs to. |
| `prompt` | yes | Public-facing localized text. |
| `answer_type` | yes | `free_text`, `single_choice`, `multi_choice`, `scale`, `optional_note`. Prefer free text and simple choices for MVP. |
| `required` | yes | Boolean. Sensitive topics should usually allow skip. |
| `sensitivity` | yes | `ordinary`, `personal`, `sensitive`, `safety_related`. |
| `normalization_hint` | no | Internal hint for allowed summary categories; not public typology language. |

### Boundary

A `QuestionSet` must not contain questions that ask for a type, profile, match score, ideal partner formula, or hidden compatibility pattern.

## 5.4 QuestionResponse

### Purpose

Stores the raw answer exactly as the user provided it. This is the authoritative user text/source and must remain separate from summaries.

### Appears in MVP flow

- Created as the user answers each question.
- Read when generating `NormalizedAnswer` objects.
- Used for user review/edit before map generation.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable response ID. |
| `session_id` | yes | References `UserSession`. |
| `question_set_id` | yes | References `QuestionSet`. |
| `question_id` | yes | References question inside the set. |
| `raw_value` | yes | Exact typed answer or selected option IDs. |
| `raw_text_snapshot` | no | Human-readable snapshot for selected options. |
| `answered_at` | yes | Timestamp. |
| `edited_at` | no | Timestamp if changed. |
| `skipped` | yes | Boolean. |
| `user_visibility` | yes | `private`, `included_in_export`, `excluded_from_export`. |

### Must preserve

- the user’s wording;
- skipped answers;
- edits and stale-derived state;
- distinction between free text and selected options.

## 5.5 NormalizedAnswer

### Purpose

A cautious, derived summary of one or more raw responses. It supports grouping, open questions, and report composition without overwriting the user’s words.

### Appears in MVP flow

- Generated after raw responses exist.
- Feeds `ConversationTheme`, `OpenQuestion`, `ReviewFlag`, `WiseNextStep`, and `ConversationMap`.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable normalized-answer ID. |
| `session_id` | yes | References `UserSession`. |
| `source_response_ids` | yes | One or more `QuestionResponse` IDs. |
| `summary` | yes | Plain-language summary. |
| `category` | yes | Example: `hope`, `fear`, `conviction`, `boundary`, `responsibility`, `counsel_need`, `unclear_topic`, `possible_concern`. |
| `uncertainty_label` | yes | From the allowed label set. |
| `derivation_note` | yes | Short internal note: why this summary exists. |
| `user_quote_refs` | no | References to exact raw-response excerpts if supported. |
| `created_at` | yes | Timestamp. |
| `stale` | yes | True if source response changed after generation. |

### Required behavior

- A normalized answer may summarize; it may not silently reinterpret motives as facts.
- If the system says “possibly,” “may,” or “seems,” the uncertainty label must reflect that caution.
- Sensitive interpretations must use `possible_concern` or `needs_human_review`, not diagnostic language.

## 5.6 ConversationTheme

### Purpose

Groups normalized answers into user-facing report themes: clear areas, unclear areas, topics not to avoid, and future conversation areas.

### Appears in MVP flow

- Created after normalization.
- Forms the major sections of `ConversationMap`.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable theme ID. |
| `session_id` | yes | References `UserSession`. |
| `title` | yes | Localized plain-language title. |
| `theme_type` | yes | `already_clear`, `still_unclear`, `topic_not_to_avoid`, `prayer_and_counsel`, `future_conversation`, `safety_or_boundary`. |
| `normalized_answer_ids` | yes | References supporting `NormalizedAnswer` objects. |
| `uncertainty_label` | yes | Highest caution level needed for the theme. |
| `user_facing_summary` | yes | Plain-language report text. |
| `sort_order` | yes | Display order in map. |

### Boundary

A theme may say “this topic needs discussion.” It must not say “this relationship will fail,” “you are compatible,” or “God wants this next step.”

## 5.7 OpenQuestion

### Purpose

A question generated or selected for prayer, self-examination, wise counsel, or future conversation with another person.

### Appears in MVP flow

- Generated from normalized answers and missing topics.
- Displayed inside `ConversationMap`.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable question ID. |
| `session_id` | yes | References `UserSession`. |
| `source_normalized_answer_ids` | no | Optional references. Required if generated from specific answers. |
| `theme_id` | no | Optional parent `ConversationTheme`. |
| `question_text` | yes | Localized plain-language question. |
| `question_type` | yes | `self_reflection`, `prayer`, `scripture_reflection`, `wise_counsel`, `future_conversation`, `safety_support`. |
| `uncertainty_label` | yes | Usually `suggested_question`, `unclear_or_missing`, or `possible_concern`. |
| `priority` | yes | `low`, `medium`, `high`. High must not mean emergency unless paired with a safety flag. |
| `display_context` | yes | Where it appears in the report. |

### Good examples

- “Where might loneliness be pushing you faster than wisdom?”
- “Who in your church could help you examine this without pressure?”
- “What topic would be hard, but necessary, to discuss before serious promises?”

### Bad examples

- “Is this person your God-given spouse?”
- “What score would prove readiness?”
- “Which type should you marry?”

## 5.8 ConversationMap

### Purpose

The generated report object. For the Start Alone path, this is the internal container for the public-facing “Карта підготовки до мудрої розмови” and may be implemented under the product name `PersonalPreparationMap` while remaining structurally a `ConversationMap`.

### Appears in MVP flow

- Generated after answers are reviewed and normalized.
- Shows the user clear areas, unclear areas, themes, open questions, review flags where appropriate, caveat text, and one wise next step.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable map ID. |
| `session_id` | yes | References `UserSession`. |
| `audience_path_id` | yes | References `AudiencePath`. |
| `question_set_id` | yes | References the source question set version. |
| `title` | yes | Localized report title. |
| `summary_intro` | yes | Plain-language introduction. |
| `theme_ids` | yes | Ordered `ConversationTheme` IDs. |
| `open_question_ids` | yes | Ordered `OpenQuestion` IDs. |
| `review_flag_ids` | no | Flags that should be visible or internally logged. |
| `wise_next_step_id` | yes | References one `WiseNextStep`. |
| `caveat_text` | yes | Must include not verdict / not promise / not replacement language. |
| `overall_uncertainty_label` | yes | Highest caution level used in the map. |
| `generated_at` | yes | Timestamp. |
| `stale` | yes | True if source data changed. |

### Required sections for Start Alone

1. What the user already named clearly.
2. What is still unclear.
3. Topics not to avoid.
4. Questions for a future conversation.
5. Questions for prayer and wise counsel.
6. One wise next step.
7. Caveat: not a verdict, prophecy, promise of marriage, or replacement for Scripture, prayer, church, counsel, or obedience.

## 5.9 ReviewFlag

### Purpose

Marks material that should be handled cautiously: missing clarity, spiritual overclaim risk, sensitive topics, safety concerns, or user text that should route toward human support rather than automated summarization.

### Appears in MVP flow

- Generated during normalization or map composition.
- May affect which caveat is shown, whether report language is softened, and what next step categories are allowed.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable flag ID. |
| `session_id` | yes | References `UserSession`. |
| `source_response_ids` | no | Raw responses that triggered the flag, if any. |
| `source_normalized_answer_ids` | no | Normalized answers that triggered the flag, if any. |
| `flag_type` | yes | `missing_answer`, `contradiction`, `possible_pressure`, `safety_related`, `spiritual_overclaim_risk`, `sensitive_topic`, `needs_human_review`. |
| `severity` | yes | `info`, `caution`, `high_caution`, `urgent`. Use `urgent` only for safety-related routing. |
| `uncertainty_label` | yes | `unclear_or_missing`, `possible_concern`, or `needs_human_review`. |
| `internal_note` | yes | Short reason. |
| `user_facing_message` | no | If shown to user, must be non-accusing and practical. |
| `allowed_next_step_categories` | no | Restricts `WiseNextStep` options where needed. |

### Boundary

A `ReviewFlag` is not a diagnosis, sin judgment, or readiness verdict. It is a caution marker for safer wording and human wisdom.

## 5.10 WiseNextStep

### Purpose

A single safe next action proposed at the end of the map. It is a category and suggestion, not a command, prophecy, or automated spiritual direction.

### Appears in MVP flow

- Selected after themes, open questions, and flags are known.
- Displayed prominently in `ConversationMap`.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable next-step ID. |
| `session_id` | yes | References `UserSession`. |
| `source_theme_ids` | yes | Supporting themes. |
| `source_flag_ids` | no | Supporting review flags, if any. |
| `category` | yes | See allowed categories below. |
| `text` | yes | Localized user-facing step. |
| `rationale` | yes | Short explanation tied to user answers and uncertainty. |
| `uncertainty_label` | yes | Always `wise_next_step`; may also include `possible_concern` context in implementation. |
| `strength` | yes | `gentle`, `recommended`, `important`, `safety_related`. |

### Allowed categories

- `continue_reflection` — answer or revisit unclear questions;
- `pray_and_read_scripture` — bring a named topic before God with Scripture;
- `seek_wise_counsel` — talk with a trusted believer, mentor, pastor, parent, or mature Christian;
- `prepare_future_conversation` — save questions for a future serious conversation;
- `pause_before_pursuing` — slow down before making promises or pursuing contact;
- `repair_or_repentance` — consider a concrete responsibility, confession, apology, or change of direction with counsel;
- `seek_safety_support` — if safety, coercion, abuse, self-harm, or severe distress is suggested, point to safe human help and appropriate local support.

### Selection rule

The MVP should choose one primary next step. It may show supporting questions, but it should not give a multi-step spiritual program or attempt to manage the user’s life.

## 5.11 FeedbackNote

### Purpose

Optional user feedback about the usefulness, clarity, safety, or tone of the flow/report. It is not part of the discernment logic.

### Appears in MVP flow

- Collected after map generation or export.
- Used for product improvement and review, not for hidden matching.

### Minimal fields

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable feedback ID. |
| `session_id` | yes | References `UserSession`, or anonymized session reference if supported. |
| `feedback_type` | yes | `clarity`, `spiritual_safety`, `usefulness`, `missing_topic`, `language`, `bug`, `other`. |
| `rating` | no | Optional simple rating; avoid turning spiritual discernment into a score. |
| `comment` | no | User-provided feedback text. |
| `created_at` | yes | Timestamp. |
| `permission_to_use_anonymized` | yes | Boolean. |

### Boundary

Feedback must not feed a hidden compatibility engine, shortlist, or matching system in the MVP.

## 6. Minimal relationship model

```text
UserSession
├─ selected AudiencePath
├─ QuestionResponses
│  └─ each references QuestionSet.question_id
├─ NormalizedAnswers
│  └─ each references one or more QuestionResponses
├─ ConversationThemes
│  └─ each references one or more NormalizedAnswers
├─ OpenQuestions
│  └─ each may reference NormalizedAnswers and/or ConversationThemes
├─ ReviewFlags
│  └─ each may reference QuestionResponses and/or NormalizedAnswers
├─ WiseNextStep
│  └─ references ConversationThemes and optional ReviewFlags
├─ ConversationMap
│  └─ references Themes, OpenQuestions, ReviewFlags, and WiseNextStep
└─ FeedbackNotes
```

## 7. MVP state transitions

```text
UserSession.started
→ UserSession.in_progress
→ UserSession.ready_for_review
→ generate NormalizedAnswer objects
→ generate ConversationTheme / OpenQuestion / ReviewFlag objects
→ choose WiseNextStep
→ generate ConversationMap
→ UserSession.map_generated
→ optional FeedbackNote
→ UserSession.completed
```

If any `QuestionResponse` is edited after normalization:

```text
QuestionResponse.edited_at set
→ related NormalizedAnswer.stale = true
→ related ConversationMap.stale = true
→ UserSession.stale_after_edit = true
→ regenerate derived objects before export/share
```

## 8. Implementation acceptance checklist

- [x] `QuestionResponse` stores raw user answers and remains separate from `NormalizedAnswer`.
- [x] `NormalizedAnswer` is derived, source-linked, and uncertainty-labeled.
- [x] `ConversationTheme`, `OpenQuestion`, `ReviewFlag`, `ConversationMap`, and `WiseNextStep` carry uncertainty or caution labels.
- [x] The spec names where every requested entity appears in the MVP flow.
- [x] The MVP excludes `DigitalTwin`, `CompatibilityScore`, and `AutomatedShortlist`.
- [x] The model supports the Start Alone path without requiring typology, psychology-first language, scores, or matchmaking.
- [x] The model preserves Scripture-first and church/counsel boundaries by limiting output to a conversation map and one safe next-step category.

## 9. Follow-up cards this spec should feed

1. Draft core question library v0 — questions must provide the raw inputs for `QuestionResponse`.
2. Design personal preparation report template — should instantiate `ConversationMap` for Start Alone.
3. Define answer normalization rules — should refine `NormalizedAnswer` categories, uncertainty labels, and stale-object behavior.
4. Inspect target app/repository for implementation path — should translate this entity model into concrete storage, API, and UI files.

Do not implement database tables, API schemas, or UI forms directly from this spec until the question library, report template, and normalization rules have been reviewed together.
