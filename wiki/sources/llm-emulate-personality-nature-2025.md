---
title: Evaluating LLMs Ability to Emulate Personality
type: source
tags: [research, personality, LLM, GPT-4, Big Five, validation]
created: 2026-04-15
updated: 2026-04-15
sources: [Nature Scientific Reports, doi:10.1038/s41598-024-84109-5]
---

# Evaluating LLMs Ability to Emulate Personality

**Authors:** Xu et al.
**Published:** Nature Scientific Reports, January 2025
**Citations:** 10
**Accesses:** 7,736

## Key Findings

### GPT-4 as Personality Emulator

GPT-4 was tested on its ability to role-play real individuals with diverse Big Five personality profiles:

1. **Superior Internal Consistency**
   - Emulated personality responses showed better internal consistency than human self-reports
   - More reliable factor organization

2. **More Structured Factor Organization**
   - GPT-4 produces cleaner factor structures than humans
   - Higher structural validity

3. **Robustness Decreases with Complexity**
   - Simple roles: very accurate
   - Complex roles with multiple attributes: accuracy decreases
   - Adding demographic info improves validity

## Methodology

### Simulation 1: Internal Consistency
- Used 400 individuals' real Big Five data as ground truth
- GPT-4 role-played these personas
- Measured: reliability, convergent validity, discriminant validity, factor structure

### Simulation 2: Robustness
- Tested with increasing role complexity
- Added supplementary information (demographics, values)
- Measured criterion-related validity

## Implications for Our Project

### What This Means
- LLM can simulate personality **at basic level** with high fidelity
- Complexity degrades accuracy
- Detailed profiles improve validity

### Application to Cognitive Matchmaker
- Use Big Five as primary personality input
- Keep persona descriptions detailed (300-500 words)
- Add demographics for better accuracy
- Validate output with human rating

## Quote

> "GPT-4 can emulate personality responses with superior internal consistency but more distinct factor organization compared to human self-reports."

## References

- Original paper: Scientific Reports, Volume 15, Article 519 (2025)
- DOI: 10.1038/s41598-024-84109-5
