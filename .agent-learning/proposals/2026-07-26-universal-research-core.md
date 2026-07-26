---
title: Universal Research Core and Application-Layer Boundary
type: agent-improvement-proposal
created: 2026-07-26
updated: 2026-07-26
status: approved
risk: moderate
target_agents: [AGENTS.md]
required_reviewers: [human-project-owner]
sources: [user-feedback-2026-07-26, AGENTS.md, wiki/concepts/four-level-compatibility-architecture.md]
---

# Agent Improvement Proposal: Universal Research Core

## 1. Target

- `AGENTS.md`
- core orientation, compatibility, and methodology pages

## 2. Observed failure or opportunity

The governance text currently defines Before We Build itself as a Christian
conversation project. This conflicts with the owner's intended research
scope: a universal architecture for studying any two people, with Christian
discernment retained as a downstream worldview/domain application.

## 3. Evidence

- Explicit project-owner direction on 2026-07-26.
- Core pages use Christian-specific sources as mandatory inputs for the
  foundational level.
- Existing scope already reaches teams, business, roles, simulation, and
  society, which requires a more general core.

## 4. Proposed instruction change

```md
Before We Build is a universal compatibility research framework for studying
any two people. Its four-level architecture consists of a value-moral
foundation plus strategic, operational, and tactical levels.

Christian relationship discernment is the first developed application and
worldview lens. Core theory pages must remain worldview-capable; Christian
normative claims belong in explicitly Christian application pages.
```

## 5. Risk assessment

- Risk level: `moderate`
- Why: changes repository-wide scope and theological placement.
- Could this increase overclaiming? `no`
- Could this bypass specialist delegation? `no`
- Could this affect high-stakes advice? `yes`, so universal safety gates remain explicit.

## 6. Required reviewers

- [x] human/project owner — explicitly approved the universal research scope
  and the name `ценностно-нравственный уровень`.
- [ ] theology reviewer — optional follow-up for Christian application wording.
- [ ] empirical/ethics reviewer — optional follow-up for operationalizing the
  universal level.

## 7. Patch sketch

- Replace Christian-only core definitions with universal definitions.
- Rename spiritual-moral core terminology to value-moral.
- Preserve Christian pages as a named specialization.
- Update `AGENTS.md`, README, index, core theory, boundaries, and log.

## 8. Acceptance criteria

- [x] The rule is explicit and enforceable.
- [x] Christian specialization is preserved.
- [x] Typology caveats remain unchanged or stronger.
- [x] Safety constraints remain universal and non-negotiable.
- [x] Core pages can describe any pair of people without assuming religion.

## 9. Rollback note

Revert the scope wording while retaining the four-level architecture if the
project owner later decides to make Before We Build itself a confessional
application rather than a universal research framework.
