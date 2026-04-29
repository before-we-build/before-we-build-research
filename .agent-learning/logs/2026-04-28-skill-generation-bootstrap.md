# Skill Generation Bootstrap

Date: 2026-04-28
Actor: master-orchestrator
Type: controlled self-improvement scaffold

## Observation

The user asked whether PsyCalc agents can support skill autocreation / skill generation / automaticity: reusable procedural knowledge generated from repeated tasks and interaction history.

## Decision

Set up a controlled skill-generation scaffold that permits agents to draft reusable skills but does not permit silent activation or self-modification.

Core rule:

```text
Auto-draft is allowed.
Auto-apply requires explicit human approval.
```

## Changes made

Created or updated:

- `.agent-learning/README.md`
- `.agent-learning/skill-generation-policy.md`
- `.agent-learning/templates/skill-draft.md`
- `.agent-learning/templates/skill-review.md`
- `.agent-learning/skill-drafts/wiki-frontmatter-audit.md`
- `.agent-learning/proposals/2026-04-28-create-skill-generation-loop.md`

Created directories:

- `.agent-learning/skill-drafts/`
- `.agent-learning/approved-skills/`

## Safety notes

- No `.opencode/agents/*.md` instructions were changed.
- No draft skill was activated.
- The initial skill draft is low-risk and limited to wiki frontmatter/schema checks.
- Future high-risk skill drafts require specialist review.

## Next steps

1. Review the proposal and policy.
2. If approved, move selected drafts to `.agent-learning/approved-skills/`.
3. If runtime skill support is added later, connect approved skills explicitly and record the activation.
