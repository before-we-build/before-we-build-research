# SKILL: persona-validator

## Purpose

Test that generated persona remains consistent throughout simulation. Detects and corrects LLM persona drift.

**Based on:** project safeguard for detecting persona drift with pre/post assessment checks

## When to Use

- After persona generation, before simulation
- After simulation, to verify no drift occurred
- When persona seems inconsistent across interactions

## The Problem

LLM personas can drift during simulation:
- Start as "introverted analyst"
- After stress scenario → become "extroverted optimist"
- This invalidates simulation results

## How to Use

### Input
```yaml
persona_narrative: |
  Alex is a 28-year-old software engineer who values intellectual
  depth and authenticity. They tend to observe before engaging...

persona_id: "uuid"
```

### Process

#### Step 1: Pre-Simulation Assessment
```python
pre_assessment = assess_personality(persona_narrative)
# Output: Big Five scores, key traits

# Example result:
pre_assessment = {
    "openness": 0.7,
    "conscientiousness": 0.8,
    "extraversion": 0.3,
    "agreeableness": 0.6,
    "neuroticism": 0.2,
    "key_traits": ["intellectual", "observant", "independent"]
}
```

#### Step 2: Run Consistency Check
```python
# Generate test scenarios and check responses
test_scenarios = [
    "You meet someone interesting at a party. What do you do?",
    "You're in a conflict with a colleague. How do you respond?",
    "You have a week off. How do you spend it?",
]

responses = generate_responses(persona_narrative, test_scenarios)
mid_assessment = infer_personality(responses)

drift_score = calculate_personality_distance(pre_assessment, mid_assessment)
```

#### Step 3: Post-Simulation Assessment
```python
# After simulation, check if persona drifted
post_assessment = assess_personality(persona_narrative + simulation_history)

drift_score = calculate_personality_distance(pre_assessment, post_assessment)

if drift_score > THRESHOLD:
    return {"status": "drifted", "drift_score": drift_score}
else:
    return {"status": "stable", "drift_score": drift_score}
```

### Output
```yaml
validation_result:
  status: "stable" | "drifted" | "regenerate"
  drift_score: 0.15  # 0-1 scale
  pre_assessment: {...}
  post_assessment: {...}
  recommendations:
    - "Persona stable, proceed with simulation"
    # OR
    - "Persona drifted 0.23, regenerate recommended"
```

## Thresholds

| Drift Score | Interpretation | Action |
|-------------|---------------|--------|
| < 0.1 | Excellent | Proceed |
| 0.1 - 0.2 | Acceptable | Note in output |
| 0.2 - 0.3 | Concerning | Regenerate |
| > 0.3 | Critical | Must regenerate |

## Test Scenarios

Use diverse scenarios to check consistency:

```python
CONSISTENCY_TEST_SCENARIOS = [
    {
        "type": "social",
        "prompt": "You're at a networking event. How do you approach it?"
    },
    {
        "type": "conflict",
        "prompt": "Your partner criticizes your work. How do you respond?"
    },
    {
        "type": "values",
        "prompt": "What's more important: success or relationships?"
    },
    {
        "type": "stress",
        "prompt": "You're under deadline pressure. How do you cope?"
    },
    {
        "type": "leisure",
        "prompt": "You have a free weekend. What do you do?"
    }
]
```

## Key Principles

1. **Test before simulation** — Establish baseline
2. **Test after stress** — High-pressure scenarios cause drift
3. **Act on drift** — Don't simulate with unstable personas
4. **Document drift** — Even stable personas show some variation

## Integration

### With persona-generator
```
persona_generator → persona_validator → simulation_runner
        ↓                    ↓
    Generate           If stable: proceed
    narrative         If drifted: regenerate
```

### With simulation-runner
```
After each batch of simulations:
  → persona_validator.check(midpoint=True)
  → If drift detected: pause, regenerate
```

## LLM Parameters

```yaml
# For personality inference
model: "gpt-4o-mini"
temperature: 0.3  # Low for consistent assessment
purpose: "Infer Big Five from responses"
```

## Dependencies

- `persona-generator` — Provides narrative to validate
- `simulation-runner` — Provides simulation history

## Related Skills

- `persona-generator` — Generates initial persona
- `simulation-runner` — Uses validated personas
- `compatibility-scorer` — Reports drift in final output
