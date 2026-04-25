---
title: Agent Improvement Proposal
type: agent-improvement-proposal
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: proposed # proposed | in-review | approved | applied | rejected | superseded
risk: safe # safe | moderate | high-risk
target_agents: []
required_reviewers: []
sources: []
---

# Agent Improvement Proposal: <short title>

## 1. Target agent(s)

- `.opencode/agents/<agent-name>.md`

## 2. Observed failure or opportunity

Describe the concrete behavior, audit finding, or recurring gap.

## 3. Evidence

- Audit/task result:
- File/page references:
- Source or policy references:

## 4. Proposed instruction change

Add/change/remove these rules:

```md
<proposed agent instruction text>
```

## 5. Risk assessment

- Risk level: `safe | moderate | high-risk`
- Why:
- Could this increase overclaiming? `yes/no`
- Could this bypass specialist delegation? `yes/no`
- Could this affect high-stakes advice? `yes/no`

## 6. Required reviewers

- [ ] `empirical-claims-caveats-reviewer`
- [ ] `source-provenance-auditor`
- [ ] `alias-canonical-naming-steward`
- [ ] domain specialist: `<agent>`
- [ ] human/project owner

## 7. Patch sketch

```diff
<diff or patch sketch>
```

## 8. Acceptance criteria

- [ ] The new rule is narrow and enforceable.
- [ ] It does not weaken caveats.
- [ ] It preserves delegation-first routing.
- [ ] It cites the relevant source/policy/audit finding.
- [ ] It can be checked in a future audit.

## 9. Rollback note

How to undo this change if it causes bad behavior.
