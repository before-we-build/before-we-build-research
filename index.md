# Index — Cognitive Matchmaker Wiki

This is the catalog of all pages in the wiki. The LLM updates this on every ingest.

## Wiki Structure

```
raw/           — Immutable source documents
wiki/          — LLM-generated wiki
├── concepts/   — Theoretical concept pages
├── entities/  — Entity pages (types, aspects, functions)
├── relations/  — Compatibility patterns, intertype relations
└── sources/   — Source summaries and derived docs
```

---

## Wiki Pages

### Concepts

| Page | Summary | Sources |
|------|---------|---------|
| [[main-idea]] | Theoretical foundations: integration of three typologies | - |
| [[latent-process]] | Hidden internal mechanisms judged by observable traces | latent-process.md |
| [[plan]] | Product and technical plan | plan.md |
| [[weight-calibration]] | Research plan for validating scoring weights | weight-calibration.md |
| [[cross-typology-mapping-framework]] | Unified pipeline: PersonaNexus + JPAF + OASIS-sim + OASIS-platform | typology-best-architecture.md |
| [[cross-typology-terminology-conflicts]] | Terms with different meanings across systems (Extraversion, Function, etc.) | web research |
| [[typology-authors-timeline]] | Who created which typology and when (Jung, Eysenck, Augustinavičiūtė, etc.) | web research |
| [[typology-activity-theory-mapping]] | Project heuristic: Socionics=Tactical, Psychosophy=Operational, Temporistics=Strategic | web research |
| [[typology-researchers]] | Academic validation researchers and studies (Blutner, Pietrak, Kovalenko, Rook, etc.) | web research |
| [[big-five-alternatives]] | Alternatives to Big Five: HEXACO, 16PF, PEN, RST, Dark Tetrad | web research |
| [[temporistics-eternity-altruism-hypothesis]] | Hypothesis: 1E/4E Eternity → collectivism, 2E/3E → individualism | user observation |
| [[agentic-skills-hang-the-dj]] | 8 agent skills to implement simulation-based compatibility testing | skills/index.md |
| [[afanasyev-model]] | Alexander Afanasyev's Psychosophy model | psycalc/Psyche-Yoga |
| [[afanasyev-syntax-of-love]] | Original "Syntax of Love" source book | psycalc/Psyche-Yoga |
| [[psychosophy-model]] | Psychosophy type structure | psycalc/Psyche-Yoga |
| [[psychosophy-functions]] | Function block descriptions | psycalc/Psyche-Yoga |
| [[socionics-model-a]] | Model A: 8 cognitive functions | raw/socionics |
| [[temporistics-model]] | Temporistics type structure | raw/temporistics |
| [[temporal-aspects]] | Past, Present, Future, and Eternity aspects | raw/temporistics |
| [[intertype-relations-matrix]] | Full compatibility matrix | raw/socionics |

### Entities — Temporistics Types (24)

#### Past Aspect (Прошлое)

| Page | Summary | Sources |
|------|---------|---------|
| [[avtor-author]] | 1st Past — forms identity, creates own story | raw/temporistics/author.md |
| [[chronicler-letopisets]] | 2nd Past — uses past as tool, good memory | raw/temporistics/letopisets-chronicler.md |
| [[kritik-critic]] | 3rd Past — derives harsh conclusions from painful past | raw/temporistics/critic.md |
| [[reader-chitatel]] | 4th Past — treats past as resource, blind spot | raw/temporistics/chitatel-reader.md |

#### Present Aspect (Настоящее)

| Page | Summary | Sources |
|------|---------|---------|
| [[host-khozyain]] | 1st Present — self-realizes through "here and now" | raw/temporistics/khozyain-host.md |
| [[local-mestnyi]] | 2nd Present — comfortable anywhere, uses present as tool | raw/temporistics/mestnyi-local.md |
| [[exile-izgnannik]] | 3rd Present — painful sense of not belonging | raw/temporistics/izgnannik-exile.md |
| [[guest-gost]] | 4th Present — blind to present, floats with current | raw/temporistics/gost-guest.md |

#### Future Aspect (Будущее)

| Page | Summary | Sources |
|------|---------|---------|
| [[captain-kapitan]] | 1st Future — creates process, plans, visionary | raw/temporistics/kapitan-captain.md |
| [[stewersman-rulevoi]] | 2nd Future — tactical, adapts, follows natural flow | raw/temporistics/rulevoi-steversman.md |
| [[stowaway-bezbiletnik]] | 3rd Future — painful fear of the future | raw/temporistics/bezbiletnik-stowaway.md |
| [[passenger-passazhir]] | 4th Future — blind to future, goes with the flow | raw/temporistics/passazhir-passenger.md |

#### Eternity Aspect (Вечность)

| Page | Summary | Sources |
|------|---------|---------|
| [[guru]] | 1st Eternity — creates meaning, spreads ideology | raw/temporistics/guru.md |
| [[philosopher-filosof]] | 2nd Eternity — treats meaning as tool, analytical | raw/temporistics/filosof-philosopher.md |
| [[philistine-obyvatel]] | 3rd Eternity — painful search for meaning | raw/temporistics/obyvatel-philistine.md |
| [[student-uchenik]] | 4th Eternity — blind to meaning, accepts others' ideologies | raw/temporistics/uchenik-student.md |

### Entities — Psychosophy

| Page | Summary | Sources |
|------|---------|---------|
| [[psychosophy-overview]] | Overview of psychosophy: Will/Emotion/Logic/Physics | raw/psychosophy/ |

### Entities — Socionics

| Page | Summary | Sources |
|------|---------|---------|
| [[socionics-overview]] | Overview of socionics: 8 IM elements, Model A, 16 types | raw/socionics/ |

#### Alpha Quadra (Idealistic)

| Page | Summary | Code |
|------|---------|------|
| [[ile-intuitive-logical-extrovert]] | Inventive, enthusiastic, creative | ILE (ENTp) |
| [[lii-intuitive-logical-introvert]] | Logical analyst, systems thinker | LII (INTj) |
| [[ese-emotional-sensory-extrovert]] | Caring host, warm, hospitable | ESE (ESFj) |
| [[sli-sensory-logical-introvert]] | Craftsman, practical, skilled | SLI (ISTp) |

#### Beta Quadra (Normative)

| Page | Summary | Code |
|------|---------|------|
| [[sle-sensory-logical-extrovert]] | Commander, bold leader, decisive | SLE (ESTp) |
| [[lie-logical-intuitive-extrovert]] | Entrepreneur, strategic organizer | LIE (ENTj) |
| [[eie-emotional-intuitive-extrovert]] | Inspirer, charismatic dramatist | EIE (ENFj) |
| [[lsi-sensory-logical-introvert]] | Inspector, principled guardian | LSI (ISTj) |

#### Gamma Quadra (Pragmatic)

| Page | Summary | Code |
|------|---------|------|
| [[sie-sensory-ethical-extrovert]] | Motivator, business-like actor | SIE (ESFp) |
| [[ili-intuitive-logical-introvert]] | Analyst, strategic critic | ILI (INTp) |
| [[esi-emotional-sensory-introvert]] | Protector, loyal sentinel | ESI (ISFj) |
| [[lse-logical-sensory-extrovert]] | Administrator, practical organizer | LSE (ESTj) |

#### Delta Quadra (Humanitarian)

| Page | Summary | Code |
|------|---------|------|
| [[iee-intuitive-ethical-extrovert]] | Visionary, humanitarian | IEE (ENFp) |
| [[eii-emotional-intuitive-introvert]] | Humanist, moralist | EII (INFj) |
| [[see-sensory-ethical-extrovert]] | Politician, social climber | SEE (ESFp) |
| [[lii-logical-intuitive-introvert]] | Analyst, scientific researcher | LII (INTj) |

### Relations

| Page | Summary | Sources |
|------|---------|---------|
| [[socionics-intertype-relations]] | Socionics relation system summary | raw/socionics/intertype-relations.md |
| [[psychosophy-intertype-relations]] | Psychosophy relation system summary | socionika.info / Syntax of Love |
| [[temporistics-intertype-relations]] | Experimental Temporistics compatibility heuristics | project synthesis |

### Sources (Derived)

| Page | Summary | Raw Sources |
|------|---------|------------|
| [[temporistics-detailed]] | Strategic level: Past/Present/Future/Eternity aspects, 24 types | raw/temporistics/ |
| [[psychosophy-detailed]] | Operational level: Logic/Emotion/Will/Physics functions | raw/psychosophy/ |
| [[socionics-detailed]] | Tactical level: Model A, 8 functions, 16 types | raw/socionics/ |
| [[typology-full-description]] | Complete reference for all three typologies | - |
| [[common-projects]] | Related projects and research | - |
| [[deep-research-report]] | Agent frameworks, orchestration, memory comparison | - |
| [[research-program]] | Validation framework for typological constructs | research-program.md |
| [[hang-the-dj-simulation-compatibility]] | Black Mirror episode used as simulation metaphor, including the fictional 99.8% reveal | - |
| [[brain-typology-neuroscience]] | Mapping typology systems to brain regions and neural networks | web research |

### Research on AI in Psychology

| Page | Summary | Source |
|------|---------|--------|
| [[llm-emulate-personality-nature-2025]] | GPT-4 emulates constrained Big Five response patterns with high internal consistency | Scientific Reports |
| [[llm-psychological-simulators-methodology]] | Methodological guide: LLM as psychological simulators | arXiv:2506.16702 |
| [[ai-agents-psychometric-approach]] | Psychometric approach to assigning personalities to AI agents using BFI-2 | arXiv:2410.19238 |
| [[psypilot-ai-psychologist-toolkit]] | AI as copilot for psychologists: risks and governance | Frontiers in Psychology |
| [[s-researcher-llm-social-scientists]] | 100K agents for social science research, human-in-the-loop | arXiv:2604.01520 |
| [[ai-experiment-participants]] | Trained AI as experiment participants: behavioral economics | Current Psychology |
| [[smart-mobilization-typology-wartime]] | AI recruitment, personality typology in wartime | Web research 2026 |
| [[psychosophy-typing-methods]] | Methods for psychosophy typing: tests, dichotomies, accentuations | Web research 2026 |

### Reference

| Page | Summary |
|------|---------|
| [[glossary-core]] | Core terminology definitions |
| [[glossary-extended]] | Extended disambiguation (60+ terms) |
| [[project-requirements]] | Project description |
| [[scientific-contribution-statement]] | Academic contribution statement |

---

## Raw Sources

### temporistics/

| Source | Summary | Archived |
|--------|---------|----------|
| theory-description.md | Full theory description | 2025-01-15 |
| types.md | Type matrix, tetra classifications | 2025-04-15 |
| mystery-of-third-aspect.md | Dr. Radut's article on the third aspect | - |
| author.md | Author (1P) type description | - |
| critic.md | Critic (3P) type description | - |
| guru.md | Guru (1E) type description | - |
| khozyain-host.md | Host (1 Present) type description | 2025-01-15 |
| mestnyi-local.md | Local (2 Present) type description | 2025-01-15 |
| izgnannik-exile.md | Exile (3 Present) type description | 2025-01-15 |
| gost-guest.md | Guest (4 Present) type description | 2025-01-15 |
| kapitan-captain.md | Captain (1 Future) type description | 2025-01-15 |
| rulevoi-steversman.md | Steersman (2 Future) type description | 2025-02-14 |
| bezbiletnik-stowaway.md | Stowaway (3 Future) type description | 2024-12-04 |
| passazhir-passenger.md | Passenger (4 Future) type description | 2025-02-14 |
| filosof-philosopher.md | Philosopher (2 Eternity) type description | 2025-01-15 |
| obyvatel-philistine.md | Philistine (3 Eternity) type description | 2024-12-04 |
| uchenik-student.md | Student (4 Eternity) type description | 2025-03-17 |
| letopisets-chronicler.md | Chronicler (2 Past) type description | 2025-01-15 |
| chitatel-reader.md | Reader (4 Past) type description | 2024-12-04 |
| how-to-distinguish-author-from-critic.md | Article on distinguishing Past types | 2025-01-15 |
| comet-in-brain-birth-of-temporistics.md | History of Temporistics creation | 2025-01-15 |

### psychosophy/

| Source | Summary | Source |
|--------|---------|--------|
| what-is-psychosophy.md | Official definition and summary | Psychosophy Library |
| aspects.md | The four aspects: Will, Emotion, Logic, Physics | Psychosophy Library |
| first-function.md | First function properties | Psychosophy Library |
| second-function.md | Second function properties | Psychosophy Library |
| third-function.md | Third function properties | Psychosophy Library |
| fourth-function.md | Fourth function properties | Psychosophy Library |
| psychosophy-quadras.md | Six psychosophy quadras and type clusters | Psychosophy Library / community sources |
| psychosophy-accentuations.md | Subtype system: 8 accentuations per function | BestSocionics |
| psychosophy-compatibility-research.md | Synthax of Love, 4 Greek models, function compatibility | Multiple sources |

### Intertype Relations

| Page | Summary | Sources |
|------|---------|---------|
| [[socionics-intertype-relations]] | Complete descriptions of 16 Socionics relationship types (EN/UK) | psycalc/socionics_matching_algorithm |
| [[temporistics-intertype-relations]] | Temporal relationship types based on aspect position | psycalc/temporistics_matching_algorithm |
| [[psychosophy-intertype-relations]] | Psychosophy relationship compatibility | psycalc/temporistics_matching_algorithm |

### socionics/

| Source | Summary | Source |
|--------|---------|--------|
| what-is-socionics.md | Official definition and summary | BestSocionics |
| model-a.md | Model A: 8 functions, properties | BestSocionics |
| information-aspects.md | 8 information aspects (white/black) | BestSocionics |
| intertype-relations.md | Types of information exchange | BestSocionics |
| reinin-traits.md | Additional dichotomies beyond Jung | BestSocionics |
| subtypes-dcnh.md | DCNH subtype theory | BestSocionics |
| intertype-relations-ratings.md | Star ratings (0-5) for relations | Type•volution |
| intertype-mapper-scoring.md | Rank-based scoring (1-16) | Neocities Mapper |
| empirical-validation-studies.md | Scientific studies on intertype relations | Multiple researchers |
| socion-app.md | Dating app using Socionics + empirical research | Socion.app |
| opteamyzer-compatibility.md | Intensity concept for group compatibility | Opteamyzer |

### general/

| Source | Summary | Source |
|--------|---------|--------|
| autoreasearch.md | Karpathy's AutoResearch adaptation | - |
| christian-perspectives.md | Christian views on typologies (Orthodox, Protestant) | Multiple sources |
| typology-crisis-war.md | Stress resilience, military leadership, crisis teams | Multiple sources |
| type-distribution-statistics.md | MBTI and Socionics type distribution data | MBTI Manual, Terra Socionika |
| scientific-validation-plan.md | Framework for scientifically validating typological systems | Academic standards |
| existing-validation-research.md | Existing peer-reviewed studies on MBTI and Socionics | Multiple researchers |
| simple-research-guide.md | Beginner-friendly guide: hypothesis → data → analysis → report | - |
| ai-research-agents.md | AI agents for research: GPT Researcher, The AI Scientist, ChatGPT Code Interpreter | - |
| agentic-research-pipelines.md | Multi-agent pipelines: Agent Laboratory, CrewAI, STORM, workflow architectures | - |
| participant-recruitment.md | How to attract participants: Reddit, Telegram, snowball sampling | - |
| automated-research-plan.md | Full autonomous pipeline: Typology Agent, 6 automated research agents | - |
| optimal-2026-tech-stack.md | Optimal 2026 stack: CrewAI + Claude Sonnet 4.6 + GPT Researcher, complete implementation | - |
| modern-agentic-systems.md | Production-ready systems: InternAgent, The Agentic Researcher, Anthropic patterns, SciDER | arXiv 2026 |
| smart-mobilization-typology-wartime.md | Smart mobilization: AI recruitment, personality typology in military | Web research 2026 |
| psychosophy-typing-methods.md | Methods for psychosophy typing: tests, dichotomies, accentuations | Web research 2026 |
| fourth-physics-deep-research.md | Fourth Physics (4Ф) deep research: characteristics, warnings, suicidality risk | Deep research 2026 |

---

## Statistics

- **Skills created**: 2 (psychosophy-typer, psychosophy-accentuation-typer)
- **Agents created**: 12 (full team)
- **Raw sources**: 53 (21 temporistics + 8 psychosophy + 11 socionics + 13 general)
- **Entity pages created**: 33 (16 temporistics + 1 psychosophy + 1 socionics overview + 15 socionics types)
- **Articles ingested**: 39
- **Relations pages**: 3 (socionics, temporistics, psychosophy)
- **Concepts**: 14 (including 7 new stubs)
- **Last updated**: 2026-04-15
