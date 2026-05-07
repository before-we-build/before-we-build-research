# Consolidated Action Plan: Cognitive Matchmaker

**Last Updated:** 2026-04-15
**Status:** Research scan complete — several claims still need ongoing source tightening during implementation

---

## Executive Summary

Build a simulation-based dating concierge that:
1. Creates digital twins from personality assessments (BFI-2 validated)
2. Runs adversarial scenarios (Hang the DJ style)
3. Scores compatibility via repeated choice metric
4. Validates against real-world outcomes

**Core Principle:** AI as Copilot, not Oracle — human validates, AI suggests

**MVP Cost:** See `mvp-cost-estimation.md` for illustrative ballpark only; recompute before build
**Research Foundation:** CogniPair + Love First + Psychology Research

---

## Part 1: What We Have

### AI/Dating Research

| Paper | Key Finding | Confidence |
|-------|-------------|------------|
| CogniPair (arXiv preprint, 2025) | GNWT-style agent architecture with reported attraction correlation | Medium |
| Love First, Know Later (arXiv preprint / NeurIPS 2025 workshop) | Simulation-first compatibility evaluation as a promising design direction | Medium |
| Bradley-Terry style ranking | Pairwise comparison as a useful scoring approach | Medium |

### Psychology Research (NEW)

| Paper | Key Finding | Application |
|-------|-------------|-------------|
| Scientific Reports (2025) | GPT-4 emulates constrained Big Five questionnaire responses with high consistency | Persona quality |
| LLM psych simulation methodology | Richer personas may help, but no fixed minimum length is validated | Persona depth |
| Psychometric Approach (preprint) | BFI-2-style prompts outperform simple adjectives on some measures | Persona method |
| Frontiers: Psypilot (2026) | Decision-support / copilot framing with human oversight | Positioning |
| S-Researcher (preprint, 2026) | Large-scale agent orchestration with human oversight is technically plausible | Architecture |
| Current Psychology (2025) | AI benchmarking can help generate hypotheses before human validation | Validation method |

### Key Insights from Psychology Research

1. **BFI-2 > Simple Prompts** — Use validated personality scales, not just adjectives
2. **Persona detail matters** — richer prompts may improve simulation, but length should be tuned empirically
3. **AI Inflates Moral Ratings** — Need calibration against human baseline
4. **Consistency Test Recommended** — verify stability rather than assuming the persona holds
5. **Copilot > Oracle** — Position as suggestion system, not decision-maker
6. **AI for Hypothesis → Humans for Validation** — Pilot with AI, verify with real pairs

---

## Part 2: MVP Scope

### What to Build (MVP-1)

```
┌─────────────────────────────────────────────────────────────┐
│                     MVP-1: Hang the DJ Test                  │
│                                                              │
│  Core Principle: AI as Copilot, not Oracle                   │
│                                                              │
│  Pipeline:                                                   │
│  1. BFI-2 Assessment → Detailed Persona Prompt               │
│  2. Pre-simulation Consistency Test                          │
│  3. 100 Adversarial Scenarios                               │
│  4. Post-simulation Consistency Test                         │
│  5. Repeated Choice Scoring (simulation-derived)            │
│  6. Human Validation of Output                               │
│                                                              │
│  Output: "Compatibility hypothesis — verify in real"         │
└─────────────────────────────────────────────────────────────┘
```

### What NOT to Build (Yet)

- Fully autonomous matching
- AI making decisions without human review
- Mass dating pool integration
- Automatic messaging
- Calendar booking

---

## Part 3: Skills (12 Total)

```
skills/
├── persona-generator.md        # BFI-2 based persona prompts
├── persona-cloner.md          # GNWT weights from Big Five
├── persona-validator.md      # Pre/post consistency test ⭐ NEW
├── global-workspace.md         # GNWT broadcast mechanism
├── simulation-runner.md        # 3-phase pipeline
├── observer-agent.md          # External LLM analysis
├── adversarial-designer.md     # Pressure scenarios
├── reward-model.md            # Bradley-Terry + IRL
├── choice-tracker.md           # Repeated choices
├── memory-persister.md         # 4-layer memory
├── compatibility-scorer.md      # Simulation-derived score
└── explanation-generator.md     # "Hypothesis" output
```

---

## Part 4: Persona Generation — Research-Backed Method

### The Problem

Simple prompts like "You are an introverted person" produce inconsistent, shallow personas.

### The Solution: BFI-2 Based Approach

Based on Huang et al. (2025) — Psychometric Approach:

```python
# Input: BFI-2 scores
persona_input = {
    "openness": {"score": 0.7, "items": [...]},
    "conscientiousness": {"score": 0.8, "items": [...]},
    "extraversion": {"score": 0.3, "items": [...]},
    "agreeableness": {"score": 0.6, "items": [...]},
    "neuroticism": {"score": 0.2, "items": [...]},
    "demographics": {"age": 28, "gender": "female", "occupation": "engineer"}
}

# Output: structured persona narrative / prompt packet
persona_narrative = generate_persona(persona_input)
```

### Validation Chain

```
BFI-2 Assessment → Prompt Engineering → LLM Persona → Validation

Step 1: BFI-2 gives validated personality dimensions
Step 2: Prompt includes all 5 dimensions + demographics
Step 3: Generate standardized persona narrative
Step 4: Validate with user: "Does this describe you?" (use pilot data to set thresholds)
```

### Critical Rules

1. **Use sufficient detail** — treat persona depth as an empirical tuning variable, not a fixed rule
2. **Test demographics carefully** — added context may help some tasks but can also distort outputs
3. **Use all 5 dimensions** — Don't skip neuroticism or agreeableness
4. **Validate output** — User rates persona accuracy

---

## Part 5: Persona Consistency Testing

### The Problem

LLM personas can drift — starting as one type, ending as another.

Source posture: recent persona-modeling work suggests drift is a real concern, but exact reduction figures should not be treated as settled benchmarks here

### The Solution: Pre/Post Assessment

```python
def consistency_test(persona_narrative):
    # Pre-simulation: Test persona stability
    pre_assessment = assess_personality(persona_narrative)
    
    # Run 10 interactions
    interactions = run_test_conversations(persona_narrative, n=10)
    
    # Post-simulation: Did persona drift?
    post_assessment = assess_personality(persona_narrative)
    
    # Calculate drift
    drift = calculate_personality_distance(pre_assessment, post_assessment)
    
    # If drift > threshold, regenerate persona
    if drift > 0.2:
        return regenerate_persona(persona_narrative)
    
    return persona_narrative, drift
```

### Validation Criteria

| Drift Score | Action |
|-------------|--------|
| < 0.1 | Excellent — persona stable |
| 0.1 - 0.2 | Acceptable — note in output |
| > 0.2 | Regenerate persona |

---

## Part 6: Validation Methodology

### The Problem

AI simulation ≠ real-world outcomes. Need systematic validation.

### The Solution: AI for Hypothesis → Humans for Validation

Based on recent methodology papers and case studies on AI benchmarking and simulation:

```
┌─────────────────────────────────────────────────────────────┐
│  Validation Pipeline                                          │
│                                                              │
│  Phase 1: AI Simulation (cheap, fast)                       │
│  ├── Run 100 scenarios per pair                             │
│  ├── Calculate repeated-choice score                         │
│  └── Output: "Hypothesis: 87% compatible"                   │
│                                                              │
│  Phase 2: Human Pilot (expensive, slow)                      │
│  ├── Recruit 10-20 real pairs                              │
│  ├── Collect actual dates                                    │
│  ├── Compare simulation to reality                           │
│  └── Calibrate prediction model                             │
│                                                              │
│  Phase 3: Ongoing (continuous improvement)                  │
│  ├── Collect feedback after each real date                   │
│  ├── Retrain/adjust scoring weights                         │
│  └── Improve future predictions                              │
└─────────────────────────────────────────────────────────────┘
```

### Ablation Tests

| Test | What It Measures |
|------|----------------|
| Profile matching only | Baseline (current dating apps) |
| + Typology features | Socionics contribution |
| + Simulation | Simulation contribution |
| Full pipeline | Total accuracy |

Goal: test whether simulation features improve predictive performance over profile-only baselines

---

## Part 7: Implementation Roadmap

### Phase 0: Foundation (Week 1)

**Goal:** Technical stack ready

| Task | Deliverable |
|------|-------------|
| Setup Python project | `poetry init`, dependencies |
| LLM abstraction | `llm.py` with model switching |
| BFI-2 schema | `schemas/persona.py` with Big Five |
| Assessment form | BFI-2 questionnaire integration |
| Unit tests | Basic test suite |

**Cost:** $0
**Time:** 4-8h

### Phase 1: Persona Pipeline (Week 2)

**Goal:** BFI-2 → Validated persona

| Task | Deliverable | Research Source |
|------|-------------|----------------|
| BFI-2 to prompt | Structured → prompt | Huang et al. |
| Persona generator | Structured persona narrative | LLM simulation methodology |
| Consistency test | Pre/post assessment | Project validation choice |
| User validation | "Rate 1-7" interface | CogniPair |
| Socionics mapping | MBTI → Socionics | Type Mapper |

**Cost:** ~$0.10
**Time:** 8-16h

### Phase 2: Simulation (Week 3)

**Goal:** Run multi-turn conversations

| Task | Deliverable |
|------|-------------|
| Turn loop | 10-turn conversation |
| Memory injection | Cross-turn context |
| Parallel execution | Batch processing |
| Transcript logging | JSONL storage |

**Cost:** ~$2.00 (100 conversations)
**Time:** 16-24h

### Phase 3: Adversarial Scenarios (Week 4)

**Goal:** Test under pressure

| Task | Deliverable |
|------|-------------|
| Scenario designer | Forced separation, better option, distance |
| Stress injection | Escalating pressure |
| Choice tracking | accept/reject, seek_reunion, stay_loyal |
| Rebellion score | Did they resist system? |

**Cost:** ~$0.50
**Time:** 8-16h

### Phase 4: Scoring & Output (Week 5)

**Goal:** Hypothesis, not oracle

| Task | Deliverable |
|------|-------------|
| Repeated choice metric | Simulation-derived reunion / selection rate |
| Observer analysis | External compatibility assessment |
| Calibration | Adjust for AI inflation |
| Explanation | "Hypothesis: likely compatible — verify in real" |

**Key:** Output as hypothesis, not verdict

**Cost:** ~$0.10
**Time:** 8-16h

### Phase 5: Human Validation (Week 6-8)

**Goal:** Verify simulation predicts reality

| Task | Method | Deliverable |
|------|--------|-------------|
| Recruit pairs | Partner pool | 10-20 real pairs |
| Run simulation | Full pipeline | Hypotheses |
| Collect dates | Real-world | Ground truth |
| Compare | Correlation | Score calibration |

**Cost:** ~$5.00 + recruitment effort
**Time:** 40-60h

---

## Part 8: Technical Architecture

### Stack

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (Streamlit MVP)                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Layer (FastAPI)                     │
│                                                              │
│  POST /assessments/bfi2     → BFI-2 questionnaire          │
│  POST /personas             → Generate validated persona  │
│  POST /simulate             → Run 100 scenarios          │
│  GET  /compatibility        → Hypothesis + explanation     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Simulation Engine                          │
│                                                              │
│  bfi2_to_persona()      (BFI-2 → standardized persona prompt)│
│  consistency_test()       (Pre/post personality stability)   │
│  simulation_runner()       (100 adversarial scenarios)       │
│  choice_tracker()         (Repeated choice metric)           │
│  observer_agent()        (External analysis)                │
│  compatibility_scorer()   (Calibrated score)               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       Storage (SQLite MVP)                   │
│                                                              │
│  assessments/          BFI-2 responses                     │
│  personas/              Generated + validated personas      │
│  transcripts/            Full simulation logs               │
│  outcomes/               Real-world validation data         │
└─────────────────────────────────────────────────────────────┘
```

### LLM Parameters (Research-Backed)

| Task | Model | Temperature | Source |
|------|-------|-------------|--------|
| Persona Generation | Gemini 2.5 Flash Lite | 0.8 | Love First |
| Consistency Test | gpt-4o-mini | 0.3 | Cheap + reliable |
| Conversation | Mistral-Nemo | 0.6 | Love First |
| Observer | gpt-4o | 0.3 | Low variance |
| Calibration | gpt-4o | 0.2 | Precise |

---

## Part 9: Success Metrics

### Simulation Quality

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Persona accuracy | Working pilot threshold | User rating |
| Consistency drift | <0.2 | Pre/post assessment |
| Token cost per pair | <$0.10 | API logs |

### Prediction Accuracy

| Metric | Target | Source |
|--------|--------|--------|
| Simulation vs real | Working pilot target | Pilot data |
| vs Profile matching | Test for uplift | Ablation |
| vs Random | Must beat simple baseline | Baseline |

### User Understanding

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Comprehension | Working pilot target | Survey |
| Trust in "hypothesis" framing | Working pilot target | Survey |
| Actionable insight | Working pilot target | Survey |

---

## Part 10: Key Principles (Research-Backed)

### 1. Copilot, Not Oracle
> "AI as workflow-embedded decision support rather than autonomous care" — Frontiers: Psypilot

**Implementation:** Every output includes "Verify in real life"

### 2. BFI-2 for Persona
> "BFI-2 prompts produce more human-like responses than simple adjectives" — Huang et al.

**Implementation:** Use validated personality scales, not just type labels

### 3. Rich Persona Prompts
> More detailed persona profiles may improve simulation quality, but the exact threshold should be established empirically.

**Implementation:** Standardize persona structure and test prompt depth experimentally

### 4. Consistency Testing
> Persona drift is a real risk in simulation and should be measured directly in the pipeline.

**Implementation:** Pre/post personality assessment required

### 5. Calibrate for Inflation
> "AI tends to inflate moral ratings" — Huang et al.

**Implementation:** Compare AI scores to human baseline, adjust

### 6. AI for Hypothesis → Humans for Validation
> Use AI to generate and prioritize hypotheses, then validate against human data.

**Implementation:** Pilot with AI, verify with real pairs

---

## Part 11: Risk Mitigation

| Risk | Mitigation |
|------|------------|
| LLM persona drift | Pre/post consistency test |
| Inflated compatibility scores | Calibration against human baseline |
| User over-trusts AI | "Hypothesis" framing, not "Verdict" |
| Simulation ≠ Reality | Mandatory human validation phase |
| Bias in scoring | Ablation tests, diverse pilot pairs |

---

## Part 12: File Structure

```
before-we-build-engine/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── llm/
│   │   ├── client.py           # Model abstraction
│   │   └── prompts.py          # BFI-2 based prompts
│   ├── skills/
│   │   ├── persona_generator.py # BFI-2 → narrative
│   │   ├── persona_validator.py  # Consistency test ⭐
│   │   ├── simulation_runner.py # Multi-turn
│   │   ├── observer_agent.py   # External analysis
│   │   ├── choice_tracker.py    # Repeated choice
│   │   └── compatibility_scorer.py # Calibrated score
│   ├── schemas/
│   │   ├── bfi2.py             # BFI-2 assessment
│   │   ├── persona.py          # Persona + consistency
│   │   └── assessment.py       # Final output
│   └── api/
│       └── routes.py
├── data/
│   ├── personas/               # Generated personas
│   ├── transcripts/            # Simulation logs
│   └── outcomes/               # Validation data
└── tests/
```

---

## Appendix: Research Sources

| Source | Key Contribution |
|--------|------------------|
| CogniPair (arXiv preprint, 2025) | GNWT-style agent architecture, reported attraction correlation |
| Love First (workshop/preprint) | 3-phase simulation pipeline, observer/reward ideas |
| Scientific Reports | GPT-4 personality-response emulation |
| LLM simulation methodology | validation-first simulator guidance |
| arXiv: Psychometric Approach | BFI-2 for AI agents |
| Frontiers: Psypilot | Copilot, not oracle |
| arXiv: S-Researcher | Human-in-the-loop |
| Current Psychology | AI for hypothesis → validate with humans |

---

## Next Steps

1. [ ] Review this plan
2. [ ] Decide: Build solo or find team?
3. [ ] Clone/start repo
4. [ ] Week 1: Setup technical stack
