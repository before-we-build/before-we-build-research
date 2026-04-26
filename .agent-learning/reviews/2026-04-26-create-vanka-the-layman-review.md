---
title: Review — Create Vanka the Layman Agent
type: agent-improvement-review
created: 2026-04-26
updated: 2026-04-26
proposal: .agent-learning/proposals/2026-04-26-create-vanka-the-layman.md
status: approved
risk: safe
reviewer: agent-improvement-steward
---

# Review: Create Vanka the Layman Agent

## Decision

Approved for implementation because the user explicitly requested the new agent and the change is additive, narrow, and low-risk.

## Safety risks

- A blunt layperson persona can become insulting if not constrained.
- Simplicity pressure can remove necessary caveats.
- Skepticism can become automatic rejection instead of useful clarity review.

## Required specialist reviews

None for initial creation. Future changes that allow the agent to judge truth, validity, ethics, theology, clinical claims, or typological correctness should be routed to the relevant specialist and/or `empirical-claims-caveats-reviewer`.

## Required safeguards

- Do not mock ordinary people, poverty, or workers.
- Do not remove caveats to make an idea smoother.
- Do not decide whether claims are true.
- Preserve referral to specialists for high-stakes or evidence-sensitive claims.

## Outcome

Implemented as `.opencode/agents/vanka-the-layman.md` and added to master-orchestrator routing.
