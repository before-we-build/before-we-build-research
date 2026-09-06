---
title: Agent organization cleanup
type: agent-improvement-proposal
created: 2026-09-06
updated: 2026-09-06
status: applied
risk: moderate
target_agents: [all-project-agents]
required_reviewers: []
sources: [AGENTS.md, .opencode/ORGANIZATION.md]
---

## 1. Target agents

All `.opencode/agents/*.md`: explicit mode and canonical organization reference.
Focused changes to root/research coordinators, reporting metadata and scheduling language.

## 2. Observed failure

See ../logs/2026-09-06-agent-organization-audit.md. The roster, hierarchy and
instructions disagree; static checks do not detect organizational drift.

## 3. Evidence

53 manifests, opencode.json, ORGANIZATION.md, scripts/lint-agents.py and repository workflows.
Official references: https://opencode.ai/docs/agents/ and
https://opencode.ai/v2/docs/permissions (accessed 2026-09-06).
Documentation versions differ; no installed runtime is available to select a permission migration.

## 4. Proposed instruction change

- Set explicit subagent mode on every non-root agent.
- Canonicalize the roster from manifest name, mode, reportsto and scope.
- Put research-orchestrator directly under master; put study-method specialists
  under research-orchestrator and Psychosophy readers under typing-lead.
- Replace duplicated organizational trees with a canonical reference.
- Make typology-researcher a source-doctrine coordinator only; route empirical
  pipelines directly to research-orchestrator, without a mandatory extra hop.
- Define one deliverable owner, bounded handoffs and distinct editorial outputs.
- Mark specialty roles on-demand and schedules as recommendations, not running jobs.
- Preserve model IDs, domain caveats, specialist review and publication authorization.

## 5. Risk assessment

Moderate: routing changes affect task allocation. No scientific, clinical,
theological, statistical or typological doctrine is changed. No role is removed.
Does not increase overclaiming or bypass domain review. Existing permission
declarations remain unverified rather than receiving a blind runtime migration.

## 6. Reviewers

Organizational self-review by the implementing assistant, recorded separately.
No independent expert review is claimed. Domain review is required if later work
changes substantive methods/caveats or retires a safety reviewer.
The user's explicit cleanup request authorizes this organizational implementation.

## 7. Patch sketch

`mode: subagent`; corrected `reportsto`; shared organization link; generated roster;
structural linter checks for root, parents, cycles, depth and roster synchronization.

## 8. Acceptance criteria

- Exactly one project primary matching default_agent; all other agents explicit subagents.
- No missing parent, cycle or reporting chain deeper than three nodes.
- All manifests represented in generated roster; no planned role presented as active.
- No false runtime, cron, least-privilege or independent-review claims.
- Structural regression tests and required repository checks executed.

## 9. Rollback

Revert only this change's manifest, organization, checker and test edits from its
reviewed diff. Preserve unrelated working-tree changes and governance history.
