---
title: Agentic Research Pipeline Team
type: agent-improvement-proposal
created: 2026-04-25
updated: 2026-04-25
status: applied
risk: moderate
target_agents:
  - .opencode/agents/research-orchestrator.md
  - .opencode/agents/experiment-designer.md
  - .opencode/agents/data-pipeline-engineer.md
  - .opencode/agents/ethics-and-consent-reviewer.md
  - .opencode/agents/literature-researcher.md
  - .opencode/agents/master-orchestrator.md
required_reviewers:
  - agent-improvement-steward
  - empirical-claims-caveats-reviewer
  - source-provenance-auditor
sources:
  - AGENTS.md
  - user-request
---

# Agent Improvement Proposal: Agentic Research Pipeline Team

## 1. Target agent(s)

- `.opencode/agents/research-orchestrator.md`
- `.opencode/agents/experiment-designer.md`
- `.opencode/agents/data-pipeline-engineer.md`
- `.opencode/agents/ethics-and-consent-reviewer.md`
- `.opencode/agents/literature-researcher.md`
- `.opencode/agents/master-orchestrator.md`

## 2. Observed failure or opportunity

PsyCalc needs a repeatable agentic research pipeline for real-world validation data. Existing agents cover many specialist roles, but there was no dedicated research orchestration, experiment design, data pipeline, ethics/consent, or literature search agent for end-to-end studies.

## 3. Evidence

- User explicitly requested specialized agents to “сами разрулят” the research pipeline.
- AGENTS.md requires controlled self-improvement and review-gated agent changes.

## 4. Proposed instruction change

Add a research pipeline team that can coordinate:

- study design;
- psychometrics;
- data engineering;
- statistical validation;
- source provenance;
- consent/privacy review;
- report preparation;
- human approval gates.

## 5. Risk assessment

- Risk level: `moderate`
- Why: agents may touch research design, participant data, and empirical claims.
- Could this increase overclaiming? `yes`, mitigated by caveat/provenance/statistics review rules.
- Could this bypass specialist delegation? `yes`, mitigated by explicit Must Delegate sections.
- Could this affect high-stakes advice? `yes`, mitigated by ethics and human approval gates.

## 6. Required reviewers

- [x] `agent-improvement-steward`
- [ ] `empirical-claims-caveats-reviewer`
- [ ] `source-provenance-auditor`
- [ ] human/project owner

## 7. Patch sketch

Create new agent specs and update master orchestrator routing for research-pipeline requests.

## 8. Acceptance criteria

- [x] The new rules are narrow and enforceable.
- [x] They do not weaken caveats.
- [x] They preserve delegation-first routing.
- [x] They cite relevant policy/user request.
- [x] They can be checked in a future audit.

## 9. Rollback note

Delete the five new agent specs and remove research-pipeline routing lines from `master-orchestrator.md`.
