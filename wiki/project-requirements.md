---
title: Project Requirements
type: concept
tags: [project, requirements, realistic-ai, conversation-map]
created: 2026-04-14
updated: 2026-05-12
sources: [wiki/concepts/plan.md, docs/consolidated-action-plan.md]
---

# Before We Build Project Requirements

## 1. Current Product Definition

Before We Build is currently defined as a Christian conversation and discernment tool before serious shared decisions.

The first implementation is **not** an autonomous AI dating concierge. It is not a simulation engine and not a compatibility oracle. It starts from the level of AI that is available now: weak but useful for structuring answers, noticing missing topics, and generating better conversation questions.

Current product formula:

```text
Scripture-first questions
→ answer capture
→ map of agreement / difference / uncertainty
→ questions for conversation
→ wise next step
```

## 2. Primary Users

### MVP-1

A Christian single or any person preparing for a serious relationship before God.

The user may begin alone, without a current pair.

### MVP-2

Two people considering a serious relationship, marriage, family decision, church service, team, or shared work.

### MVP-3

Trusted churches that want a privacy-preserving way to help single brothers and sisters consider possible introductions responsibly.

## 3. Product Non-Goals

The product must not:

- promise to find a spouse;
- output an ideal match claim;
- give a compatibility percentage as a decision basis;
- present AI simulation as truth about a person;
- replace Scripture, prayer, church, pastoral counsel, character, repentance, or responsibility;
- automate introductions, messages, or identity disclosure without consent;
- become a browsable database of single people.

## 4. Core Requirements for MVP-1: Personal Preparation Map

### Functional requirements

- Provide a relationship-preparation path that one person can start alone.
- Ask 20–40 Scripture-first and life-practical questions.
- Save raw answers.
- Summarize answers in plain language.
- Mark uncertainty and missing information.
- Identify topics for prayer, counsel, and future conversation.
- Generate 5–10 follow-up questions.
- Produce a report that can be read by the user and optionally shared with a mentor/pastor.

### Output requirements

The output should include:

- summary of hopes and expectations;
- important convictions and non-negotiables;
- unclear or undeveloped areas;
- topics that require future conversation;
- wise next step;
- explicit caveat: this is not a verdict, promise, prophecy, or pastoral authority.

## 5. Core Requirements for MVP-2: Shared Conversation Map

### Functional requirements

- Let two people answer separately.
- Keep each person’s answers private until both agree to generate the shared map.
- Group answers by themes.
- Show agreement, difference, unknowns, and avoided topics.
- Generate conversation questions.
- Mark sensitive areas where wise counsel or pastoral review may be appropriate.

### Output requirements

The output should include:

- shared themes;
- agreement areas;
- difference areas;
- topics needing direct conversation;
- suggested questions;
- review flags;
- no compatibility score or yes/no recommendation.

## 6. Core Requirements for MVP-3: Church-Mediated Pilot

### Functional requirements

- Support voluntary participation only.
- Use anonymous IDs by default.
- Separate identity data from answer/conversation-map data.
- Allow church-confirmed participation.
- Prevent open browsing of profiles.
- Require staged consent before identity disclosure.
- Log access and review actions.
- Allow participants to pause, hide, delete, and revoke consent.

### Output requirements

The output should be a limited possible-conversation signal, not a match verdict.

It may include:

- anonymous summary;
- church review note;
- consent state;
- suggested first conversation questions.

## 7. AI Use Boundaries

AI may be used for:

- summarizing answers;
- simplifying language;
- grouping themes;
- detecting missing topics;
- generating follow-up questions;
- preparing review notes.

AI must not be used as:

- an autonomous matchmaker;
- a spiritual authority;
- a hidden ranking system;
- a final judge of compatibility;
- an unsupervised introduction agent.

## 8. Deferred Research Requirements

The following are explicitly deferred and should not be built into MVP-1 or MVP-2:

- digital twins;
- autonomous relationship simulation;
- adversarial scenario batches;
- judge ensembles for final scoring;
- repeated-choice compatibility metric;
- automatic weekly shortlist;
- AI-driven messaging or scheduling.

These may remain as research-track ideas only after the simpler conversation product proves useful.

## 9. Acceptance Criteria

MVP-1 is acceptable when:

- a user understands the tool within 10 seconds;
- the user can complete it without typology knowledge;
- the report gives concrete conversation topics;
- public language is Christian, plain, and not psychology-first;
- output does not sound like a verdict.

MVP-2 is acceptable when:

- both people understand the map as a conversation aid;
- differences are shown respectfully;
- sensitive issues are marked without pressure or manipulation;
- no output implies that AI has decided the relationship.

MVP-3 is acceptable when:

- privacy boundaries are enforced;
- no one can browse all single people;
- identity is not disclosed without staged consent;
- churches understand the tool as care support, not a dating marketplace.
