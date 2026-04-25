---
title: Typology Test Evaluation Protocol Need
type: agent-learning-log
created: 2026-04-25
updated: 2026-04-25
status: implemented
sources: [AGENTS.md, user-request, typology-test-design-protocol]
---

# Typology Test Evaluation Protocol Need

## Observation

The user noted that PsyCalc does not yet have its own tests for the typologies and asked whether the system has an expert for tests or whether separate experts are needed for each typology.

## Assessment

The safer structure is not to create separate test experts for Socionics, Psychosophy, and Temporistics immediately. Psychometric standards should be centralized, while typology-specific construct review should be delegated to the relevant domain experts.

Recommended routing:

- `psychometrics-methodologist` for construct validity, item design, reliability, and interpretation limits;
- `statistical-validation-agent` or `scoring-calibration-researcher` for calibration, validation data, and uncertainty;
- `socionics-researcher`, `psychosophy-researcher`, and `temporistics-researcher` for content validity;
- `empirical-claims-caveats-reviewer` for overclaim checks;
- `ethics-and-consent-reviewer` when real participant data or opportunity-affecting recommendations are involved.

## Action

Created a wiki protocol page:

- `wiki/concepts/typology-test-design-protocol.md`

Created an improvement proposal for future routing changes:

- `.agent-learning/proposals/2026-04-25-typology-test-evaluation-protocol.md`

After explicit user request to add the necessary agents, created a single coordinating agent:

- `.opencode/agents/typology-test-evaluation-expert.md`

No per-typology test agents were created because psychometric standards should remain centralized and domain-specific content validity should be delegated to existing system experts.

## Safeguards

- Treat typology tests as heuristic instruments unless validated.
- Do not treat test outputs as definitive type assignments.
- Avoid exact confidence percentages unless calibrated.
- Require ethics review for data collection or opportunity-affecting use.
