---
title: "AI text style: evidence and editorial limits"
type: source
tags: [agents, methodology, writing, source-summary]
created: 2026-09-06
updated: 2026-09-06
lang: en
translation_group: ai-text-style-evidence
semantic_version: 1
reviewed_semantic_version: 1
document_status: active
page_role: source-summary
claim_status: [source-attribution, project-definition]
claims:
  - id: ai-style-studies-have-specific-evaluation-conditions
    status: source-attribution
  - id: naturalness-review-targets-editorial-defects
    status: project-definition
caveat_ids: [style-is-not-authorship, no-detector-evasion, language-transfer-unvalidated, pilot-not-universal]
sources: [raw/general/2026-09-06-ai-text-style-source-register.md, https://aclanthology.org/2024.acl-long.674/, https://arxiv.org/abs/2304.02819, https://aclanthology.org/2026.lrec-1.142/, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-4.pdf]
---

# AI text style: evidence and editorial limits

English · [[ai-text-style-evidence-ru|Русский]] · [[ai-text-style-evidence-uk|Українська]]

<!-- section:overview -->
## Overview

A text may feel formulaic because its transitions repeat, its claims stay vague, or its examples explain little. That is an editorial problem to examine in context. BWB distinguishes those defects from a claim about who or what wrote the text.

<!-- section:source-claims -->
## What the sources claim

- [Dugan et al., RAID (2024)](https://aclanthology.org/2024.acl-long.674/): twelve tested detectors struggled when models, generation settings, or editing changed.
- [Liang et al. (2023), author version](https://arxiv.org/abs/2304.02819): detectors falsely flagged writing by studied non-native English writers.
- [Miletic and Falk (2026)](https://aclanthology.org/2026.lrec-1.142/): LLM edits used more complex words and less lexical diversity; twenty experts in a pilot nevertheless rated them clearer and more interesting on average.
- [NIST AI 100-4 (November 2024)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-4.pdf), §§3.2.2.4, 4.2–4.2.2: generalization, languages, and short texts constrain detection; evaluation must match intended conditions.

<!-- section:source-evidence -->
## What evidence is provided

The source register records the papers and report used here. The bullets above attribute their findings; the editorial role below is a BWB design decision, not a method validated by those publications.

<!-- section:source-limitations -->
## Limitations

RAID does not establish that every detector is always useless. Liang's reported rates must not be transferred to Russian or Ukrainian. Miletic and Falk's pilot does not establish universal reader preferences. NIST does not certify a universal detector.

<!-- section:bwb-accepts -->
## What BWB accepts

BWB defines **naturalness-style-reviewer** as an agent role in the editorial panel, not a human specialist. It identifies concrete passages containing empty repeated transitions, vague generalizations, formulaic contrasts, awkward literal translations, or unconvincing examples. It explains the reading problem and proposes a specific revision.

The role preserves factual accuracy, sources, uncertainty, necessary terms, and matching meaning across EN/RU/UK. A smoother sentence must not turn a hypothesis into a fact. This is a project rule: **an editorial defect does not establish AI authorship**.

<!-- section:bwb-contested -->
## What remains open

Whether the role improves BWB texts for actual readers remains to be checked. Reviews should compare specific passages and invite reader feedback. An agent's opinion is not a measurement of audience response.

<!-- section:bwb-rejected-or-historical -->
## What is rejected

The role does not assign an “AI percentage,” certify human authorship, or optimize text to evade detectors. It does not treat all AI-associated style as poor writing or add errors to imitate a person.

<!-- section:next-reading -->
## Next reading

Continue with [[scientific-narrative-intelligence-layer-en]] and [[epistemic-status-and-inference-limits-en]].
