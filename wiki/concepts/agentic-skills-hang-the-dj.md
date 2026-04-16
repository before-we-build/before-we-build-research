---
title: Agentic Skills for Simulation-Based Compatibility Testing
type: concept
tags: [skills, architecture, hang-the-dj, simulation, agents, exploratory]
created: 2026-04-15
updated: 2026-04-15
sources: [skills/index.md, arxiv.org/abs/2506.03543, arxiv.org/abs/2512.11844]
---

# Agentic Skills for "Hang the DJ" Implementation

## Research Foundation

| Paper | Venue | Key Contributions |
|-------|-------|------------------|
| **CogniPair** | arXiv preprint (2025) | GNWT-style agent architecture, reported attraction correlation |
| **Love First, Know Later** | workshop/preprint | 3-phase pipeline, observer idea, reward-style scoring |
| **Bradley-Terry style ranking** | modeling approach | Pairwise comparison as a useful scoring tool |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     ORCHESTRATOR                            │
│                                                              │
│  persona-cloner → global-workspace → simulation-runner     │
│         │                                    ↓              │
│         │              memory-persister (4 layers)         │
│         │                        ↓                          │
│         └────────────── choice-tracker                     │
│                            ↓                               │
│                    compatibility-scorer (simulation score) │
│                            ↓                               │
│                    explanation-generator                    │
└─────────────────────────────────────────────────────────────┘
```

## Core Skills (12 Total)

### Persona & Cognition

| Skill | Purpose | Research Source |
|-------|---------|----------------|
| `persona-cloner` | Digital twins with GNWT weights | CogniPair |
| `persona-generator` | Structured → persona narrative | Project synthesis |
| `global-workspace` | GNWT broadcast mechanism | CogniPair |
| `type-mapper` | Cross-system translation | — |

### Simulation & Analysis

| Skill | Purpose | Research Source |
|-------|---------|----------------|
| `simulation-runner` | Execute 1000+ scenarios | Love First |
| `observer-agent` | External LLM analysis | Love First |
| `adversarial-designer` | Pressure scenarios | Original |
| `reward-model` | Compatibility as reward function | Love First + Pairadigm |

### Persistence & Output

| Skill | Purpose | Research Source |
|-------|---------|----------------|
| `memory-persister` | 4-layer memory (project architecture) | — |
| `choice-tracker` | Log repeated choices | Original |
| `compatibility-scorer` | Calculate simulation score | — |
| `explanation-generator` | User-friendly output | — |

## Key Research Insights

### CogniPair: GNWT-Agent

```
Each agent has 5 cognitive modules:
- Emotion Module ← Neuroticism (N)
- Memory Module ← Openness (O)
- Planning Module ← Conscientiousness (C)
- SocialNorms Module ← Agreeableness (A)
- GoalTracking Module ← Extraversion (E)

All process in parallel, integrated via global workspace.
```

### Love First, Know Later: 3 Phases

```
Phase 1: Persona Generation
  Generator model → persona narrative

Phase 2: Interaction Simulation
  Mistral-Nemo (temp=0.6) → Multi-turn conversation

Phase 3: Compatibility Assessment
  LLM Participant (self-rating) + LLM Observer (external) → Score
```

### Love First: Reward Model

```
Compatibility = Reward Modeling Problem

Hypothesis 1: Sparse Rewards
  Relationships determined by CRITICAL MOMENTS, not daily conversation

Hypothesis 2: Deterministic Decisions
  In critical moments, people show consistent (low-entropy) behavior

Theorem: As LLM policy → human policy:
  Prediction → Optimal stable matching
```

### Memory: 4 Layers (Project Architecture)

```
Layer 1: Working (ephemeral) — Current context, partial plan
Layer 2: Semantic (session) — "I prefer people like B"
Layer 3: Episodic (long-term) — "We chose each other in run 5"
Layer 4: Identity (immutable) — "I trust my feelings over system"
```

## LLM Parameters

| Use Case | Model | Temperature | Max Tokens |
|----------|-------|-------------|------------|
| Persona Generation | Gemini 2.5 Flash Lite | 0.8 | — |
| Conversation | Mistral-Nemo | 0.6 | 200 |
| GNWT Processing | gpt-4o | 0.9 | 200 |
| Observer Analysis | gpt-4o | 0.3 | — |
| Participant Rating | gpt-4o | 0.7 | — |

## "Hang the DJ" Specific Features

### Repeated Choice Metric

```
Score = (Mutual Choices / Total Runs) × 100

Example: 820/1000 = 82.0%
```

### Adversarial Scenarios

- Forced separation
- "Better" alternatives
- System interference
- Pressure points

### Cross-Run Memory

Critical for repeated choice effect:
- Agent remembers previous interactions
- Preferences evolve based on experience
- Identity core remains stable

## Implementation Priority

### Phase 1: MVP (1 week)
```
persona-generator + persona-cloner + simulation-runner + choice-tracker
```

### Phase 2: Research (1 month)
```
+ global-workspace + observer-agent + reward-model + memory-persister
```

### Phase 3: Production
```
+ adversarial-designer + compatibility-scorer + explanation-generator
```

## Validation

| Metric | Benchmark | Target |
|--------|-----------|--------|
| Persona accuracy | Pilot-defined human validation | Set in own study |
| Correlation | CogniPair (real human patterns) | 72% |
| Match prediction | CogniPair | 77.8% |
| Repeated choice | Hang the DJ inspiration | Fictional example, not benchmark |
