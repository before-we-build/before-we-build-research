# Consolidated Action Plan: Before We Build

**Last Updated:** 2026-05-12
**Status:** Revised to a realistic weak-AI starting point. Earlier simulation-concierge ideas are preserved only as a future research track.

---

## Executive Summary

Build a Christian conversation and discernment tool that helps people pause before serious shared decisions.

The first product does **not** try to be an autonomous AI dating concierge. It does **not** create digital twins, run large-scale simulations, score compatibility, or generate weekly candidate shortlists.

Instead, it starts from what current AI can do with reasonable reliability:

1. ask structured questions;
2. summarize answers;
3. identify missing or unclear topics;
4. map agreement and difference;
5. suggest wise conversation questions;
6. keep humans, Scripture, prayer, church, and counsel in the decision loop.

**Core Principle:** AI as a weak helper for conversation, not an oracle, matchmaker, pastor, or decision-maker.

---

## Part 1: Strategic Reset

### Old direction

Earlier drafts explored a Cognitive Matchmaker with:

- BFI-2-style persona generation;
- digital twins;
- adversarial scenarios;
- repeated-choice scoring;
- judge ensembles;
- automatic shortlists;
- validation against real dating outcomes.

That remains a possible research horizon, but it is too heavy and unreliable for the first build.

### New direction

The first practical product is:

```text
Scripture-first questions
→ answer capture
→ map of agreement / difference / uncertainty
→ questions for conversation
→ wise next step
```

The question to validate first is not "Can AI predict compatibility?"

The first question is:

> Does this help people have wiser, clearer, more honest conversations before serious decisions?

---

## Part 2: MVP Scope

### MVP-1: Personal Preparation Map

**Audience:** a Christian single or any person preparing for a serious relationship before God.

**Goal:** let a person begin alone, even without a current pair.

**Pipeline:**

1. Choose path: preparing for serious relationship.
2. Answer 20–40 Scripture-first and life-practical questions.
3. AI summarizes with uncertainty labels.
4. System identifies missing topics and possible tensions.
5. Report gives conversation questions and wise next steps.

**Output:** `PersonalPreparationMap`

Includes:

- hopes and expectations;
- non-negotiables;
- unclear areas;
- topics for prayer and counsel;
- questions for a future serious conversation.

Does not include:

- candidate search;
- compatibility score;
- digital twin;
- simulated relationship;
- promise of marriage;
- AI recommendation to pursue a person.

---

### MVP-2: Shared Conversation Map

**Audience:** two people considering a serious relationship, marriage, family decision, service, team, or common work.

**Pipeline:**

1. Person A answers separately.
2. Person B answers separately.
3. Answers are grouped by themes.
4. System shows agreement, difference, unknowns, and avoided topics.
5. System suggests conversation questions.
6. Sensitive flags recommend wise counsel or pastoral review.

**Output:** `SharedConversationMap`

No percentage score. No yes/no verdict. No simulated future.

---

### MVP-3: Church-Mediated Pilot

**Audience:** trusted churches helping single brothers and sisters consider introductions responsibly.

**Pipeline:**

1. Voluntary closed profile.
2. Anonymous matching/answer data separated from identity.
3. Church-confirmed participation.
4. Limited possible-conversation signal.
5. Human church review.
6. Staged consent before disclosure.
7. Introduction questions, not AI decision.

**Output:** `AnonymousConversationSignal` + `ChurchReviewNote` + `ConsentState`

No open browsing of singles. No photo-first marketplace. No automatic contact sharing.

---

## Part 3: Technical Architecture

```text
Question Library
→ Answer Capture
→ Answer Normalizer
→ Theme Mapper
→ Difference Mapper
→ Question Generator
→ Report Composer
→ Optional Human / Church Review
→ Feedback Notes
```

### Components

- **Question Library:** Scripture-first and life-practical questions by audience path.
- **Answer Capture:** forms or chat flow with save/resume.
- **Answer Normalizer:** separates facts, self-descriptions, uncertainty, and possible concerns.
- **Theme Mapper:** groups answers into conversation themes.
- **Difference Mapper:** compares two people only in pair mode.
- **Question Generator:** creates follow-up questions without verdict language.
- **Report Composer:** produces warm plain-language reports.
- **Review Layer:** human/pastor/church-worker review for sensitive issues.

---

## Part 4: Data Entities

Near-term entities:

- `UserSession`
- `AudiencePath`
- `QuestionSet`
- `QuestionResponse`
- `NormalizedAnswer`
- `ConversationTheme`
- `DifferenceItem`
- `OpenQuestion`
- `ConversationMap`
- `ReviewFlag`
- `WiseNextStep`
- `ConsentRecord`
- `FeedbackNote`

Deferred research entities:

- `DigitalTwin`
- `SimulationBatch`
- `SimulationRun`
- `CompatibilityScore`
- `AutomatedShortlist`
- `AutonomousConciergeAction`

---

## Part 5: Implementation Roadmap

### Phase 0: Foundation Specs — Week 1

Deliverables:

- Scripture-first promise and boundaries;
- public language rules;
- audience map;
- first relationship-preparation question library;
- report caveats.

### Phase 1: Personal Preparation MVP — Weeks 2–4

Deliverables:

- single-person answer flow;
- save/resume session;
- answer normalization;
- personal preparation report;
- follow-up question generation;
- export/share option for mentor or pastor review.

### Phase 2: Pair Conversation MVP — Weeks 5–8

Deliverables:

- two-person invitation flow;
- separate answer capture;
- shared map generation;
- agreement/difference/unknown sections;
- review flags;
- plain-language report.

### Phase 3: Human Review and Feedback — Weeks 9–12

Deliverables:

- feedback forms;
- pastor/mentor/church-worker review notes;
- quality rubric for reports;
- improved question sets based on real use.

### Phase 4: Church-Mediated Pilot — Later

Deliverables:

- voluntary closed profiles;
- anonymous IDs;
- consent tracking;
- limited church review workflow;
- audit log;
- no-browsing privacy rules.

### Phase 5: Research Track — Only After Usefulness Is Proven

Possible experiments:

- typology-assisted question routing;
- scenario-based reflection prompts;
- limited supervised simulations;
- judge ensembles for internal review;
- outcome calibration.

These are research experiments, not MVP requirements.

---

## Part 6: Success Metrics

### MVP-1

- User understands the tool in under 10 seconds.
- User can complete the path without typology knowledge.
- Report gives concrete next conversation topics.
- Report avoids verdict, score, and overpromise language.
- Scripture-first reviewers do not see the tool as replacing God, Scripture, church, or counsel.

### MVP-2

- Pair reports that the map helped them discuss important topics.
- Report fairly presents differences without pressure.
- Sensitive areas are visible but not sensationalized.
- Users understand that the output is a conversation aid, not a decision.

### MVP-3

- No open browsing of single people.
- No identity disclosure without staged consent.
- Church contacts understand the tool as care support, not a dating marketplace.
- Participants can pause, hide, delete, and revoke consent.

---

## Part 7: Risk Mitigation

| Risk | Mitigation |
|------|------------|
| User treats AI as verdict | No scores, no yes/no recommendation, repeated caveats |
| Tool sounds psychological or typological | Public language uses Scripture, wisdom, conversation, counsel |
| AI invents motives | Separate facts, self-description, uncertainty, and hypotheses |
| Sensitive differences are mishandled | Review flags and human/pastor review path |
| Church tool becomes a singles database | Anonymous profiles, staged consent, no browsing, audit logs |
| Product drifts back into expensive concierge | Keep simulation/shortlist/digital twin entities deferred until validated |

---

## Part 8: What Not to Build Yet

Do not build yet:

- autonomous AI dating concierge;
- candidate pool scraping;
- weekly AI shortlists;
- digital twin simulation;
- 100 adversarial scenarios;
- compatibility score;
- automatic messages;
- scheduling or venue suggestions;
- marketplace dynamics;
- fully automated church introductions.

---

## Part 9: Most Correct Current Formula

```text
Before We Build starts as a Christian conversation map before serious shared decisions.
```

Long-term research may explore stronger agentic systems, but the first useful product is:

```text
good questions, clear differences, honest uncertainty, wise next step
```
