---
title: Cross-Typology Terminology Conflicts
type: concept
tags: [typology, terminology, conflict, ambiguity, mapping]
created: 2026-04-16
updated: 2026-04-16
sources: []
---

# Cross-Typology Terminology Conflicts

> **Status:** Active research — This document catalogs terms that have different meanings across typological systems. Using these terms requires explicit qualification.

## Rationale

Different typological systems developed independently, often using the same words for different constructs. This creates confusion when mapping between systems or building unified models. This document identifies critical conflicts and provides disambiguation rules.

---

## Critical Conflicts

### CONFLICT-1: Extraversion — Five Distinct Meanings

| System | Construct | Definition | Basis |
|--------|----------|------------|-------|
| **Jung (1921)** | Attitude type | Direction of psychic energy (libido) | Qualitative |
| **Eysenck (PEN)** | Factor | Cortical arousal level | Biological: low arousal → seeks stimulation |
| **Big Five** | Factor (OCEAN E) | Sociability, activity, positive affect | Factor analysis |
| **MBTI** | Dichotomy | E vs I directional preference | Simplified Jung |
| **Socionics** | Type attitude + element polarity | Type-level E/I exists, and i/e also marks information elements | Mixed: type-level and element-level |

**Key Insight:** These are NOT the same construct. "Extraversion" in Eysenck refers to biological arousal, while in Jung it refers to psychic energy direction. Both are labeled "E" but have different theoretical foundations.

**Disambiguation Rule:**
- Always specify: "Jungian extraversion", "Eysenckian extraversion", "Big Five Extraversion"
- For Socionics: type-level E/I is valid, but clarify that Socionics E/I is not interchangeable with MBTI E/I

**Example:**
```yaml
# Confusion:
mbti: "ENTP"  # MBTI extraversion
socionics: "ILE"  # often mapped to ENTP, but only approximately
# Socionics does use E/I terminology, but not identically to MBTI
```

---

### CONFLICT-2: Function — Three Distinct Meanings

| System | Construct | Definition |
|--------|----------|------------|
| **Jung/Socionics** | Psychic function | Unit of information processing (8 elements) |
| **Psychosophy** | Aspect | Will, Emotion, Logic, Physics |
| **Big Five** | Facet | Sub-trait within main factor |

**Disambiguation Rule:**
- Socionics: "psychic function" or element name (Te, Ti, etc.)
- Psychosophy: "psychosophy aspect" or "function position"
- Big Five: "facet" or "sub-trait"

---

### CONFLICT-3: Introversion — Two Distinct Meanings

| System | Construct | Inverted Meaning |
|--------|----------|----------------|
| **Jung/MBTI** | Attitude | Energy directed inward |
| **Socionics** | Type attitude + element polarity | Socionics has introverted types and introverted elements, but the construct is not identical to MBTI |

**Critical Problem:** In MBTI, INTJ = introverted. In Socionics, a type may also be called introverted, but it still contains both introverted and extraverted information elements. The shared label hides different underlying theory.

**Disambiguation Rule:** For Socionics, it is acceptable to use type-level E/I, but clarify that Socionics introversion/extraversion is not a drop-in synonym for MBTI E/I.

---

### CONFLICT-4: Intuition — Two Distinct Meanings

| System | Construct | Definition |
|--------|----------|------------|
| **Jung/MBTI** | Perception function | Sensing vs Intuition (S/N dichotomy) |
| **Socionics** | Intuition element | Ni (Time), Ne (Ideas) |
| **Psychosophy** | No direct equivalent | Psychosophy does not have a canonical standalone Intuition aspect |

**Disambiguation Rule:**
- MBTI: "intuition" = perception mode
- Socionics: "intuition element" or specify Ni/Ne
- Psychosophy: avoid treating "intuition" as a standard Psychosophy aspect unless a specific non-canonical school is being discussed

---

### CONFLICT-5: Feeling — Two Distinct Meanings

| System | Construct | Definition |
|--------|----------|------------|
| **Jung/MBTI** | Judgment function | T vs F dichotomy |
| **Socionics** | Feeling element | Fi (internal), Fe (external) |
| **Psychosophy** | Emotions (E) | Soul/feeling function |

**Disambiguation Rule:** MBTI Feeling and Socionics Fe/Fi are related only loosely. Any mapping between them should be treated as approximate.

---

### CONFLICT-6: Sensing — Two Distinct Meanings

| System | Construct | Definition |
|--------|----------|------------|
| **Jung/MBTI** | Perception function | S vs N dichotomy |
| **Socionics** | Sensing element | Si (comfort), Se (will) |
| **Psychosophy** | Physics (F) | Attitude to the physical/material domain, including comfort, resources, and bodily reality |

---

## System-Specific Terminology Gaps

### Terms That Exist in One System But Not Others

| System | Unique Term | Other Systems |
|--------|------------|--------------|
| **Socionics** | Model A, Block structure | No direct equivalent |
| **Socionics** | Quadra (4 groups) | No equivalent |
| **Socionics** | PoLR (Vulnerable function) | No equivalent |
| **Psychosophy** | Repression/Vagination | Different constructs |
| **Temporistics** | Aspect position (1-4) | No direct equivalent |
| **Big Five** | OCEAN acronym | Different naming |

---

## Mapping Confidence Guidelines

| Mapping | Confidence | Reason |
|---------|------------|--------|
| MBTI ↔ Socionics | Common but disputed | Widely attempted in practice, but not a stable one-to-one mapping |
| Big Five ↔ MBTI | Approximate only | Trait vs typology constructs differ substantially |
| Big Five ↔ Socionics | Weak direct mapping | No standard direct correspondence |
| Psychosophy ↔ Any | Exploratory | Requires more research |
| Temporistics ↔ Any | Exploratory | Requires more research |

---

## Practical Implications

### For Cross-Typology Work

1. **Never assume term equivalence** — Check which system the term originates from
2. **Always qualify** — Say "Socionics Fi" not just "feeling"
3. **Track confidence** — Note mapping confidence in outputs
4. **Flag ambiguous** — When unclear, ask for clarification or note uncertainty

### For This Project

When building unified compatibility models:
- Use Socionics as primary for information processing
- Map MBTI → Socionics for compatibility
- Big Five used for broad trait validation only
- Psychosophy and Temporistics — research needed

---

## Related Pages

- [[cross-typology-mapping-framework]] — Mapping methodology
- [[glossary-core]] — Core terminology definitions
- [[glossary-extended]] — Additional disambiguation
- [[socionics-detailed]] — Socionics function definitions
- [[psychosophy-detailed]] — Psychosophy aspect definitions

---

## TODO

- [ ] Add research on Psychosophy ↔ other system mappings
- [ ] Clarify Temporistics terminology
- [ ] Document system-specific assessment instruments
- [ ] Create visual terminology map

---

*This document is part of the Cognitive Matchmaker knowledge base. It will be updated as research clarifies terminology conflicts.*
