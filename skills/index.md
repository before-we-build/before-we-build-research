# SKILL INDEX: Hang the DJ Implementation

## Based on Research

## Researcher Attraction Skills

These are the minimum `Claude-style` modular skills needed before serious researcher outreach.

### Core Outreach Layer

| Skill | Purpose | Why It Matters |
|-------|---------|----------------|
| `researcher-outreach-workflow` | Orchestrate the full outreach cycle | Turns isolated skills into a repeatable pipeline |
| `researcher-targeter` | Find and rank the right researchers/labs | Avoid generic outreach and wasted contacts |
| `research-bridge-builder` | Translate project language into research language | Makes the project legible outside typology circles |
| `evidence-packager` | Build a short evidence packet | Lets researchers assess the project quickly |
| `outreach-personalizer` | Write target-specific outreach | Converts overlap into actual responses |
| `collaboration-ask-designer` | Turn interest into one concrete ask | Lowers friction to engage |
| `objection-handler` | Handle pseudoscience / validation / ethics objections | Prevents the pitch from collapsing on first contact |

### Existing Skills That Support Outreach

| Existing Skill | How It Helps |
|----------------|--------------|
| `type-mapper` | Helps explain where mappings are approximate and where they are not |
| `persona-validator` | Shows that persona fidelity is treated as a measurable issue |
| `explanation-generator` | Helps produce readable, non-hype project explanations |

### AI/Dating Research

| Paper | Key Contributions | Skills Informed |
|-------|------------------|----------------|
| CogniPair (arXiv preprint, 2025) | GNWT-style agent architecture, reported attraction correlation | `global-workspace`, `persona-cloner`, `memory-persister` |
| Love First, Know Later (workshop/preprint) | 3-phase pipeline, observer idea, reward-style scoring | `persona-generator`, `simulation-runner`, `reward-model`, `observer-agent` |
| Bradley-Terry style ranking | Pairwise comparison as a useful modeling tool | `reward-model` |

### Psychology Research

| Paper | Key Contributions | Skills Informed |
|-------|------------------|----------------|
| Scientific Reports (2025) | GPT-4 emulates constrained Big Five questionnaire responses with high consistency | `persona-generator`, `persona-validator` |
| LLM simulation methodology | Richer persona prompts may help, but no fixed minimum length is established | `persona-generator` |
| arXiv: Psychometric Approach | BFI-2 prompts > simple adjectives | `persona-generator` |
| Frontiers: Psypilot (2026) | Copilot / decision-support framing with human oversight | All (positioning) |
| arXiv: S-Researcher (2026) | Large-scale agent orchestration is technically plausible | `compatibility-scorer` |
| Current Psychology (2025) | AI benchmarking can help generate hypotheses before human validation | Validation pipeline |
| Persona-drift concern | Consistency testing is a project safeguard, not a settled benchmark | `persona-validator` |

---

## Core Skills (Required)

### 1. persona-cloner
**Creates digital twins with GNWT module weights**

| Aspect | Value |
|--------|-------|
| Input | Big Five, MBTI, Socionics |
| Output | GNWT-Agent with module weights |
| Benchmark | Pilot-defined persona quality threshold |
| LLM | gpt-4o, temp=0.9 |

### 2. persona-generator
**Converts BFI-2 → structured persona prompts**

| Aspect | Value |
|--------|-------|
| Input | BFI-2 scores (validated personality scales) |
| Output | Structured persona narrative / prompt packet |
| Model | Gemini 2.5 Flash Lite |
| Based on | Huang et al. (psychometric approach) |

**Key rules:**
- Use sufficiently rich, standardized persona prompts
- Test whether demographics help for the specific task
- Use all 5 Big Five dimensions

### 3. persona-validator ⭐ NEW
**Tests persona consistency, detects drift**

| Aspect | Value |
|--------|-------|
| Method | Pre/post Big Five assessment |
| Drift threshold | 0.2 (regenerate if higher) |
| Based on | Project validation safeguard |

### 4. global-workspace
**Implements GNWT broadcast mechanism**

| Aspect | Value |
|--------|-------|
| Modules | Emotion, Memory, Planning, SocialNorms, GoalTracking |
| Integration | `Response = Σ α·R_M + β·G(GW)` |
| Based on | CogniPair Figure 5 |

### 5. simulation-runner
**Executes multi-agent scenarios at scale**

| Aspect | Value |
|--------|-------|
| Phase 1 | Persona generation (Gemini) |
| Phase 2 | Conversation (Mistral-Nemo, temp=0.6) |
| Phase 3 | Assessment (LLM Observer + Participant) |
| Memory | Persistent across runs (Hang the DJ) |

**Updated:** Working defaults informed by recent papers, not fixed research constants

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
| Output | Simulation-derived reunion / selection rate |
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

**Updated:** 4-layer architecture as a working project choice

### 9. compatibility-scorer
**Produces final simulation-derived score**

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
│  │ choice-tracker │ → Log repeated choices                 │
│  └───────┬────────┘                                         │
│          │                                                  │
│          ▼                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           compatibility-scorer                       │   │
│  │           → simulation score                      │   │
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
├── persona-generator.md        # Structured persona prompts ⭐ NEW
├── global-workspace.md         # GNWT broadcast mechanism ⭐ NEW
├── simulation-runner.md       # Execute scenarios
├── observer-agent.md           # External LLM analysis ⭐ NEW
├── adversarial-designer.md     # Pressure scenarios
├── reward-model.md            # Compatibility as reward ⭐ NEW
├── choice-tracker.md          # Log decisions
├── memory-persister.md        # 4-layer memory
├── compatibility-scorer.md     # Calculate simulation score
├── explanation-generator.md    # User output
└── type-mapper.md             # Cross-system translation
```
