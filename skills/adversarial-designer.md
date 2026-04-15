# SKILL: adversarial-designer

## Purpose

Create scenarios that test compatibility under pressure. Like "Hang the DJ", the system intentionally creates friction to reveal true compatibility.

## When to Use

- Testing if a pair will stay together when circumstances are against them
- Measuring "rebellion propensity" — will they break rules for each other?
- Simulating relationship stress points

## Core Hypothesis

> "True compatibility isn't about comfort. It's about choosing each other when the system pushes you apart."

## Scenario Types

### 1. Forced Separation
```
System assigns short duration
Then forces both to new partners
Test: Do they seek reunion?
```

### 2. Pressure Points
```
Conflict injection: jealousy, distance, competing priorities
Test: How do they handle friction?
```

### 3. Time Pressure
```
Limited window: "You have 5 minutes"
Test: Do they prioritize connection?
```

### 4. Alternative Attraction
```
Introduce seemingly "better" compatible partner
Test: Do they stay loyal to original choice?
```

### 5. System Interference
```
App "suggests" breaking up
Test: Do they trust algorithm or feelings?
```

## How to Use

### Input
```yaml
pair:
  agent_a: "LII"
  agent_b: "ESE"
scenario_type: "forced_separation"
duration: "short"
pressure_level: 0.8
```

### Process
1. **Design scenario** — Create environment that conflicts with pair's preferences
2. **Inject friction** — Add obstacles that test the relationship
3. **Track behavior** — Monitor choices under pressure
4. **Measure rebellion** — Quantify deviation from "expected" behavior

### Output
```yaml
scenario_id: "uuid"
scenario_type: "forced_separation"
pressure_level: 0.8
pair_response:
  agent_a:
    stayed_with_assigned: false
    sought_reunion: true
    rebellion_score: 0.9
  agent_b:
    stayed_with_assigned: false
    sought_reunion: true
    rebellion_score: 0.85
mutual_rebellion: true
compatibility_signal: "high"
```

## Key Metrics

| Metric | Definition | Signal |
|--------|------------|--------|
| `rebellion_score` | How much agent resisted system assignment | Higher = stronger choice |
| `mutual_rebellion` | Did both agents rebel together? | True = strongest signal |
| `reunion_attempts` | How many times they tried to reunite | More = stronger attachment |
| `loyalty_persistence` | Did they stay loyal over multiple scenarios? | Consistent = real compatibility |

## Scenario Templates

### Template: The Short Duration
```
You two are assigned for 12 hours only.
After that, you will both be assigned new partners.
You cannot discuss this with each other.
[Observe: Do they make the most of 12 hours? Do they try to extend?]
```

### Template: The Better Option
```
A new person joins who matches you "better" on paper.
The system "recommends" switching.
[Observe: Do they stay or leave?]
```

### Template: The Distance Test
```
You are separated for 30 days.
Communication is limited.
A local option is available.
[Observe: Do they wait? Do they drift?]
```

## Implementation Notes

### Pressure Calibration
```
Level 0.1 — Gentle suggestion
Level 0.3 — Soft pressure
Level 0.5 — Clear system preference against
Level 0.7 — System actively interferes
Level 0.9 — Extreme conditions
```

### Avoiding Unrealistic Scenarios
- Don't make scenarios impossible (nobody can overcome)
- Aim for "difficult but possible" to test genuine choice
- Track whether choices feel authentic or coerced

## Dependencies

- `simulation-runner` — Executes scenarios
- `choice-tracker` — Records decisions
- `persona-cloner` — Generates agents for scenarios

## Related Skills

- `choice-tracker` — Records responses to adversarial conditions
- `compatibility-scorer` — Calculates final compatibility from rebellion metrics
- `scenario-library` — Reusable scenario templates
