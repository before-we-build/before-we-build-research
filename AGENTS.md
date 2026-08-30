# AGENTS.md — LLM Wiki Schema for Before We Build

This document defines the schema and conventions for maintaining the Before We Build knowledge base.

## Project Overview

**Before We Build** is a universal compatibility research framework for
studying how any two people may build, decide, coordinate, and sustain
relationships or shared work. It is based on a **fundamental reconceptualization
of typologies** (Socionics, Psychosophy, and Temporistics), interpreting them
not as deterministic character labels, but as heuristic models of latent
psychological processes. It treats typological structures as compressed
hypotheses that may support conversation maps, structured compatibility
research, and questions that can be checked in real interaction.

The first developed application and worldview lens is a weak-AI Christian
conversation map that helps individuals, pairs, and later churches surface
questions, differences, uncertainty, and wise next steps before serious
shared decisions. This application does not define or exhaust the universal
research core.

**Cognitive Matchmaker** is an earlier downstream dating application concept
for Before We Build. It is treated as a future research track, not the near
MVP.

### Core Theory

Before We Build uses four compatibility levels. The first is a universal
value-moral foundation; the other three use typologies as proposed
latent-process models:

| Level | Primary source/model | Process or criterion | Frame Type |
|-------|----------------------|----------------------|------------|
| Value-moral / foundational | Worldview, stated commitments, observed conduct, consent and safety evidence | Values, moral obligations, dignity, truth, responsibility, reciprocity, repair, non-negotiable boundaries | Normative frame |
| Strategic | Temporistics | Abductive, inductive, and deductive structuring of temporal experience | Temporal frame |
| Operational | Psychosophy | Analysis, synthesis, action organization | Action frame |
| Tactical | Socionics | Selecting, compressing, organizing, inferring from, and updating partial information models of one shared reality | Information frame |

The value-moral level is not a fourth typology, psychometric moral-worth
scale, or automated verdict. A Christian application may interpret it through
Christ, Scripture, observable fruit, church community, and mature counsel;
other worldview applications must state their own normative sources rather
than treating one specialization as universal.

Required formula:

- **Value-moral foundation → values, moral obligations, observed conduct,
  consent, safety, responsibility, reciprocity, repair, and non-negotiable
  boundaries**
- **Socionics → latent processes of selecting, compressing, organizing,
  inferring from, and updating partial information models of one shared
  reality**
- **Psychosophy → latent processes of synthesis and analysis in action**
- **Temporistics → latent processes of abduction, induction, and deduction in temporal/existential experience**

A type in Before We Build is not a personality type or a kind of person. In
plain language, it is a **type of perception and experience organization**; in
technical language, it is a compact type-pattern hypothesis about how a
narrower process may select, order, interpret, or organize experience. A type
pattern is distinct from both the latent-process hypothesis proposed to explain
it and the further hypothesis that the predisposition has a natural basis.

These mappings and the possible natural basis of a predisposition are project
heuristics and research hypotheses. Natural does not mean demonstrated innate,
biological, fixed, or context-independent. They should not be written as
scientifically proven personality facts or deterministic compatibility rules;
learning, role, culture, state, stress, and context remain rival explanations.

For Socionics, keep four layers distinct:

1. **aspect content** — which distinctions or relations the proposed partial
   model retains;
2. **aspect operation** — how it selects, compresses, organizes, infers, or
   updates those distinctions;
3. **Model A position mode** — how that operation is proposed to be used;
4. **observable trace** — task, speech, choice, revision, or coordination data
   that may support or contradict the hypothesis.

The classical `object/field × static/dynamic × internal/external` axes are
attributed source language. The eight operation definitions in
`wiki/concepts/socionics-reality-modeling-{en,ru,uk}.md` are a revisable BWB
reconstruction, not an established cognitive architecture. Never equate an
aspect or position with an ability, deficit, brain module, innate essence, or
objectively established information channel. Do not rank Model A hypotheses
without evidence for both aspect operations and position modes.

### Scope Boundary

- **Before We Build core** = universal ontology, four-level compatibility
  architecture, latent-process research, context/safety constraints, and
  research wiki for any pair of people.
- **Christian Before We Build application** = the first developed
  worldview/domain specialization for Christian relationship and family
  discernment.
- **Cognitive Matchmaker** = dating-oriented application built on top of Before We Build.

Do not frame the whole repository as only Christian, only dating, or only a
family product. Application pages may be explicitly Christian or discuss
Cognitive Matchmaker directly, but orientation, theory, glossary, and
methodology pages should use the universal Before We Build core as the primary
frame and clearly label worldview-specific claims.

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
│   ├── glossary-core-{en,ru,uk}.md      # Core terminology triad
│   ├── glossary-extended-{en,ru,uk}.md  # Extended disambiguation triad
│   └── slug-migrations.json             # Historical path mapping
├── index.md                # Generated language-neutral wiki catalog
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
lang: en | ru | uk
translation_group: stable-slug
semantic_version: 1
reviewed_semantic_version: 1
document_status: active | draft | historical
page_role: hub | explanation | application | research-appendix | source-summary | entity | relation
claim_status: [project-definition]
claims:
  - id: stable-claim-id
    status: research-hypothesis
caveat_ids: []
sources: []
---

# Page Title

Content...
```

### Naming Conventions

- **Files**: `stable-slug-en.md`, `stable-slug-ru.md`, and
  `stable-slug-uk.md`; all three peers are equal.
- **Translation groups**: stable kebab-case slugs without a language suffix.
- **Entities**: lowercase with hyphens (for example,
  `1st-past-author-{en,ru,uk}.md`).
- **Concepts**: descriptive nouns (for example,
  `latent-process-{en,ru,uk}.md`).
- `canonical` and `translation_of` are not used.

An `active` group must contain exactly one EN, RU, and UK page with equal
`semantic_version`, `reviewed_semantic_version`, `page_role`, claim IDs,
caveat IDs, source references, and synchronized `<!-- section:id -->`
markers. A page remains `draft` until semantic review is complete in all
three languages.

### Cross-References

Use wikilinks for internal references:
- `[[concept-name-en]]` from an English page
- `[[entity-name-ru]]` from a Russian page
- `[[source-name-uk]]` from a Ukrainian page

Example: `See [[latent-process-en]] for the theoretical foundation.`

Cross-language links are reserved for explicit language switching or
comparison. Repository paths in `sources` must be complete and unambiguous.

### Central Page Contract

Central explanation pages in every language contain, with shared section IDs:

1. a 90-second summary;
2. definition and scope;
3. the same life example across the triad;
4. direct observations;
5. interpretations or research hypotheses;
6. alternative explanations;
7. non-inferences;
8. practical conversation questions;
9. an explicit researcher route;
10. the next recommended page.

Pages for the four levels additionally distinguish inclusion/exclusion,
latent construct, observable indicators, possible pair mechanism,
counterexamples and rival hypotheses, falsification conditions, and current
evidence status.

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
3. Create or update all three language peers in `wiki/`
4. Separate source attribution, evidence, limitations, accepted claims,
   contested claims, and rejected or historical claims
5. Run the strict wiki checks and regenerate `index.md`
6. Append an entry to `log.md`

### Query Workflow

When answering questions:

1. Read `index.md` to find relevant pages
2. Read relevant pages for detailed information
3. Synthesize answer with citations
4. If the answer creates durable new knowledge, create or update the complete
   EN/RU/UK group and regenerate the index

### Lint Workflow

Run the blocking checks used by `.github/workflows/wiki-quality.yml`:

- `python3 -m unittest discover -s tests -v`
- `python3 scripts/validate_wiki.py --strict`
- `python3 scripts/add_wiki_section_ids.py --check`
- `python3 scripts/check_wikilinks.py --strict`
- `python3 scripts/audit_claim_language.py --strict`
- `python3 scripts/generate_wiki_index.py --check`
- `python3 scripts/generate_wiki_inventory.py --output reports/wiki-migration-inventory.json --check`
- `python3 scripts/lint-agents.py --static-only`

Also review:

- [ ] Contradictions between pages
- [ ] Stale claims superseded by new sources
- [ ] Orphan pages with no inbound links
- [ ] Important concepts lacking dedicated pages
- [ ] Missing cross-references
- [ ] Data gaps requiring web search

## Content Guidelines

### Universal Core vs Application Layers

- Core orientation, theory, compatibility, glossary, and methodology pages
  should be usable for any two people and must not assume a specific religion,
  relationship domain, culture, or family form unless the page is explicitly
  specialized.
- Worldview-neutral does not mean value-free: core pages should retain
  dignity, consent, coercion, abuse, violence, exploitation, responsibility,
  reciprocity, and safety boundaries.
- Christian pages may use Scripture-first normative language, but should link
  back to the universal construct they specialize.
- Do not present all worldviews as equally true or compatible; represent their
  commitments accurately and make conflicts visible without assigning human
  worth from a profile.

### Concept Pages

Describe theoretical constructs:
- Definition and scope
- Theoretical foundations
- Relationships to other concepts
- Practical applications

### Entity Pages

Describe specific instances:
- For types: attributed description, proposed indicators, alternatives, and caveats
- For aspects: position, hypothesized latent process, observable indicators, and limits
- For functions: attributed properties, candidate manifestations, relationships, and non-inferences

### Relation Pages

Describe compatibility patterns:
- Possible resources in a specified context
- Possible tensions in that context
- Alternative explanations
- What should be checked in real interaction

## Key Terminology

See `wiki/glossary-core-en.md` and `wiki/glossary-extended-en.md` for disambiguation of ambiguous terms; use the `-ru.md` or `-uk.md` peer when working in those languages:

- **Model** has 4 meanings (formal model, information model, Model A, mathematical model)
- **Function** has 3 meanings (psychic function, mathematical function, software function)
- **Frame** = internal principle of selection, ordering, interpretation

## Questions to Explore

When maintaining the wiki, investigate:

1. Empirical validation of typological claims
2. Cross-system correlations (Temporistics ↔ Psychosophy ↔ Socionics)
3. Prerequisites, validation, uncertainty, and safety requirements for any future measurement model
4. Observable behavioral markers for latent processes
5. Real-world case studies and outcomes

## Last Updated

2026-08-30
