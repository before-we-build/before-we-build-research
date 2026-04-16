---
title: Evaluating LLMs Ability to Emulate Personality
type: source
tags: [research, personality, LLM, GPT-4, Big Five, validation]
created: 2026-04-15
updated: 2026-04-15
sources: [Scientific Reports, doi:10.1038/s41598-024-84109-5]
---

# Evaluating LLMs Ability to Emulate Personality

**Authors:** Yilei Wang, Jiabao Zhao, Deniz S. Ones, Liang He, Xin Xu
**Venue:** Scientific Reports
**Published:** 2 January 2025
**Status:** Peer-reviewed journal article

## Key Findings

### GPT-4 as Personality Emulator

GPT-4 was tested on its ability to role-play real individuals with diverse Big Five personality profiles:

1. **Superior Internal Consistency**
   - Emulated personality responses showed better internal consistency than human self-reports
   - More reliable factor organization

2. **More Structured Factor Organization**
   - GPT-4 produces cleaner factor structures than the corresponding human self-reports
   - Stronger loadings and fewer cross-loadings in this constrained questionnaire setting

3. **Robustness Changes With Added Prompt Context**
   - The main pattern largely replicated under added demographic context
   - Some psychometric relationships weakened under the added prompt complexity tested by the authors
   - Demographic context improved some criterion-related validity outcomes in that setup

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
- GPT-4 can emulate Big Five questionnaire-response patterns under constrained prompting conditions
- Robustness is weaker once more context is added
- This should not be generalized to unrestricted personality simulation

### Application to Cognitive Matchmaker
- Use Big Five as primary personality input
- Add demographic context carefully and test whether it improves or distorts outputs
- Validate output with human rating

## Quote

> Best read as evidence for questionnaire-response emulation under constrained setup, not as proof of general personality simulation.

## References

- Scientific Reports, 15, Article 519 (2025)
- DOI: 10.1038/s41598-024-84109-5
