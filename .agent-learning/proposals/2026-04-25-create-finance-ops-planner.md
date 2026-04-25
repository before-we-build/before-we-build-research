---
title: Create Finance Ops Planner Agent
type: agent-improvement-proposal
created: 2026-04-25
updated: 2026-04-25
status: applied
risk: moderate
target_agents: [finance-ops-planner]
required_reviewers: [human/project-owner]
sources: [AGENTS.md, user-request]
---

# Agent Improvement Proposal: Create Finance Ops Planner

## 1. Target agent(s)

- `.opencode/agents/finance-ops-planner.md`

## 2. Observed failure or opportunity

The user identified the need for financial expertise after discussing the cost of automated video generation and autoposting for PsyCalc / Cognitive Matchmaker.

## 3. Evidence

- User statement: “я так понимаю мне нужен эксперт по финансам”
- User approval: “да давай”
- Context: cost estimation for social video automation, API tools, content production, and growth operations.

## 4. Proposed instruction change

Create a finance/operations planning agent that can estimate and model:

- cost per generated / approved / posted video;
- content production budgets;
- API/tool/subscription costs;
- contractor costs;
- CAC and lead acquisition assumptions;
- funnel economics;
- break-even scenarios;
- MVP operating budgets.

## 5. Risk assessment

- Risk level: `moderate`
- Why: financial estimates can be mistaken for guarantees or regulated advice.
- Could this increase overclaiming? `yes`, if speculative CAC/LTV are presented as facts.
- Could this bypass specialist delegation? `low`, with routing to data/statistics when actual experiments are analyzed.
- Could this affect high-stakes advice? `yes`, if treated as investment, tax, or legal advice.

Mitigation: the agent explicitly avoids tax, legal, securities, investment, accounting, and guaranteed ROI advice. It frames outputs as assumptions, scenarios, and rough estimates.

## 6. Required reviewers

- [x] human/project owner approval requested and given in chat
- [ ] human review before using estimates in investor materials or public claims

## 7. Patch sketch

```diff
++ .opencode/agents/finance-ops-planner.md
+ finance ops and unit economics agent for content automation and early growth budgets
```

## 8. Acceptance criteria

- [x] The new agent is narrow and enforceable.
- [x] It includes clear financial-advice boundaries.
- [x] It distinguishes estimates, assumptions, scenarios, and actuals.
- [x] It supports content pipeline and early growth unit economics.
- [x] It preserves delegation to data/statistics agents for experiment analysis.

## 9. Rollback note

Delete `.opencode/agents/finance-ops-planner.md` and mark this proposal as reverted if the agent produces unsafe or overconfident financial guidance.
