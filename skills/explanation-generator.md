# SKILL: explanation-generator

## Purpose

Create human-readable explanations for compatibility scores. Transforms a simulation-derived percentage into a story users understand.

## When to Use

- After compatibility-scorer produces final percentage
- Before showing result to user
- Explaining why two types are compatible or not

## Input

```yaml
pair:
  user_a_type: "LII"
  user_b_type: "ESE"
final_score: 82.0
breakdown:
  total_runs: 1000
  mutual_choices: 820
  adversarial_mutual: 195
  adversarial_total: 200
  early_choice_rate: 0.999
  late_choice_rate: 0.996
scenario_insights:
  - "Your simulated versions chose each other in 100% of 'better option' scenarios"
  - "Pressure increased rather than decreased mutual choosing"
  - "No significant divergence over 1000 scenarios"
```

## Output Templates

### High Compatibility (95%+)
```yaml
headline: "You keep finding each other."
interpretation: |
  In our simulation, your digital versions met 1,000 times
  in different scenarios — sometimes as strangers, sometimes
  after being assigned to others. Every time, they found
  their way back to each other.
  
  When we made it difficult — introduced tempting alternatives,
  separated them, created friction — they chose each other anyway.
  That's not chemistry. That's repeated choice.
  
  Strong repeated choice across many runs.
details:
  - "Your versions never wavered, even under pressure"
  - "Better options didn't distract them"
  - "Consistent across all scenario types"
```

### Medium Compatibility (70-94%)
```yaml
headline: "There's potential here — with conditions."
interpretation: |
  Your digital versions chose each other in most scenarios,
  but not all. In some situations — particularly when
  [specific conditions] — they drifted apart.
  
  This doesn't mean incompatibility. It means the connection
  works best when [specific conditions]. Knowing this can
  help you build around it.
details:
  - "Strong in [scenario type] scenarios"
  - "Weaker in [scenario type] scenarios"
  - "Consider: [advice]"
```

### Low Compatibility (<70%)
```yaml
headline: "Different gravitational pulls."
interpretation: |
  In our simulation, your digital versions didn't
  consistently gravitate toward each other. This doesn't
  mean you can't have a relationship — simulations capture
  initial attraction patterns, not destiny.
  
  What it does suggest: the automatic "yes" that some pairs
  feel may not be there for you two. Building connection
  would require more deliberate effort.
details:
  - "Consider: compatibility isn't just initial pull"
  - "Some pairs build on different foundations"
```

## Explaining the Method

Users often ask: "How did you simulate this?"

```yaml
method_explanation: |
  We created digital versions of both of you based on
  [personality assessment / interview / profile].
  
  Then we ran 1,000 simulated scenarios — first dates,
  pressure situations, tempting alternatives — and tracked
  whether your versions chose each other.
  
  The percentage reflects how often mutual choice happened.
  It's not about "should you be together." It's about:
  "Do your simulated versions keep gravitating toward each other?"
```

## Customization by System

### For MBTI/Socionics Users
```yaml
type_explanation: |
  LII (INTJ) and ESE (ESFJ) are Socionics "duality" pairs.
  They have complementary functions: where one leads with
  logic, the other leads with emotion. This creates natural
  balance.
  
  Your simulation results align with Socionics theory — 
  your types showed strong mutual selection patterns.
```

### For Big Five Users
```yaml
trait_explanation: |
  Looking at your Big Five profiles:
  - [Trait A]: You both score similarly → shared values
  - [Trait B]: Complementary → natural balance
  
  The simulation tested whether these traits translated
  to actual choice patterns.
```

## Key Principles

1. **Be honest about method** — Don't oversell simulation as prediction
2. **Focus on "repeated choice"** — That's the insight, not "destiny"
3. **Acknowledge limitations** — "This is one signal, not certainty"
4. **Be specific** — Name scenario types, not just percentages
5. **Empower user** — Give them insight to interpret themselves

## Anti-Patterns to Avoid

❌ "You are 99.8% compatible — meant to be!"
✓ "Your simulated versions often chose each other across many scenarios"

❌ "The algorithm says you should be together"
✓ "The simulation shows strong gravitational pull"

❌ "This is your soulmate score"
✓ "This reflects repeated choice patterns under various scenarios"

## Dependencies

- `compatibility-scorer` — Produces the score to explain
- `type-mapper` — Provides type-specific context
- `scenario-library` — References specific scenario types

## Related Skills

- `compatibility-scorer` — Source of data to explain
- `report-generator` — Formats final output for user
- `type-mapper` — Adds type-specific context
