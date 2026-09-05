---
title: Adapt Scientific Narrative Skill to the Available Runtime
type: agent-improvement-proposal
created: 2026-09-05
updated: 2026-09-05
status: applied
risk: moderate
target_agents:
  - .agents/skills/scientific-narrative/SKILL.md
required_reviewers:
  - source-provenance-auditor
  - system-runtime-reviewer
  - human-project-owner
sources:
  - protocols/scientific-narrative-intelligence-layer.md
  - raw/general/scientific-narrative-intelligence-layer.md
---

# Agent Improvement Proposal: Adapt SNIL to the available runtime

## 1. Target skill

- `.agents/skills/scientific-narrative/SKILL.md`
- `.agents/skills/scientific-narrative/references/architecture-specification.md`

## 2. Observed failure or opportunity

The active skill names unavailable execution calls and is too brief to reproduce
its promised five-role collegium, scoring gates, reader panel, and epistemic veto
behavior. A caller may therefore fail to run the skill or present simulated
retention estimates as if they were measured.

## 3. Evidence

- The entrypoint at commit
  `391ab10207d03bb4350472546efe75a646b044ec`, path
  `.agents/skills/scientific-narrative/SKILL.md`, ends with `invoke_subagent`,
  which is not an available tool in this Codex collaboration runtime.
- `raw/general/scientific-narrative-intelligence-layer.md` and
  `protocols/scientific-narrative-intelligence-layer.md` prescribe a nested
  `codex exec` review, while the active entrypoint also adds the unavailable
  `invoke_subagent` instruction.
- The first recorded governance review requested explicit provenance and
  deviation notes before approval.
- The user explicitly requested installation, execution, commit, and push.

## 4. Proposed instruction change

Replace unavailable execution instructions with tool-agnostic collaboration
guidance. Define four operating modes and five composite review roles. Add one
routed reference with the 22 theoretical perspectives, scorecard gates,
drop-off-map contract, and report format.

Document these intentional runtime adaptations:

- replace nested CLI execution with the available collaboration mechanism;
- treat `lambda(s) > 0.40` as an unvalidated source-package proposal rather than
  a publication gate;
- replace the unsourced fixed `4±1` active-concept rule with qualitative
  working-memory and prerequisite-load review;
- keep `protocols/research-bridge-builder.md` and
  `protocols/evidence-packager.md` as optional adjacent protocols, not mandatory
  dependencies for every readability audit;
- retain the BWB inference ladder: whole person → observable trace or pattern →
  typological-model hypothesis → latent-process hypothesis → natural-
  predisposition hypothesis.

## 5. Risk assessment

- Risk level: `moderate`
- Why: the change affects runtime delegation and review behavior.
- Could this increase overclaiming? `no`; it adds explicit calibration rules.
- Could this bypass specialist delegation? `no`; it requires independent roles
  when collaboration is available and disclosure otherwise.
- Could this affect high-stakes advice? `indirectly`; epistemic and safety
  guardrails are strengthened rather than relaxed.

## 6. Required reviewers

- [x] source/provenance reviewer
- [x] system-runtime reviewer
- [x] human/project owner — explicit installation and execution request

## 7. Patch sketch

```diff
- Используется invoke_subagent ... codex exec
+ Use available collaboration subagents in parallel or waves.
+ Label all score and retention estimates as simulated model judgments.
+ Route detailed role contracts to references/architecture-specification.md.
```

## 8. Acceptance criteria

- [x] No unavailable runtime command remains.
- [x] Audit mode cannot silently edit files.
- [x] Full mode preserves all five composite roles.
- [x] Scientific accuracy and epistemic calibration retain veto priority.
- [x] Simulated reader scores are never described as measured behavior.
- [x] The five BWB inference levels remain explicit.
- [x] Every intentional deviation from the preserved protocol is documented.
- [x] The entrypoint routes to every required supporting reference.
- [x] Structural validation and a realistic independent dry run pass.
- [x] Repository CI checks pass.

## 9. Rollback note

Revert this proposal's skill and reference-file commit to restore the upstream
entrypoint. No wiki content or source record depends on the adapted runtime
instructions.
