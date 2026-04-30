---
title: Create Copyright Licensing Reviewer Agent
type: agent-learning-log
created: 2026-04-30
updated: 2026-04-30
source: user-request
status: applied
---

# Learning Log: Create Copyright Licensing Reviewer Agent

## Trigger

The user requested an agent “lawyer” to automatically handle legal checking for publication/republication of sources in the PsyCalc wiki.

## Observation

The repository has wiki ingestion, source provenance, caveat, and ethics agents, but no narrow publication-rights reviewer for copyright, licensing, attribution, fair use/fair dealing risk, source excerpts, or web/PDF republication risk.

## Decision

Create a **narrow non-lawyer risk-screening agent**, not a broad legal advisor. The agent must explicitly state that it is not a lawyer and does not replace licensed legal counsel. Data/privacy issues should be secondary routing to `ethics-and-consent-reviewer`, not the agent’s primary domain.

Risk level is `moderate`: it touches legal-risk triage, but the patch adds caveats, narrows scope, and increases delegation rather than making definitive legal claims.

## Action

- Created `.opencode/agents/copyright-licensing-reviewer.md`.
- Updated `.opencode/agents/master-orchestrator.md` routing for source publication/republication rights checks.
- Updated `.opencode/ORGANIZATION.md` Wiki Team listing.
- Created proposal `.agent-learning/proposals/2026-04-30-create-copyright-licensing-reviewer.md` with status `applied` because the user explicitly requested implementation.

## Follow-up

Recommended review by `source-provenance-auditor`, `ethics-and-consent-reviewer`, and a human/project owner. For contested or high-value publication decisions, consult licensed legal counsel.
