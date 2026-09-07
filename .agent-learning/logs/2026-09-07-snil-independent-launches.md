---
title: SNIL role coverage was not a guarantee of independent launches
type: agent-learning-log
created: 2026-09-07
updated: 2026-09-07
status: recorded
sources:
  - .agents/skills/scientific-narrative/SKILL.md
  - .agents/skills/scientific-narrative/references/architecture-specification.md
  - .agents/registry.json
  - .agents/ORGANIZATION.md
---

# SNIL role coverage was not a guarantee of independent launches

## Observed feedback and audit

The user asked whether the scientific-narrative skill was correctly constructed
and whether all six agents really spawned. A read-only audit found that the
pre-change skill required six composite perspectives but expressly permitted
combining roles under capacity limits (SKILL.md, former lines 44–46) and
disclosed orchestrator performance (former lines 64–66). Six role descriptions
therefore did not establish six independent child launches.

Only `naturalness-style-reviewer` was registered as a named agent. The five
`snil_*` labels were workflow task names without explicit generic dispatch
instructions. The reference still described the current skill as five runtime
clusters, although SKILL.md disclosed naturalness as a sixth role. The final
report template did not require child IDs or completed-result evidence.

These findings concern the instruction contract. They do not establish how
many children any previous full review actually launched; that requires its
runtime trace.

## Authorization and ownership

After the audit, the user explicitly requested correction: “сделай правильно”.
The task owner relayed that authorization to this steward. The task owner
owns changes to the skill and architecture reference. This steward owns this
log and the linked proposal, and will return review findings separately.

## Intended correction

Full mode requires six distinct child identities, explicit dispatch, waves
instead of merging, and a result ledger tied to the reviewed target revision.
Missing or failed contributions prevent a full-collegium completion verdict.
The coordinator is not a seventh child; focused and manual modes are disclosed.
Scoring, scientific claims, and substantive caveats remain outside this patch.

## Verification status

Implementation and checks are pending at the time of this record. No full
SNIL execution or six-agent runtime verification is claimed by this audit.
Acceptance criteria are recorded in
`.agent-learning/proposals/2026-09-07-snil-independent-launches.md`.

## Implementation outcome

Implemented on explicit user request. Six distinct child reviews completed on fixture v1. All blocking repository checks passed (110 tests); adapter generation/check passed. Bundled skill validator could not execute without PyYAML. Independent reviewer condition (restore relative source link) was corrected and verified by the main session. See matching review and reports/snil-independent-launches-2026-09-07.md for evidence and limits.
