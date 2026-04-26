---
title: Create Visual Explainer Agent
type: agent-learning-log
created: 2026-04-26
updated: 2026-04-26
source: user-request
status: implemented
---

# Learning Log: Create Visual Explainer Agent

## Trigger

The user explicitly requested creation of a new specialized expert agent called **Visual Explainer**.

## Observation

The existing explanation team contains plain-language, presentation, storyboard, and social-content agents, but lacks a dedicated information-design / explainer-illustration agent focused on translating complex ideas into simple visual metaphors, drawings, infographics, and storyboard concepts.

## Decision

This is a low-risk additive agent instruction change. It does not alter existing agent authority, weaken caveats, or add claims about typology, science, theology, clinical matters, or role-fit. The new agent is constrained to visual explanation and must preserve caveats for Christian, scientific/psychological, and technical topics.

## Action

- Create `.opencode/agents/visual-explainer.md`.
- Create a matching proposal record under `.agent-learning/proposals/`.
- Create a lightweight review record under `.agent-learning/reviews/` documenting safe implementation.

## Follow-up

Future audits should verify that the agent simplifies visual concepts without turning hypotheses into facts, manipulating religious audiences, or hiding technical uncertainty behind polished metaphors.
