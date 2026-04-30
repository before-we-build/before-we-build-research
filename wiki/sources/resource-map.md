---
title: Internet Resource Map
type: source
tags: [resources, provenance, sources, internet, governance]
created: 2026-04-29
updated: 2026-04-30
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

| Resource | URL | Type | Language | Useful for PsyCalc | Caveat |
|---|---|---|---|---|---|
| Wikisocion Archive | https://wikisocion.github.io/ | archive / secondary-summary | EN | Convenient entry point for Model A, information elements, intertype relations, dichotomies, and type pages | Community archive, not an official school; article quality is uneven |
| Classic Socionics | https://classicsocionics.wordpress.com/ | primary-source / archive | EN | Translations and collections of classical Socionics texts, including early Aushra-related materials | Translation/editorial project; verify original publication context before key claims |
| International Institute of Socionics | https://socionic.info/en/esocjur.html#top | primary-source / school | EN/RU/UA | Journals, conferences, and the Bukalov/IIS institutional layer | Institutional claims of scientific status need independent evaluation |
| Humanitarian Socionics / Gulenko | https://socioniks.net/ | primary-source / school | RU/UA/EN | School-specific materials on Gulenko, Model G, subtypes, relations, and signs | School-specific, not neutral Model A canon; mark Model G separately |
| Socionika.info | https://socionika.info/ | secondary-summary / tool | RU | Popular hub for Model A, aspects, Reinin signs, relation tables, and tests | Popularizing/compiled resource; source depth varies |
| Socionavigator | https://socionavigator.com/ | tool / secondary-summary | RU/EN | Diagnostic materials, diagrams, FAQ, and authorial tools | Authorial methodology requires separate review |
| World Socionics Society | https://worldsocionics.org/ | secondary-summary | EN | Modern English-language introduction and educational material | Authorial/commercial layer; may simplify disputed points |
| The16types forum | https://www.the16types.info/ | community | EN | Historical discussions, school disputes, translations, typing debates | Noisy forum evidence; not for core claims |
| Reddit r/Socionics | https://www.reddit.com/r/Socionics/ | community | EN | Current audience questions and terminology confusion, especially MBTI overlap | Low reliability; use only as reception signal |
| Wikipedia — Socionics | https://en.wikipedia.org/wiki/Socionics | critique / overview | EN | External critical framing and quick bibliographic orientation | Not a primary source; article framing may be disputed |

### Psychosophy

Use this section for resources on Afanasyev’s model, the four aspects, function positions, type descriptions, relation descriptions, and typing methods.

Preferred order:

1. Afanasyev-related primary texts and archives;
2. direct school materials;
3. secondary descriptions and translations;
4. community typing materials and tests.

| Resource | URL | Type | Language | Useful for PsyCalc | Caveat |
|---|---|---|---|---|---|
| Psychosophy.ru | https://psychosophy.ru/ | community / secondary-summary | RU | Major modern hub for types, functions, tests, books, and ecosystem navigation | Not Afanasyev primary text; may include editorial and commercial layers |
| Psychosophy of A. Yu. Afanasyev | https://psychosophy.ru/psychosophy | secondary-summary | RU | Introductory overview of four aspects, positions, and basic terms | Interpretive overview, not canonical source text |
| Psychosophy.ru tests | https://psychosophy.ru/tests | tool | RU | Mapping of current online typing tools | Tests are not validated psychometric instruments unless documented otherwise |
| Syntax of Love — book page | https://psychosophy.ru/books/sintaksislubvi | primary-source / bibliography | RU | Bibliographic anchor for the central Afanasyev text | Page about the book; verify edition and full text separately |
| Afanasyev Typology — Google Books | https://books.google.com/books/about/Типология_Афанасьева.html?id=IEptDwAAQBAJ | archive / bibliography | RU | Bibliographic metadata and discoverability for printed tradition | Partial access; not a substitute for the full primary text |
| xsp.ru Psychosophy | https://www.xsp.ru/psychosophy/ | archive | RU | Older web archive layer for type descriptions and historical context | May contain outdated or weakly attributed formulations |
| Unified Typological Project — Psychosophy | http://typologies.ru/psycheyoga/ | archive / secondary-summary | RU | Early typology-runet summaries and cross-system framing | Old resource; possible broken links and mixed school assumptions |
| Large Psychosophy test | http://typtest.ru/psychosofy.htm | tool | RU | Practical test resource for the tools layer | Methodology and validity are unclear |
| Afanasyev test | https://typtest.ru/aleafan.htm | tool | RU | Alternative test entry point | The name does not guarantee authorial authenticity |
| Psychosophy of Afanasyev — Психологи.рф | https://психологи.рф/психософия-афанасьева/ | secondary-summary | RU | External popular overview outside the core community | Needs checking against primary and archive materials |

### Temporistics

Use this section for resources on Past, Present, Future, Eternity, position archetypes, full type permutations, and any proposed relation logic.

Preferred order:

1. original temporistics texts and author-linked sources;
2. archived source pages already represented in `raw/temporistics/`;
3. secondary summaries;
4. PsyCalc-only hypotheses, clearly marked as `project-hypothesis`.

| Resource | URL | Type | Language | Useful for PsyCalc | Caveat |
|---|---|---|---|---|---|
| Theory Description — Temporistics | http://temporistics.ru/?q=theory_description | primary-source | RU | Core theory entry point: aspects, positions, and general frame | Site may be unstable; authorial typology, not empirically validated model |
| Types — Temporistics | http://temporistics.ru/?q=types | primary-source | RU | Key index for 24 full types, 16 archetypes, tetrads, and aliases | Compact reference; does not replace full descriptions |
| Comet in the Brain, or the Birth of Temporistics | http://temporistics.ru/?q=node/66 | primary-source | RU | Origin story, authorship context, links to Berdyaev and Afanasyev | Historical authorial testimony, not a neutral history |
| How to Distinguish Author from Critic | http://temporistics.ru/?q=node/70 | primary-source | RU | Useful for distinguishing close Past archetypes, especially 1P vs 3P | Narrow article, not a general overview |
| Mystery of the Third Aspect | URL уточнить | primary-source | RU | Important text for understanding third-position dynamics | Exact source URL still needs manual verification/archive link |
| Wayback snapshots for temporistics.ru | https://web.archive.org/web/*/http://temporistics.ru/* | archive | multi | Recovery of unstable/dead pages and version tracking | Snapshots may be incomplete; verify dates and page integrity |
| Personality Database / Temporistics pages | URL уточнить | community | EN | English aliases and non-canonical reception | Fan/community synthesis; not source-backed canon |
| Forum discussions of Temporistics | URL уточнить | community | RU/EN | Reception history, examples, disputed interpretations | Low evidential value; use only with strict caveats |

### Methodology and Psychometrics

Use this section for resources on validation, reliability, construct validity, measurement invariance, personality assessment, compatibility outcomes, and baseline models such as Big Five or HEXACO.

| Resource | URL | Type | Language | Useful for PsyCalc | Caveat |
|---|---|---|---|---|---|
| Standards for Educational and Psychological Testing | https://www.testingstandards.net/ | methodology / tool | EN | High-level standards for validity, reliability, fairness, and score interpretation | Not typology-specific; some materials may not be fully open access |
| COSMIN checklists | https://www.cosmin.nl/tools/checklists-assessing-methodological-study-qualities/ | methodology / tool | EN | Practical criteria for measurement instrument quality | Developed for health/PROM contexts; transfer to personality requires care |
| Cronbach & Meehl — Construct Validity in Psychological Tests | https://doi.org/10.1037/h0040957 | primary-source / methodology | EN | Classic construct validity framing | Older source; does not cover modern CFA/IRT/invariance practice |
| Messick — Validity of Psychological Assessment | https://doi.org/10.1037/0003-066X.50.9.741 | primary-source / methodology | EN | Validity as justification of inferences from scores | Strong theory, not a simple implementation checklist |
| Flake, Pek & Hehman — Construct Validation | https://doi.org/10.1177/1948550617693063 | critique / methodology | EN | Modern critique of weak construct validation in social/personality research | Not typology-specific |
| Soto & John — BFI-2 | https://doi.org/10.1037/pspp0000096 | primary-source / baseline | EN | Big Five baseline for personality assessment comparisons | Trait baseline, not final truth about personality |
| International Personality Item Pool | https://ipip.ori.org/ | tool / baseline | EN | Open item pool for baseline scales | Quality depends on selected scale and procedure |
| HEXACO Personality Inventory-Revised | https://hexaco.org/ | tool / baseline | EN | Alternative trait baseline, including Honesty-Humility | Self-report trait model; not a direct test of typological categories |
| McCrae & Costa — MBTI from the Five-Factor Model perspective | https://doi.org/10.1111/j.1467-6494.1989.tb00759.x | critique | EN | Bridge for comparing type labels with continuous trait dimensions | MBTI-specific; do not automatically transfer conclusions to all typologies |
| Pittenger — Measuring the MBTI... And Coming Up Short | URL уточнить | critique | EN | Classic critique of reliability/validity and forced dichotomies | Older and MBTI-specific; verify publication URL before formal citation |
| Boyle — MBTI: Some Psychometric Limitations | URL уточнить | critique | EN | Often-cited critique of psychometric limits of typological dichotomies | MBTI-specific; update with modern evidence where possible |

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
