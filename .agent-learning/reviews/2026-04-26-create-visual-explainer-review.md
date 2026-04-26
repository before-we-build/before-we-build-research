---
title: Review — Create Visual Explainer Agent
type: agent-improvement-review
created: 2026-04-26
updated: 2026-04-26
proposal: .agent-learning/proposals/2026-04-26-create-visual-explainer.md
status: approved
risk: safe
reviewer: agent-improvement-steward
---

# Review: Create Visual Explainer Agent

## Decision

Approved for implementation because the user explicitly requested the new agent and the change is additive, narrow, and low-risk.

## Safety risks

- Visual metaphors can oversimplify hypotheses into apparent facts.
- Religious visuals can become manipulative if designed for emotional pressure rather than respectful explanation.
- Technical metaphors can hide architectural details if not paired with a reality check.

## Required specialist reviews

None for initial creation. Future changes that make the agent assert domain claims should be routed to the relevant specialist and/or `empirical-claims-caveats-reviewer`.

## Required safeguards

- Preserve scientific/psychological caveats.
- Use respectful, non-manipulative handling for Christian topics.
- For technical topics, explain metaphor first, then distinguish the actual architecture.
- Do not use polished visuals to imply certainty, validation, guaranteed outcomes, or authority not present in the source concept.

## Outcome

Implemented as `.opencode/agents/visual-explainer.md`.
