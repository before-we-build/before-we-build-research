# SKILL: compatibility-scorer

## Purpose

Calculate a final compatibility signal from tracked choices. Produces a simulation-derived score shown to users.

## When to Use

- After completing all simulation runs for a pair
- Aggregating metrics from different scenario types
- Generating final compatibility report for user

## Input from choice-tracker

```yaml
pair_id: "a1-b2"
total_runs: 1000
mutual_choices: 820
compatibility_score: 82.0
adversarial_strength: 0.97  # Under pressure
early_lead: 0.02            # Small dropoff over time
divergence_rate: 0.001
```

## Scoring Components

### 1. Base Compatibility Score
```
base = (mutual_choices / total_runs) × 100
```

### 2. Adversarial Bonus
```
If adversarial scenarios included:
  bonus = (adversarial_mutual / adversarial_total - base) × 0.2
  Higher bonus = stronger choice under pressure
```

### 3. Consistency Bonus
```
If early_lead is small (choices stayed consistent):
  consistency_bonus = 2.0
If early_lead is large (choices diverged over time):
  consistency_penalty = -5.0
```

### 4. Mutual Alignment
```
If divergence_rate < 0.01:
  alignment_bonus = 1.0
```

### Final Score
```
final = base + adversarial_bonus + consistency_bonus + alignment_bonus
final = clamp(final, 0, 100)
```

## Output Formats

### For User
```yaml
compatibility_percentage: 82.0
interpretation: "Across many simulated scenarios,
                your digital versions often chose each other,
                including under some pressure conditions."
confidence: "very_high"
summary: "Your simulated versions demonstrated remarkable 
          consistency in choosing each other."
```

### Detailed Report
```yaml
pair_id: "a1-b2"
final_score: 82.0
breakdown:
  base_score: 82.0
  adversarial_bonus: 0.0
  consistency_bonus: 0.0
  alignment_bonus: 0.0
metrics:
  total_runs: 1000
  mutual_choices: 998
  adversarial_mutual: 198
  adversarial_total: 200
  early_choice_rate: 0.999
  late_choice_rate: 0.996
insights:
  - "Your choice of each other remained consistent across all scenarios"
  - "Pressure made your simulated versions more likely to choose each other"
  - "Virtually no divergence between your simulated decisions"
recommendation: "strong_compatibility_signal"
```

## Interpretation Thresholds

| Score | Signal | Meaning |
|-------|--------|---------|
| 95-100% | Very Strong | "Keep choosing each other across scenarios" |
| 85-94% | Strong | "High consistency, likely real compatibility" |
| 70-84% | Moderate | "Some compatibility, but mixed signals" |
| 50-69% | Weak | "Limited mutual choice" |
| <50% | Very Weak | "Simulated versions don't gravitate toward each other" |

## Key Principles

1. **Repeated choice > single perfect match** — stable patterns across many runs matter more than one perfect scene
2. **Pressure reveals truth** — Choices under stress matter more
3. **Consistency matters** — Early and late choices should align
4. **No false precision** — prefer coarse, uncertainty-aware reporting over overconfident exactness

## Edge Cases

### Too Few Runs
```
If total_runs < 100:
  warning: "Score based on limited scenarios, confidence lower"
```

### All Mutual
```
If mutual_choices == total_runs:
  score = 100.0
  note: "Perfect consistency — unusual, verify simulation quality"
```

### No Mutual
```
If mutual_choices == 0:
  score = 0.0
  note: "Simulated versions never chose each other"
```

## Dependencies

- `choice-tracker` — Provides raw choice data
- `history-analyzer` — Identifies patterns
- `explanation-generator` — Creates human-readable interpretation

## Related Skills

- `choice-tracker` — Feeds data into scorer
- `explanation-generator` — Explains score to user
- `report-generator` — Creates final user-facing output
