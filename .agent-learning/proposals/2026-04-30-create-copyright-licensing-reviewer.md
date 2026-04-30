---
title: Create Copyright Licensing Reviewer Agent
type: agent-improvement-proposal
created: 2026-04-30
updated: 2026-04-30
status: applied
risk: moderate
target_agents: [".opencode/agents/copyright-licensing-reviewer.md", ".opencode/agents/master-orchestrator.md", ".opencode/ORGANIZATION.md"]
required_reviewers: ["source-provenance-auditor", "ethics-and-consent-reviewer", "human/project owner", "licensed attorney if high-stakes"]
sources: ["user request", "AGENTS.md", ".opencode/agents/source-provenance-auditor.md", ".opencode/agents/ethics-and-consent-reviewer.md", ".opencode/ORGANIZATION.md"]
---

# Agent Improvement Proposal: Create Copyright Licensing Reviewer

## 1. Target agent(s)

- `.opencode/agents/copyright-licensing-reviewer.md`
- `.opencode/agents/master-orchestrator.md`
- `.opencode/ORGANIZATION.md`

## 2. Observed failure or opportunity

The user explicitly requested a legal-checking agent for publication/republication of sources in PsyCalc wiki. Existing agents cover source provenance and ethics/consent, but not focused copyright/licensing/publication-rights triage for wiki/source ingestion.

## 3. Evidence

- Audit/task result: direct user request in the current task.
- File/page references: `.opencode/agents/source-provenance-auditor.md`, `.opencode/agents/wiki-contributor.md`, `.opencode/ORGANIZATION.md`.
- Source or policy references: `AGENTS.md` controlled self-improvement workflow.

## 4. Proposed instruction change

Add a narrow Wiki Team specialist for publication-rights risk screening. It must not be a broad “lawyer” agent and must caveat that it is not a lawyer or substitute for licensed legal advice.

```md
Create `.opencode/agents/copyright-licensing-reviewer.md` with scope limited to copyright, licensing, attribution, fair use/fair dealing risk, source excerpts, web/PDF republication risk, and secondary routing for data/privacy concerns.
```

## 5. Risk assessment

- Risk level: `moderate`
- Why: Legal-risk screening is consequential, but this agent narrows scope, adds explicit non-lawyer caveats, routes privacy issues to ethics review, and requires licensed legal review for high-stakes cases.
- Could this increase overclaiming? `yes`, if future edits remove caveats or let the agent make definitive legal conclusions.
- Could this bypass specialist delegation? `no`, the patch adds routing to provenance, ethics, and licensed counsel.
- Could this affect high-stakes advice? `yes`, publication/republication decisions can carry legal risk.

## 6. Required reviewers

- [ ] `source-provenance-auditor`
- [ ] `ethics-and-consent-reviewer`
- [ ] human/project owner
- [ ] licensed attorney for high-risk, contested, jurisdiction-specific, or commercially important publication decisions

## 7. Patch sketch

```diff
++ .opencode/agents/copyright-licensing-reviewer.md
+ Narrow publication-rights reviewer with non-lawyer caveats and output checklist.

~ .opencode/agents/master-orchestrator.md
+ Add Wiki Team entry and routing rule for publication/republication rights checks.

~ .opencode/ORGANIZATION.md
+ Add agent to Wiki Team listing and purpose.
```

## 8. Acceptance criteria

- [x] The new rule is narrow and enforceable.
- [x] It does not weaken caveats.
- [x] It preserves delegation-first routing.
- [x] It cites the relevant source/policy/audit finding.
- [x] It can be checked in a future audit.

## 9. Rollback note

Remove `.opencode/agents/copyright-licensing-reviewer.md` and revert the related entries in `.opencode/agents/master-orchestrator.md` and `.opencode/ORGANIZATION.md` if the agent encourages legal overconfidence or broad legal advice.
