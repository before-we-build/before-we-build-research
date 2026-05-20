# Answer Normalization Rules

**Project:** Before We Build  
**Scope:** Start Alone / weak-AI Christian conversation-map MVP  
**Status:** Internal implementation and review spec v0  
**Created:** 2026-05-13  
**Depends on:** `docs/mvp-data-entities.md`, `docs/start-alone-question-library-v0.md`, `wiki/concepts/report-caveat-standard.md`

## 1. Purpose

This spec defines how raw user answers may be turned into `NormalizedAnswer`, `ConversationTheme`, `OpenQuestion`, `ReviewFlag`, and `WiseNextStep` objects without turning the system into a verdict engine.

The normalization layer must protect five boundaries:

1. **Facts stay facts.** A user-stated fact must not be rewritten as a hidden motive, diagnosis, sin pattern, readiness verdict, or personality label.
2. **Self-descriptions stay attributed.** If a user describes themself, the output must preserve that it is the user's own description, not the system's conclusion.
3. **Uncertainty remains visible.** Every AI-created summary, concern, question, or next-step suggestion must carry a visible uncertainty label.
4. **Sensitive material triggers care.** Abuse, coercion, self-harm, severe distress, sexual pressure, unsafe family context, doctrinal conflict, and spiritual manipulation must be eligible for `ReviewFlag` instead of ordinary advice.
5. **The report remains a conversation map.** No normalized object may become a score, match verdict, spouse promise, spiritual verdict, diagnosis, prophecy, or substitute for Scripture, prayer, church, wise counsel, repentance, and responsibility.

## 2. Normalization pipeline

```text
QuestionResponse
  → extract user-stated fragments
  → classify each fragment by claim kind
  → create cautious NormalizedAnswer objects
  → group repeated or related objects into ConversationTheme objects
  → create OpenQuestion objects for unclear or important topics
  → create ReviewFlag objects for sensitive or unsafe material
  → choose one WiseNextStep category only after flags are considered
```

Implementation rule: do not generate downstream objects directly from raw answers without a traceable `NormalizedAnswer` or `ReviewFlag` reference.

## 3. Claim kinds

Each normalized fragment must use exactly one primary claim kind.

| Claim kind | Meaning | Allowed source | Required label | Example safe output | Forbidden rewrite |
|---|---|---|---|---|---|
| `fact` | A concrete statement the user gave as true. | Direct user words only. | `user_stated_fact` | “You wrote that you attend a Baptist church.” | “You are spiritually mature because you attend church.” |
| `self_description` | The user's own description of habit, emotion, desire, fear, weakness, conviction, or responsibility. | Direct user words, lightly summarized. | `user_self_description` | “You describe loneliness as sometimes pushing you toward haste.” | “Your motive is desperation.” |
| `clear_summary` | A concise summary directly supported by several answers. | Multiple raw answers with clear overlap. | `clear_from_answers` | “Several answers return to the need for wise counsel before promises.” | “You cannot decide without a pastor.” |
| `partial_summary` | A possible pattern supported by thin, mixed, or incomplete evidence. | One or more weak signals. | `partly_clear` | “There may be an unclear area around money expectations.” | “You have financial irresponsibility issues.” |
| `unclear_area` | A topic the user skipped, contradicted, or answered vaguely. | Missing, vague, or conflicting answers. | `unclear_or_missing` | “Your answers do not yet make family expectations clear.” | “You are avoiding your family issues.” |
| `possible_concern` | A cautious concern that deserves human wisdom but is not a diagnosis. | Concerning user language or repeated pressure signals. | `possible_concern` | “There may be pressure or haste that should be brought to a trusted believer.” | “This relationship would be unsafe.” |
| `human_review_needed` | Material too sensitive for ordinary generated advice. | Safety, abuse, coercion, self-harm, severe distress, or spiritual manipulation signals. | `needs_human_review` | “This answer should be handled with safe human help rather than an automated report.” | “Here is how to solve the abuse/conflict yourself.” |
| `proposed_question` | A question for prayer, counsel, or future conversation. | Derived from facts, uncertainty, or themes. | `suggested_question` | “Who could help you examine this wisely before moving forward?” | “Ask this because your hidden fear is control.” |
| `next_step` | A safe category of action, not a command. | Derived only after checking flags. | `wise_next_step` | “Consider speaking with a trusted mature believer before making promises.” | “God wants you to pause this relationship.” |

## 4. Required fields for normalized objects

Every `NormalizedAnswer` must store enough information for review.

Recommended fields:

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable internal ID. |
| `source_response_ids` | yes | One or more `QuestionResponse` IDs. |
| `source_quote_refs` | yes | Short references or offsets to the user's own words; avoid exposing private raw text unnecessarily in public UI. |
| `claim_kind` | yes | One value from section 3. |
| `uncertainty_label` | yes | Must match the claim kind unless a stricter label is needed. |
| `normalized_text` | yes | Cautious plain-language summary. |
| `attribution` | yes | `user_stated`, `user_self_described`, `system_summarized`, or `system_hypothesis`. |
| `sensitivity_tags` | no | Zero or more tags from section 8. |
| `review_flag_ids` | no | References related flags. |
| `public_visibility` | yes | `show`, `show_with_caveat`, `hide_from_report`, or `human_review_only`. |
| `stale_after_edit` | yes | True when any source response changes. |

Hard rule: if `attribution` is `system_summarized` or `system_hypothesis`, the visible output must include uncertainty language.

## 5. Attribution language rules

Use attribution words that clearly separate the user from the system.

| Situation | Safer phrasing | Avoid |
|---|---|---|
| User-stated fact | “You wrote that…” / “You said…” | “It is clear that God is leading you to…” |
| User self-description | “You describe yourself as…” / “You named…” | “You are the kind of person who…” |
| Clear summary | “Several answers point to…” | “The truth about you is…” |
| Partial summary | “This may be an area to examine…” | “Your real motive is…” |
| Missing information | “This topic is not yet clear from your answers…” | “You are hiding…” |
| Concern | “This could be worth bringing to wise counsel…” | “This proves danger/sin/immaturity…” |
| Sensitive flag | “This should be handled with safe human help…” | “The tool can guide you through this safely by itself…” |
| Next step | “A wise next step may be…” | “You must…” / “God wants…” |

## 6. Rewrite prohibitions

The normalization layer must never perform these rewrites:

1. `I feel lonely` → “The user is desperate.”
2. `I am afraid of choosing wrongly` → “The user lacks faith.”
3. `My parents pressure me` → “The user dishonors parents.”
4. `I struggle with conflict` → “The user is unsafe to marry.”
5. `I want children` → “The user will have a faithful family.”
6. `I am unsure about church counsel` → “The user rejects authority.”
7. `I have debt` → “The user is financially irresponsible.”
8. `I sinned / need repentance` → “The user is spiritually unready for marriage.”
9. `I like this person` → “This is a possible match.”
10. `We agree on many things` → “The relationship is compatible.”

If a stronger interpretation seems possible, record it only as a `partial_summary`, `possible_concern`, `OpenQuestion`, or `ReviewFlag` with cautious language and source references.

## 7. Uncertainty label escalation

Use the least dramatic label that protects truth and safety, then escalate when needed.

```text
user_stated_fact
  → user_self_description
  → clear_from_answers
  → partly_clear
  → unclear_or_missing
  → possible_concern
  → needs_human_review
```

Escalation rules:

- If a summary contains any AI interpretation beyond direct restatement, do not use `user_stated_fact`.
- If one answer hints at a theme but does not establish it, use `partly_clear`.
- If answers conflict, use `unclear_or_missing` unless one part raises a safety concern.
- If ordinary counsel may be insufficient or unsafe, use `possible_concern` or `needs_human_review`.
- If the output might lead a vulnerable person to act without human help, use `needs_human_review` and suppress ordinary report advice.

## 8. Sensitive tags and review flags

A `ReviewFlag` should be created when the answer touches a sensitive area that needs careful handling, limited wording, human review, or suppression from the ordinary report.

Recommended sensitivity tags:

| Tag | Trigger examples | Default handling |
|---|---|---|
| `abuse_or_coercion` | threats, control, forced disclosure, intimidation, violence, fear of another person | `needs_human_review`; do not generate ordinary relationship advice. |
| `self_harm_or_suicidality` | self-harm, suicidal thoughts, inability to stay safe | `needs_human_review`; point to immediate safe human help / local emergency support in implementation. |
| `severe_distress` | panic, despair, inability to function, intense fear | `needs_human_review` or `possible_concern`; avoid automated counsel. |
| `sexual_pressure_or_boundary_violation` | pressure, coercion, unwanted contact, purity boundaries being forced or ignored | `needs_human_review` when coercive; otherwise `possible_concern`. |
| `spiritual_manipulation` | “God told me you must…”, leader pressure, threats framed as spiritual authority | `needs_human_review`; do not validate the claim. |
| `unsafe_family_context` | family violence, control, forced marriage pressure, unsafe disclosure | `needs_human_review`; do not advise automatic family involvement. |
| `doctrinal_or_church_conflict` | disputed husband/wife role claims, church discipline, pastoral authority conflict | `possible_concern`; route to church/pastor review language. |
| `legal_or_financial_risk` | debt crisis, fraud, legal threats, immigration/document pressure | `possible_concern` or `needs_human_review`; avoid pretending to give legal/financial advice. |
| `medical_or_clinical` | diagnosis, medication, trauma treatment, addiction crisis | `needs_human_review` for acute risk; otherwise caveat and human help. |
| `minor_or_age_concern` | underage relationship, large age/power imbalance, safeguarding issue | `needs_human_review`; suppress ordinary romantic guidance. |
| `privacy_or_consent` | sharing another person's data, church/family disclosure without consent | `possible_concern`; remind that sharing must be user-controlled and consent-based. |

ReviewFlag minimal fields:

| Field | Required | Notes |
|---|---:|---|
| `id` | yes | Stable internal ID. |
| `source_response_ids` | yes | Source answers. |
| `sensitivity_tags` | yes | One or more tags. |
| `severity` | yes | `low`, `medium`, `high`, `critical`. |
| `uncertainty_label` | yes | Usually `possible_concern` or `needs_human_review`. |
| `safe_public_text` | yes | Cautious text shown to user, if any. |
| `suppress_report_sections` | yes | Boolean or list of sections to suppress. |
| `recommended_next_step_category` | yes | `trusted_believer`, `pastor_or_church_leader`, `qualified_counselor`, `emergency_or_local_help`, `pause_and_seek_help`, or `privacy_review`. |

## 9. Report visibility rules

Not every normalized object belongs in the user's generated report.

| Visibility | Use when | Report behavior |
|---|---|---|
| `show` | Clear, ordinary, non-sensitive summary. | Can appear normally with caveat. |
| `show_with_caveat` | Helpful but uncertain or doctrine-sensitive summary. | Must include “may”, “seems”, “not yet clear”, or similar uncertainty language. |
| `hide_from_report` | Implementation needs it internally, but showing it could shame, over-interpret, or expose another person. | Do not display; may generate a safer open question. |
| `human_review_only` | Sensitive or high-risk material. | Suppress ordinary report section and show safe human-help language. |

Never display hidden motives, diagnostic labels, inferred sin labels, personality type labels, compatibility categories, or internal sensitivity tags as public conclusions.

## 10. Theme grouping rules

`ConversationTheme` objects may group normalized answers only when the grouping is traceable and humble.

Allowed theme names:

- `faith_and_foundation`
- `hopes_fears_and_loneliness`
- `character_repentance_and_responsibility`
- `church_counsel_and_community`
- `daily_life_and_marriage_expectations`
- `conflict_forgiveness_and_reconciliation`
- `money_work_time_and_stewardship`
- `service_calling_and_shared_direction`
- `children_family_and_future_direction`
- `boundaries_consent_safety_and_next_step`

Theme rule: a theme summary must say what is named, repeated, unclear, or concerning. It must not say what the user's heart “really” wants, whether they are ready for marriage, whether a future relationship will work, or whether God approves a step.

## 11. Open question rules

`OpenQuestion` objects are safer than strong conclusions. Use them when:

- the user gave partial or unclear answers;
- the topic is important before serious promises;
- a direct conclusion would overreach;
- a sensitive area needs prayer, Scripture, counsel, or careful conversation.

Good question forms:

- “Who could help you examine this wisely before moving forward?”
- “What would need to become clearer before you make promises?”
- “Which Scripture truths and trusted counsel should shape this decision?”
- “What should be discussed calmly before expectations become pressure?”
- “What should remain private until you freely choose to share it?”

Bad question forms:

- “Why are you avoiding obedience?”
- “Is your fear really unbelief?”
- “Should this person be your spouse?”
- “Are you compatible enough to proceed?”
- “What does your type prove about your relationship?”

## 12. Wise next step rules

A `WiseNextStep` must be a safe category, not a command, prophecy, or verdict.

Allowed categories:

| Category | Use when | Safe wording |
|---|---|---|
| `continue_reflection` | Answers are ordinary but incomplete. | “Continue answering and praying through the unclear areas.” |
| `prepare_conversation_question` | A future conversation topic is clear. | “Write one question to discuss honestly when the time is right.” |
| `seek_trusted_believer_counsel` | The user names uncertainty, haste, loneliness, pressure, or important decisions. | “Consider speaking with a mature trusted believer before taking a serious step.” |
| `pastor_or_church_counsel` | The topic touches doctrine, church life, promises, discipline, or pastoral care. | “Consider bringing this to a pastor or church leader you trust.” |
| `pause_before_promises` | Haste, pressure, confusion, or major unresolved questions appear. | “It may be wise to pause before making promises while you seek counsel.” |
| `seek_safe_human_help` | High-risk safety flags appear. | “This should be handled with safe human help rather than an automated report.” |
| `privacy_and_consent_review` | Sharing or another person's data is involved. | “Review what should remain private and what requires consent before sharing.” |

A next step must not say:

- “God is telling you…”
- “You are ready / not ready for marriage.”
- “This person is / is not for you.”
- “Your ideal match is…”
- “Your score means…”
- “The system recommends this person.”

## 13. Concrete normalization examples

### Example A — loneliness and haste

Raw answer:

```text
I feel lonely and sometimes want to say yes quickly if someone notices me.
```

Allowed objects:

```json
{
  "claim_kind": "self_description",
  "uncertainty_label": "user_self_description",
  "attribution": "user_self_described",
  "normalized_text": "You describe loneliness as sometimes making haste feel tempting.",
  "public_visibility": "show_with_caveat"
}
```

```json
{
  "claim_kind": "proposed_question",
  "uncertainty_label": "suggested_question",
  "attribution": "system_hypothesis",
  "normalized_text": "Who could help you slow down and examine a serious step wisely before making promises?",
  "public_visibility": "show"
}
```

Forbidden:

```text
You are desperate for attention and therefore not ready for marriage.
```

### Example B — church counsel uncertainty

Raw answer:

```text
I do not know who I could ask in church. I am afraid people will gossip.
```

Allowed objects:

```json
{
  "claim_kind": "self_description",
  "uncertainty_label": "user_self_description",
  "attribution": "user_self_described",
  "normalized_text": "You describe uncertainty about whom to ask for counsel and concern about gossip.",
  "sensitivity_tags": ["privacy_or_consent"],
  "public_visibility": "show_with_caveat"
}
```

```json
{
  "claim_kind": "next_step",
  "uncertainty_label": "wise_next_step",
  "attribution": "system_hypothesis",
  "normalized_text": "A wise next step may be to identify one mature, discreet believer before sharing private details widely.",
  "public_visibility": "show_with_caveat"
}
```

Forbidden:

```text
You reject church authority and need to submit.
```

### Example C — coercion or danger

Raw answer:

```text
He says God told him I must marry him, and I am scared to say no.
```

Required flag:

```json
{
  "sensitivity_tags": ["spiritual_manipulation", "abuse_or_coercion"],
  "severity": "high",
  "uncertainty_label": "needs_human_review",
  "safe_public_text": "This should be handled with safe human help rather than an automated relationship report. Consider speaking with a trusted mature believer, pastor, or appropriate local support before responding alone.",
  "suppress_report_sections": true,
  "recommended_next_step_category": "pause_and_seek_help"
}
```

Forbidden:

```text
This may be God's will; pray and obey if you feel peace.
```

### Example D — money and debt

Raw answer:

```text
I have debt from school and I am trying to pay it monthly.
```

Allowed object:

```json
{
  "claim_kind": "fact",
  "uncertainty_label": "user_stated_fact",
  "attribution": "user_stated",
  "normalized_text": "You wrote that you have school debt and are trying to pay it monthly.",
  "public_visibility": "show"
}
```

Allowed open question:

```text
What would be wise to discuss about debt, work, giving, saving, and family support before making serious promises?
```

Forbidden:

```text
Your finances show you are not ready for marriage.
```

## 14. Implementation review checklist

Before implementation passes review, verify:

- [ ] raw `QuestionResponse` text is preserved separately from normalized summaries;
- [ ] every generated object includes `uncertainty_label`;
- [ ] every generated object includes attribution (`user_stated`, `user_self_described`, `system_summarized`, or `system_hypothesis`);
- [ ] no generated object silently converts facts into motives;
- [ ] no generated object states hidden motives as fact;
- [ ] no generated object uses diagnostic, typological, compatibility-score, spouse-promise, or spiritual-verdict language;
- [ ] every sensitive tag can create a `ReviewFlag`;
- [ ] high-risk flags suppress ordinary report advice;
- [ ] next steps are categories, not commands;
- [ ] privacy and consent are protected before any sharing/export behavior;
- [ ] user edits mark dependent normalized objects stale;
- [ ] reviewer logs can trace each normalized claim back to source responses.

## 15. Handoff to implementation

Use these rules when building cards 12 and 13 from `docs/hermes-kanban-action-plan.md`:

- AI summary prompts must require JSON fields for claim kind, uncertainty label, attribution, source response IDs, sensitivity tags, and visibility.
- Prompt wording must explicitly forbid hidden motive claims, readiness verdicts, compatibility conclusions, and spiritual authority claims.
- Generated text should prefer open questions over strong conclusions when evidence is thin.
- Report rendering must visually distinguish user-stated material from system-suggested questions or next steps.
- Any `needs_human_review` flag must alter the report flow before ordinary report text is shown.
