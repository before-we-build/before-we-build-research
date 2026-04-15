# SKILL INDEX: Hang the DJ Implementation

## Core Skills (Required)

### 1. persona-cloner
**Creates digital twins from real users**
- Input: interview / questionnaire / profile
- Output: Agent with consistent behavioral policies
- Key: Cross-system type mapping (Big Five ↔ MBTI ↔ Socionics)

### 2. simulation-runner
**Executes multi-agent scenarios at scale**
- Manages parallel execution of 1000+ runs
- Handles turn-taking, timeouts, memory injection
- Outputs: Decision logs for choice-tracker

### 3. choice-tracker
**Logs all decisions across runs**
- Captures: accept/reject, seek reunion, loyalty signals
- Calculates: repeated choice metrics
- Stores: Per-pair history for analysis

### 4. compatibility-scorer
**Produces final "99.8%" score**
- Aggregates: base + adversarial + consistency bonuses
- Outputs: Final percentage + detailed breakdown
- Thresholds: Very Strong (95%+), Strong (85-94%), etc.

### 5. explanation-generator
**Creates user-understandable output**
- Translates: 99.8% → "You keep finding each other"
- Explains: Method, limitations, context
- Customizes: By personality system (Socionics, MBTI, etc.)

## Support Skills (Required for Core)

### 6. type-mapper
**Translates between personality systems**
- Bidirectional: Big Five ↔ MBTI ↔ Socionics
- Confidence scoring for uncertain mappings
- Handles: Temporistics (theoretical mapping)

### 7. adversarial-designer
**Creates "system interference" scenarios**
- Forces separation, introduces alternatives
- Measures: rebellion_score, loyalty_persistence
- Templates: forced_separation, better_option, distance_test

### 8. memory-persister
**Maintains agent memory across runs**
- Episodic: "Remember what happened"
- Semantic: "Know what I prefer"
- Critical: For "Hang the DJ" repeated choice effect

## Orchestration

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

## Quick Start

### Minimal Viable Product (MVP)

For first test, use only:
1. `persona-cloner` — Create 2 agent twins
2. `simulation-runner` — Run 100 simple scenarios
3. `choice-tracker` — Log decisions
4. `compatibility-scorer` — Calculate 100/100 = 100%

### Full Implementation

All 8 skills in production pipeline.

## Skill Dependencies

```
persona-cloner
├── type-mapper
└── (needs: user profile or assessment)

simulation-runner
├── persona-cloner
├── adversarial-designer
├── memory-persister
└── choice-tracker

choice-tracker
└── (feeds: simulation-runner output)

compatibility-scorer
├── choice-tracker
└── (needs: 1000 runs minimum for confidence)

explanation-generator
├── compatibility-scorer
└── type-mapper
```

## Testing Checklist

- [ ] persona-cloner produces valid agents from Big Five input
- [ ] type-mapper correctly converts INTJ → LII
- [ ] adversarial-designer creates believable interference
- [ ] simulation-runner handles 1000 parallel runs
- [ ] choice-tracker logs all decisions correctly
- [ ] memory-persister maintains identity across runs
- [ ] compatibility-scorer calculates 99.8% from 998/1000
- [ ] explanation-generator produces user-friendly output

## Future Skills (Roadmap)

### validation-harness
Tests if simulation predictions match real-world outcomes.

### typology-tester
Specifically tests Socionics/Temporistics hypotheses:
- "Conflict types show lower scores but real-world success"
- "Duality pairs match simulation predictions"

### human-simulation-comparator
Compares simulation choices to actual human choices in same scenarios.

## File Locations

```
skills/
├── index.md                    # This file
├── persona-cloner.md           # Create digital twins
├── type-mapper.md             # Cross-system translation
├── simulation-runner.md       # Execute scenarios
├── adversarial-designer.md    # Create pressure scenarios
├── choice-tracker.md          # Log decisions
├── memory-persister.md         # Cross-run memory
├── compatibility-scorer.md     # Calculate 99.8%
└── explanation-generator.md    # User-friendly output
```
