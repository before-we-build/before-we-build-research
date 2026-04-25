---
title: Smart Mobilization
type: concept
tags: [smart-mobilization, military, role-fit, recruitment, ethics, research-hypothesis]
created: 2026-04-25
updated: 2026-04-25
sources: [smart-mobilization-research-note, smart-mobilization-typology-wartime, ukraine-military-specialties-current, esco-typology-mapping]
---

# Smart Mobilization

## Definition

**Smart Mobilization** is a PsyCalc concept for **voluntary, non-coercive role-fit recommendations** in a military recruitment context.

The idea is to combine:

- current military vacancies and role families;
- a person's civilian skills and work background;
- self-reported role preferences;
- typology-based hypotheses from Socionics, Psychosophy, and Temporistics;
- human recruiter or advisor review.

The output should be a set of **possible role-family matches**, not an assignment order, readiness judgment, or automated personnel decision.

## One-Sentence Summary

Smart Mobilization means helping a volunteer find a role where current needs, real skills, and cautious typology-based fit hypotheses overlap — while keeping consent, human oversight, and non-coercion central.

## Problem It Addresses

In wartime recruitment, a person may want to serve but not know where their background fits. At the same time, military organizations have concrete needs that change over time.

The mismatch problem has several parts:

- real vacancies are fragmented across role families and units;
- civilians may not know how their profession maps to military specialties;
- recruiters may not have enough time to explore every person's full background;
- people may choose roles based on stereotypes rather than practical fit;
- poor fit can increase stress, dropout risk, wasted training time, and role dissatisfaction.

Smart Mobilization is a proposed matching layer for making this conversation more structured.

## Core Principle

The most defensible use case is **better voluntary placement**, not forced assignment.

The system should answer:

> “Given your skills, preferences, current role needs, and tentative PsyCalc hypotheses, which role families might be worth discussing with a human recruiter?”

It should not answer:

> “Where should this person be assigned?”

## Inputs

### 1. Current Role Needs

The system starts from actual role demand, such as:

- vacancies;
- branch or unit requirements;
- role family;
- required training;
- physical and legal requirements;
- technical or language requirements.

See [[ukraine-military-specialties-current]] for the current role-family cataloging direction.

### 2. Civilian Skills

Civilian background is the primary practical anchor:

- profession;
- technical skills;
- certifications;
- tools and platforms;
- leadership or team experience;
- logistics, engineering, medical, communications, IT, UAV, EW/RER, analytical, or administrative experience.

See [[esco-typology-mapping]] for the broader civilian-to-role mapping logic.

### 3. Preferences and Constraints

Recommendations should respect volunteered constraints:

- preferred role families;
- unacceptable role families;
- health or accessibility limits, where voluntarily disclosed;
- location or training constraints;
- language constraints;
- risk tolerance and family constraints, if voluntarily disclosed.

These should not be inferred secretly.

### 4. Typology-Based Hypotheses

PsyCalc may add a tentative typology layer:

- **Socionics** → heuristic model of information modeling;
- **Psychosophy** → heuristic model of synthesis and analysis in action;
- **Temporistics** → heuristic model of induction and deduction in temporal/existential experience.

This layer can suggest communication style, action organization, planning orientation, or stress points. It must remain secondary to real skills, requirements, and human review.

## Matching Logic

Smart Mobilization should follow this order:

1. Start with real vacancies and role families.
2. Filter by hard requirements and volunteered constraints.
3. Match civilian skills to role tasks.
4. Use typology only as a hypothesis layer for fit, risks, and support needs.
5. Produce ranked role-family suggestions with explanations and uncertainty.
6. Send outputs to human review, not automatic assignment.

## Output Format

A safe recommendation should look like:

- **Possible fit:** role family or specialty cluster;
- **Why it may fit:** skills, experience, preferences, role demand;
- **Typology hypothesis:** cautious note, not proof;
- **Uncertainty:** missing data or reasons to verify;
- **Questions for recruiter/advisor:** what to check next;
- **Alternatives:** adjacent roles if the first option is unavailable or unsuitable.

Recommended wording:

- “may fit”;
- “worth discussing”;
- “hypothesis-based”;
- “requires human review”;
- “not assignment guidance.”

Avoid wording like:

- “best soldier type”;
- “guaranteed fit”;
- “combat-effective because of type”;
- “must be assigned to this role.”

## Ethical Boundaries

Smart Mobilization is high-stakes because it touches military service, safety, identity, and possible coercion. Therefore, the following boundaries are required.

### Required Safeguards

- Participation must be opt-in and informed.
- Users must understand what data is collected, why, who can access it, and how deletion works.
- Typology results must never be the sole basis for assignment, exclusion, promotion, clearance, deployment, or training access.
- Recommendations must be contestable: a person should be able to question, correct, or reject them.
- Human review is mandatory for any real-world opportunity-affecting recommendation.
- Data collection must be minimized and separated by category: skills, preferences, vacancies, typology results, and any interaction logs.
- Outputs must not be treated as medical, psychological, loyalty, obedience, or dangerousness assessments.
- Public reporting should be aggregated and de-identified.

### Red Lines

Do not use Smart Mobilization to:

- force a person into a role;
- infer mental health, dangerousness, political reliability, spirituality, or coercion resistance;
- rank human worth or patriotism;
- claim typology predicts combat effectiveness or mission success;
- secretly profile people from behavior or platform data;
- reuse research data as operational personnel data without explicit new consent and legal/ethics review;
- publish identifiable case studies about applicants, soldiers, units, or sensitive role needs.

## Research Status

Smart Mobilization is a **research and design hypothesis**, not a validated operational method.

Existing sources support the broader context:

- military recruitment and personnel selection are mature practical domains;
- Ukraine already has public role-based recruitment channels;
- AI-assisted recruitment and personnel analytics exist internationally;
- personality and trait research has been studied in military contexts.

Existing sources do **not** establish Socionics, Psychosophy, or Temporistics as validated standard frameworks for military assignment.

Therefore, PsyCalc's role-fit claims must remain provisional, testable, and caveated.

## Relationship to PsyCalc

Smart Mobilization is an applied use case of PsyCalc's broader role-fit architecture.

It uses the three typological systems at different levels:

| Level | System | Possible Role-Fit Use |
|-------|--------|-----------------------|
| Strategic | Temporistics | orientation to time, mission horizon, uncertainty, long-term meaning |
| Operational | Psychosophy | action organization, effort, communication of priorities, support needs |
| Tactical | Socionics | information exchange, team communication, task-environment fit |

These mappings are project heuristics and should be tested against real outcomes before being operationalized.

## In Scope

- voluntary role discovery;
- role-family recommendation;
- civilian-to-military skill translation;
- recruiter/advisor conversation support;
- research design and validation planning;
- opt-in self-assessment tools;
- aggregated analysis of role-fit hypotheses.

## Out of Scope

- forced mobilization routing;
- autonomous assignment;
- medical or psychological fitness decisions;
- security clearance decisions;
- loyalty, obedience, or ideology screening;
- combat-readiness certification;
- deterministic type-to-role tables.

## See Also

- [[smart-mobilization-research-note]] — Existing practice and project novelty
- [[smart-mobilization-typology-wartime]] — Broader wartime AI/personnel research note
- [[ukraine-military-specialties-current]] — Current role-family catalog direction
- [[esco-typology-mapping]] — Civilian skills to role-fit mapping
- [[military-profile-sli-elvf-vpnb]] — Example applied profile with caveats
- [[scientific-contribution-statement]] — Research positioning and limitations
