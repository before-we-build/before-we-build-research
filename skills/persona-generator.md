# SKILL: persona-generator

## Purpose

Generate natural language persona narratives from structured data. Converts personality scores into structured persona prompts that LLMs can use to simulate behavior.

**Based on:** simulation-first persona generation ideas plus this project's validation choices

## When to Use

- User has structured assessment (Big Five, MBTI, Socionics)
- Need narrative for LLM to roleplay
- Creating personas at scale (100+ agents)

## Method

### Input Formats

```yaml
# Format 1: Big Five Scores
source:
  type: "big_five"
  scores:
    O: 0.7    # Openness
    C: 0.8    # Conscientiousness
    E: 0.3    # Extraversion
    A: 0.6    # Agreeableness
    N: 0.2    # Neuroticism
  demographics:
    age: 28
    gender: "female"
    occupation: "software engineer"

# Format 2: MBTI Type
source:
  type: "mbti"
  type_code: "INTJ"
  demographics:
    age: 32
    gender: "male"
    occupation: "product manager"

# Format 3: Socionics Type
source:
  type: "socionics"
  type_code: "LII"
  quadra: "alpha"
  functions: ["Ti", "Ne", "Si", "Fe"]
  demographics:
    age: 28
    gender: "female"
    occupation: "data analyst"
```

### Generation Prompt Template

```
You are generating a persona narrative for a dating simulation.
Given the following personality assessment, create a realistic persona
description that captures the person's essence.

---
PERSONALITY DATA:
{structured_data}

---
REQUIREMENTS:
1. Start with name, age, occupation
2. Describe values and what matters most
3. Include social behavior tendencies
4. Add relationship preferences and deal-breakers
5. End with how they approach new connections
6. Write in third person
7. Use enough detail to support stable simulation, but do not force a fixed word count

---
OUTPUT FORMAT:
[First Name] is a [age]-year-old [occupation]...
```

### Output
```yaml
persona_id: "generated-uuid"
narrative: |
  Alex is a 28-year-old software engineer who values intellectual depth,
  authenticity, and independence. In social situations, they tend to
  observe before engaging, preferring to understand the dynamics before
  contributing...

  Their ideal partner would be someone who appreciates deep conversations
  and can engage with complex ideas. They are motivated by competence
  and growth, and tend to avoid superficial small talk...

  [Structured persona narrative]

metadata:
  word_count: 423
  type_system: "socionics"
  type_code: "LII"
```

## LLM Parameters

```yaml
# Working project default
model: "gemini-2.5-flash-lite"
temperature: 0.8  # Some creativity but consistent
purpose: "Fast persona generation at scale"
```

## Batch Generation

For 100+ personas:
```python
def generate_batch(sources: list[dict]) -> list[Persona]:
    """
    Generate personas in parallel batches
    Target: 100 personas in ~5 minutes
    """
    results = []
    for batch in chunk(sources, size=10):
        # Gemini 2.5 Flash Lite handles 10 parallel
        batch_results = llm.generate_parallel(batch)
        results.extend(batch_results)
    return results
```

## Quality Checks

1. **Prompt richness** — Persona should contain enough detail for stable simulation
2. **Coverage** — All 5 Big Five traits represented
3. **Consistency** — No contradictions with assessment scores
4. **Naturalness** — Reads like human writing, not template

## Validation

After generation, validate with user:
```
Rate this persona description on a scale of 1-7:
"How well does this describe you?"
Define the acceptance threshold in your own pilot study.
```

## Dependencies

- `type-mapper` — Normalizes input to structured format
- `persona-cloner` — Finalizes persona with GNWT weights

## Related Skills

- `persona-cloner` — Uses generated narrative
- `type-mapper` — Prepares structured input
- `observer-agent` — Validates generated personas
