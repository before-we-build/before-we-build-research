---
title: Cross-Typology Mapping Framework
type: concept
tags: [architecture, mapping, tooling, personanexus, jpaf, oasis]
created: 2026-04-15
updated: 2026-04-15
sources: []
---

# Cross-Typology Mapping Framework

## Overview

Proposed pipeline for experimenting with bridges between three typological systems (Temporistics, Psychosophy, Socionics) and more mainstream trait/persona frameworks. This page records project architecture ideas, not an established mapping standard.

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────┐
│  CROSS-TYPOLOGY MAPPING LAYER                         │
│                                                         │
│  Temporistics (24 types) ──→ MBTI/Jungian (16 types)  │
│  Psychosophy (81 types)  ──→ MBTI/Jungian (16 types)  │
│  Socionics (16 types)    ──→ MBTI/Jungian (16 types) │
│                        ↓                                │
│              PersonaNexus (trait bridge)                │
│              OCEAN ↔ DISC ↔ Jungian ↔ Custom          │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  SIMULATION LAYER (JPAF)                               │
│                                                         │
│  Triple mechanisms:                                     │
│  - Dominant-Auxiliary Coordination (personality core)  │
│  - Reinforcement-Compensation (context adaptation)      │
│  - Reflection Mechanism (long-term evolution)           │
│                                                         │
│  100% MBTI alignment, >90% type activation             │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  SOCIAL INTERACTION LAYER (OASIS-sim)                  │
│                                                         │
│  - 1M agent social simulation                          │
│  - Twitter/Reddit platform models                      │
│  - Dynamic networks, recommendation algorithms          │
│  - Group polarization, herd effects                    │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  EMPIRICAL VALIDATION LAYER (OASIS-platform)          │
│                                                         │
│  - AI-powered survey interviews                         │
│  - Voice and text chat agents                          │
│  - Semi-structured interview guides                   │
│  - Multi-provider LLM support                          │
│  - FAIR-compliant data export                           │
└─────────────────────────────────────────────────────────┘
```

## Cross-System Mapping

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

### Psychosophy → MBTI (Hypothesized)

4-aspect structure maps through function weighting:

| Psychosophy Pattern | Possible MBTI-Like Echo | Notes |
|--------------------|--------------------------|-------|
| Logic-heavy | Thinking emphasis | Approximate only |
| Emotion-heavy | Feeling emphasis | Approximate only |
| Physics-heavy | Sensing emphasis | Approximate only |
| Will-heavy | Judgment / agency emphasis | Approximate only |

## Validation Hypothesis Examples

### H1: Dual Socionics pairs show higher JPAF-measured harmony
- **Method:** JPAF simulates 100 conversations per pair
- **Metric:** Reflection score, reinforcement-compensation balance
- **Expected:** Duality > Activation > Mirage

### H2: Temporistics Present types prefer real-time communication
- **Method:** OASIS-sim measures message timing, response patterns
- **Metric:** Latency correlation with temporal frame
- **Expected:** test whether Present-heavy profiles respond faster in synchronous settings

### H3: Combined Temporistics + Socionics predicts satisfaction better than either alone
- **Method:** OASIS-platform interviews 200 couples
- **Metric:** Multi-factor regression, cross-validated
- **Expected:** test whether combined features improve prediction over single-system baselines

## Vendor Tools Reference

### PersonaNexus
- **Purpose:** Declarative personality definition with framework mapping
- **Key features:** OCEAN↔DISC↔Jungian bidirectional, YAML identity files, archetype inheritance
- **Command:** `pip install personanexus`
- **Example:** `personanexus personality jungian-to-traits --preset intj`

**Audit note:** Vendor/source verification for this tooling stack is incomplete in the current repo; treat these tool references as exploratory pointers.

### JPAF (Jungian Personality Adaptation Framework)
- **Purpose:** LLM personality simulation with triple mechanisms
- **Key features:** 100% MBTI alignment, type activation >90%, personality evolution
- **Install:** `conda create -n jpaf python=3.10 && pip install -r requirement.txt`
- **Example:** `python personality_test.py --method=test --mbti_num=16 --model=QWEN`

### OASIS-sim (Social Simulation)
- **Purpose:** 1M agent social media simulation
- **Key features:** Twitter/Reddit models, dynamic networks, 23 actions
- **Install:** `git clone https://github.com/camel-ai/oasis && poetry install`
- **Example:** Replicates information spread, group polarization, herd effects

### OASIS-platform (Survey Interviews)
- **Purpose:** AI-powered qualitative interviews
- **Key features:** Voice/text agents, multi-LLM, Docker deploy, FAIR-compliant
- **Install:** `git clone https://github.com/oasis-surveys/oasis-platform && docker compose up`
- **License:** Open Non-Commercial Research License v1.0

## Next Steps

1. **Verify Socionics→MBTI mapping** using PersonaNexus archetypes
2. **Hypothesize Temporistics→MBTI** based on aspect patterns
3. **Test with JPAF:** Run compatibility simulation for 16 MBTI pairs
4. **Validate with OASIS-sim:** Social dynamics of typed agents
5. **Empirical check:** OASIS-platform interviews with typed participants
