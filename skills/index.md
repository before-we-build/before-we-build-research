# SKILL INDEX: Hang the DJ Implementation

## Based on Research

| Paper | Key Contributions | Skills Informed |
|-------|------------------|----------------|
| CogniPair (ICLR 2026) | GNWT-Agent, 72% correlation, 5 cognitive modules | `global-workspace`, `persona-cloner`, `memory-persister` |
| Love First, Know Later (NeurIPS 2025) | 3-phase pipeline, LLM Observer, reward modeling | `persona-generator`, `simulation-runner`, `reward-model`, `observer-agent` |
| Pairadigm (2026) | Bradley-Terry, CGCoT, pairwise comparison | `reward-model` |
| 2026 Agent Memory (Best Practices) | 4-layer memory architecture | `memory-persister` |

---

## Core Skills (Required)

### 1. persona-cloner
**Creates digital twins with GNWT module weights**

| Aspect | Value |
|--------|-------|
| Input | Big Five, MBTI, Socionics |
| Output | GNWT-Agent with module weights |
| Benchmark | 5.6/7.0 (CogniPair) |
| LLM | gpt-4o, temp=0.9 |

**Updated:** Now includes GNWT module weight initialization

### 2. global-workspace ⭐ NEW
**Implements GNWT broadcast mechanism**

| Aspect | Value |
|--------|-------|
| Modules | Emotion, Memory, Planning, SocialNorms, GoalTracking |
| Integration | `Response = Σ α·R_M + β·G(GW)` |
| Based on | CogniPair Figure 5 |

### 3. persona-generator ⭐ NEW
**Converts structured data → 300-500 word narratives**

| Aspect | Value |
|--------|-------|
| Input | Structured scores |
| Output | Narrative for LLM roleplay |
| Model | Gemini 2.5 Flash Lite |
| Based on | Love First, Know Later |

### 4. simulation-runner
**Executes multi-agent scenarios at scale**

| Aspect | Value |
|--------|-------|
| Phase 1 | Persona generation (Gemini) |
| Phase 2 | Conversation (Mistral-Nemo, temp=0.6) |
| Phase 3 | Assessment (LLM Observer + Participant) |
| Memory | Persistent across runs (Hang the DJ) |

**Updated:** Real LLM parameters from research

### 5. observer-agent ⭐ NEW
**External LLM analyzes conversations**

| Aspect | Value |
|--------|-------|
| Input | Full transcript |
| Output | Compatibility scores (engagement, flow, signals) |
| Model | gpt-4o, temp=0.3 |
| Based on | Love First, Know Later |

### 6. choice-tracker
**Logs decisions across 1000+ runs**

| Aspect | Value |
|--------|-------|
| Metric | "Did they choose each other?" |
| Output | 99.8% = 998/1000 |
| Critical for | Hang the DJ effect |

### 7. reward-model ⭐ NEW
**Compatibility as reward function**

| Aspect | Value |
|--------|-------|
| Framework | Inverse RL + Bradley-Terry |
| Signals | Engagement, flow, attraction, comfort |
| Training | Columbia dataset, Divorce dataset |
| Based on | Love First + Pairadigm |

### 8. memory-persister
**4-layer memory architecture**

| Layer | Content | Persistence |
|-------|---------|-------------|
| 1 | Working memory | Ephemeral |
| 2 | Semantic memory | Session |
| 3 | Episodic memory | Long-term |
| 4 | Identity core | Immutable |

**Updated:** 4-layer architecture from 2026 best practices

### 9. compatibility-scorer
**Produces final "99.8%" score**

| Aspect | Value |
|--------|-------|
| Input | Choice tracker + Observer + Participant |
| Output | Final percentage + breakdown |
| Thresholds | 95%+ = Very Strong |

### 10. explanation-generator
**User-friendly output**

| Aspect | Value |
|--------|-------|
| Format | "You keep finding each other" |
| Method | Explains simulation approach |
| Honesty | No false destiny claims |

---

## Orchestration

```
┌─────────────────────────────────────────────────────────────┐
│                     ORCHESTRATOR                              │
│                                                              │
│  ┌────────────────┐                                         │
│  │ persona-       │ → persona-generator → persona-cloner   │
│  │ cloner         │ → global-workspace                      │
│  └───────┬────────┘                                         │
│          │                                                  │
│          ▼                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           simulation-runner (1000x)                  │   │
│  │                                                      │   │
│  │  agent_a ←→ agent_b  (GNWT processing)             │   │
│  │      ↓              ↓                               │   │
│  │  global-workspace   (parallel modules)              │   │
│  │      ↓                                               │   │
│  │  memory-persister  (cross-run memory)              │   │
│  │      ↓                                               │   │
│  │  observer-agent  (external analysis)                │   │
│  │      ↓                                               │   │
│  │  reward-model  (compatibility score)               │   │
│  └─────────────────────────────────────────────────────┘   │
│          │                                                  │
│          ▼                                                  │
│  ┌────────────────┐                                         │
│  │ choice-tracker │ → Log 998/1000 choices                 │
│  └───────┬────────┘                                         │
│          │                                                  │
│          ▼                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           compatibility-scorer                       │   │
│  │           → 99.8%                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│          │                                                  │
│          ▼                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           explanation-generator                      │   │
│  │           → "You keep finding each other"          │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### MVP (1 week)
```
persona-cloner + persona-generator + simulation-runner + choice-tracker
```
- 2 typed personas
- 100 simple scenarios
- Basic compatibility score

### Research Version (1 month)
```
All 10 skills
```
- Full GNWT implementation
- 1000 runs with persistent memory
- LLM Observer + Participant scoring
- Reward model trained on Columbia data

---

## LLM Parameters Reference

| Use | Model | Temperature | Max Tokens |
|-----|-------|-------------|------------|
| Persona Generation | Gemini 2.5 Flash Lite | 0.8 | — |
| Conversation | Mistral-Nemo | 0.6 | 200 |
| GNWT Processing | gpt-4o | 0.9 | 200 |
| Observer Analysis | gpt-4o | 0.3 | — |
| Participant Rating | gpt-4o | 0.7 | — |

---

## File Locations

```
skills/
├── index.md                    # This file
├── persona-cloner.md           # Create digital twins with GNWT
├── persona-generator.md        # 300-500 word narratives ⭐ NEW
├── global-workspace.md         # GNWT broadcast mechanism ⭐ NEW
├── simulation-runner.md       # Execute scenarios
├── observer-agent.md           # External LLM analysis ⭐ NEW
├── adversarial-designer.md     # Pressure scenarios
├── reward-model.md            # Compatibility as reward ⭐ NEW
├── choice-tracker.md          # Log decisions
├── memory-persister.md        # 4-layer memory
├── compatibility-scorer.md     # Calculate 99.8%
├── explanation-generator.md    # User output
└── type-mapper.md             # Cross-system translation
```
