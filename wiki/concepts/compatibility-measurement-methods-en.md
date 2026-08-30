---
title: Compatibility Measurement Methods
type: concept
tags: [measurement, psychometrics, research-appendix]
created: 2026-08-30
updated: 2026-08-30
lang: en
translation_group: compatibility-measurement-methods
semantic_version: 1
reviewed_semantic_version: 1
document_status: active
page_role: research-appendix
claim_status: [application-guidance, project-definition]
claims:
  - id: model-form-follows-outcome
    status: application-guidance
  - id: no-usable-bwb-measurement-model
    status: project-definition
caveat_ids: [abstract-methods-only, no-coefficients, validation-before-use]
sources: [AGENTS.md]
---

# Compatibility Measurement Methods

English · [[compatibility-measurement-methods-ru|Русский]] · [[compatibility-measurement-methods-uk|Українська]]

<!-- section:in-90-seconds -->
## In 90 seconds

This appendix describes possible research model families without selecting a BWB formula. No coefficients, weights, cut-offs, or operational compatibility score are proposed.

<!-- section:definition-and-scope -->
## Model families

- Descriptive profiles preserve multiple outcomes without aggregation.
- Gate models represent conditions that must not be traded away.
- Additive models represent compensable contributions only when that meaning is justified.
- Interaction models test whether the effect of one feature depends on another.
- Longitudinal models represent change, feedback, and time-to-event outcomes.

Model choice follows the construct and decision, not convenience.

<!-- section:shared-example -->
## Shared example

In relocation research, factual accuracy and burden balance might be separate continuous outcomes, while freely given consent is a gate. Treating consent as a small additive contribution would change the moral meaning of the model and is therefore unacceptable.

<!-- section:observations -->
## Measurement pipeline

Specify construct → write indicators → review content validity → pilot cognitively → estimate reliability → test factor structure and invariance → validate against external criteria → calibrate on separate data → test on held-out and external samples → monitor drift and harm.

<!-- section:hypotheses -->
## Statistical questions

Estimate measurement error, base rates, missingness, dependence within pairs, non-linearity, interactions, temporal stability, and calibration. Use cross-validation or preregistered hold-out data and report uncertainty intervals, not only discrimination.

<!-- section:alternatives -->
## Rejection and simplification

Reject or simplify a model when indicators are unreliable, factors are unstable, subgroup comparability fails, a simpler baseline performs similarly, calibration fails, replication fails, or use creates unacceptable harm.

<!-- section:non-inferences -->
## Prohibited shortcuts

Do not turn ordinal categories into precise distances without evidence, fit weights to the development sample and call them validated, infer pair outcomes from separate individual totals, optimize engagement as relationship success, or average away a safety gate.

<!-- section:conversation-questions -->
## Design review questions

- What decision would this model affect?
- Is aggregation meaningful for every included variable?
- Which groups bear false-positive and false-negative costs?
- Can a qualitative profile answer the question more honestly?

<!-- section:researcher-route -->
## Reporting contract

Report provenance, sample, exclusions, missingness, instrument version, reliability, validity, calibration, uncertainty, subgroup performance, replication status, intended use, prohibited use, and known harms.

<!-- section:next-reading -->
## Next reading

Return to [[compatibility-measurement-roadmap-en]] and [[validation-program-en]].
