---
title: Plan
type: concept
tags: [product, technical, roadmap, realistic-ai, conversation-map]
created: 2026-04-14
updated: 2026-05-13
sources: [autoreasearch.md, wiki/concepts/compatibility-level-boundaries.md, wiki/concepts/typology-code-conventions.md, wiki/concepts/weight-calibration.md]
---

# Before We Build: Product and Technical Plan

This is the current working plan. It intentionally steps back from the earlier "AI dating concierge / digital twin simulation" ambition.

The governing assumption is simple: **current AI is weak and unreliable for autonomous matchmaking**. It can help structure thought, summarize answers, expose missing topics, and generate good conversation questions. It should not be treated as a reliable judge of souls, spouse-readiness, compatibility, or God's will.

Therefore the first product is not a concierge and not a matching oracle. It is a **Christian conversation and discernment tool before serious shared decisions**.

Compressed formula:

```text
Before We Build v1 = Scripture-first questions + map of differences + wise next step
not = autonomous matchmaker, digital twin simulator, or compatibility verdict
```

---

## 0. Methodology Update — 2026-05-12

Earlier drafts described a sophisticated Cognitive Matchmaker: multi-agent simulation, digital twins, adversarial scenarios, judge ensembles, weekly shortlists, and later automation.

That direction remains useful as a long-term research horizon, but it is **not the implementation plan for the near product**.

Current plan:

1. Start with what weak AI can do reliably.
2. Use AI for structure, questions, translation, summarization, and checks.
3. Keep humans responsible for discernment, pastoral wisdom, consent, and final decisions.
4. Avoid public language that promises matchmaking, prediction, scores, or spiritual certainty.
5. Treat typology and simulation as hidden research/support layers, not as the public door.

Current governing pages remain:

- [[compatibility-level-boundaries]] — strategic, operational, and tactical boundaries.
- [[typology-code-conventions]] — canonical and localized type-code rules.
- [[weight-calibration]] — scoring and aggregation remain research questions, not product doctrine.

---

## 1. Product Goal

### What the product should do now

- Help a Christian person or pair pause before building a relationship, family, service, team, or common work.
- Ask simple, serious questions that people often avoid until too late.
- Produce a plain-language map of agreement, difference, uncertainty, and topics needing conversation.
- Help lonely Christian singles begin preparation even before they have a pair.
- Give questions for prayer, Scripture reflection, wise counsel, and honest conversation.
- Support church-mediated introductions later without becoming a public dating app.

### What the product should not do now

- It should not promise to find a spouse.
- It should not rank people as ideal / non-ideal matches.
- It should not output compatibility percentages as a decision basis.
- It should not simulate a person and present the result as truth.
- It should not automate introductions, messages, or disclosure without consent.
- It should not replace Scripture, prayer, church, pastoral counsel, character, repentance, or responsibility.

---

## 2. The Realistic AI Principle

Current AI is useful as a **scribe, organizer, translator, and question generator**.

It is weak as:

- an autonomous matchmaker;
- a stable digital twin of a real person;
- a spiritual or moral judge;
- a predictor of marriage outcomes;
- a fully reliable interpreter of hidden motives;
- a safe agent for unsupervised introductions.

Therefore the near-term system should use AI only where errors are recoverable and human review is natural.

Good uses:

- rewrite a complex answer into a clear summary;
- separate facts, self-descriptions, hypotheses, and unknowns;
- identify unanswered important topics;
- suggest conversation questions;
- translate internal categories into ordinary Christian language;
- prepare a digest for a human/pastor/church worker to review.

Bad near-term uses:

- "this is your best match";
- "you are compatible / incompatible";
- "the simulation proves...";
- "the AI recommends you contact this person";
- hidden ranking without explanation and consent.

---

## 3. Public Product Shape

The public product should be framed as:

```text
A Christian path of questions before people build together.
```

Better public names for features:

- "Начать с простых вопросов"
- "Карта разговора"
- "Вопросы перед серьёзным шагом"
- "Темы, которые стоит обсудить"
- "Что мы уже понимаем, а что ещё не ясно"

Avoid as public first-door language:

- AI dating concierge;
- matchmaker;
- digital twin;
- simulation;
- compatibility score;
- psychological profile;
- typology verdict;
- ideal match;
- prediction.

---

## 4. Three-Stage Product Roadmap

### Stage 1 — Start Alone

**Audience:** a lonely Christian brother or sister, or any person preparing for a serious relationship before God.

**Goal:** help one person prepare for wise conversation and discernment.

**What it does:**

- asks a small set of Scripture-first and life-practical questions;
- helps the person name hopes, fears, expectations, non-negotiables, and unclear areas;
- identifies topics the person has not thought through;
- produces a simple personal preparation map;
- suggests questions to bring to prayer, Scripture, wise counsel, and a future conversation.

**Output:**

- `PersonalPreparationMap`
- `OpenQuestions`
- `WiseNextStep`

**Not included:** candidate search, pair scoring, digital twin, simulation, automated recommendations.

---

### Stage 2 — Walk Through Together

**Audience:** two people considering a serious relationship, marriage, family decision, service, team, or shared work.

**Goal:** help them compare answers and start honest conversation without a verdict.

**What it does:**

- both people answer separately;
- the system groups answers by themes;
- it shows agreement, difference, uncertainty, and avoided topics;
- it suggests conversation questions;
- it marks where wise counsel or pastoral review may be helpful.

**Output:**

- `SharedConversationMap`
- `AgreementAreas`
- `DifferenceAreas`
- `NeedsConversation`
- `SuggestedQuestions`
- `CounselReviewFlags`

**Not included:** compatibility percentage, automatic yes/no recommendation, simulated future marriage, hidden ranking.

---

### Stage 3 — Church-Mediated Introduction Support

**Audience:** trusted churches that want to help single brothers and sisters meet responsibly.

**Goal:** support church-led, consent-based introductions without turning people into a browsable dating database.

**What it does:**

- collects voluntary closed profiles;
- keeps identity separate from answer/fit data;
- gives limited possible-conversation signals to responsible church contacts;
- requires staged consent before disclosure;
- logs access and decisions;
- produces questions for the first careful conversation.

**Output:**

- `ClosedProfile`
- `AnonymousConversationSignal`
- `ChurchReviewNote`
- `ConsentState`
- `IntroductionQuestionSet`

**Not included:** open browsing, photos-first search, automatic contact sharing, autonomous messaging, AI final decision.

---

## 5. Future Research Track — Not MVP

The earlier Cognitive Matchmaker plan is now classified as a **future research track**.

It may explore:

- richer evidence profiles;
- typology-assisted hypotheses;
- scenario libraries;
- limited simulations;
- judge ensembles;
- outcome calibration;
- multi-agent orchestration.

But these should only be introduced after the simple conversation product proves useful and after real-world feedback shows where automation would actually help.

Research-track rule:

```text
No simulation or scoring feature becomes user-facing until it is validated, explainable, consent-safe, and reviewable by humans.
```

---

## 6. Compatibility Ontology as Hidden Support

Before We Build may still use its three-level ontology internally:

| Level | Internal lens | Public question |
|-------|---------------|-----------------|
| Strategic | Temporistics | Where are we going, and what gives life direction? |
| Operational | Psychosophy | How do we make decisions, carry responsibility, and handle pressure? |
| Tactical | Socionics | How do we communicate, misunderstand, repair, and coordinate? |

Public-facing outputs should not lead with type labels. They should translate internal categories into plain questions.

Typologies are useful only as secondary aids for:

- question selection;
- conversation categories;
- noticing possible blind spots;
- research hypotheses;
- optional deeper interpretation.

They are not the foundation of Christian discernment.

---

## 7. Minimal Technical Architecture

The first version can be simple.

```text
Question Library
→ Answer Capture
→ Answer Normalizer
→ Difference Mapper
→ Question Generator
→ Human-Readable Report
→ Optional Human/Church Review
→ Feedback Notes
```

### Components

1. **Question Library**
   - Scripture-first and life-practical question sets.
   - Audience paths: alone, pair, family, service, team, common work.

2. **Answer Capture**
   - Simple form or chat flow.
   - Saves raw answers and timestamps.

3. **Answer Normalizer**
   - Separates facts, self-descriptions, uncertainties, and inferred concerns.
   - Uses AI cautiously and labels uncertainty.

4. **Difference Mapper**
   - For pair mode, compares two sets of answers.
   - Shows agreement/difference/unknown rather than score.

5. **Question Generator**
   - Produces follow-up questions for conversation.
   - Avoids verdict language.

6. **Report Composer**
   - Outputs warm, plain-language summary.
   - Includes caveats: not a verdict, not pastoral authority, not a promise.

7. **Review Layer**
   - Human/pastor/church-worker review where sensitive issues appear.

---

## 8. Data Entities

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

Explicitly deferred entities:

- `DigitalTwin`
- `SimulationBatch`
- `SimulationRun`
- `CompatibilityScore`
- `AutomatedShortlist`
- `AutonomousConciergeAction`

These deferred entities may exist in research documents, but they should not define the first build.

---

## 9. First MVP Scope

### MVP-1: Personal Preparation Map

**User story:**

> As a Christian single, I want to begin alone and prepare for a serious relationship before God, so that I do not enter relationship decisions only from loneliness, fear, or fantasy.

**Included:**

- one audience path: "I am preparing for a serious relationship";
- 20–40 core questions;
- save/resume session;
- AI-assisted summary with uncertainty labels;
- personal preparation report;
- 5–10 suggested questions for future conversation;
- explicit caveat that this is not a verdict and not a promise of marriage.

**Success criteria:**

- user understands what the tool is in under 10 seconds;
- user can complete the path without typology knowledge;
- output gives concrete conversation topics;
- output avoids psychological/typological jargon;
- conservative Scripture-first reader does not feel the tool replaces Scripture or pastoral wisdom.

---

## 10. Second MVP Scope

### MVP-2: Shared Conversation Map

**User story:**

> As two people considering a serious step, we want to answer separately and receive a map of topics to discuss, so that we can speak honestly before making promises.

**Included:**

- two-person invitation flow;
- separate answers;
- comparison by themes;
- agreement/difference/unknown map;
- follow-up questions;
- review flags for faith, marriage expectations, children, money, church, family, conflict, and responsibility.

**Success criteria:**

- the pair reports that the map helped them have a better conversation;
- the output does not pressure them toward yes/no;
- sensitive differences are presented respectfully;
- report is understandable without technical background.

---

## 11. Third MVP Scope

### MVP-3: Church-Mediated Pilot

**User story:**

> As a church contact, I want a privacy-preserving way to help single brothers and sisters consider possible introductions, so that people become visible for care but not open for curiosity.

**Included:**

- voluntary profiles;
- anonymous IDs;
- separated identity and answer data;
- church-confirmed participation;
- limited possible-conversation signals;
- consent before disclosure;
- audit log;
- human review before any introduction.

**Success criteria:**

- no open browsing of singles;
- no contact sharing without staged consent;
- churches understand the tool as support for care, not a dating marketplace;
- participants can pause, hide, delete, and revoke consent.

---

## 12. Validation Approach

The first validation question is not:

> Can AI predict compatibility?

The first validation question is:

> Does this help people have wiser, clearer, more honest conversations before serious decisions?

Measure:

- clarity of output;
- user trust without over-trust;
- whether users discuss topics they would otherwise avoid;
- whether pastors/mentors/church workers find the report usable;
- whether people understand the caveats;
- whether the tool reduces confusion without replacing responsibility.

Only after this is proven should the project test stronger claims about matching or prediction.

---

## 13. What to Defer

Defer until much later:

- autonomous AI dating concierge;
- large candidate pool triage;
- digital twins;
- adversarial scenario simulation;
- compatibility scores;
- automatic shortlist;
- automatic messages;
- AI-driven scheduling;
- prediction claims;
- optimization for engagement or marketplace growth.

These may be research directions, but they are not the product foundation.

---

## 14. What to Build in the First 30 Days

### Week 1

- finalize Scripture-first product promise;
- define public language boundaries;
- write the first audience path: "start alone";
- draft the core question library.

### Week 2

- build answer capture;
- define `QuestionResponse`, `NormalizedAnswer`, and `ConversationTheme`;
- create first report template.

### Week 3

- add AI-assisted summarization with uncertainty labels;
- add follow-up question generation;
- add no-verdict/no-promise caveats.

### Week 4

- test with 5–10 trusted users;
- collect feedback on clarity, spiritual safety, and usefulness;
- revise language and questions;
- decide whether to build pair mode next.

---

## 15. Final Product Promise and Most Correct Product Formula

### Final internal promise

```text
Before We Build is a Scripture-first preparation tool that uses good questions, clear differences, and honest uncertainty to help people prepare for wise conversation and name a wise next step before serious shared decisions.
```

### Final public-facing promise

```text
Before We Build допомагає перед серйозним спільним кроком зупинитися перед Богом: пройти добрі запитання, побачити важливі відмінності й чесно назвати, що ще не ясно, щоб підготуватися до мудрої розмови та наступного кроку.
```

Promise boundaries:

- no promise of a spouse, family, or guaranteed outcome;
- no score, verdict, or compatibility percentage;
- no replacement for Scripture, prayer, church, wise counsel, or personal responsibility;
- the tool prepares people for honest conversation; it does not decide for them.

If compressed completely:

```text
Before We Build starts as a Christian conversation map before serious shared decisions.
```

The later research dream may become:

```text
evidence-based simulation of joint behavior under constraint
```

But the first useful product is humbler:

```text
good questions, clear differences, honest uncertainty, wise next step
```

If done weakly, the project becomes a pseudo-spiritual or pseudo-scientific oracle.
If done strongly, it begins as a simple tool for wisdom and may later grow into more advanced support only where real evidence justifies it.
