---
title: Typology Test Evaluation Protocol Review
type: agent-improvement-review
created: 2026-04-25
updated: 2026-04-25
status: approved
proposal: 2026-04-25-typology-test-evaluation-protocol.md
reviewers: [psychometrics-methodologist, statistical-validation-agent, empirical-claims-caveats-reviewer]
decision: approved
---

# Typology Test Evaluation Protocol Review

## Proposal Metadata

- Proposal file: `.agent-learning/proposals/2026-04-25-typology-test-evaluation-protocol.md`
- Target agent: `.opencode/agents/typology-test-evaluation-expert.md`
- Date: 2026-04-25
- Decision: `approved`

## Review Summary

### Psychometrics Review

Decision: conditionally acceptable.

The psychometrics review approved a single coordinating test-evaluation agent if it remains a meta-review/orchestration role rather than a definitive typing authority. Required safeguards included:

- treat typologies as heuristic latent-process hypotheses;
- separate theory review, item review, psychometrics, statistics, ethics, caveats, and domain review;
- avoid deterministic claims;
- require construct maps and contamination checks;
- preserve uncertainty and evidence gaps.

These safeguards are included in the agent specification.

### Empirical Claims / Caveats Review

Decision: acceptable with caveats.

The caveats review required the agent to prevent claims such as “this test proves your type,” “scores guarantee fit,” or “the construct is scientifically proven.” It also required:

- provisional interpretation of questionnaire results;
- reliability/validity separation;
- no clinical, diagnostic, compatibility-deterministic, or role-fit-deterministic claims;
- clear uncertainty and alternative explanations.

These safeguards are included in the agent specification.

### Statistical Validation Review

Initial decision: needs changes.  
Final decision after changes: approved.

Required changes were added:

- empirical support required for accuracy, calibration, ranking, or predictive claims;
- “ready for pilot” separated from validation/deployment readiness;
- leakage and circularity red flags added;
- validation review topics added: sample size, split/external validation, missing data, multiple testing, uncertainty intervals;
- operational and public predictive claims blocked when based only on face validity, internal consistency, or small uncontrolled pilots.

## Safety Checks

- [x] Does not make typological hypotheses sound proven.
- [x] Does not introduce deterministic compatibility, dating, career, or military rules.
- [x] Does not reduce medical, theological, public-figure, or military caveats.
- [x] Does not route around relevant specialist agents.
- [x] Does not treat prior LLM output as primary evidence.
- [x] Does not add uncited empirical/neuroscience/psychometric claims.

## Governance Checks

- [x] Consistent with `AGENTS.md` proposal-first self-improvement workflow.
- [x] Agent scope remains clear.
- [x] Reporting line remains research-team aligned.
- [x] Instructions are not duplicated as per-typology test agents.
- [x] High-risk review trail is stored in `.agent-learning/reviews/`.

## Approved Patch Notes

Approved creation of one coordinating agent:

- `.opencode/agents/typology-test-evaluation-expert.md`

Not approved / not applied in this patch:

- per-typology test agents;
- master-orchestrator routing changes;
- any claim that PsyCalc tests are validated.

## Follow-Up Tasks

- Consider master-orchestrator routing update only in a separate proposal if test-evaluation requests become frequent.
- Consider a future `psychometric-item-bank-steward` only if item-bank maintenance becomes a large recurring workload.
