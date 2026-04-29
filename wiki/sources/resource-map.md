---
title: Internet Resource Map
type: source
tags: [resources, provenance, sources, internet, governance]
created: 2026-04-29
updated: 2026-04-29
lang: en
canonical: resource-map.md
sources: []
---

# Internet Resource Map

This page is a curated map of internet resources that may be useful for PsyCalc research, source ingestion, and claim tracing.

It is **not** a list of endorsed authorities. A listed resource only means: “this resource may be useful to inspect.” Any theoretical claim still needs source-specific verification before it is used in the wiki.

See also [[multilingual-translation-policy]], [[hypothesis-status-of-psycalc]], and [[limits-of-typological-inference]].

## Purpose

The resource map helps maintainers:

- distinguish primary sources from summaries and commentary;
- avoid losing unstable web materials;
- document language, school context, and reliability caveats;
- route future source ingestion into `raw/`, `wiki/sources/`, and derived concept pages;
- keep PsyCalc’s own interpretations separate from what an external source actually says.

## Source Type Labels

Use these labels consistently:

| Label | Meaning | Typical use |
|------|---------|-------------|
| `primary-source` | Original author text, direct school archive, original interview, original publication | Core theory claims |
| `secondary-summary` | Overview, textbook-style explanation, curated article, translation with commentary | Orientation and comparison |
| `critique` | Methodological, empirical, theological, ethical, or skeptical critique | Caveats and non-claims |
| `archive` | Mirror, web archive, document repository | Preservation and source recovery |
| `community` | Forum, social media group, discussion thread, informal typing practice | Weak evidence, terminology variants |
| `tool` | Test, calculator, search index, dataset, software utility | Practical experiments, not proof |
| `project-hypothesis` | Internal PsyCalc synthesis or extension | Must not be attributed to external sources |
| `unverified` | Found but not manually reviewed yet | Intake queue only |

## Reliability Labels

Reliability is separate from source type.

| Label | Meaning |
|------|---------|
| `high` | Primary source, stable archive, peer-reviewed or well-documented publication |
| `medium` | Known topical site with identifiable authorship or editorial structure |
| `low` | Forum, anonymous blog, unsourced compilation, AI-generated text, unstable social post |
| `unknown` | Not yet reviewed |

## Availability Labels

| Label | Meaning |
|------|---------|
| `active` | URL works and appears maintained |
| `stale` | URL works but appears old or unmaintained |
| `archived` | Main access is through an archive snapshot or mirror |
| `dead` | Original URL no longer works |
| `restricted` | Paywalled, login-gated, or otherwise limited |
| `offline-copy` | Preserved locally or manually, not publicly reachable |

## Resource Card Template

Use this template for each web resource:

```md
### Resource Name

- **URL:**
- **Archive URL:**
- **Author / organization:**
- **Publication date:**
- **Accessed:** YYYY-MM-DD
- **Language:** en / ru / uk / other
- **System:** socionics / psychosophy / temporistics / methodology / theology / psychology / general
- **Type:** primary-source / secondary-summary / critique / archive / community / tool / unverified
- **Reliability:** high / medium / low / unknown
- **Availability:** active / stale / archived / dead / restricted / offline-copy
- **Useful for PsyCalc:**
- **Claims to verify before reuse:**
- **Risks / caveats:**
- **Linked wiki pages:**
```

## Intake Queue

These sections are placeholders for future audited entries. Do not treat an empty section as a claim that no resources exist.

### Socionics

Use this section for resources on Model A, information elements, intertype relations, Reinin traits, school-specific extensions, and terminology variants.

Preferred order:

1. primary or school-origin materials;
2. stable reference sites and archived texts;
3. secondary explanations;
4. community discussions and tools.

### Psychosophy

Use this section for resources on Afanasyev’s model, the four aspects, function positions, type descriptions, relation descriptions, and typing methods.

Preferred order:

1. Afanasyev-related primary texts and archives;
2. direct school materials;
3. secondary descriptions and translations;
4. community typing materials and tests.

### Temporistics

Use this section for resources on Past, Present, Future, Eternity, position archetypes, full type permutations, and any proposed relation logic.

Preferred order:

1. original temporistics texts and author-linked sources;
2. archived source pages already represented in `raw/temporistics/`;
3. secondary summaries;
4. PsyCalc-only hypotheses, clearly marked as `project-hypothesis`.

### Methodology and Psychometrics

Use this section for resources on validation, reliability, construct validity, measurement invariance, personality assessment, compatibility outcomes, and baseline models such as Big Five or HEXACO.

### Theology, Ethics, and Pastoral Boundaries

Use this section for resources that help separate typological heuristics from Christian anthropology, pastoral discernment, moral responsibility, and family formation guidance.

## Claim-Use Rules

1. A URL is not enough. Important claims need a specific source page, quoted passage or close paraphrase, and access date.
2. Do not cite community resources for core theory claims unless a primary or stronger secondary source supports the same point.
3. If PsyCalc extends a source, label the extension as `project-hypothesis`.
4. If sources disagree, document the disagreement instead of merging them into a false consensus.
5. AI-generated summaries are not evidence. They can only help find sources that humans verify.
6. Broken links should be replaced with archive links where possible, not silently deleted.

## Maintenance Rhythm

- Add a resource card when a new web resource is found.
- During source ingestion, promote verified materials into `raw/` and create or update a `wiki/sources/` page.
- Check high-value links quarterly or before major publication.
- Mark dead links as `dead` and add an archive URL if available.
- Keep this map navigational; detailed analysis belongs in dedicated source pages.
