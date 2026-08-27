---
title: Canonical Typology Registry and Pseudonym Hardening
type: agent-improvement-proposal
created: 2026-08-27
updated: 2026-08-27
status: approved
risk: safe
target_agents: [skills/public-figure-typologist.md, scripts/validate_typology_profile.py]
required_reviewers: [alias-canonical-naming-steward, human/project owner]
sources: [raw/temporistics/types.md, skills/public-figure-typologist.md]
---

# Agent Improvement Proposal: Canonical Typology Registry and Pseudonym Hardening

## 1. Target agent / skill / tool

- `skills/public-figure-typologist.md`
- `scripts/validate_typology_profile.py` (Deterministic validation tool)
- `wiki/concepts/canonical-typology-registry.md` (SSOT documentation)

## 2. Observed failure or opportunity

Subagents and synthesis pipelines produce permutation hallucinations in typological pseudonyms:
- `ФВЛЭ` was mislabeled as `«Эпикур»` (canonical: `«Гёте»`; `«Эпикур»` is `ФЛЭВ`).
- `БНПВ` was mislabeled as `«Первопроходец» / «Пионер»` (canonical: `«Колонист»`; `«Пионер»` is `БПНВ`).

## 3. Evidence

- Incident Log: `.agent-learning/logs/2026-08-27-typology-pseudonym-drift.md`
- Canonical Source: `raw/temporistics/types.md`
- Afanasyev Canonical Names: *«Синтаксис Любви»* (1993).

## 4. Proposed instruction & system changes

1. **Embed Canonical SSOT Matrices directly in `skills/public-figure-typologist.md`:**
   - Psychosophy (24 canonical names)
   - Temporistics (24 canonical names)
   - Socionics (16 canonical names)
2. **Add Strict Nomenclature & Anti-Drift Rule:**
   - Prohibit informal adjectives/metaphors as official type names.
   - Mandate strict syntax: `[Formula] — «[Canonical Pseudonym]»`.
3. **Hardcode SSOT Verification in Adversarial Auditor:**
   - Auditor must explicitly verify formula-to-pseudonym mapping against the SSOT table.
4. **Deploy Deterministic Python Linter:**
   - Provide `scripts/validate_typology_profile.py` for automated zero-error validation.

## 5. Risk assessment

- Risk level: `safe`
- Why: Eliminates factual inaccuracies and hallucinations without altering theoretical foundations or relaxing caveats.
- Could this increase overclaiming? No.
- Could this bypass specialist delegation? No.
- Could this affect high-stakes advice? No.

## 6. Required reviewers

- [x] `alias-canonical-naming-steward`
- [x] human/project owner (explicitly requested fix)

## 7. Patch sketch

Add Section 5 (Canonical SSOT Registry) and Section 6 (Strict Nomenclature Rule & Auditor Step) to `skills/public-figure-typologist.md`.

## 8. Acceptance criteria

- [x] All 24 Psychosophy, 24 Temporistics, and 16 Socionics types have unambiguous canonical mappings.
- [x] Rule prevents confusing permutations (ФВЛЭ vs ФЛЭВ, БНПВ vs БПНВ).
- [x] Linter script verifies formulas automatically.

## 9. Rollback note

If changes cause formatting conflicts, revert `skills/public-figure-typologist.md` to git commit state.
