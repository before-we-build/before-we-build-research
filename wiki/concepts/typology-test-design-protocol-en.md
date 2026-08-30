---
title: Typology Test Design Protocol
type: concept
tags: [methodology, psychometrics, validation, typology-tests, socionics, psychosophy, temporistics]
created: 2026-04-25
updated: 2026-04-25
sources: [wiki/concepts/validation-program-en.md, wiki/concepts/compatibility-measurement-roadmap-en.md, wiki/sources/psychosophy-typing-methods-en.md, .agent-learning/proposals/2026-04-25-typology-test-evaluation-protocol.md]
lang: en
translation_group: typology-test-design-protocol
semantic_version: 3
reviewed_semantic_version: 3
document_status: active
page_role: research-appendix
claim_status: [research-hypothesis]
claims: []
caveat_ids: []
---

# Typology Test Design Protocol

<!-- section:purpose -->
## Purpose

This protocol defines how Before We Build should design, review, validate, and interpret typology-based instruments for Socionics, Psychosophy, and Temporistics.

The target “type” is a model hypothesis about perception and experience organization, not a personality type. A proposed natural predisposition is a separate unvalidated hypothesis. See [[typology-reconceptualization-en]].

It exists because typology tests can easily become overconfident: a questionnaire may look precise while measuring social desirability, community stereotypes, verbal style, mood, or prior self-typing rather than the intended construct.

The goal is to build instruments that translate typological hypotheses into measurable constructs while preserving empirical caution.

<!-- section:scope -->
## Scope

This protocol applies to:

- self-report questionnaires;
- observer-rating forms;
- interview coding schemes;
- scenario-based tests;
- behavioral task proposals;
- hybrid typing instruments.

It does not assume that traditional type categories are already valid. Validation must occur at the level of constructs, scales, profiles, and decision rules.

A score produced by an individual typology instrument is not a compatibility score for a pair. It may summarize response evidence for a construct or type hypothesis only; it cannot be converted into a pair verdict without a separately defined and validated outcome model, which Before We Build does not currently have.

<!-- section:before-we-build-construct-frame -->
## Before We Build Construct Frame

All test design should preserve the project's three-system framing:

- **Socionics** → latent processes of selecting, compressing, inferring from, and updating partial models of one shared reality;
- **Psychosophy** → latent processes of synthesis and analysis in action;
- **Temporistics** → latent processes of abduction, induction, and deduction in temporal/existential experience.

These mappings are working hypotheses, not established psychological facts.

Socionics instruments must keep aspect-operation evidence separate from Model A position-mode evidence, cover selection, compression, inference, and updating, and treat self-report as auxiliary. The system-specific design is defined in [[socionics-test-specification-en]] and [[socionics-reality-modeling-en]].

<!-- section:recommended-expert-routing -->
## Recommended Expert Routing

Before We Build should use one shared psychometric pipeline rather than separate psychometric experts for each typology.

| Role | Responsibility |
|------|----------------|
| Domain expert | Defines the typology-specific construct and checks theory fidelity |
| Psychometrics methodologist | Converts constructs into measurable variables and reviews item quality |
| Statistical validation agent | Tests reliability, dimensionality, calibration, uncertainty, and invariance |
| Empirical claims caveat reviewer | Prevents overclaiming and deterministic interpretation |
| Ethics reviewer | Required when real participant data, sensitive use, or recommendations are involved |

Domain experts include:

- [[socionics-overview-en]] / Socionics researcher for information-modeling constructs;
- [[psychosophy-overview-en]] / Psychosophy researcher for action-priority constructs;
- [[temporistics-model-en]] / Temporistics researcher for temporal/existential constructs.

<!-- section:why-not-separate-test-experts-per-typology -->
## Why Not Separate Test Experts Per Typology

Separate test experts for each system are not the first choice because psychometric quality standards are shared across systems:

- construct definition;
- item clarity;
- reliability;
- validity;
- invariance;
- calibration;
- bias control;
- uncertainty reporting.

The better structure is:

- **centralized psychometric standards**;
- **distributed domain review** for Socionics, Psychosophy, and Temporistics.

For recurring test and item-bank review, Before We Build uses `typology-test-evaluation-expert` as a coordinating safety layer. It does not replace the psychometrics, statistics, caveats, ethics, or domain-specific experts. A future `psychometric-item-bank-steward` may still be proposed if item-bank maintenance becomes a large recurring workload.

<!-- section:core-design-principles -->
## Core Design Principles

- Measure latent constructs, not lore labels.
- Prefer observable tendencies over identity statements.
- Separate theory-informed hypotheses from validated findings.
- Avoid deterministic claims about personality, compatibility, role fit, or life outcomes.
- Treat type assignment as model-based inference, not direct observation.
- Preserve dimensional scores before deriving categories.
- Avoid exact confidence percentages unless calibrated against validation data.

<!-- section:construct-definition-template -->
## Construct Definition Template

Each proposed scale or subscale should document:

1. **Construct being measured**
   - plain-language definition;
   - typology source system;
   - expected manifestations;
   - plausible opposites or neighboring constructs.

2. **Why it matters**
   - theoretical role in Before We Build;
   - expected relation to profiles, behavior, compatibility, or role-fit hypotheses.

3. **Observable indicators**
   - recurring choices;
   - attentional patterns;
   - decision habits;
   - narrative style;
   - interaction patterns.

4. **Exclusions**
   - what the construct is not;
   - adjacent constructs likely to contaminate measurement.

<!-- section:item-writing-rules -->
## Item Writing Rules

Items should:

- describe concrete tendencies or recurring patterns;
- avoid typology jargon where possible;
- avoid prestige-loaded wording;
- avoid forcing identification with a type narrative;
- avoid double-barreled statements;
- avoid metaphysical certainty claims;
- avoid obvious “I am type X” cueing;
- be understandable across languages and educational backgrounds.

<!-- section:item-review-checklist -->
## Item Review Checklist

Every item should be reviewed for:

- construct contamination;
- acquiescence bias;
- social desirability bias;
- reading complexity;
- translation difficulty;
- self-typing cueing;
- excessive abstraction;
- cultural loading;
- emotional valence imbalance.

<!-- section:recommended-item-mix -->
## Recommended Item Mix

Use multiple formats where possible:

- direct self-report items;
- scenario-based items;
- forced-tradeoff items where justified;
- observer-report variants for externally visible tendencies;
- interview prompts;
- optional behavioral indicators if feasible.

No single item format should be treated as sufficient for final type inference.

<!-- section:item-lifecycle -->
## Item Lifecycle

1. **Theory extraction** — convert typological claims into candidate latent constructs.
2. **Operational definition** — specify what would count as evidence for the construct.
3. **Initial item pool** — create broad, redundant item coverage.
4. **Expert review** — domain + psychometric review for wording, theory alignment, and contamination.
5. **Cognitive pretesting** — interview participants about comprehension and response process.
6. **Pilot study** — estimate distributions, missingness, variance, and basic dimensionality.
7. **Item reduction** — remove weak, redundant, unstable, or ambiguous items.
8. **Validation study** — test reliability, structure, convergent/discriminant validity, and decision rules.
9. **Replication** — re-test in new samples, contexts, languages, and modes.
10. **Ongoing monitoring** — track drift, subgroup bias, calibration decay, and misuse.

<!-- section:recommended-measurement-architecture -->
## Recommended Measurement Architecture

Preferred order:

1. Build construct scales first.
2. Derive profiles second.
3. Infer type-like classifications last, if justified.

This prevents the system from forcing weak dimensional evidence into rigid type categories too early.

<!-- section:validation-framework -->
## Validation Framework

<!-- section:reliability-checks -->
### Reliability Checks

- internal consistency where appropriate;
- test-retest stability;
- inter-rater reliability for observer/coder instruments;
- alternate-form checks if parallel item sets are used.

<!-- section:validity-checks -->
### Validity Checks

- **Content validity:** expert mapping of items to constructs;
- **Convergent validity:** relation to nearby measures where theoretically expected;
- **Discriminant validity:** separation from mood, status, verbal style, social desirability, broad traits, and ideology;
- **Criterion validity:** relation to relevant behaviors or judgments;
- **Predictive validity:** cautious testing of future outcomes where justified.

<!-- section:structural-checks -->
### Structural Checks

- dimensionality / factor structure;
- item discrimination;
- local dependence;
- subgroup functioning;
- calibration stability across samples.

<!-- section:invariance-checks -->
### Invariance Checks

Test across:

- language;
- culture;
- gender;
- age;
- testing context;
- self-report vs observer-report mode.

<!-- section:threats-to-validity -->
## Threats to Validity

Common threats include:

- circular validation against prior type assignments;
- construct contamination from Big Five-like traits, intelligence, status, mood, or ideology;
- self-typing bias from participant familiarity with typology systems;
- demand characteristics in typology communities;
- overfitting small enthusiast samples;
- translation drift across languages;
- category inflation from weak dimensional evidence.

<!-- section:interpretation-rules -->
## Interpretation Rules

- Report findings as evidence for measured tendencies, not proof of fixed essence.
- Do not describe classifications as clinical diagnoses.
- Do not infer compatibility outcomes without direct criterion studies.
- Do not collapse low-validity scales into high-confidence type labels.
- Do not use test scores as the sole basis for high-stakes recommendations.
- Label evidence status: source-backed, expert hypothesis, pilot finding, validation finding, or speculation.

<!-- section:minimum-evidence-threshold-before-public-use -->
## Minimum Evidence Threshold Before Public Use

Before operational deployment, require:

- documented construct definitions;
- pilot-tested item pool;
- acceptable reliability;
- at least one independent validation sample;
- caveat-reviewed interpretation language;
- ethics review if personal data are collected or if results affect recommendations.

<!-- section:ethics-requirements -->
## Ethics Requirements

Ethics review is required when a test collects real participant data or is used for matching, career, military, dating, team, or other opportunity-affecting recommendations.

Minimum requirements:

- informed consent;
- data minimization;
- deletion and retention policy;
- separation of raw and derived data;
- no hidden profiling;
- no sensitive inference without explicit review;
- no deterministic or punitive use of typology results.

<!-- section:recommended-next-steps -->
## Recommended Next Steps

1. Define construct maps for Socionics, Psychosophy, and Temporistics.
2. Build broad item banks without typology jargon.
3. Run expert domain review.
4. Run psychometric item review.
5. Conduct cognitive interviews.
6. Pilot with heterogeneous samples.
7. Test dimensional structure and reliability.
8. Evaluate convergent/discriminant validity.
9. Test invariance across languages and groups.
10. Only then evaluate classification usefulness.

<!-- section:see-also -->
## See Also

- [[validation-program-en]] — Overall validation framework
- [[compatibility-measurement-roadmap-en]] — Prerequisites for any future pair measure
- [[psychosophy-typing-methods-en]] — Existing psychosophy typing methods note
- [[socionics-model-a-en]] — Socionics Model A hub
- [[afanasyev-model-en]] — Psychosophy model structure
- [[temporistics-model-en]] — Temporistics model structure
- [[epistemic-status-and-inference-limits-en]] — Research positioning and inference limits
