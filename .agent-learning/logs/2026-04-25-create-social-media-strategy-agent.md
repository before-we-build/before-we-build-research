---
title: Social Media Strategy Agent Creation
type: agent-learning-log
created: 2026-04-25
updated: 2026-04-25
status: implemented
sources: [AGENTS.md, user-request]
---

# Social Media Strategy Agent Creation

## Observation

The user wants to delegate promotion of PsyCalc / Cognitive Matchmaker across TikTok, YouTube, Instagram, Facebook, X, and Threads to agents rather than manually managing social media strategy.

## Action

Created a dedicated agent specification:

- `social-media-strategy-agent`

## Safeguards

- The agent distinguishes PsyCalc as a research framework from Cognitive Matchmaker as a downstream dating application.
- The agent is instructed not to promise ideal partners, soulmate prediction, deterministic type-based matching, or scientifically proven compatibility.
- The agent routes risky empirical, ethical, sociological, and sensitive-attribute claims to appropriate reviewers.

## Next recommended agents

If the first agent is useful, create in this order:

1. `marketing-claims-safety-reviewer`
2. `short-form-video-scriptwriter`
3. `platform-adaptation-agent`
