---
title: Create Vanka the Layman Agent
type: agent-improvement-proposal
created: 2026-04-26
updated: 2026-04-26
status: applied
risk: safe
target_agents: [".opencode/agents/vanka-the-layman.md", ".opencode/agents/master-orchestrator.md"]
required_reviewers: []
sources: ["user request", "AGENTS.md"]
---

# Agent Improvement Proposal: Create Vanka the Layman

## 1. Target agent(s)

- `.opencode/agents/vanka-the-layman.md`
- `.opencode/agents/master-orchestrator.md`

## 2. Observed failure or opportunity

The user explicitly requested a dedicated ordinary-person comprehension reviewer for checking whether complex ideas, websites, products, theories, infographics, and startup explanations are understandable and practically valuable to non-experts.

## 3. Evidence

- Audit/task result: direct user request in the current task.
- File/page references: adjacent explanation agents exist, but none embody a blunt practical layperson viewpoint.
- Source or policy references: `AGENTS.md` controlled agent self-improvement workflow.

## 4. Proposed instruction change

Add a new explanation-team agent that:

```md
- acts as a practical, skeptical, non-expert reviewer;
- asks what the idea is, why anyone should care, what problem it solves, and whether it sounds fake or overcomplicated;
- translates complex ideas into simple everyday language;
- uses the requested A-I output format;
- refuses to judge scientific truth, validation, clinical/theological/statistical correctness, or typological accuracy.
```

Update master-orchestrator routing to delegate ordinary-person understandability checks to this new agent.

## 5. Risk assessment

- Risk level: `safe`
- Why: Additive explanation/review agent; no domain-claim authority.
- Could this increase overclaiming? `no`, agent is instructed not to validate truth and not to remove caveats.
- Could this bypass specialist delegation? `no`, agent is specifically not a specialist validator.
- Could this affect high-stakes advice? `no`, it only reviews clarity and practical understandability.

## 6. Required reviewers

- [ ] `empirical-claims-caveats-reviewer` — not required for initial creation; recommended if future edits make the agent evaluate claim truth.
- [ ] `source-provenance-auditor` — not required.
- [ ] `alias-canonical-naming-steward` — not required.
- [ ] domain specialist: not required.
- [x] human/project owner — explicit user request to implement.

## 7. Patch sketch

```diff
+ .opencode/agents/vanka-the-layman.md
+ .agent-learning/logs/2026-04-26-create-vanka-the-layman.md
+ .agent-learning/proposals/2026-04-26-create-vanka-the-layman.md
+ .agent-learning/reviews/2026-04-26-create-vanka-the-layman-review.md
~ .opencode/agents/master-orchestrator.md
```

## 8. Acceptance criteria

- [x] The new rule is narrow and enforceable.
- [x] It does not weaken caveats.
- [x] It preserves delegation-first routing.
- [x] It cites the relevant source/policy/audit finding.
- [x] It can be checked in a future audit.

## 9. Rollback note

Delete `.opencode/agents/vanka-the-layman.md`, revert master-orchestrator routing additions, and mark this proposal/review as superseded or rolled back if the agent becomes insulting, over-skeptical, or removes necessary caveats.
