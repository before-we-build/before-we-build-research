---
title: Typology Pseudonym Drift and Permutation Hallucination
type: agent-learning-log
created: 2026-08-27
updated: 2026-08-27
severity: moderate
tags: [typology, psychosophy, temporistics, nomenclature, hallucinatory-drift]
---

# Incident Log: Typology Pseudonym Drift and Permutation Hallucination

## 1. Context & Trigger
During the execution of a multi-agent public figure typing analysis for Valeriy Zaluzhnyi using the `public-figure-typologist` skill, agents identified the correct formulas across systems:
- Psychosophy: **ФВЛЭ** (1Ф-2В-3Л-4Э)
- Temporistics: **БНПВ** (1Б-2Н-3П-4В)
- Socionics: **СЛЭ** (Se-Ti)

However, synthesized reports and subagents assigned incorrect canonical pseudonyms to the formulas:
1. **Psychosophy:** Labeled `ФВЛЭ` as `«Эпикур»`. In Afanasyev's canonical system, `ФВЛЭ` is **«Гёте»**, whereas `«Эпикур»` is `ФЛЭВ` (1Ф-2Л-3Э-4В).
2. **Temporistics:** Labeled `БНПВ` as `«Первопроходец» / «Пионер»`. In Radut's canonical system, `БНПВ` is **«Колонист»**, `БПНВ` is **«Пионер»**, and `«Первопроходец»` is an informal generic descriptor.

## 2. Root Cause Analysis
1. **Lack of SSOT in Prompt Context:** Neither `skills/public-figure-typologist.md` nor the agent prompts contained a canonical Single Source of Truth (SSOT) mapping table for the $4! = 24$ Psychosophy types, $24$ Temporistics types, and $16$ Socionics types.
2. **LLM Permutation Hallucination:** Relying on parametric weights leads LLMs to confound adjacent permutations with identical letters (e.g., F-V-L-E vs F-L-E-V; B-N-P-V vs B-P-N-V).
3. **Auditor Blindspot:** The Adversarial Auditor checklist tested for Barnum statements, OPSEC, and Popperian falsification, but lacked an explicit deterministic nomenclature validation check against an SSOT lookup table.
4. **Permissive Generation of Non-Canonical Metaphors:** Agents freely used colloquial metaphors as type names without strict formatting constraints.

## 3. Corrective Actions Required
1. Add full canonical lookup tables (Psychosophy 24, Temporistics 24, Socionics 16) directly to `skills/public-figure-typologist.md` and create `wiki/concepts/canonical-typology-registry.md`.
2. Add a strict nomenclature constraint prohibiting informal metaphors as type titles.
3. Integrate a mandatory SSOT validation step into the Adversarial Auditor prompt checklist.
4. Provide a deterministic script validator (`scripts/validate_typology_profile.py`) for automated profile checks.
