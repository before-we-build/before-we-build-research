---
title: Typology Test Evaluation Protocol / Expert Routing
type: agent-improvement-proposal
created: 2026-04-25
updated: 2026-04-25
status: applied
risk: high-risk
target_agents: [typology-test-evaluation-expert]
required_reviewers: [psychometrics-methodologist, statistical-validation-agent, empirical-claims-caveats-reviewer]
sources: [AGENTS.md, user-request, typology-test-design-protocol]
---

# Improvement Proposal: Typology Test Evaluation Protocol / Expert Routing

## Target agent(s)

Potentially affected:

- master/orchestrator agent routing behavior
- `psychometrics-methodologist`
- `statistical-validation-agent`
- `scoring-calibration-researcher`
- `empirical-claims-caveats-reviewer`
- possible future `typology-test-evaluation-expert` or `psychometric-item-bank-steward`

## Observed Failure or Opportunity

The user noted that PsyCalc currently lacks its own typology tests and asked whether there is an expert for tests or whether each typology needs a separate test expert.

Current risk:

- typology test outputs may be treated as stronger evidence than warranted;
- agents may answer test-design questions without routing to psychometric/statistical expertise;
- separate test experts per typology could duplicate responsibilities and fragment validity standards;
- users may interpret questionnaires as definitive type assignment tools.

## Evidence / Source for the Finding

Conversation context on 2026-04-25:

- User asked whether PsyCalc has typology tests and whether separate experts are needed per typology.
- Expert review recommended one shared psychometric pipeline plus domain experts for Socionics, Psychosophy, and Temporistics.

Governance source:

- `AGENTS.md` Agent Self-Improvement Workflow: agent instruction changes require controlled proposal/review before modifying `.opencode/agents/*.md`.

## Proposed Action

Do **not** add per-typology test agents.

First action already created:

- Document a wiki protocol: `wiki/concepts/typology-test-design-protocol.md`.

Future routing rule, not applied in this patch:

1. Treat typology tests as heuristic instruments, not validated diagnostic tools unless empirical validation exists.
2. Route construct validity, item design, scale wording, and interpretation limits to `psychometrics-methodologist`.
3. Route scoring weights, calibration, predictive accuracy, validation datasets, and outcome metrics to `statistical-validation-agent` or `scoring-calibration-researcher`.
4. Route typology-specific content review to the relevant system expert:
   - `socionics-researcher`
   - `psychosophy-researcher`
   - `temporistics-researcher`
5. Route overclaiming and public interpretation language to `empirical-claims-caveats-reviewer`.
6. Require ethics review if tests collect personal data or affect recommendations.

## Future Instruction Change Sketch

Optionally add to relevant orchestrator/routing instructions later after separate approval:

```markdown
## Typology Test Requests

For requests involving typology tests, questionnaires, item design, score interpretation, reliability, validity, or calibration:

- Do not treat test scores as definitive type assignments.
- Route construct-validity, item-design, and interpretation questions to `psychometrics-methodologist`.
- Route scoring, weighting, calibration, validation datasets, and predictive accuracy questions to `statistical-validation-agent` or `scoring-calibration-researcher`.
- Route system-specific content validity to the relevant Socionics, Psychosophy, or Temporistics expert.
- Route personal-data or opportunity-affecting deployments to `ethics-and-consent-reviewer`.
- Use calibrated uncertainty language.
- Avoid exact confidence percentages unless supported by validation data.
- If evidence is anecdotal, simulated, or project-internal, label it accordingly.
```

## Applied Agent

After explicit user request, create one dedicated coordination agent:

- `typology-test-evaluation-expert`

Purpose:

- coordinate review of typology questionnaires and item banks;
- ensure domain review + psychometric review + statistical validation + caveat review are all completed;
- prevent overinterpretation of test outputs.

This agent must not replace psychometrics, statistics, caveat, ethics, or domain experts.

Applied file:

- `.opencode/agents/typology-test-evaluation-expert.md`

## Risk Level

High-risk.

Reason: this affects construct validity, typing methods, score interpretation, empirical claims, and user trust in test results.

## Required Reviewers

- `psychometrics-methodologist`
- `statistical-validation-agent` or `scoring-calibration-researcher`
- `empirical-claims-caveats-reviewer`

Optional reviewers:

- `source-provenance-auditor` if citation/evidence labels are changed;
- `ethics-and-consent-reviewer` if tests collect or use participant data;
- domain experts for Socionics, Psychosophy, and Temporistics if item banks are created.

## Acceptance Criteria

- Typology-test requests are routed to psychometric/statistical specialists.
- Agents do not overclaim validity of test scores.
- Exact confidence percentages are avoided unless calibrated.
- Test outputs are framed as hypotheses, not final type determinations.
- Domain experts review content validity for each typology.
- Ethics review is triggered for personal data collection or opportunity-affecting uses.
- Delegation-first architecture is preserved.

## Rollback Note

If the new routing rule causes over-routing or slows simple user-facing explanations, revert the agent-routing change and keep only the wiki protocol page describing typology-test caveats.
