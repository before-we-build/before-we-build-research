---
title: Create Responsive UI & Design Systems Expert Agent
type: agent-learning-log
created: 2026-04-26
updated: 2026-04-26
source: user-request
status: implemented
---

# Learning Log: Create Responsive UI & Design Systems Expert Agent

## Trigger

The user explicitly requested creation of a new specialized expert agent called **Responsive UI & Design Systems Expert** based on their provided prompt.

## Observation

The existing agent set includes presentation, visual explanation, and data/operations specialists, but lacks a dedicated frontend UI specialist focused on responsive layout, mobile adaptation, design systems, component libraries, spacing, typography, accessibility, and frontend visual consistency.

## Decision

This is a low-risk additive agent instruction change. It does not alter existing agent authority, weaken caveats, or add claims about typology, science, clinical matters, theology, or role-fit. The new agent is constrained to frontend UI analysis and implementation guidance.

## Action

- Create `.opencode/agents/responsive-ui-design-systems-expert.md`.
- Create a matching proposal record under `.agent-learning/proposals/`.
- Create a lightweight review record under `.agent-learning/reviews/` documenting safe implementation.

## Follow-up

Future audits should verify that the agent remains technology-flexible, accessibility-aware, and focused on clear, usable, maintainable responsive interfaces rather than decorative polish alone.
