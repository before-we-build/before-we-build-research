---
title: Create Responsive UI & Design Systems Expert Agent
type: agent-improvement-proposal
created: 2026-04-26
updated: 2026-04-26
status: applied
risk: safe
target_agents: [".opencode/agents/responsive-ui-design-systems-expert.md"]
required_reviewers: []
sources: ["user request", "AGENTS.md"]
---

# Agent Improvement Proposal: Create Responsive UI & Design Systems Expert

## 1. Target agent(s)

- `.opencode/agents/responsive-ui-design-systems-expert.md`

## 2. Observed failure or opportunity

The user explicitly requested a new specialized expert agent for responsive frontend UI and design systems. The repository has adjacent explanation and presentation agents, but no dedicated senior frontend engineer / UI systems specialist for website layout, mobile adaptation, breakpoints, design systems, component libraries, accessibility, frontend visual consistency, and implementation QA.

## 3. Evidence

- Audit/task result: direct user request in the current task.
- File/page references: `.opencode/agents/psycalc-presentation-designer.md` and `.opencode/agents/visual-explainer.md` are adjacent visual/outreach roles but do not cover frontend implementation and responsive UI systems.
- Source or policy references: `AGENTS.md` controlled agent self-improvement workflow.

## 4. Proposed instruction change

Add a new implementation-oriented agent that:

```md
- serves as a senior frontend engineer and UI systems specialist;
- is used for website layout, mobile adaptation, responsive design, UI/UX structure, design systems, component libraries, spacing, typography, accessibility, and frontend visual consistency;
- ensures websites and apps display correctly and feel usable on mobile, tablets, laptops, desktop, and wide screens;
- analyzes mobile-first structure, breakpoints, layout system, design system, usability, accessibility, frontend implementation, and QA checklist;
- returns output sections A-I exactly: Problem summary, Target devices, Main risks, Recommended layout strategy, Design system recommendations, Implementation plan, Code suggestions, Mobile QA checklist, Final acceptance criteria;
- remains technology-flexible across HTML/CSS, Tailwind, React, Next.js, Vue, component libraries, and existing design systems.
```

## 5. Risk assessment

- Risk level: `safe`
- Why: Additive frontend/UI specialist; does not modify existing authority or make high-stakes domain claims.
- Could this increase overclaiming? `no`, it is constrained to UI implementation and QA recommendations.
- Could this bypass specialist delegation? `no`, it adds a distinct technical design role without changing orchestration rules.
- Could this affect high-stakes advice? `no`, it does not provide clinical, empirical, theological, compatibility, or role-fit advice.

## 6. Required reviewers

- [ ] `empirical-claims-caveats-reviewer` — not required for this safe additive implementation.
- [ ] `source-provenance-auditor` — not required.
- [ ] `alias-canonical-naming-steward` — not required.
- [ ] domain specialist: not required.
- [x] human/project owner — explicit user request to implement.

## 7. Patch sketch

```diff
+ .opencode/agents/responsive-ui-design-systems-expert.md
+ .agent-learning/logs/2026-04-26-create-responsive-ui-design-systems-expert.md
+ .agent-learning/proposals/2026-04-26-create-responsive-ui-design-systems-expert.md
+ .agent-learning/reviews/2026-04-26-create-responsive-ui-design-systems-expert-review.md
```

## 8. Acceptance criteria

- [x] The new rule is narrow and enforceable.
- [x] It does not weaken caveats.
- [x] It preserves delegation-first routing.
- [x] It cites the relevant source/policy/audit finding.
- [x] It can be checked in a future audit.

## 9. Rollback note

Delete `.opencode/agents/responsive-ui-design-systems-expert.md` and mark this proposal/review as superseded or rolled back if the agent causes poor technical routing, inaccessible UI recommendations, or unmaintainable implementation guidance.
