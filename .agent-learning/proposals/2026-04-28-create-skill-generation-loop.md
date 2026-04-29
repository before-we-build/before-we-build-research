# Improvement Proposal: Create Controlled Skill Generation Loop

Date: 2026-04-28
Status: proposed / partially implemented as governance scaffolding
Proposed by: master-orchestrator
Related log: `.agent-learning/logs/2026-04-28-skill-generation-bootstrap.md`

## Summary

Add a controlled skill-generation workflow so agents can draft reusable procedures from repeated tasks without silently changing active behavior.

## Problem

Agents can repeat similar procedures across sessions, but without durable written workflows they may repeat old mistakes. At the same time, allowing agents to automatically activate new skills would create unsafe silent self-modification.

## Proposed change

Create governance artifacts for skill generation:

- `.agent-learning/skill-generation-policy.md`
- `.agent-learning/skill-drafts/`
- `.agent-learning/approved-skills/`
- `.agent-learning/templates/skill-draft.md`
- `.agent-learning/templates/skill-review.md`

Use the rule:

```text
Auto-draft is allowed.
Auto-apply requires explicit approval.
```

## Initial low-risk pilot

Create inactive draft skill:

- `.agent-learning/skill-drafts/wiki-frontmatter-audit.md`

This pilot focuses only on wiki structure and metadata, not truth validation.

## Risks

- Agents may treat drafts as active instructions.
- Agents may overgeneralize from generated outputs.
- A skill could accidentally replace specialist review.
- High-risk domain knowledge could be proceduralized too aggressively.

## Guardrails

- Drafts are inactive until approved.
- Approved skills still require runtime connection before use.
- High-risk skills require specialist review.
- Skills must include when-not-to-use rules and forbidden shortcuts.
- Skills must preserve caveats and delegation-first routing.

## Reviewers

For this low-risk governance scaffold: human review is sufficient.

Future high-risk skill drafts should be routed to relevant experts, such as:

- `source-provenance-auditor`
- `empirical-claims-caveats-reviewer`
- `psychometrics-methodologist`
- `statistical-validation-agent`
- system-specific researchers
- clinical, theology, neuroscience, military, or ethics experts as applicable

## Acceptance criteria

- Skill-generation policy exists.
- Draft and approved skill directories exist.
- Draft and review templates exist.
- At least one low-risk inactive skill draft exists.
- README documents that drafts are inactive and auto-apply is forbidden without approval.

## Rollback

Remove or archive the new policy, templates, directories, and draft. No active agent instructions are changed by this proposal.
