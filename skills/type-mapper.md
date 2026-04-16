# SKILL: type-mapper

## Purpose

Translate personality types between different typological systems. Enables cross-system validation and allows using the best aspects of each system.

## When to Use

- User has MBTI type but you need Socionics functions
- Combining Temporistics + Psychosophy + Socionics into unified model
- Validating consistency across different assessments

## Supported Systems

| System | Types | Dimensions |
|--------|-------|------------|
| Big Five | Continuous (0-1 per trait) | O, C, E, A, N |
| MBTI | 16 types | E/I, S/N, T/F, J/P |
| Socionics | 16 types + quadras | 8 functions, IM elements |
| Psychosophy | 81 types (theoretical) | V, F, L, E / 4 positions |
| Temporistics | 24 types | P, N, F, E / 4 positions |

## How to Use

### Input
```yaml
source_type: "mbti"
source_value: "INTJ"
target_system: "socionics"
```

### Output
```yaml
source: "INTJ"
target: "LII"
mapping_status: "disputed approximation"
mapping_method: "description-level comparison"
notes: "MBTI↔Socionics mappings are common in practice but not one-to-one"
```

## Mapping Tables

### MBTI ↔ Socionics (Common But Disputed)

There is no universally accepted one-to-one crosswalk between MBTI and Socionics. Use approximate examples only, then validate against fuller descriptions.

| MBTI | Common Socionics Approximation | Notes |
|------|-------------------------------|-------|
| ENTP | ILE | Common community mapping |
| ENTJ | LIE | Common community mapping |
| ENFJ | EIE | Common community mapping |
| ENFP | IEE | Common community mapping |
| INTP | LII or ILI | Depends on school and interpretation |
| INTJ | ILI or LII | Especially disputed because MBTI and Socionics J/P do not align cleanly |
| INFJ | EII or IEI | Commonly disputed |
| ISFP | SEI or ESI | Commonly disputed |

### Big Five ↔ MBTI (Approximate)

| Big Five | MBTI Direction |
|----------|-----------------|
| O > 0.5 | N > S |
| C > 0.5 | J > P |
| E > 0.5 | E > I |
| A > 0.5 | F > T |
| N < 0.3 | Higher emotional stability |

## Key Principles

1. **Preserve uncertainty** — Some mappings do not resolve cleanly
2. **Prefer descriptive comparison** — Compare functions, motivations, and behavior, not just letters
3. **Do not assume one-to-one equivalence** — especially for MBTI ↔ Socionics
4. **Use external validation** — questionnaire, examples, and scenario behavior should override letter-matching heuristics

## Known Gaps

### Psychosophy → Other Systems
- NOT established — Psychosophy uses Will/Emotion/Logic/Physics dimensions
- Requires custom mapping research
- May need OCEAN as intermediary

### Temporistics → Other Systems
- NOT established — Temporistics is niche and has a small source ecosystem
- Requires hypothesis testing
- Best approach: treat any cross-system mapping as exploratory

## Implementation Notes

### Confidence Handling
```
mapping_status ∈ {common approximation, weak approximation, exploratory}
evidence = description match + questionnaire overlap + scenario validation
final judgment should be revised after real behavioral checks
```

### Hybrid Mapping (Socionics + Temporistics)
```
Step 1: MBTI → Socionics (approximate only)
Step 2: Socionics IM elements → Temporistics aspect hypothesis
Step 3: Validate with simulation
```

## Dependencies

- None — standalone conversion utility

## Related Skills

- `persona-cloner` — Uses type mapping for persona generation
- `hypothesis-tester` — Tests mapping accuracy through simulation
