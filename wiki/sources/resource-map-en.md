---
title: Internet Resource Map
type: source
tags: [resources, provenance, sources, internet, governance]
created: 2026-04-29
updated: 2026-06-07
lang: en
sources: []
translation_group: resource-map
semantic_version: 1
reviewed_semantic_version: 1
document_status: active
page_role: source-summary
claim_status: [source-attribution]
claims: []
caveat_ids: []
---

# Internet Resource Map

This page is a curated map of internet resources that may be useful for Before We Build research, source ingestion, and claim tracing.

It is **not** a list of endorsed authorities. A listed resource only means: “this resource may be useful to inspect.” Any theoretical claim still needs source-specific verification before it is used in the wiki.

See also [[multilingual-translation-policy-en]], [[epistemic-status-and-inference-limits-en]], and [[epistemic-status-and-inference-limits-en]].

<!-- section:purpose -->
## Purpose

The resource map helps maintainers:

- distinguish primary sources from summaries and commentary;
- avoid losing unstable web materials;
- document language, school context, and reliability caveats;
- route future source ingestion into `raw/`, `wiki/sources/`, and derived concept pages;
- keep Before We Build’s own interpretations separate from what an external source actually says.

<!-- section:source-type-labels -->
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
| `project-hypothesis` | Internal Before We Build synthesis or extension | Must not be attributed to external sources |
| `unverified` | Found but not manually reviewed yet | Intake queue only |

<!-- section:reliability-labels -->
## Reliability Labels

Reliability is separate from source type.

| Label | Meaning |
|------|---------|
| `high` | Primary source, stable archive, peer-reviewed or well-documented publication |
| `medium` | Known topical site with identifiable authorship or editorial structure |
| `low` | Forum, anonymous blog, unsourced compilation, AI-generated text, unstable social post |
| `unknown` | Not yet reviewed |

<!-- section:availability-labels -->
## Availability Labels

| Label | Meaning |
|------|---------|
| `active` | URL works and appears maintained |
| `stale` | URL works but appears old or unmaintained |
| `archived` | Main access is through an archive snapshot or mirror |
| `dead` | Original URL no longer works |
| `restricted` | Paywalled, login-gated, or otherwise limited |
| `offline-copy` | Preserved locally or manually, not publicly reachable |

<!-- section:resource-card-template -->
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
- **Useful for Before We Build:**
- **Claims to verify before reuse:**
- **Risks / caveats:**
- **Linked wiki pages:**
```

<!-- section:intake-queue -->
## Intake Queue

These sections are placeholders for future audited entries. Do not treat an empty section as a claim that no resources exist.

<!-- section:socionics -->
### Socionics

Use this section for resources on Model A, information elements, intertype relations, Reinin traits, school-specific extensions, and terminology variants.

Preferred order:

1. primary or school-origin materials;
2. stable reference sites and archived texts;
3. secondary explanations;
4. community discussions and tools.

| Resource | URL | Type | Language | Useful for Before We Build | Caveat |
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

<!-- section:psychosophy -->
### Psychosophy

Use this section for resources on Afanasyev’s model, the four aspects, function positions, type descriptions, relation descriptions, and typing methods.

Preferred order:

1. Afanasyev-related primary texts and archives;
2. direct school materials;
3. secondary descriptions and translations;
4. community typing materials and tests.

| Resource | URL | Type | Language | Useful for Before We Build | Caveat |
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

<!-- section:temporistics -->
### Temporistics

Use this section for resources on Past, Present, Future, Eternity, position archetypes, full type permutations, and any proposed relation logic.

Preferred order:

1. original temporistics texts and author-linked sources;
2. archived source pages already represented in `raw/temporistics/`;
3. secondary summaries;
4. Before We Build-only hypotheses, clearly marked as `project-hypothesis`.

| Resource | URL | Type | Language | Useful for Before We Build | Caveat |
|---|---|---|---|---|---|
| Theory Description — Temporistics | http://temporistics.ru/?q=theory_description | primary-source | RU | Core theory entry point: aspects, positions, and general frame | Site may be unstable; authorial typology, not empirically validated model |
| Types — Temporistics | http://temporistics.ru/?q=types | primary-source | RU | Key index for 24 full types, 16 archetypes, tetrads, and aliases | Compact reference; does not replace full descriptions |
| Comet in the Brain, or the Birth of Temporistics | http://temporistics.ru/?q=node/66 | primary-source | RU | Origin story, authorship context, links to Berdyaev and Afanasyev | Historical authorial testimony, not a neutral history |
| How to Distinguish Author from Critic | http://temporistics.ru/?q=node/70 | primary-source | RU | Useful for distinguishing close Past archetypes, especially 1P vs 3P | Narrow article, not a general overview |
| Mystery of the Third Aspect | http://temporistics.ru/?q=node/90 | primary-source | RU | Important text for understanding third-position dynamics | Key authorial article on the third/painful aspect |
| Wayback snapshots for temporistics.ru | https://web.archive.org/web/*/http://temporistics.ru/* | archive | multi | Recovery of unstable/dead pages and version tracking | Snapshots may be incomplete; verify dates and page integrity |
| Personality Database / Temporistics pages | https://www.personality-database.com/subcategory/22184/temporistics-personality-type | community | EN | English aliases and non-canonical reception | URL needs verification (access may be blocked by Cloudflare, returns 403 for bots); fan/community synthesis, not source-backed canon |
| Forum discussions of Temporistics | https://socioforum.su/viewforum.php?f=959 | community | RU | Reception history, examples, and disputed interpretations | URL needs verification; low evidential value, use only with strict caveats |

<!-- section:cross-system-typology-resources -->
### Cross-System Typology Resources

Use this section for databases, forums, and theoretical frameworks that attempt to compare, synthesize, or house multiple typological systems (e.g., Socionics, Psychosophy, Temporistics, and MBTI) in a single platform.

| Resource | URL | Type | Language | Useful for Before We Build | Caveat |
|---|---|---|---|---|---|
| Unified Typological Project | http://typologies.ru/ | archive / secondary-summary | RU | Mapping and nesting different typologies using logical levels based on the Dilts pyramid | Highly theoretical; contains outdated links and mixes diverse school assumptions |
| Personality Database | https://www.personality-database.com/ | community / tool | EN | Large dataset of crowd-sourced typological profiles across multiple systems | Low reliability; profiles are crowd-voted and often lack formal methodology. Note: bot access may be blocked by Cloudflare (returns 403), requires manual verification. |
| Socioforum | https://socioforum.su/ | community | RU | Largest Slavic discussion forum for cross-system typing and correlation debates | Unstructured forum discussions; low canonical evidence value, but rich reception history |

<!-- section:internal-synthesis-note-psychosophy-vs-socionics-in-the-before-we-build-research-layer -->
#### Internal synthesis note: Psychosophy vs Socionics in the Before We Build research layer

- **Type:** `project-hypothesis`
- **System:** cross-system / psychosophy / socionics
- **Useful for Before We Build:** keeps Psychosophy and Socionics from being collapsed merely because both can speak about “logic,” “process,” “structure,” or “action.”
- **Working distinction:** Socionics is treated as a map of information modeling: how a person models a situation and interaction through information channels. For example, structural logic models through relations, correspondence, order, contradiction, classification, hierarchy, and rule-like structure; pragmatic/business logic models through processes, results, sequence of actions, resource conversion, efficiency, and applicability.
- **Psychosophy distinction:** Psychosophy is treated as a map of inner action organization: what a person tries to synthesize, what they must analyze, and how much energy, confidence, tension, proof-demand, avoidance, or support-seeking appears around that process.
- **Research caveat:** this is a Before We Build interpretive hypothesis, not an externally verified claim and not a deterministic description of a person. Use it as a translation layer for “typical character patterns, not fixed human types.”

<!-- section:methodology-and-psychometrics -->
### Methodology and Psychometrics

Use this section for resources on validation, reliability, construct validity, measurement invariance, personality assessment, compatibility outcomes, and baseline models such as Big Five or HEXACO.

| Resource | URL | Type | Language | Useful for Before We Build | Caveat |
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
| Pittenger — Measuring the MBTI... And Coming Up Short | https://web.archive.org/web/*/https://www.indiana.edu/~jobtalk/HRMWebsite/hrm/articles/develop/mbti.pdf | critique / archive | EN | Classic critique of reliability/validity and forced dichotomies | Older and MBTI-specific; use archived copies and verify the exact snapshot before formal citation |
| Boyle — MBTI: Some Psychometric Limitations | https://doi.org/10.1111/j.1742-9544.1995.tb01750.x | critique | EN | Often-cited critique of psychometric limits of typological dichotomies | MBTI-specific; DOI may require publisher access and should be checked manually before citation |
| Volkov, Voloskova, Gladkikh — Psychological Compatibility & Team Climate | https://humanization.ru/wp-content/uploads/2026/04/%D0%93%D0%9E-4-2025.pdf#page=41 | primary-source / psychology | RU | Academic validation: "psychological compatibility is a multilevel phenomenon" & impact on socio-psychological climate | Peer-reviewed journal article (Humanization of Education, 2025 №4); professional group focus |
| Guo et al. — Acute Stress Impacts Executive-Social Function | https://doi.org/10.1002/brb3.70231 | primary-source / neuroscience | EN | Neuroimaging validation: dyadic stress couples executive control and social communication (fNIRS hyperscanning) | Laboratory dyadic task; does not prove typologies |
| Joel et al. — Machine Learning Predictors of Relationship Quality | https://doi.org/10.1073/pnas.1917036117 | primary-source / empirical-benchmark | EN | Empirical benchmark across 11,196 couples: trait-matching explains ~0% of satisfaction; relationship processes predict ~45% | Self-report questionnaires; non-experimental longitudinal observational data |
| Butler — Temporal Interpersonal Emotion Systems (TIES) | https://doi.org/10.1177/1088868311411164 | primary-source / dynamical-systems | EN | Theoretical/methodological framework: emotional co-regulation as non-linear temporal dynamical coupling across channels | Dynamical theory synthesis; emotional linkage can amplify conflict as well as harmony |
| Rossignac-Milon et al. — Merged Minds: Generalized Shared Reality | https://doi.org/10.1037/pspi0000266 | primary-source / social-cognition | EN | Empirical benchmark (9 studies): generalized shared reality predicts commitment and triggers compensatory repair under threat | Subjectively experienced epistemic commonality, not verified objective truth |
| Fitzsimons, Finkel & vanDellen — Transactive Goal Dynamics | https://doi.org/10.1037/a0039654 | primary-source / self-regulation | EN | Dyadic self-regulation framework: interdependent goal pursuit, volition pooling, and coordination costs | Theoretical model; task efficiency can coexist with individual burden or reduced agency |
| Schaner — Intrahousehold Preference Heterogeneity & Savings | https://doi.org/10.1257/app.20130271 | primary-source / field-experiment | EN | Randomized field experiment: mismatch in spouses' intertemporal discount rates causes strategic mistrust and welfare loss | Monetary choices in rural developing economy; shaped by institutional bargaining and gender norms |


<!-- section:theology-ethics-and-pastoral-boundaries -->
### Theology, Ethics, and Pastoral Boundaries

Use this section for resources that help separate typological heuristics from Christian anthropology, pastoral discernment, moral responsibility, and family formation guidance.

| Resource | URL | Type | Language | Useful for Before We Build | Caveat |
|---|---|---|---|---|---|
| 9Marks resources on church ministry and discipleship | https://www.9marks.org/ | critique / pastoral-methodology | EN | Pastoral frame for keeping identity, holiness, membership, and discipleship in biblical categories rather than typological labels | Homepage verified; use site search to locate specific articles before citing |
| CCEF resources on biblical counseling | https://www.ccef.org/ | critique / methodology | EN | Biblical-counseling frame for distinguishing observations about the heart from Christian anthropology, repentance, and sanctification | Homepage verified; use site search to locate specific articles before citing |
| The State of Theology | https://thestateoftheology.com/ | primary-source / tool | EN | Baseline survey of theological beliefs and moral constructs, showing deviation from classical orthodoxy | Focused on doctrinal stance rather than personality traits, but serves as a benchmark for worldview |
| The Enneagram: Gnostic or Just Silly? | https://www.thegospelcoalition.org/article/enneagram-gnostic-silly/ | critique | EN | Sharp critique of modern typology trends, highlighting gnostic roots and reductionist traps | URL needs verification (access may be blocked by Cloudflare, returns 403 for bots); specific to Enneagram but generalizable to other typologies |

<!-- section:claim-use-rules -->
## Claim-Use Rules

1. A URL is not enough. Important claims need a specific source page, quoted passage or close paraphrase, and access date.
2. Do not cite community resources for core theory claims unless a primary or stronger secondary source supports the same point.
3. If Before We Build extends a source, label the extension as `project-hypothesis`.
4. If sources disagree, document the disagreement instead of merging them into a false consensus.
5. AI-generated summaries are not evidence. They can only help find sources that humans verify.
6. Broken links should be replaced with archive links where possible, not silently deleted.

<!-- section:maintenance-rhythm -->
## Maintenance Rhythm

- Add a resource card when a new web resource is found.
- During source ingestion, promote verified materials into `raw/` and create or update a `wiki/sources/` page.
- Check high-value links quarterly or before major publication.
- Mark dead links as `dead` and add an archive URL if available.
- Keep this map navigational; detailed analysis belongs in dedicated source pages.

<!-- section:source-assessment -->
## Source Assessment

<!-- section:source-claims -->
### What the Source Claims

The resource map claims to catalog the main raw materials, wiki summaries, and research routes used by the repository.

<!-- section:source-evidence -->
### Data or Evidence Provided

Its evidence is repository paths, source metadata, and links to maintained pages; it contains no independent empirical finding.

<!-- section:source-limitations -->
### Limitations

Coverage can be incomplete or stale, categories are editorial, and the presence of a resource does not assess its quality.

<!-- section:bwb-accepts -->
### What BWB Accepts

BWB accepts the map as navigation and provenance infrastructure.

<!-- section:bwb-contested -->
### What Remains Contested or Open

Completeness, priority, and the current relevance of individual entries remain open to periodic audit.

<!-- section:bwb-rejected-or-historical -->
### Rejected or Historical-Only

BWB rejects treating inclusion as endorsement, agreement, empirical support, or permission to bypass the corresponding source assessment.
