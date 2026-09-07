---
title: Require auditable independent launches for the full SNIL collegium
type: agent-improvement-proposal
created: 2026-09-07
updated: 2026-09-07
status: applied
risk: safe
target_agents: [master-orchestrator, naturalness-style-reviewer]
required_reviewers: [agent-improvement-steward]
sources:
  - .agent-learning/logs/2026-09-07-snil-independent-launches.md
  - .agents/skills/scientific-narrative/SKILL.md
  - .agents/skills/scientific-narrative/references/architecture-specification.md
  - .agents/registry.json
  - .agents/ORGANIZATION.md
---

# Agent Improvement Proposal: auditable full SNIL launches

## 1. Target agent(s)

The main-session director and delegated SNIL reviewers use
`.agents/skills/scientific-narrative/SKILL.md` and its architecture reference.
This proposal changes that workflow contract, not canonical role files or the
role registry. `naturalness-style-reviewer` retains its existing role scope.

## 2. Observed failure or opportunity

The previous skill allowed combined roles and did not require an invocation
ledger. Its six perspectives therefore could not substantiate the stronger
claim that six independent children had completed review. Five task names also
lacked explicit generic-agent dispatch instructions.

## 3. Evidence

- Audit record: `.agent-learning/logs/2026-09-07-snil-independent-launches.md`.
- Pre-change SKILL.md lines 44–46 allowed merging; lines 64–66 allowed
  disclosed orchestrator performance; lines 109–111 specified a named-agent
  fallback only for naturalness.
- Architecture reference line 24 still described five current runtime clusters.
- `.agents/registry.json` registered naturalness but not the five `snil_*` names.
- `.agents/ORGANIZATION.md` requires bounded delegation and truthful disclosure
  of independent review, with one writer per artifact.
- User authorization, relayed by the task owner: “сделай правильно”. This
  approves implementation; it does not certify future checks or execution.

## 4. Proposed instruction change

```md
Full collegium requires six distinct child identities, one per composite role.
Dispatch snil_* as task names through a generic/default child with the relevant
reference instructions. Use the named naturalness role when available and its
canonical instructions with generic dispatch otherwise. Under capacity limits,
run waves rather than merging roles. Keep a ledger of role, child ID, status,
target revision and completed result. A missing, failed or stale contribution
prevents a full-collegium completion verdict. The director is the coordinator,
not another child. Label focused or manual review explicitly.
```

## 5. Risk assessment

- Risk level: `safe`.
- Why: narrow execution and evidence-accounting correction; no new empirical
  claims, score changes, model settings or substantive reviewer authority.
- Could this increase overclaiming? No; it narrows claims of completed review.
- Could this bypass specialist delegation? No; it requires distinct children.
- Could this affect high-stakes advice? No substantive advice change.

## 6. Required reviewers

- [x] `agent-improvement-steward`: review the implemented contract and evidence.
- [x] Human/project owner: explicit implementation request recorded above.

No statistical, psychometric or domain review is required for this bounded
workflow patch; any scoring or substantive scientific change would be outside
this authorization and requires its appropriate review.

## 7. Patch sketch

```diff
- If capacity is limited, combine adjacent roles or run them in waves.
+ In full mode, use six distinct child identities and run them in waves when
+ capacity is limited. Never count merged or director-performed roles as six
+ independent reviews.
+ Document generic dispatch and the naturalness named-role fallback.
+ Record IDs, statuses, target revision and completed results in the report.
+ Report missing/failed/stale roles and withhold a full completion verdict.
- The current skill preserves five runtime clusters.
+ The current skill uses six runtime roles: five source clusters plus the
+ naturalness reviewer. The director remains the coordinating session.
```

## 8. Acceptance criteria

- [x] Full mode unambiguously requires six distinct children.
- [x] Dispatch distinguishes task names from registered role names.
- [x] Capacity limits lead to waves, not role merging in full mode.
- [x] The ledger requires child IDs, result/status evidence and target revision.
- [x] Missing, failed or stale results cannot support a completed full verdict.
- [x] Focused/manual execution and coordinator identity are explicit.
- [x] SKILL.md and reference agree on the six-role architecture.
- [x] Scientific caveats and scoring semantics remain unchanged.
- [x] Skill validation and applicable repository checks are recorded honestly.
- [x] Static checks are not described as proof of an actual six-child run.

Acceptance reviewed after implementation. Repository checks and runtime exercise passed; the bundled skill validator remains unavailable (missing PyYAML), recorded honestly as required. See the matching review and reports/snil-independent-launches-2026-09-07.md. Independent approval was conditional on a link correction, verified by the main session.

## 9. Rollback note

Revert only the authorized skill/reference hunks if they cause runtime problems,
preserving concurrent work and this audit trail. Any rollback must continue to
disclose actual independent participation; it must not restore an unsupported
claim of six completed launches.
