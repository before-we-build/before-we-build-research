---
name: public-figure-typologist
description: Create typology profiles for public figures using publicly available information. Use when user wants to analyze a public figure's personality using Temporistics, Psychosophy, and Socionics frameworks based on public statements and behavior.
---

# Public Figure Typologist

## Purpose

Create respectful, ethical typology profiles for public figures based on publicly available information using three typological systems.

## When to Use

- User requests typology for a public figure (celebrity, politician, military leader, etc.)
- User wants analysis based on public statements, interviews, documented behavior
- User asks to "type" someone

## When NOT to Use

- Private individuals without their consent
- Any clinical diagnosis claims
- Commercial purposes without consent

## Ethical Framework

### ALWAYS Required: Disclaimer

Every typology analysis MUST include:

```
DISCLAIMER: This typology is an interpretation based on publicly available 
information only. It does not constitute a psychological diagnosis. 
No examination was conducted. The subject has not consented to this analysis. 
This is opinion, not fact.
```

### Acceptable Scenarios

| Scenario | OK? | Notes |
|----------|-----|-------|
| Public figure (academic analysis) | ✅ | With disclaimer |
| Public figure (non-commercial) | ✅ | With disclaimer |
| Private individual | ❌ | Needs consent |
| Clinical diagnosis | ❌ | Never claim this |
| Commercial use | ❌ | Needs consent |

## Workflow

### Step 1: Research (Required)

Before any typing, research publicly available information:

1. Search for recent interviews, speeches, public statements
2. Find biographical information
3. Look for documented leadership style, decisions
4. Find quotes about values, worldview, goals

**Required**: At least 3-5 public sources

### Step 2: Analyze for Evidence

For each typological system, find evidence for:

#### Temporistics (Strategic - Past/Present/Future/Eternity)
- Past: What past experiences shaped them?
- Present: How do they handle current reality?
- Future: What are their goals/vision?
- Eternity: What is their sense of meaning/legacy?

#### Psychosophy (Operational - 4 Functions × 4 Positions)

Each person has ONE position (1/2/3/4) for each of 4 aspects = 2-letter type!

**Type format**: [Aspect][Position] + [Aspect][Position]
- Example: LE means 1st position in Logic, 2nd in Emotion

**How to determine**:
- Which aspect is LEADING (1)? = What they naturally drive
- Which aspect is CREATIVE (2)? = What they develop with others
- Which is VULNERABLE (3)? = What causes anxiety
- Which is ROLE (4)? = How they present

**Reference**: `wiki/sources/psychosophy-detailed.md` for full function descriptions

#### Socionics (Tactical - 8 functions)
- Leading function: What drives them?
- Creative function: What do they excel at?
- Vulnerable function: What do they struggle with?
- Role function: How do they present themselves?

### Step 3: Draft Typology

Use this template:

```markdown
# Typology Analysis: [Name]

**DISCLAIMER**: [Standard disclaimer]

---

## Summary Profile

| System | Type Format | Rationale |
|--------|-------------|------------|
| Temporistics | [2-letter ring] | [Brief explanation] |
| Psychosophy | [2 letters x 2 positions] | Example: LE = 1L2E |
| Socionics | [4-letter code] | Example: LIE |

---

## Key Observations

### [Category]
- [Evidence from public sources]

---

## Temporistics Analysis

### [Type determination]
**Rationale**: [Explanation with evidence]

[Detailed temporal analysis]

---

## Psychosophy Analysis (4 aspects × 4 positions = LEVF format)

### Determining Positions

Each aspect (L/E/V/F) has position 1-4:

| Position | What to look for |
|----------|----------------|
| 1 (Leading) | What they naturally drive, confident in |
| 2 (Creative) | What they develop with others |
| 3 (Vulnerable) | What causes anxiety/doubt |
| 4 (Role) | How they present externally |

**Output format**: 4-character like "1L2E3V4F" or simplified "LEV" (just leading + creative)

### Analysis

[Which position for each: L, E, V, F]

---

## Socionics Analysis

### [Type determination]
**Rationale**: [Explanation with evidence]

[Function-by-function breakdown]

---

## Combined Profile

[Three-layer summary]

---

## Notes

1. This is speculative analysis based on public behavior only
2. No examination conducted — cannot verify accuracy
3. Typology is opinion, not psychological diagnosis
4. Subject has not consented to this analysis
```

### Step 4: Review and Save

Before finalizing, verify:

- [ ] Disclaimer is present
- [ ] No clinical diagnosis claims
- [ ] Based on public sources only
- [ ] Clear this is opinion, not fact
- [ ] Non-commercial framing

## Typology Reference

### Temporistics Types

| Ring | Aspect | Description |
|------|--------|-------------|
| 1st | Past/Present | Current vs historical orientation |
| 2nd | Future/Eternity | Goals vs meaning |
| Rings 1-2 × 6 rings | 24 types | Full system |

### Psychosophy Functions (4 positions each!)

Each function has 4 positions. Type = 4 characters like "1L2E3V4F" or "LEVF"

| Position | Properties | Description |
|----------|------------|-------------------|
| 1st | Subjective, Unconscious | Leading, result-oriented |
| 2nd | Subjective, Conscious | Creative, process-oriented |
| 3rd | Objective, Conscious | Vulnerable, anxious |
| 4th | Objective, Unconscious | Role, flexible |

**Example**: 1L2E3V4F = Logic leading (1L), Emotion creative (2E), Will vulnerable (3V), Physics role (4F)

**Full Psychosophy reference**: See `wiki/sources/psychosophy-detailed.md`

### Socionics Functions (Model A)

| Type | Leading | Creative | Role | Vulnerable |
|------|---------|----------|---------|---------|-----------|
| ILE | Ne | Ti | Se | Fi |
| SEI | Si | Fe | Ne | Te |
| LIE | Ne | Ti | Se | Fe |
| ESFj | Fe | Si | Ne | Ti |
| SLE | Te | Si | Fe | Ne |
| EII | Fi | Ne | Ti | Se |
| IEE | Ne | Fi | Te | Si |
| SLI | Si | Te | Fi | Ne |
| ... | ... | ... | ... | ... |

## Examples

### Example: Zaluzhnyi (Completed)

See `docs/typology-zaluzhnyi.md` for complete example showing:
- Research process
- Evidence-based reasoning
- Three-system analysis
- Proper disclaimer

## Sources

- Ethics framework: `docs/ethics-legal-typology-public-figures.md`
- Typology systems: See wiki/ folder
- Example: `docs/typology-zaluzhnyi.md`