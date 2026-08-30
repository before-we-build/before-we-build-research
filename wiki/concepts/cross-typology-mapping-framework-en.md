---
title: Cross-Typology Mapping Framework
type: concept
tags: [architecture, mapping, tooling, personanexus, jpaf, oasis]
created: 2026-04-15
updated: 2026-04-15
sources: []
lang: en
translation_group: cross-typology-mapping-framework
semantic_version: 1
reviewed_semantic_version: 1
document_status: active
page_role: research-appendix
claim_status: [research-hypothesis]
claims: []
caveat_ids: []
---

# Cross-Typology Mapping Framework

<!-- section:overview -->
## Overview

Proposed pipeline for experimenting with bridges between three typological systems (Temporistics, Psychosophy, Socionics) and more mainstream trait frameworks. This page records project architecture ideas and empirical survey validation, not simulation or an established mapping standard.

<!-- section:pipeline-architecture -->
## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────┐
│  CROSS-TYPOLOGY MAPPING LAYER                           │
│                                                         │
│  Temporistics (24 types) ──→ MBTI/Jungian (16 types)    │
│  Psychosophy (81 types)  ──→ MBTI/Jungian (16 types)    │
│  Socionics (16 types)    ──→ MBTI/Jungian (16 types)    │
│                        ↓                                │
│              PersonaNexus (trait bridge)                │
│              OCEAN ↔ DISC ↔ Jungian ↔ Custom            │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  EMPIRICAL SURVEY VALIDATION LAYER (OASIS-platform)     │
│                                                         │
│  - AI-assisted survey interviews and questionnaires     │
│  - Semi-structured interview guides                     │
│  - Multi-provider LLM support for transcription/coding  │
│  - FAIR-compliant data export                           │
└─────────────────────────────────────────────────────────┘
```

<!-- section:cross-system-mapping -->
## Cross-System Mapping

<!-- section:socionics-mbti-common-but-disputed-approximation -->
### Socionics → MBTI (Common But Disputed Approximation)

| Socionics | Common MBTI Approximation | Note |
|-----------|----------------------------|------|
| ILE | ENTP | Common community mapping |
| LIE | ENTJ | Common community mapping |
| EIE | ENFJ | Common community mapping |
| IEE | ENFP | Common community mapping |
| ILI | INTP or INTJ | Disputed |
| LII | INTP or INTJ | Disputed |
| EII | INFJ | Common but still approximate |
| SEE | ESFP | Approximate |

<!-- section:temporistics-mbti-hypothesized -->
### Temporistics → MBTI (Hypothesized)

Temporal framing dimension maps to cognitive style preferences:

| Temporistics Frame | Primary Preference | Secondary |
|-------------------|-------------------|-----------|
| Present types (1-4N) | Sensing (concrete) | Se/Si |
| Future types (1-4F) | Intuitive (abstract) | Ne/Ni |
| Eternity types (1-4E) | Reflective (Ni/Si) | Balanced |
| Past types (1-4P) | Memory-oriented | Si-heavy |

**Mapping approach:** Temporistics aspect combinations map to Jungian dichotomies:
- Temporal focus (P/N/F/E) → tentative orientation cues
- Aspect density → S/N preference
- Aspect role → T/F and J/P

<!-- section:psychosophy-mbti-hypothesized -->
### Psychosophy → MBTI (Hypothesized)

4-aspect structure maps through function weighting:

| Psychosophy Pattern | Possible MBTI-Like Echo | Notes |
|--------------------|--------------------------|-------|
| Logic-heavy | Thinking emphasis | Approximate only |
| Emotion-heavy | Feeling emphasis | Approximate only |
| Physics-heavy | Sensing emphasis | Approximate only |
| Will-heavy | Judgment / agency emphasis | Approximate only |

<!-- section:validation-hypothesis-example -->
## Validation Hypothesis Example

<!-- section:combined-temporistics-socionics-predicts-satisfaction-better-than-either-alone -->
### Combined Temporistics + Socionics predicts satisfaction better than either alone
- **Method:** OASIS-platform interviews and structured surveys with 200 real couples
- **Metric:** Multi-factor regression, cross-validated
- **Expected:** test whether combined features improve prediction over single-system baselines

<!-- section:tooling-reference -->
## Tooling Reference

<!-- section:personanexus -->
### PersonaNexus
- **Purpose:** Declarative personality definition with framework mapping
- **Key features:** OCEAN↔DISC↔Jungian bidirectional, YAML identity files, archetype inheritance
- **Command:** `pip install personanexus`
- **Example:** `personanexus personality jungian-to-traits --preset intj`

**Audit note:** Vendor/source verification for this tooling stack is incomplete in the current repo; treat these tool references as exploratory pointers.

<!-- section:oasis-platform-survey-interviews -->
### OASIS-platform (Survey Interviews)
- **Purpose:** Qualitative research interviews and survey intake
- **Key features:** Voice/text interview assistance, multi-LLM transcription and coding support, Docker deploy, FAIR-compliant
- **Install:** `git clone https://github.com/oasis-surveys/oasis-platform && docker compose up`
- **License:** Open Non-Commercial Research License v1.0

<!-- section:next-steps -->
## Next Steps

1. **Verify Socionics→MBTI mapping** using PersonaNexus archetypes
2. **Hypothesize Temporistics→MBTI** based on aspect patterns
3. **Empirical check:** OASIS-platform interviews with real typed participants
