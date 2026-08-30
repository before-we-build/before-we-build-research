---
title: Premature Compatibility Scoring Audit
type: agent-improvement-log
created: 2026-08-30
updated: 2026-08-30
status: resolved
---

# Premature compatibility scoring audit

The repository-wide ambiguity review found that active agent instructions
still required invented compatibility percentages, fixed relation rankings,
and calibration weights even though Before We Build has no validated outcome
measure or human calibration dataset.

The project owner explicitly approved removing the current numerical
compatibility model and retaining only a research roadmap for possible future
measurement. This requires coordinated agent changes so that generated output
cannot silently reintroduce the retired score model.

Affected active roles included `compatibility-calculator`,
`scoring-calibration-researcher`, `master-orchestrator`, and specialist routing
rules that delegated compatibility questions to those agents.
