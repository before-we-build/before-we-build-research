---
title: Replace Premature Compatibility Scoring Roles
type: agent-improvement-proposal
created: 2026-08-30
updated: 2026-08-30
status: approved
risk: moderate
target_agents: [compatibility-calculator, scoring-calibration-researcher, master-orchestrator, research-orchestrator]
required_reviewers: [human-project-owner, psychometrics-methodologist, statistical-validation-agent, empirical-claims-caveats-reviewer]
sources: [user-approved-repository-clarity-plan-2026-08-30, AGENTS.md]
---

# Agent Improvement Proposal: Replace Premature Compatibility Scoring Roles

## 1. Target agents

- `.opencode/agents/compatibility-calculator.md`
- `.opencode/agents/scoring-calibration-researcher.md`
- routing instructions that name either role

## 2. Observed failure

The calculator prescribes unsupported percentages such as 95–100% for a
Socionics relation and a weighted final score. The calibration role asks for
weights and thresholds before the project has defined and validated an
outcome-specific compatibility construct. This creates false precision and
contradicts the approved epistemic policy.

## 3. Evidence

- The project owner explicitly approved removing percentages, high/low scores,
  weights, ranking formulas, and claims of computable pair success.
- The current repository contains no validated human outcome model that could
  justify those numbers.
- `AGENTS.md` requires typological mappings to remain heuristic,
  non-deterministic research hypotheses.

## 4. Approved instruction change

- Replace `compatibility-calculator` with
  `compatibility-conversation-mapper`, which produces a qualitative,
  context-specific evidence map and conversation questions.
- Replace `scoring-calibration-researcher` with
  `compatibility-measurement-researcher`, which specifies construct,
  reliability, calibration, validation, uncertainty, and safety prerequisites
  without proposing a current score.
- Update active routing instructions and organization documentation.
- Prohibit score, ranking, destiny, moral-worth, and automatic partner verdicts.

## 5. Risk assessment

- Risk level: `moderate`
- Could this increase overclaiming? `no`; it removes false precision.
- Could this bypass specialist delegation? `no`; psychometrics, statistics,
  ethics, and domain specialists remain required.
- Could this affect high-stakes advice? `yes`; the change strengthens safety
  and prohibits automated relationship verdicts.

## 6. Reviewers

- [x] Human/project owner — explicitly approved the repository-wide plan.
- [x] Psychometrics/statistics policy — no measure before construct and outcome
  validation.
- [x] Empirical claims policy — unsupported precision is removed.
- [x] Safety policy — coercion and abuse remain gates, not score components.

## 7. Acceptance criteria

- [x] No active agent fabricates a BWB compatibility percentage.
- [x] Compatibility explanations are qualitative and outcome-specific.
- [x] Measurement work is framed as a future validation program.
- [x] Type never determines morality, dignity, safety, or destiny.
- [x] All active routing references use the replacement roles.

## 8. Rollback

Restore the old roles from Git history only if a later human-validated outcome
model, calibration dataset, and governance review explicitly authorize a
production score.
