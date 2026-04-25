# AGENTS.md — LLM Wiki Schema for PsyCalc

This document defines the schema and conventions for maintaining the PsyCalc knowledge base.

## Project Overview

**PsyCalc** is a research-oriented framework for interpreting Socionics, Psychosophy, and Temporistics as heuristic models of latent psychological processes. It treats typological structures not as final personality labels, but as compressed hypotheses about hidden processes that can inform compatibility architecture, role fit, team design, and AI-based simulation of interpersonal dynamics.

**Cognitive Matchmaker** is one downstream application of PsyCalc: an autonomous AI dating concierge that uses simulation-based evaluative modeling for compatibility assessment. It is not the whole project.

### Core Theory

Three typological systems are integrated as proposed latent-process models for human compatibility at three levels:

| Level | Typology | Latent Process | Frame Type |
|-------|----------|---------------|------------|
| Strategic | Temporistics | Inductive-deductive structuring of temporal experience | Temporal frame |
| Operational | Psychosophy | Analysis, synthesis, action organization | Action frame |
| Tactical | Socionics | Information modeling (information metabolism) | Information frame |

Required formula:

- **Socionics → latent processes of information modeling**
- **Psychosophy → latent processes of synthesis and analysis in action**
- **Temporistics → latent processes of induction and deduction in temporal/existential experience**

These mappings are project heuristics and research hypotheses. They should not be written as scientifically proven personality facts or deterministic compatibility rules.

### Scope Boundary

- **PsyCalc** = broader ontology, latent-process model, compatibility architecture, and research wiki.
- **Cognitive Matchmaker** = dating-oriented application built on top of PsyCalc.

Do not frame the whole repository as only a dating product. Application pages may discuss Cognitive Matchmaker directly, but orientation, theory, glossary, and methodology pages should use PsyCalc as the primary frame.

## Directory Structure

```
/
├── raw/                    # Immutable source documents
│   ├── temporistics/       # Sources on temporistics typology
│   ├── psychosophy/        # Sources on psychosophy typology
│   ├── socionics/          # Sources on socionics typology
│   └── general/             # General project sources
├── wiki/                   # LLM-generated wiki
│   ├── concepts/            # Theoretical concept pages
│   ├── entities/            # Entity pages (types, aspects, functions)
│   ├── relations/           # Compatibility patterns, intertype relations
│   ├── sources/             # Source summaries and derived docs
│   ├── glossary-core.md      # Core terminology
│   └── glossary-extended.md  # Extended disambiguation
├── index.md                # Wiki catalog
├── log.md                  # Chronological activity log
└── .agent-learning/        # Controlled self-improvement logs, proposals, reviews, templates
```

## Wiki Conventions

### Page Structure

Every wiki page should have frontmatter:

```markdown
---
title: Page Title
type: concept | entity | relation | source
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-file.md]
---

# Page Title

Content...
```

### Naming Conventions

- **Files**: kebab-case (e.g., `past-aspect.md`, `model-a-functions.md`)
- **Entities**: lowercase with hyphens (e.g., `1st-past-author.md`)
- **Concepts**: descriptive nouns (e.g., `latent-processes.md`)

### Cross-References

Use wikilinks for internal references:
- `[[concept-name]]` for concepts
- `[[entity-name]]` for entities
- `[[source-name]]` for sources

Example: `See [[latent-processes]] for theoretical foundation.`

## Operations

### Agent Self-Improvement Workflow

Agent instruction changes are governance changes. They should be handled through the controlled learning loop in `.agent-learning/`, not silent self-modification.

1. Record the observed failure, audit finding, or user feedback in `.agent-learning/logs/`.
2. Create an improvement proposal in `.agent-learning/proposals/` using the template.
3. Route high-risk changes to relevant reviewers, such as provenance, caveats, psychometrics, statistics, theology, neuroscience, clinical, sociology, military, or system-specific experts.
4. Apply patches to `.opencode/agents/*.md` only after explicit user request or approval.
5. Store review decisions in `.agent-learning/reviews/`.

Self-improvement should make agents more truthful, traceable, humble, and better delegated. It must not weaken caveats or convert hypotheses into facts.

### Ingest Workflow

When adding a new source:

1. Place raw source in appropriate `raw/` subdirectory
2. Read and analyze the source
3. Create or update relevant pages in `wiki/`
4. Update `index.md` with new entries
5. Append entry to `log.md`

### Query Workflow

When answering questions:

1. Read `index.md` to find relevant pages
2. Read relevant pages for detailed information
3. Synthesize answer with citations
4. If answer creates new knowledge, create new wiki page

### Lint Workflow

Periodically check:

- [ ] Contradictions between pages
- [ ] Stale claims superseded by new sources
- [ ] Orphan pages with no inbound links
- [ ] Important concepts lacking dedicated pages
- [ ] Missing cross-references
- [ ] Data gaps requiring web search

## Content Guidelines

### Concept Pages

Describe theoretical constructs:
- Definition and scope
- Theoretical foundations
- Relationships to other concepts
- Practical applications

### Entity Pages

Describe specific instances:
- For types: description, characteristics, examples
- For aspects: position, latent process, manifestations
- For functions: properties, behaviors, relationships

### Relation Pages

Describe compatibility patterns:
- Good combinations with examples
- Challenging combinations with explanations
- Mechanisms behind compatibility

## Key Terminology

See `glossary-core.md` and `glossary-extended.md` for disambiguation of ambiguous terms:

- **Model** has 4 meanings (formal model, information model, Model A, mathematical model)
- **Function** has 3 meanings (psychic function, mathematical function, software function)
- **Frame** = internal principle of selection, ordering, interpretation

## Questions to Explore

When maintaining the wiki, investigate:

1. Empirical validation of typological claims
2. Cross-system correlations (Temporistics ↔ Psychosophy ↔ Socionics)
3. Weight calibration for compatibility scoring
4. Observable behavioral markers for latent processes
5. Real-world case studies and outcomes

## Last Updated

2026-04-24
