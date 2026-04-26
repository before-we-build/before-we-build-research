---
title: Biblical Claim Audit Skill for Baptist Pastor
type: agent-learning-log
created: 2026-04-26
updated: 2026-04-26
source: user-request
status: implemented
---

# Learning Log: Biblical Claim Audit Skill for Baptist Pastor

## Trigger

The user requested creation or activation of a skill for the `baptist-pastor` agent called **Biblical Claim Audit**.

## Observation

The existing `baptist-pastor` agent already includes Scripture-grounded Baptist review, anti-proof-texting guidance, Baptist diversity caveats, and pastoral safety boundaries. It does not yet have a dedicated reusable audit workflow for extracting individual biblical/theological claims, checking them against Scripture in context, assigning verdicts, and rewriting unsafe wording.

## Decision

This belongs in a skill file plus a narrow activation note in the agent instructions. Because the change is in a theological/pastoral domain, it requires an auditable proposal and theological safety review. The skill should be safety-enhancing rather than more assertive: it must preserve context, avoid proof-texting, distinguish Scripture from Baptist interpretation and opinion, and recommend `christian-theology-researcher` or local pastoral review for disputed/high-stakes claims.

## Action

- Created proposal `.agent-learning/proposals/2026-04-26-biblical-claim-audit-skill.md`.
- Created review `.agent-learning/reviews/2026-04-26-biblical-claim-audit-skill-review.md`.
- Added `.opencode/skills/biblical-claim-audit.md`.
- Added a narrow activation section to `.opencode/agents/baptist-pastor.md`.

## Follow-up

Future audits should verify that the skill extracts claims faithfully, avoids proof-texting, labels Baptist interpretation distinctly from direct biblical teaching, and does not replace local pastoral counsel or specialist theological review.
