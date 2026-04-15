---
title: Common Projects
type: source
tags: [research, related-work]
created: 2026-04-14
updated: 2026-04-15
sources: []
---

# Agentic Compatibility via LLM Social Simulation and Activity-Theoretic Typology

## Problem framing and a translation layer to mainstream research

Your target system—**Agentic Compatibility**—can be stated (in research-friendly terms) as *counterfactual interpersonal simulation* using LLM-driven agents that (a) carry stable “deep profiles,” (b) interact over multi-episode timelines, and (c) yield measurable compatibility signals from emergent dynamics rather than static trait similarity. fileciteturn0file0

A clean way to make this legible to both HCI/LLM-agent researchers and computational social scientists is to align your three-tier architecture with the canonical hierarchy in **entity["people","A.N. Leontiev","activity theory psychologist"]’s activity theory**: *activity → actions → operations* (often mapped to *motive → goal → conditions/automatic routines*). citeturn4search7turn4search18

From that bridge, each of your typologies gains a “public-science” counterpart that potential collaborators will recognize:

- **Strategic (motive/values, your Temporistics):** maps naturally to (i) *time perspective / temporal orientation* work (e.g., the Zimbardo framework) and (ii) *values hierarchies* (e.g., Schwartz values). citeturn14search1turn14search2turn14search28  
- **Operational (goal & energy allocation, your Psychosophy):** can be pitched as *goal prioritization + self-regulation + emotion/agency tradeoffs* (often treated via decision-theoretic or clinical skill frameworks for interpersonal effectiveness). citeturn3academia42  
- **Tactical (automatic information metabolism/cognitive style, your Socionics):** can be translated to *persona adherence, cognitive-style-conditioned behavior, and micro-level reaction patterns* that show up in persona-agent evaluation, role-play agents, and user-behavior simulation. citeturn1search2turn2search1

The “Inner Parliament” idea is also easy to anchor in established cognitive metaphors: **entity["people","Marvin Minsky","society of mind author"]’s** view of mind as a society of interacting “agents” (subprocesses) is an especially relevant precedent for a multi-agent *within-one-mind* decomposition. citeturn4search16turn4search2

## Scientific frontier: LLM agents as text-world engines and social digital twins

The closest research analogs to your “Love First, Know Later / Text World Engine” framing already exist, but scattered across four literatures that rarely talk to each other.

**Interactive social simulacra and long-horizon interpersonal dynamics.** The most widely recognized “proof point” is *Generative Agents*, which extends an LLM with (i) memory, (ii) reflection, and (iii) planning, yielding believable individual and emergent social behaviors in a sandbox town—and explicitly calls out “rehearsal spaces for interpersonal communication” as a target use case. citeturn0search0turn1search0  
A closely related line is *Social Simulacra*, which uses prompting workflows to generate large populations and simulate community interactions for social computing prototyping. citeturn0search1turn0search9

**Audience simulation as “compatibility rehearsal” for communications.** The *Explore–Generate–Simulate (EGS)* framework formalizes the idea of generating candidate messages and simulating audience reactions with LLMs, with human evaluations across multiple interpersonal scenarios and evidence that simulated reactions can agree with human raters in many settings. citeturn3search0turn3search5  
This is an unusually direct precedent for your idea of simulating interpersonal outcomes *before* real-world commitment.

**Conflict rehearsal and psychologically grounded relationship work.** Systems like *Rehearsal* explicitly let users practice conflicts with a simulated interlocutor and explore counterfactual “what if” paths, grounded in conflict-resolution theory and evaluated in a CHI-style human study pipeline. citeturn2search0turn2search3turn2search13  
On the romantic-relationship axis, *ConflictLens* is a relevant emerging artifact: an LLM-based interactive system aimed at reflection and guided exercises for romantic conflict resolution, emphasizing deeper mechanisms (coping styles, emotional responses, habits). citeturn3search2turn3search9  
For skills + emotion regulation together, *IMBUE* explicitly combines simulated practice with just-in-time feedback grounded in DBT interpersonal effectiveness, reporting measurable improvements in learning outcomes in a randomized study. citeturn3academia42

**Social Digital Twins as population or platform replicas.** Recent work has started to use LLMs as “cognitive engines” inside agent-based digital twins. One example is an LLM-powered social digital twin framework for policy response simulation that includes demographic/psychographic conditioning and an explicit calibration layer to match population-level metrics. citeturn0search2turn0search18  
For social platforms specifically, *Y Social* describes an LLM-powered “social media digital twin” focused on user interactions, content dynamics, and policy experimentation. citeturn0search6turn0search22

**Persona fidelity and psychometric comparability are becoming explicit evaluation targets.** The persona-agent space is now producing dedicated evaluation infrastructure; *PersonaGym* proposes a dynamic evaluation framework and a metric grounded in decision theory for persona adherence, explicitly arguing that model scale does not guarantee persona fidelity. citeturn1search2turn1search14

A recurring caution in this whole frontier is that social simulations can quickly become “too unbounded”: there are focused critiques arguing LLM-based social simulation needs careful boundary-setting (scope, assumptions, and validation loops) to be scientifically meaningful. citeturn0search21

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["Generative Agents Smallville screenshot","Social simulacra SimReddit prototype screenshot","Rehearsal Simulating Conflict to Teach Conflict Resolution interface","LLM-powered social digital twin framework diagram"],"num_per_query":1}

## People and researchers to contact

The table below is optimized for your specific thesis: multi-episode interpersonal simulation + deep profiling + an “inner-parliament” cognitive architecture + compatibility as an emergent property, not a static score.

| Person | What to read first (anchor artifacts) | Closest overlap with your three-tier model |
|---|---|---|
| entity["people","Joon Sung Park","generative agents author"] | *Generative Agents* (LLM+memory+reflection+planning; emergent social behaviors) and *Social Simulacra* (populated prototypes). citeturn0search0turn0search1 | Strategic: long-horizon plan/reflection loops (a mechanizable “temporal unity” substrate). Tactical: persona-conditioned micro-behaviors in a text-world. citeturn0search0turn0search1 |
| entity["people","Michael S. Bernstein","stanford hci professor"] | *Generative Agents* (coauthor) + *Rehearsal* (counterfactual conflict simulation). citeturn0search0turn2search0 | Operational: goal pursuit + negotiation dynamics in simulated dialogue. Strategic: reflective memory/planning components. citeturn2search0turn0search0 |
| entity["people","Ranjay Krishna","audience simulation coauthor"] | *Improving Interpersonal Communication by Simulating Audiences…* (EGS framework). citeturn3search0turn3search4 | Operational: explicit goals + predicted reactions, a clean hook for Psychosophy-like “energy allocation.” Strategic: scenario-level planning; Tactical: simulated audience micro-responses. citeturn3search0 |
| entity["people","Thomas L. Griffiths","cognitive scientist"] | EGS paper (higher-order reasoning about others’ reactions; human comparison). citeturn3search0turn3search10 | Strategic: rational/strategic modeling lens for “values → plans,” useful for formalizing temporistics-like time orientation into decision models. citeturn3search0 |
| entity["people","Tim Althoff","human behavior researcher"] | *IMBUE* (interpersonal effectiveness training via LLM simulation + expert feedback; DBT grounding). citeturn3academia42 | Operational: explicit integration of emotion management with communication skill goals (a direct bridge to your operational layer). citeturn3academia42 |
| entity["people","Vinay Samuel","personagym first author"] | *PersonaGym* (dynamic persona evaluation; PersonaScore). citeturn1search2turn1search14 | Tactical: measuring persona adherence (your “information metabolism” layer needs this kind of fidelity tooling). Also supports “psychometric comparability” positioning. citeturn1search2 |
| entity["people","Karthik Narasimhan","persona agents researcher"] | *PersonaGym* (coauthor; persona agents framing). citeturn1search2turn1search14 | Tactical: persona agents as controllable “cognitive style.” Strategic: decision-theoretic evaluation language may help formalize compatibility objectives. citeturn1search2 |
| entity["people","Giulio Rossetti","y social author"] | *Y Social: an LLM-powered Social Media Digital Twin* (platform-level twin + network dynamics). citeturn0search6turn0search22 | Tactical: social-network diffusion + interaction dynamics. Strategic: policy-lever experimentation mindset ports well to “compatibility interventions.” citeturn0search6 |
| entity["people","Y Zhang","k-level reasoning author"] | *K-Level Reasoning…* (recursive higher-order beliefs for strategic reasoning with LLMs). citeturn1search3turn1search11 | Strategic: formal handle on “beliefs about beliefs” (Level-k), relevant to compatibility as a multi-agent game with nested models. citeturn1search3 |
| entity["people","Chi Wang","autogen author"] | *AutoGen* (multi-agent conversation framework; interaction patterns for tool-using agents). citeturn15view0turn0search3 | Architecture: pragmatic substrate for your Inner Parliament orchestration (agents debating/negotiating before action). citeturn0search3 |

**Vector on CIS typologies (socionics/psychosophy/temporistics): what surfaced vs. what did not.** In open academic indexing, explicitly *LLM-plus-socionics* work is still sparse; most “socionics” references appear as background typology mentions rather than as a formalized computational agenda. citeturn12view0turn10search9  
There *are* structured socionics resources that operationalize “information metabolism” and intertype relations (often outside mainstream psychology), which can still be valuable as *ontology/prior* material for schema design and RAG conditioning—if you treat them as hypotheses to validate in simulation. citeturn10search4turn11search5turn11search32  
For temporistics and psychosophy specifically, most discoverable material remains community/grey literature (forums, compiled PDFs, translations), suggesting that your strongest “scientific novelty” is not in citing a large existing academic canon, but in **recasting these typologies as machine-testable priors inside a validated agent simulation loop** (e.g., PersonaGym-like evaluation + EGS/Rehearsal-style counterfactual experiments). citeturn10search23turn11search3turn1search2turn3search0

## Organizations and startups

Exactly five targets below are chosen because they align with your system *as a whole* (simulation-first compatibility, digital twins, or agentic matchmaking), not just with generic “AI + personality.”

**entity["organization","Stanford HCI Group","human-computer interaction lab"]**  
This research group is among the clearest academic homes for “text-world engines” used as rehearsal spaces for interpersonal dynamics, spanning populated social simulacra, generative agents, and conflict rehearsal interfaces. citeturn0search0turn2search17turn2search0

**entity["company","Artificial Societies","yc w25 ai simulation startup"]**  
A YC-backed company explicitly building networks of AI personas to simulate stakeholder/audience reactions—very close in spirit to “social digital twins,” but framed as decision testing (marketing/comms) rather than romance/teams. Its YC profile lists founders, positioning, and the core thesis (simulating high-stakes audiences). citeturn8search3turn5search5turn8search6

**entity["company","Sitch","ai matchmaking app, new york"]**  
An AI-powered matchmaking product positioned around deep onboarding and curated introductions, explicitly framed (in reporting) as moving beyond swipe mechanics toward richer preference models—useful for scouting product patterns, retention incentives, and UX expectations. citeturn8search4turn5search26turn5search22

**entity["company","Fate","ai dating app, london"]**  
Representative of the current “agentic AI dating” wave discussed in mainstream tech press, including an interview-style onboarding agent, curated matches, and optional coaching; this is directly adjacent competitive/adjacent-territory intelligence for your “Love First, Know Later” simulation narrative. citeturn8search22turn8search5turn5search19

**entity["company","Harver","hiring platform, netherlands"]** and **entity["company","pymetrics","behavioral hiring assessments"]**  
While this lineage is not “LLM simulation-first,” it is a highly relevant HR precedent for psychometrics-in-the-loop talent matching, and it demonstrates an enterprise path (assessment → decisioning) plus acquisition dynamics. citeturn5search0turn5search6turn5search25

## Communities and signal channels for persona fidelity and agent architectures

For your scouting objective, you want places where people discuss (a) persona conditioning and evaluation, (b) multi-agent orchestration patterns, and (c) practical fine-tuning/RAG for profile-grounded agents.

**High-signal discussion hubs**
- entity["organization","r/LocalLLaMA","reddit community"] — concentrated discussion on running and tuning local models (useful for persona-fidelity iteration loops without high inference cost). citeturn6search0  
- entity["organization","r/AI_Agents","reddit community"] and entity["organization","r/aiagents","reddit community"] — broad agent-building patterns, orchestration, failures, and tooling. citeturn6search1turn6search5  

**Builder communities where multi-agent + RAG details get answered**
- entity["company","LangChain","llm app framework"] Community Slack (official) — a large, active hub for agent tooling patterns and production constraints. citeturn6search12  
- entity["company","LlamaIndex","llm data framework"] community chat — official community page points users to their real-time community channel, and the company site routes OSS questions there. citeturn6search21turn6search25  

**Open research collectives (useful for evaluation rigor and datasets)**
- entity["organization","EleutherAI","open ai research collective"] — open research culture; their public Discord invites and model ecosystem make it relevant if you want reproducible evaluation/benchmarking muscle. citeturn7search0turn7search26  
- entity["organization","LAION","open ml research network"] — large open community around datasets and research collaboration; relevant if your next step is building/curating interaction datasets at scale. citeturn7search1turn7search31  

**Agent-framework communities**
- entity["organization","AG2","autogen community"] — community hub for AutoGen/AG2 (multi-agent conversation patterns). citeturn7search2turn7search24  

**Platform for collaboration and code discovery**
- entity["company","GitHub","code hosting platform"] remains the default place where persona-agent benchmarks and agent frameworks surface first (often with Discussions/Issues acting as “mini-communities”). citeturn1search26turn3search27turn7search36

## Cold email framework for outreach

A good outreach note for this space must do two things simultaneously: (1) make your idea sound like a **testable research program**, not a “typology app,” and (2) show you understand the **failure modes** (evaluation, boundary conditions, safety/privacy) in LLM social simulation. citeturn0search21turn1search2

A structure that reliably lands with senior researchers/founders:

### Subject line patterns
Use one of these (short, non-hype, instantly legible):
- “LLM-based interpersonal simulation: compatibility as an emergent property”
- “Inner-parliament agent architecture + persona fidelity evaluation”
- “From Activity Theory (motive/goal/operation) to LLM social digital twins”

### The message body blueprint

**Hook (one sentence):**  
State a concrete, technically framed objective.  
> “I’m building an LLM-agent system that simulates multi-episode interpersonal dynamics and outputs compatibility signals from emergent interaction patterns—not from static trait similarity.”

**Credibility anchor (one sentence):**  
Name *one* close precedent of theirs + one precise delta.  
> “Your work on [X] showed [Y]; my delta is to treat a person as a *multi-agent cognitive architecture* (‘inner parliament’) and test compatibility as a function of interactions between two such systems.”

(If you’re writing to the HCI/social simulacra crowd, anchor on Generative Agents / Rehearsal / EGS; if you’re writing to persona-eval people, anchor on PersonaGym. citeturn0search0turn2search0turn3search0turn1search2)

**Novelty claim (three bullets, each testable):**
- “I represent a mind as a small committee of sub-agents with competing objectives (e.g., motivation vs emotion regulation), then learn/validate which arbitration patterns predict stable cooperation.” (Tie to the Society-of-Mind precedent without over-claiming.) citeturn4search16  
- “I structure the agent into motive/goal/operation layers (Activity Theory), which gives a clean scaffold for long-horizon consistency tests.” citeturn4search7turn4search18  
- “I’m prepared to evaluate persona fidelity and interaction stability with benchmark-style metrics rather than only ‘vibes’.” citeturn1search2turn3search0

**Validation plan (one short paragraph):**  
This is where you look like a scientist-engineer rather than a typology enthusiast.  
Include: (a) what you measure, (b) what baselines you compare against, (c) what “success” would falsifiably mean.  
Example:  
> “I’m running counterfactual interaction suites (conflict, negotiation, intimacy-building, planning) and measuring (i) persona adherence under pressure, (ii) long-horizon consistency, (iii) mutual predictability / belief alignment (Level‑k style), and (iv) post-interaction convergence vs divergence.”

**Ethics/privacy sentence (non-negotiable):**  
One line that signals maturity (and makes founders/researchers safer replying).  
> “I’m explicitly avoiding ‘diagnosis’ framing; I treat profiles as user-consented, auditable hypotheses and I’m designing for opt-out, data minimization, and bias auditing.”

**Ask (one small, specific request):**  
Pick exactly one:
- 20-minute call to sanity-check the evaluation design  
- a pointer to a dataset / benchmark / related lab  
- feedback on a 1–2 page technical note

### A concrete email template

Subject: Inner-parliament LLM agents for interpersonal compatibility simulation

Hi [Name],  
I’m building an LLM-agent system that simulates multi-episode interpersonal dynamics and estimates compatibility as an emergent property of interaction—not as a static trait match.

I’m reaching out because your work on [their paper/product] is the closest precedent I’ve found to what I’m trying to measure. My key twist is a cognitive architecture: each “person” is a small *inner parliament* of sub-agents (e.g., motive/value layer, goal/energy layer, and fast reactive layer), and compatibility is evaluated by running counterfactual scenarios in a controlled text-world environment.

I’m currently validating three things: (1) persona fidelity under interaction pressure, (2) long-horizon consistency across scenarios, and (3) whether belief-alignment dynamics predict stable cooperation better than trait similarity baselines.

If you’re open, I’d love 20 minutes to ask: what evaluation design would convince *you* that an LLM-based compatibility simulator is measuring something real (and not just prompt aesthetics)?

Best,  
[Your name]  
[1-line credential: e.g., “building X, shipping Y; interested in reproducible benchmarks”]