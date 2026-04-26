---
title: Review — Create Responsive UI & Design Systems Expert Agent
type: agent-improvement-review
created: 2026-04-26
updated: 2026-04-26
proposal: .agent-learning/proposals/2026-04-26-create-responsive-ui-design-systems-expert.md
status: approved
risk: safe
reviewer: agent-improvement-steward
---

# Review: Create Responsive UI & Design Systems Expert Agent

## Decision

Approved for implementation because the user explicitly requested the new agent and the change is additive, narrow, and low-risk.

## Safety risks

- UI recommendations can prioritize visual polish over accessibility or usability if not constrained.
- Code suggestions can become too framework-specific if the agent assumes a stack not present in the project.
- Responsive fixes can introduce maintainability problems if they rely on one-off breakpoints and non-reusable CSS.

## Required specialist reviews

None for initial creation. Future changes that expand the agent into high-stakes product claims, empirical UX claims, accessibility compliance certification, or regulated-domain advice should be routed to the relevant specialist and/or `empirical-claims-caveats-reviewer`.

## Required safeguards

- Prioritize clarity, usability, accessibility, and maintainability over decoration.
- Stay technology-flexible and adapt to the existing stack or design system.
- Use testable acceptance criteria and mobile QA checks.
- Do not claim formal accessibility compliance unless audited against the relevant standard.

## Outcome

Implemented as `.opencode/agents/responsive-ui-design-systems-expert.md`.
