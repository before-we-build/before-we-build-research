---
title: Designing AI-Agents with Personalities — Psychometric Approach
type: source
tags: [research, psychometric, Big Five, BFI-2, AI-agents, personality]
created: 2026-04-15
updated: 2026-04-15
sources: [arXiv:2410.19238]
---

# Designing AI-Agents with Personalities: A Psychometric Approach

**Authors:** Huang, Zhang, Soto, Evans
**Published:** arXiv preprint, first posted 25 October 2024
**Latest arXiv version noted in audit:** November 2025
**Status:** Preprint, not peer-reviewed
**Code:** github.com/muhua-h/Psychometrics4AI

## Core Contribution

Three-study framework for assigning Big Five-based trait profiles to AI agents and testing for partial psychometric alignment.

## Three Studies

### Study 1: Semantic Adjectives
- Simple personality adjectives in prompts
- Results: Basic alignment with human responses
- Limitation: Lacks nuance

### Study 2: BFI-2 Format
- Uses Big Five Inventory-2 items
- Results: Newer models aligned more closely with human responses on some measures
- Limitation: Finer response patterns were not uniformly consistent

### Study 3: Moral Judgment
- Evaluated on risk-taking and moral-dilemma vignettes
- BFI-2-Expanded format most closely matches human responses
- BUT: AI tends to **inflate "moral" ratings**

## Key Findings

### What Works
- BFI-2 prompts produce more human-like responses
- Correlations between Big Five traits and behaviors match human patterns
- Potentially useful for preliminary research

### What Doesn't Work
- Finer response patterns inconsistent
- AI sometimes inflates certain traits
- Cannot fully substitute for human participants in precision or high-stakes settings

## Practical Implications

### For Our Project: Project Extrapolation

- Big Five-based prompting is a reasonable starting point for persona generation
- Demographic and contextual information may improve realism in some setups
- Any such persona prompt should still be benchmarked against human data rather than assumed valid by default

## References

- arXiv:2410.19238
- Code: github.com/muhua-h/Psychometrics4AI
