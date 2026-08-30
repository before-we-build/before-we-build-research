---
title: Make All Typing Output Provisional and Evidence-Bounded
type: agent-improvement-proposal
created: 2026-08-30
updated: 2026-08-30
status: approved
risk: high
target_agents: [master-orchestrator, typing-lead, psychosophy-test-typer, psychosophy-quick-typer, psychosophy-interview-typer, typology-researcher]
required_reviewers: [human-project-owner, ethics-and-consent-reviewer, psychometrics-methodologist, empirical-claims-caveats-reviewer]
sources: [user-approved-repository-clarity-plan-2026-08-30, AGENTS.md]
---

# Agent Improvement Proposal: Provisional Typing Output

## Observed failure

Active instructions treated unvalidated rankings and response totals as sufficient to establish a Psychosophy type. Public-figure guidance encoded project-specific cognitive interpretations as strict mechanisms and used moral or military behavior as type evidence.

## Approved instruction change

- Distinguish direct observations and instrument scores from interpretation.
- Label every proposed type as an unvalidated research hypothesis, never an identity fact.
- Require at least two rival explanations and explicit disconfirming evidence.
- Do not convert a confidence adjective into psychometric certainty; describe evidence quality and method limits instead.
- Prohibit inference to morality, dignity, diagnosis, safety, career or military suitability, private belief, or relationship outcome.
- Treat code and pseudonym registries as nomenclature validation only, not validation that a person has a type.

## Risk assessment

Risk is `high` because public-person profiling and high-stakes role inferences can cause reputational, occupational, safety, and epistemic harm. The change reduces authority and does not introduce a replacement diagnostic model.

## Acceptance criteria

- [x] Test, quick, and interview agents return provisional hypotheses with alternatives and limitations.
- [x] Public-figure protocol separates observation, attribution, and interpretation.
- [x] No typing instruction uses moral, clinical, career, or military evidence as a deterministic marker.
- [x] Instrument scores remain separable from pair compatibility.

## Rollback

Do not restore verdict-style typing. Any future validated classification procedure requires construct validation, reliability, measurement-invariance and calibration evidence, independent review, and explicit owner approval.
