---
title: Self-Improvement Bootstrap Log
type: agent-learning-log
created: 2026-04-25
updated: 2026-04-25
sources: [Hermes Agent README, repository audit results, AGENTS.md]
---

# Self-Improvement Bootstrap Log

## Trigger

User asked whether the PsyCalc agent system can adopt a Hermes-style self-improvement loop for local `.opencode/agents/*.md` agents.

## Decision

Implement a controlled self-improvement loop rather than silent autonomous agent self-modification.

## Implemented artifacts

- `.opencode/agents/agent-improvement-steward.md`
- `.agent-learning/README.md`
- `.agent-learning/templates/improvement-proposal.md`
- `.agent-learning/templates/review-checklist.md`
- `.agent-learning/logs/`
- `.agent-learning/proposals/`
- `.agent-learning/reviews/`

## Governance rule

Agent instruction changes should follow:

```text
Experience / audit finding
→ learning log entry
→ improvement proposal
→ specialist review if needed
→ human approval or explicit implementation request
→ patch to agent instructions
→ post-change verification
```

## Initial improvement opportunities from audit results

1. Harden system experts against source/reconstruction drift.
2. Harden applied agents against deterministic percentages and high-stakes recommendations.
3. Normalize evidence labels and provenance rules in wiki governance agents.
4. Route self-improvement requests to `agent-improvement-steward` through `master-orchestrator`.

## Status

Bootstrap implemented. Initial proposals can now be stored in `.agent-learning/proposals/` and reviewed before broad agent rewrites.
