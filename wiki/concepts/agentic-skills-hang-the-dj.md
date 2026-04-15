---
title: Agentic Skills for Simulation-Based Compatibility Testing
type: concept
tags: [skills, architecture, hang-the-dj, simulation, agents]
created: 2026-04-15
updated: 2026-04-15
sources: [skills/index.md]
---

# Agentic Skills for "Hang the DJ" Implementation

## Overview

Eight specialized agent skills that, combined, implement the simulation-based compatibility testing seen in Black Mirror's "Hang the DJ". Each skill handles a specific part of the pipeline from persona creation to user explanation.

## Skill Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     ORCHESTRATOR                            │
│                                                              │
│  persona-cloner → simulation-runner → choice-tracker       │
│         ↑                                    ↓              │
│         │              memory-persister                    │
│         │                    ↓                              │
│         └────────── compatibility-scorer                   │
│                             ↓                               │
│                    explanation-generator                      │
│                             ↓                               │
│                        USER OUTPUT                          │
└─────────────────────────────────────────────────────────────┘
```

## Core Skills

### 1. persona-cloner

Creates a digital twin (agent) from real user data.

**Input:** Interview transcript, questionnaire, or existing assessment (Big Five, MBTI, Socionics)
**Output:** Agent with consistent behavioral policies and validated personality

**Key capability:** Cross-system type mapping (Big Five ↔ MBTI ↔ Socionics)

**Validation target:** 5.6/7.0 (CogniPair benchmark)

### 2. simulation-runner

Executes multi-agent scenarios at scale.

**Configuration:**
- `total_runs: 1000` — Number of simulations per pair
- `parallel_execution: true` — Run multiple simultaneously
- `max_parallel: 50` — Batch size for parallel runs
- `memory_persistence: "persistent"` — Cross-run memory

**Output per run:** Transcript, final choices, timing metrics

### 3. choice-tracker

Logs all decisions made by agents across multiple runs.

**Core metric:** `Repeated Choice Score`
```
Compatibility = (Times Chose Each Other / Total Scenarios) × 100
```

**Tracked decisions:**
- `accept_assigned` / `reject_assigned`
- `seek_reunion` / `stay_loyal`
- `switch_partner` / `express_preference`

### 4. compatibility-scorer

Calculates final "99.8%" from tracked choices.

**Scoring components:**
1. **Base score** — Raw mutual choice percentage
2. **Adversarial bonus** — Weight for choices under pressure
3. **Consistency bonus** — Reward for stable choices over time
4. **Alignment bonus** — Reward for mutual agreement

**Thresholds:**
| Score | Signal |
|-------|--------|
| 95-100% | Very Strong |
| 85-94% | Strong |
| 70-84% | Moderate |
| 50-69% | Weak |
| <50% | Very Weak |

### 5. explanation-generator

Transforms percentage into user-understandable narrative.

**Template for 95%+:**
> "In our simulation, your digital versions met 1,000 times in different scenarios. Every time, they found their way back to each other. When we made it difficult — separated them, created tempting alternatives — they chose each other anyway. That's not chemistry. That's repeated choice."

## Support Skills

### 6. type-mapper

Translates personality types between systems.

**Supported mappings:**
- MBTI ↔ Socionics (established, 0.95 confidence)
- Big Five ↔ MBTI (approximate, 0.8 confidence)
- Socionics → Temporistics (theoretical, requires validation)

### 7. adversarial-designer

Creates scenarios that test compatibility under pressure.

**Scenario types:**
- `forced_separation` — Short duration, then forced to new partners
- `better_option` — Introduce seemingly "better" compatible partner
- `distance_test` — Separation with local alternative
- `system_interference` — App "recommends" breaking up

**Key metric:** `rebellion_score` — How much agent resisted system assignment

### 8. memory-persister

Maintains agent memory across simulation runs.

**Memory layers:**
1. **Episodic** — "Remember: we chose each other in run 5"
2. **Semantic** — "Know: I prefer people like B"
3. **Identity Core** — "Am: Loyal to my choices" (immutable)

**Critical for:** "Hang the DJ" effect where agents remember past choices

## Connection to Research

### CogniPair Foundation

CogniPair (ICLR 2026) provides the base architecture:
- GNWT-Agent with 5 cognitive modules
- 72% correlation with human attraction patterns
- 77.8% match prediction accuracy

Our skills extend CogniPair with:
- Adversarial scenario design (missing in CogniPair)
- Repeated choice metric (novel)
- Cross-system type mapping (Socionics/Temporistics)

### "Hang the DJ" Philosophy

The series teaches us:
1. **Test under adversity** — Not comfort, but resistance to system pressure
2. **Repeated choice > single match** — 998/1000 > 100/100
3. **Rebellion is signal** — Choosing each other despite interference = real compatibility
4. **Simulation reveals truth** — What questionnaires miss, behavior shows

## Implementation Priority

### Phase 1: MVP (1-2 weeks)
```
persona-cloner + simulation-runner + choice-tracker + compatibility-scorer
```
- 2 typed personas
- 100 simple scenarios
- Basic compatibility score

### Phase 2: Full Core (1 month)
```
+ adversarial-designer + memory-persister + type-mapper + explanation-generator
```
- 1000 runs with pressure scenarios
- Cross-run memory
- User-friendly output

### Phase 3: Research (ongoing)
```
+ typology-tester + validation-harness
```
- Test Socionics/Temporistics hypotheses
- Compare simulation vs real-world outcomes
