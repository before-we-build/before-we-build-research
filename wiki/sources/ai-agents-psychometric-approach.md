---
title: Designing AI-Agents with Personalities — Psychometric Approach
type: source
tags: [research, psychometric, Big Five, BFI-2, AI-agents, personality]
created: 2026-04-15
updated: 2026-04-15
sources: [arXiv:2410.19238]
---

# Designing AI-Agents with Personalities: A Psychometric Approach

**Authors:** Huang, Zhang, Soto, Evans (Stanford)
**Published:** arXiv, October 2024
**Code:** github.com/muhua-h/Psychometrics4AI

## Core Contribution

Three-study framework for assigning **quantifiable, psychometrically validated personalities** to AI agents using Big Five framework.

## Three Studies

### Study 1: Semantic Adjectives
- Simple personality adjectives in prompts
- Results: Basic alignment with human responses
- Limitation: Lacks nuance

### Study 2: BFI-2 Format
- Uses Big Five Inventory-2 items
- Results: Much closer to human responses
- Better at capturing subtle personality variations

### Study 3: Moral Judgment
- Validated on risk-taking and moral dilemmas
- BFI-2-Expanded format most closely matches human responses
- BUT: AI tends to **inflate "moral" ratings**

## Key Findings

### What Works
- BFI-2 prompts produce more human-like responses
- Correlations between Big Five traits and behaviors match human patterns
- Valid for preliminary research

### What Doesn't Work
- Finer response patterns inconsistent
- AI sometimes inflates certain traits
- Cannot fully substitute for human participants

## Practical Implications

### For Our Project: Persona Generation

Use this prompt structure:
```
Based on the following Big Five Inventory-2 scores:
- Openness: [score]
- Conscientiousness: [score]
- Extraversion: [score]
- Agreeableness: [score]
- Neuroticism: [score]

And demographics:
- Age: [age]
- Gender: [gender]
- Occupation: [occupation]

Describe how this person would respond to [scenario]
```

### Validation Checklist
- [ ] Check internal consistency of responses
- [ ] Compare to human baseline
- [ ] Test for consistency over multiple prompts
- [ ] Validate against external criteria

## References

- arXiv: 2410.19238
- Code: github.com/muhua-h/Psychometrics4AI
- Models used: GPT-4, newer models show better alignment
