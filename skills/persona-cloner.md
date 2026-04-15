# SKILL: persona-cloner

## Purpose

Create a digital twin (persona) of a human for simulation purposes. The twin must exhibit consistent personality traits and behave like the original person in social scenarios.

## When to Use

- Starting a new simulation with real users
- Generating synthetic personas for testing
- Mapping existing personality assessments (MBTI, Big Five, Socionics) to agent behavior

## How to Use

### Input
```yaml
source:
  type: interview | questionnaire | existing_assessment | social_profile
data:
  # For interview: transcript or summary
  # For questionnaire: Big Five / MBTI / Socionics scores
  # For social profile: posts, interactions, preferences
```

### Process
1. **Extract traits** — Identify core personality dimensions
2. **Map to type** — Classify into personality system (Big Five, MBTI, Socionics, Temporistics)
3. **Generate behavioral policies** — Define how this persona responds to scenarios
4. **Validate** — Confirm twin behaves consistently with source

### Output
```yaml
persona_id: "uuid"
type_system: "socionics"
type_code: "LII"
traits:
  oocean:
    O: 0.7
    C: 0.8
    E: 0.3
    A: 0.6
    N: 0.2
behavioral_policies:
  conflict_response: "retreat_and_analyze"
  flirtation: "subtle_intellectual"
  loyalty_trigger: "shared_values"
validation_score: 0.85
```

## Key Principles

1. **Behavioral consistency** — Twin must respond same way to same stimulus as original would
2. **Trait stability** — Core traits don't change; only behaviors adapt to context
3. **Evolvability** — Twin can learn within simulation without losing core identity
4. **Cross-system mapping** — Support conversion between Big Five ↔ MBTI ↔ Socionics

## Implementation Notes

### Trait Extraction
```
Interview → LLM extract core values, fears, desires
Questionnaire → Direct trait scores
Social profile → Behavioral patterns → Inferred traits
```

### Type Mapping Reference

| Big Five | MBTI Dichotomy | Socionics | Temporistics |
|----------|----------------|-----------|--------------|
| O (Openness) | Intuition > Sensing | Ne/Ni > Se/Si | Future > Present |
| C (Conscientiousness) | Judging > Perceiving | Te/Ti > Fe/Fi | Order/Captain |
| E (Extraversion) | Extrovert > Introvert | E/I | Social orientation |
| A (Agreeableness) | Feeling > Thinking | Fe/Fi > Te/Ti | Harmony/Emotion |
| N (Neuroticism) | — | Emotional stability | — |

### Validation Method
Ask original person to rate twin responses: "Would you say this?"
Target: 5.6/7.0 (CogniPair benchmark)

## Dependencies

- `type-mapper` — For cross-system translation
- `behavior-generator` — For creating response policies
- `validator` — For consistency checking

## Related Skills

- `type-mapper` — Converts between personality systems
- `adversarial-designer` — Uses personas for stress testing
- `choice-tracker` — Tracks decisions made by persona
