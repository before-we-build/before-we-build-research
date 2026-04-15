# AGENTS.md — LLM Wiki Schema for Cognitive Matchmaker

This document defines the schema and conventions for maintaining the Cognitive Matchmaker knowledge base.

## Project Overview

**Cognitive Matchmaker** is an autonomous AI dating concierge that uses simulation-based evaluative modeling for personality-based compatibility matching.

### Core Theory

Three typological systems are integrated to model human compatibility at three levels:

| Level | Typology | Latent Process | Frame Type |
|-------|----------|---------------|------------|
| Strategic | Temporistics | Inductive-deductive structuring of temporal experience | Temporal frame |
| Operational | Psychosophy | Analysis, synthesis, action organization | Action frame |
| Tactical | Socionics | Information modeling (information metabolism) | Information frame |

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
└── log.md                  # Chronological activity log
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

2026-04-15
