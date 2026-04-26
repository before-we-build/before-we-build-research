---
title: Create Visual Explainer Agent
type: agent-improvement-proposal
created: 2026-04-26
updated: 2026-04-26
status: applied
risk: safe
target_agents: [".opencode/agents/visual-explainer.md"]
required_reviewers: []
sources: ["user request", "AGENTS.md"]
---

# Agent Improvement Proposal: Create Visual Explainer

## 1. Target agent(s)

- `.opencode/agents/visual-explainer.md`

## 2. Observed failure or opportunity

The user explicitly requested a new specialized expert agent called **Visual Explainer** for information design and explainer illustration. The repository has adjacent explanation agents, but no dedicated agent whose core output is simple, emotionally understandable visual concepts.

## 3. Evidence

- Audit/task result: direct user request in the current task.
- File/page references: `.opencode/agents/psycalc-plain-language-translator.md`, `.opencode/agents/psycalc-presentation-designer.md`, `.opencode/agents/visual-storyboard-agent.md` show adjacent but non-identical explanation roles.
- Source or policy references: `AGENTS.md` controlled agent self-improvement workflow.

## 4. Proposed instruction change

Add a new explanation-team agent that:

```md
- serves as Visual Explainer, information designer, and explainer illustrator;
- converts complex ideas into simple drawings, visual metaphors, infographics, and storyboards;
- optimizes for simple, emotionally understandable visual concepts;
- follows the workflow: core meaning, audience, problem, visual metaphor, drawing concept, simplicity check, final output;
- returns final output in sections A-H;
- preserves caveats for Christian, scientific/psychological, and technical topics.
```

## 5. Risk assessment

- Risk level: `safe`
- Why: Additive outreach/explanation agent; does not modify existing authority or make domain claims.
- Could this increase overclaiming? `no`, if the caveat rules are included.
- Could this bypass specialist delegation? `no`, the agent is instructed to visualize already-approved or caveated concepts and request specialist review for domain claims.
- Could this affect high-stakes advice? `no`, it does not provide advice; it packages explanations visually.

## 6. Required reviewers

- [ ] `empirical-claims-caveats-reviewer` — not required for this safe additive implementation, but recommended if future edits expand science/psychology claim authority.
- [ ] `source-provenance-auditor` — not required.
- [ ] `alias-canonical-naming-steward` — not required.
- [ ] domain specialist: not required.
- [x] human/project owner — explicit user request to implement.

## 7. Patch sketch

```diff
+ .opencode/agents/visual-explainer.md
+ .agent-learning/logs/2026-04-26-create-visual-explainer.md
+ .agent-learning/proposals/2026-04-26-create-visual-explainer.md
+ .agent-learning/reviews/2026-04-26-create-visual-explainer-review.md
```

## 8. Acceptance criteria

- [x] The new rule is narrow and enforceable.
- [x] It does not weaken caveats.
- [x] It preserves delegation-first routing.
- [x] It cites the relevant source/policy/audit finding.
- [x] It can be checked in a future audit.

## 9. Rollback note

Delete `.opencode/agents/visual-explainer.md` and mark this proposal/review as superseded or rolled back if the agent causes unsafe visual simplification, manipulative framing, or claim overreach.
