# SKILL: persona-cloner

## Purpose

Create a digital twin (persona) of a human for simulation purposes. The twin must exhibit consistent personality traits and behave like the original person in social scenarios.

**Based on:** CogniPair-style GNWT initialization plus this project's persona-generation pipeline

## When to Use

- Starting a new simulation with real users
- Generating synthetic personas for testing
- Mapping existing personality assessments (MBTI, Big Five, Socionics) to agent behavior

## How to Use

### Input Types

```yaml
# Type 1: Structured Assessment
source:
  type: big_five
  scores:
    O: 0.7  # Openness
    C: 0.8  # Conscientiousness
    E: 0.3  # Extraversion
    A: 0.6  # Agreeableness
    N: 0.2  # Neuroticism

# Type 2: Interview Transcript
source:
  type: interview
  transcript: "..."
  duration_minutes: 45

# Type 3: Socionics/MBTI Type
source:
  type: socionics
  type_code: "LII"
  quadra: "alpha"
  functions: ["Ti", "Ne", "Si", "Fe"]
```

### Process (3 Phases)

#### Phase 1: Trait Extraction
```
Structured Assessment → Direct scores
Interview Transcript → LLM extracts values, fears, desires
Social Profile → Behavioral patterns → Inferred traits
```

#### Phase 2: Narrative Generation
```
Extract traits → Generate structured persona narrative
```

**Project note:** Narrative length should be treated as a tuning variable, not a fixed research-backed rule.

**Persona Narrative Template:**
```markdown
[Name] is a [age]-year-old [occupation] who values [top 3 values].
In social situations, they tend to [behavioral tendency].
When meeting someone new, they [first impression strategy].
Their ideal partner would [preference description].
They are motivated by [drives] and tend to avoid [avoidances].
Key traits: [list 5-7 defining characteristics]
```

#### Phase 3: Module Weight Initialization
```
Narrative → Map to GNWT cognitive modules:

Emotion Module ← Neuroticism (N)
Memory Module ← Openness (O)
Planning Module ← Conscientiousness (C)
SocialNorms Module ← Agreeableness (A)
GoalTracking Module ← Extraversion (E)
```

### Output
```yaml
persona_id: "uuid"
persona_name: "Alex"
type_system: "socionics"
type_code: "LII"

# For CogniPair integration
gnwt_weights:
  emotion: 0.2      # From N=0.2
  memory: 0.7        # From O=0.7
  planning: 0.8     # From C=0.8
  social_norms: 0.6 # From A=0.6
  goal_tracking: 0.3 # From E=0.3

# Narrative for LLM
narrative: |
  Alex is a 28-year-old software engineer who values intellectual
  depth, authenticity, and independence. In social situations, they
  tend to observe before engaging...
  [Structured narrative]

# Behavioral policies
policies:
  conflict_response: "retreat_and_analyze"
  flirtation_approach: "intellectual_bonding"
  loyalty_trigger: "shared_values"
  decision_style: "analytical_deliberate"

validation:
  target: pilot_defined  # define threshold in your own validation protocol
  method: "self_rating_comparison"
```

## Key Principles

1. **Behavioral consistency** — Twin must respond same way to same stimulus as original
2. **Trait stability** — Core traits don't change; only behaviors adapt to context
3. **Evolvability** — Twin can learn within simulation without losing core identity
4. **Cross-system mapping** — Support conversion Big Five ↔ MBTI ↔ Socionics

## Implementation Reference

### LLM Parameters (from CogniPair)
```yaml
model: "gpt-4o"
temperature: 0.9      # High for persona diversity
top_p: 1.0
max_tokens: 200
min_tokens: 0
```

### Validation Method
```
Ask original person: "Would you say this? Rate 1-7"
Use a pilot-defined human validation threshold rather than assuming a fixed external benchmark.
```

## Dependencies

- `type-mapper` — For cross-system translation
- `global-workspace` — For GNWT module integration
- `narrative-generator` — For persona narrative creation

## Related Skills

- `type-mapper` — Converts between personality systems
- `global-workspace` — Initializes GNWT cognitive modules
- `persona-generator` — Creates narrative from structured data
- `observer-agent` — Validates persona with external analysis
