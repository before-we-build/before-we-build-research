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
| Psychosophy | 81 types (theoretical) | V, F, L, P (first function dominant) |
| Temporistics | 24 types | P/F/V/N, 4 positions per aspect |

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
confidence: 0.95
mapping_method: "function_equivalence"
notes: "Both share Ti-Ne as leading functions"
```

## Mapping Tables

### MBTI ↔ Socionics (Established)

| MBTI | Socionics | Quadra | Leading Functions |
|------|-----------|--------|-------------------|
| INTJ | LII | Alpha | Ti Ne |
| ENTP | ILE | Alpha | Ne Ti |
| ESFJ | ESE | Alpha | Fe Si |
| ISTP | SLI | Alpha | Si Te |
| ESTP | SLE | Beta | Se Ti |
| ENTJ | LIE | Beta | Te Ni |
| ENFJ | EIE | Beta | Fe Ni |
| ISTJ | LSI | Beta | Si Te |
| ESFP | SIE | Gamma | Se Fi |
| INTP | ILI | Gamma | Ni Te |
| ISFJ | ESI | Gamma | Fi Si |
| ESTJ | LSE | Gamma | Te Si |
| ENFP | IEE | Delta | Ne Fi |
| INFJ | EII | Delta | Fi Ne |
| ISFP | ESI | Delta | Se Fi |
| ENTJ | LIE | Delta | Te Ne |

### Big Five ↔ MBTI (Approximate)

| Big Five | MBTI Direction |
|----------|-----------------|
| O > 0.5 | N > S |
| C > 0.5 | J > P |
| E > 0.5 | E > I |
| A > 0.5 | F > T |
| N < 0.3 | Higher emotional stability |

## Key Principles

1. **Bidirectional** — Can convert A→B and B→A
2. **Confidence scoring** — Not all mappings are equally certain
3. **Preserve uncertainty** — Some types don't map cleanly
4. **Function-based** — Prefer function mapping over letter mapping

## Known Gaps

### Psychosophy → Other Systems
- NOT established — Psychosophy uses Will/Emotion/Logic/Physics dimensions
- Requires custom mapping research
- May need OCEAN as intermediary

### Temporistics → Other Systems
- NOT established — Temporistics is niche, single-author (Dr. Radut)
- Requires hypothesis testing
- Best approach: map through aspect combinations to Big Five dimensions

## Implementation Notes

### Confidence Calculation
```
confidence = base_match × consistency × validation_history
base_match = 0.8 for established (MBTI↔Socionics)
            = 0.5 for approximate (Big Five↔MBTI)
            = 0.3 for theoretical (Temporistics↔others)
```

### Hybrid Mapping (Socionics + Temporistics)
```
Step 1: MBTI → Socionics (0.95 confidence)
Step 2: Socionics IM elements → Temporistics aspect hypothesis
Step 3: Validate with simulation
```

## Dependencies

- None — standalone conversion utility

## Related Skills

- `persona-cloner` — Uses type mapping for persona generation
- `hypothesis-tester` — Tests mapping accuracy through simulation
