# Hermes Kanban Action Plan: Before We Build

**Source plans:**
- `docs/consolidated-action-plan.md`
- `wiki/concepts/plan.md`

**Created:** 2026-05-13

## Purpose

Turn the current Before We Build plan into a Hermes Kanban-ready work graph: small cards, clear dependencies, review gates, and profile assignments.

The product direction remains:

```text
Before We Build starts as a Christian conversation map before serious shared decisions.
```

Near-term product rule:

```text
good questions, clear differences, honest uncertainty, wise next step
```

Do not turn the first build into an autonomous matchmaker, dating marketplace, digital twin simulator, compatibility oracle, or spiritual verdict system.

## Current Hermes profile situation

`hermes profile list` currently shows only one runnable profile:

- `default`

So the first Kanban version can work, but it will be mostly a durable single-worker queue.

For stronger practical use, create or configure additional profiles later, for example:

- `planner` — decomposes product work and writes exact implementation specs.
- `writer` — drafts Scripture-first public copy and question wording.
- `coder` — implements application changes.
- `reviewer` — checks claims, safety, caveats, and regression risk.
- `researcher` — checks source material, doctrine-sensitive phrasing, and evidence boundaries.

Until those exist, every card below can be assigned to `default`.

## Kanban lanes

### Lane A — Product promise and boundaries

Goal: make the first product unmistakably humble, Scripture-first, and non-oracular.

Cards:

1. **Finalize product promise**
   - Assignee now: `default`
   - Future assignee: `writer` or `planner`
   - Inputs: `wiki/concepts/plan.md`, `docs/consolidated-action-plan.md`
   - Output: one short internal promise and one public-facing promise.
   - Final internal promise:
     > Before We Build is a Scripture-first preparation tool that uses good questions, clear differences, and honest uncertainty to help people prepare for wise conversation and name a wise next step before serious shared decisions.
   - Final public-facing promise:
     > Before We Build допомагає перед серйозним спільним кроком зупинитися перед Богом: пройти добрі запитання, побачити важливі відмінності й чесно назвати, що ще не ясно, щоб підготуватися до мудрої розмови та наступного кроку.
   - Acceptance:
     - no promise of spouse/family;
     - no score/verdict language;
     - clearly says the tool helps prepare for wise conversation.
     - keeps the formula: good questions, clear differences, honest uncertainty, wise next step.

2. **Define public language boundaries**
   - Assignee now: `default`
   - Future assignee: `writer` + `reviewer`
   - Depends on: card 1
   - Output: `wiki/concepts/public-language-boundaries.md`, a do/don’t vocabulary list for public Russian/Ukrainian copy.
   - Acceptance:
     - avoids psychological and typological front-door language;
     - uses Scripture, wisdom, character, discernment, counsel, conversation, map of differences;
     - no mixed English terms in public Russian/Ukrainian copy.
   - Completed artifact:
     - `wiki/concepts/public-language-boundaries.md` defines preferred/rejected terms, button wording, report wording, good/bad phrase examples, Scripture-near anchors, and reviewer safety checks.

3. **Create caveat standard for all reports**
   - Assignee now: `default`
   - Future assignee: `reviewer`
   - Depends on: card 1
   - Output: reusable caveat block.
   - Acceptance:
     - says report is not verdict, not pastoral authority, not promise;
     - points back to Scripture, prayer, church, counsel, responsibility.

### Lane B — First audience path: start alone

Goal: define the first path for a Christian single preparing before God for serious relationship decisions.

Cards:

4. **Write audience path spec: Start Alone**
   - Assignee now: `default`
   - Future assignee: `planner`
   - Depends on: card 1
   - Output: `docs/start-alone-audience-path-spec.md` — internal spec for the first path.
   - Acceptance:
     - audience is clear in under 10 seconds;
     - no typology knowledge required;
     - no promise of marriage;
     - one clear next action for the user;
     - preserves Scripture-first and church/counsel boundaries.

5. **Draft core question library v0**
   - Assignee now: `default`
   - Future assignee: `writer` + `researcher`
   - Depends on: cards 2 and 4
   - Output: `docs/start-alone-question-library-v0.md` — 39 questions grouped by themes, with optional first set, localization notes, coverage checklist, and review flags.
   - Acceptance:
     - questions are Scripture-first and life-practical;
     - questions cover hopes, expectations, faith, church, family, money, conflict, responsibility, service, children, counsel;
     - questions do not sound clinical or like a dating quiz.
   - Completed artifact:
     - `docs/start-alone-question-library-v0.md` drafts 39 Start Alone questions across faith, hopes, character, church/counsel, daily life, conflict, money/work, service, children/family, boundaries/safety, and next-step themes.

6. **Review question library for spiritual safety**
   - Assignee now: `default`
   - Future assignee: `reviewer`
   - Depends on: card 5
   - Output: review notes and approved/rejected questions.
   - Acceptance:
     - no manipulative wording;
     - no extra-biblical authority claims;
     - no AI-as-discernment replacement tone.
   - Completed artifact:
     - `docs/start-alone-question-library-spiritual-safety-review.md` reviews all 39 Start Alone questions and the optional 8-question first set, with approved/rewrite/rejected statuses, safer replacement wording, pastor-check flags, and implementation guardrails for privacy, counsel, and non-oracular AI use.

### Lane C — Data and report model

Goal: make the minimal internal objects concrete before implementation.

Cards:

7. **Specify MVP data entities**
   - Assignee now: `default`
   - Future assignee: `planner` or `coder`
   - Depends on: card 4
   - Output: entity spec for `UserSession`, `AudiencePath`, `QuestionSet`, `QuestionResponse`, `NormalizedAnswer`, `ConversationTheme`, `OpenQuestion`, `ConversationMap`, `ReviewFlag`, `WiseNextStep`, `FeedbackNote`.
   - Acceptance:
     - separates raw answers from normalized summaries;
     - includes uncertainty labels;
     - excludes deferred entities: `DigitalTwin`, `CompatibilityScore`, `AutomatedShortlist`.
   - Completed artifact:
     - `docs/mvp-data-entities.md` defines the requested MVP entities, raw-vs-normalized separation, uncertainty labels, flow placement, explicit exclusions, and follow-up handoff notes.

8. **Design personal preparation report template**
   - Assignee now: `default`
   - Future assignee: `writer` + `planner`
   - Depends on: cards 3, 5, and 7
   - Output: template for `PersonalPreparationMap`.
   - Acceptance:
     - includes hopes/expectations, unclear areas, topics for prayer/counsel, future conversation questions, wise next step;
     - no verdict/score/promise;
     - plain-language Russian/Ukrainian ready.
   - Completed artifact:
     - `docs/personal-preparation-map-template.md` defines the first Start Alone report template, including required caveat placement, clear/unclear sections, hopes and expectations, prayer/counsel topics, future conversation questions, review-flag handling, one wise next step, localized wording directions, and implementation handoff contract.

9. **Define answer normalization rules**
   - Assignee now: `default`
   - Future assignee: `planner` + `reviewer`
   - Depends on: card 7
   - Output: `docs/answer-normalization-rules.md` — rules for separating facts, self-descriptions, uncertainties, possible concerns, and AI hypotheses.
   - Acceptance:
     - every AI inference is labeled as uncertain;
     - user-provided facts are not silently rewritten as motives;
     - sensitive areas can trigger review flags.
   - Completed artifact:
     - `docs/answer-normalization-rules.md` defines claim kinds, attribution requirements, uncertainty escalation, sensitive review flags, report visibility rules, examples, and implementation review checks.

### Lane D — Technical MVP

Goal: build the smallest useful version of the Start Alone flow.

Cards:

10. **Inspect target app/repository for implementation path**
    - Assignee now: `default`
    - Future assignee: `coder`
    - Depends on: card 7
    - Output: exact repo, stack, files, and implementation approach.
    - Acceptance:
      - identifies where question flow, persistence, report generation, and UI copy should live;
      - lists exact commands to run and tests to add.
   - Completed artifact:
     - `docs/technical-mvp-implementation-path.md` identifies `before-we-build.github.io` as the Start Alone MVP target repo, separates it from `church-intro-bot`, maps question flow, local persistence, normalization, report generation, UI copy, controlled export, commands, and tests.

11. **Implement answer capture v0**
    - Assignee now: `default`
    - Future assignee: `coder`
    - Depends on: cards 5, 7, and 10
    - Output: user can answer the Start Alone question set.
    - Acceptance:
      - save/resume exists or is explicitly deferred with reason;
      - raw answers are stored;
      - flow is usable without typology knowledge.

12. **Implement AI-assisted summary with uncertainty labels**
    - Assignee now: `default`
    - Future assignee: `coder`
    - Depends on: cards 9 and 11
    - Output: normalized answer summaries.
    - Acceptance:
      - summaries preserve user meaning;
      - uncertainty is visible;
      - no hidden compatibility verdict.

13. **Implement PersonalPreparationMap report**
    - Assignee now: `default`
    - Future assignee: `coder`
    - Depends on: cards 8 and 12
    - Output: first generated report.
    - Acceptance:
      - includes conversation questions and wise next step;
      - includes caveat block;
      - avoids psychological/typological public language.

14. **Add export/share option for mentor or pastor review**
    - Assignee now: `default`
    - Future assignee: `coder`
    - Depends on: card 13
    - Output: shareable/exportable report format.
    - Acceptance:
      - user controls sharing;
      - report includes caveats;
      - no automatic disclosure.

### Lane E — Review and validation

Goal: test whether the tool helps people have wiser, clearer, more honest conversations.

Cards:

15. **Create review rubric**
    - Assignee now: `default`
    - Future assignee: `reviewer`
    - Depends on: cards 3 and 8
    - Output: `docs/generated-report-review-rubric.md` — rubric for clarity, spiritual safety, usefulness, over-trust risk, and language.
    - Acceptance:
      - checks “not replacing Scripture/prayer/church/counsel”;
      - checks no verdict/score/promise;
      - checks whether output gives concrete conversation topics.
    - Completed artifact:
      - `docs/generated-report-review-rubric.md` defines pass/block criteria for generated reports across clarity, spiritual safety, concrete conversation usefulness, over-trust risk, language/localization, privacy/consent, and safety escalation; it includes hard blockers for verdicts, scores, promises, replacement of Scripture/prayer/church/counsel, hidden motive-reading, automatic disclosure, and unsafe abuse/coercion/self-harm handling.

16. **Run internal review on generated report**
    - Assignee now: `default`
    - Future assignee: `reviewer`
    - Depends on: cards 13 and 15
    - Output: pass/block review with required changes.
    - Acceptance:
      - report passes rubric or creates follow-up fix cards;
      - blockers are explicit.

17. **Prepare trusted-user test plan**
    - Assignee now: `default`
    - Future assignee: `planner` or `researcher`
    - Depends on: card 15
    - Output: `docs/trusted-user-test-plan.md` — plan for 5–10 trusted users.
    - Acceptance:
      - measures clarity, spiritual safety, usefulness, caveat understanding;
      - does not test compatibility prediction;
      - includes feedback questions;
      - defines how feedback will be summarized without overclaiming.
    - Completed artifact:
      - `docs/trusted-user-test-plan.md` defines a private 5–10 trusted-user test focused on clarity, spiritual safety, usefulness for wise conversation, caveat understanding, trust without over-trust, privacy/consent, and missing topics; it excludes compatibility prediction and gives feedback questions, observer notes, stop criteria, and cautious synthesis rules.

18. **Collect and synthesize first feedback**
    - Assignee now: `default`
    - Future assignee: `researcher`
    - Depends on: cards 16 and 17
    - Output: feedback summary and next-step recommendation.
    - Acceptance:
      - identifies confusing wording;
      - identifies missing topics;
      - recommends whether to revise Start Alone or proceed toward pair mode.

## Dependency graph

```text
1 product promise
├─ 2 language boundaries
├─ 3 caveat standard
└─ 4 Start Alone spec
   ├─ 5 question library
   │  └─ 6 spiritual-safety review
   └─ 7 data entities
      ├─ 9 normalization rules
      └─ 10 implementation inspection

3 + 5 + 7 → 8 report template
5 + 7 + 10 → 11 answer capture
9 + 11 → 12 summary
8 + 12 → 13 report
13 → 14 export/share
3 + 8 → 15 rubric
13 + 15 → 16 internal review
15 → 17 trusted-user test plan
16 + 17 → 18 feedback synthesis
```

## Suggested actual Kanban creation order

Because only `default` exists now, use `default` in commands until more profiles exist.

Example first batch:

```bash
hermes kanban init
hermes kanban create "BWB: finalize product promise" --assignee default
hermes kanban create "BWB: define public language boundaries" --assignee default
hermes kanban create "BWB: create report caveat standard" --assignee default
hermes kanban create "BWB: write Start Alone audience path spec" --assignee default
```

For dependency-heavy creation, prefer using Hermes itself to create cards with parent links, because the CLI task ids need to be captured and linked correctly.

Recommended prompt:

```text
Create Hermes Kanban cards from /home/ubuntu/before-we-build-research/docs/hermes-kanban-action-plan.md. Use only the existing profile `default` unless I give you more profiles. Preserve dependencies exactly from the dependency graph. Do not implement the tasks yet; only create the board cards.
```

## Recommended profile setup before serious use

If you want Kanban to become practically useful instead of just a queue, create a small profile roster first:

```bash
hermes profile create planner --clone default
hermes profile create writer --clone default
hermes profile create coder --clone default
hermes profile create reviewer --clone default
hermes profile create researcher --clone default
```

Then tune each profile’s model/tool permissions later. After that, update this plan’s “Future assignee” values into real Kanban assignees.

## Next decision

Choose one of two paths:

1. **Single-profile start:** create all cards assigned to `default` now. Simpler, works immediately, less parallelism.
2. **Multi-profile setup first:** create Hermes profiles, then create cards assigned by role. Better for real Kanban orchestration.
