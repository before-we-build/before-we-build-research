---
title: Common Projects
type: source
tags: [research, related-work]
created: 2026-04-14
updated: 2026-04-15
sources: []
---

# Agentic Compatibility via LLM Social Simulation and Activity-Theoretic Typology

> **Audit note:** This page is an imported research memo. Export-time citation markers were stripped during cleanup, so the page should still be treated as a draft synthesis until normal Markdown citations and volatile startup/community references are re-verified.

## Problem framing and a translation layer to mainstream research

Your target system—**Agentic Compatibility**—can be stated (in research-friendly terms) as *counterfactual interpersonal simulation* using LLM-driven agents that (a) carry stable “deep profiles,” (b) interact over multi-episode timelines, and (c) yield measurable compatibility signals from emergent dynamics rather than static trait similarity.

A clean way to make this legible to both HCI/LLM-agent researchers and computational social scientists is to align your three-tier architecture with the canonical hierarchy in **A.N. Leontiev’s activity theory**: *activity → actions → operations* (often mapped to *motive → goal → conditions/automatic routines*). 

From that bridge, each of your typologies gains a “public-science” counterpart that potential collaborators will recognize:

- **Strategic (motive/values, your Temporistics):** maps naturally to (i) *time perspective / temporal orientation* work (e.g., the Zimbardo framework) and (ii) *values hierarchies* (e.g., Schwartz values).   
- **Operational (goal & energy allocation, your Psychosophy):** can be pitched as *goal prioritization + self-regulation + emotion/agency tradeoffs* (often treated via decision-theoretic or clinical skill frameworks for interpersonal effectiveness).  
- **Tactical (automatic information metabolism/cognitive style, your Socionics):** can be translated to *persona adherence, cognitive-style-conditioned behavior, and micro-level reaction patterns* that show up in persona-agent evaluation, role-play agents, and user-behavior simulation. 

The “Inner Parliament” idea is also easy to anchor in established cognitive metaphors: **Marvin Minsky’s** view of mind as a society of interacting “agents” (subprocesses) is an especially relevant precedent for a multi-agent *within-one-mind* decomposition. 

## Scientific frontier: LLM agents as text-world engines and social digital twins

The closest research analogs to your “Love First, Know Later / Text World Engine” framing already exist, but scattered across four literatures that rarely talk to each other.

**Interactive social simulacra and long-horizon interpersonal dynamics.** The most widely recognized “proof point” is *Generative Agents*, which extends an LLM with (i) memory, (ii) reflection, and (iii) planning, yielding believable individual and emergent social behaviors in a sandbox town—and explicitly calls out “rehearsal spaces for interpersonal communication” as a target use case.   
A closely related line is *Social Simulacra*, which uses prompting workflows to generate large populations and simulate community interactions for social computing prototyping. 

**Audience simulation as “compatibility rehearsal” for communications.** The *Explore–Generate–Simulate (EGS)* framework formalizes the idea of generating candidate messages and simulating audience reactions with LLMs, with human evaluations across multiple interpersonal scenarios and evidence that simulated reactions can agree with human raters in many settings.   
This is an unusually direct precedent for your idea of simulating interpersonal outcomes *before* real-world commitment.

**Conflict rehearsal and psychologically grounded relationship work.** Systems like *Rehearsal* explicitly let users practice conflicts with a simulated interlocutor and explore counterfactual “what if” paths, grounded in conflict-resolution theory and evaluated in a CHI-style human study pipeline.   
On the romantic-relationship axis, *ConflictLens* is a relevant emerging artifact: an LLM-based interactive system aimed at reflection and guided exercises for romantic conflict resolution, emphasizing deeper mechanisms (coping styles, emotional responses, habits).   
For skills + emotion regulation together, *IMBUE* explicitly combines simulated practice with just-in-time feedback grounded in DBT interpersonal effectiveness, reporting measurable improvements in learning outcomes in a randomized study.

**Social Digital Twins as population or platform replicas.** Recent work has started to use LLMs as “cognitive engines” inside agent-based digital twins. One example is an LLM-powered social digital twin framework for policy response simulation that includes demographic/psychographic conditioning and an explicit calibration layer to match population-level metrics.   
For social platforms specifically, *Y Social* describes an LLM-powered “social media digital twin” focused on user interactions, content dynamics, and policy experimentation. 

**Persona fidelity and psychometric comparability are becoming explicit evaluation targets.** The persona-agent space is now producing dedicated evaluation infrastructure; *PersonaGym* proposes a dynamic evaluation framework and a metric grounded in decision theory for persona adherence, explicitly arguing that model scale does not guarantee persona fidelity. 

A recurring caution in this whole frontier is that social simulations can quickly become “too unbounded”: there are focused critiques arguing LLM-based social simulation needs careful boundary-setting (scope, assumptions, and validation loops) to be scientifically meaningful.


## People and researchers to contact

The table below is optimized for your specific thesis: multi-episode interpersonal simulation + deep profiling + an “inner-parliament” cognitive architecture + compatibility as an emergent property, not a static score.

| Person | What to read first (anchor artifacts) | Closest overlap with your three-tier model |
|---|---|---|
| Joon Sung Park | *Generative Agents* (LLM+memory+reflection+planning; emergent social behaviors) and *Social Simulacra* (populated prototypes).  | Strategic: long-horizon plan/reflection loops (a mechanizable “temporal unity” substrate). Tactical: persona-conditioned micro-behaviors in a text-world.  |
| Michael S. Bernstein | *Generative Agents* (coauthor) + *Rehearsal* (counterfactual conflict simulation).  | Operational: goal pursuit + negotiation dynamics in simulated dialogue. Strategic: reflective memory/planning components.  |
| Ranjay Krishna | *Improving Interpersonal Communication by Simulating Audiences…* (EGS framework).  | Operational: explicit goals + predicted reactions, a clean hook for Psychosophy-like “energy allocation.” Strategic: scenario-level planning; Tactical: simulated audience micro-responses. |
| Thomas L. Griffiths | EGS paper (higher-order reasoning about others’ reactions; human comparison).  | Strategic: rational/strategic modeling lens for “values → plans,” useful for formalizing temporistics-like time orientation into decision models. |
| Tim Althoff | *IMBUE* (interpersonal effectiveness training via LLM simulation + expert feedback; DBT grounding). | Operational: explicit integration of emotion management with communication skill goals (a direct bridge to your operational layer). |
| Vinay Samuel | *PersonaGym* (dynamic persona evaluation; PersonaScore).  | Tactical: measuring persona adherence (your “information metabolism” layer needs this kind of fidelity tooling). Also supports “psychometric comparability” positioning. |
| Karthik Narasimhan | *PersonaGym* (coauthor; persona agents framing).  | Tactical: persona agents as controllable “cognitive style.” Strategic: decision-theoretic evaluation language may help formalize compatibility objectives. |
| Giulio Rossetti | *Y Social: an LLM-powered Social Media Digital Twin* (platform-level twin + network dynamics).  | Tactical: social-network diffusion + interaction dynamics. Strategic: policy-lever experimentation mindset ports well to “compatibility interventions.” |
| Y Zhang | *K-Level Reasoning…* (recursive higher-order beliefs for strategic reasoning with LLMs).  | Strategic: formal handle on “beliefs about beliefs” (Level-k), relevant to compatibility as a multi-agent game with nested models. |
| Chi Wang | *AutoGen* (multi-agent conversation framework; interaction patterns for tool-using agents).  | Architecture: pragmatic substrate for your Inner Parliament orchestration (agents debating/negotiating before action). |

**Vector on CIS typologies (socionics/psychosophy/temporistics): what surfaced vs. what did not.** In open academic indexing, explicitly *LLM-plus-socionics* work is still sparse; most “socionics” references appear as background typology mentions rather than as a formalized computational agenda.   
There *are* structured socionics resources that operationalize “information metabolism” and intertype relations (often outside mainstream psychology), which can still be valuable as *ontology/prior* material for schema design and RAG conditioning—if you treat them as hypotheses to validate in simulation.   
For temporistics and psychosophy specifically, most discoverable material remains community/grey literature (forums, compiled PDFs, translations), suggesting that your strongest “scientific novelty” is not in citing a large existing academic canon, but in **recasting these typologies as machine-testable priors inside a validated agent simulation loop** (e.g., PersonaGym-like evaluation + EGS/Rehearsal-style counterfactual experiments). 

## Organizations and startups

Exactly five targets below are chosen because they align with your system *as a whole* (simulation-first compatibility, digital twins, or agentic matchmaking), not just with generic “AI + personality.”

**Stanford HCI Group**  
This research group is among the clearest academic homes for “text-world engines” used as rehearsal spaces for interpersonal dynamics, spanning populated social simulacra, generative agents, and conflict rehearsal interfaces. 

**Artificial Societies**  
A YC-backed company explicitly building networks of AI personas to simulate stakeholder/audience reactions—very close in spirit to “social digital twins,” but framed as decision testing (marketing/comms) rather than romance/teams. Its YC profile lists founders, positioning, and the core thesis (simulating high-stakes audiences). 

**Sitch**  
An AI-powered matchmaking product positioned around deep onboarding and curated introductions, explicitly framed (in reporting) as moving beyond swipe mechanics toward richer preference models—useful for scouting product patterns, retention incentives, and UX expectations. 

**Fate**  
Representative of the current “agentic AI dating” wave discussed in mainstream tech press, including an interview-style onboarding agent, curated matches, and optional coaching; this is directly adjacent competitive/adjacent-territory intelligence for your “Love First, Know Later” simulation narrative. 

**Harver** and **pymetrics**  
While this lineage is not “LLM simulation-first,” it is a highly relevant HR precedent for psychometrics-in-the-loop talent matching, and it demonstrates an enterprise path (assessment → decisioning) plus acquisition dynamics. 

## Communities and signal channels for persona fidelity and agent architectures

For your scouting objective, you want places where people discuss (a) persona conditioning and evaluation, (b) multi-agent orchestration patterns, and (c) practical fine-tuning/RAG for profile-grounded agents.

**High-signal discussion hubs**
- r/LocalLLaMA — concentrated discussion on running and tuning local models (useful for persona-fidelity iteration loops without high inference cost).  
- r/AI_Agents and r/aiagents — broad agent-building patterns, orchestration, failures, and tooling.   

**Builder communities where multi-agent + RAG details get answered**
- LangChain Community Slack (official) — a large, active hub for agent tooling patterns and production constraints.  
- LlamaIndex community chat — official community page points users to their real-time community channel, and the company site routes OSS questions there.   

**Open research collectives (useful for evaluation rigor and datasets)**
- EleutherAI — open research culture; their public Discord invites and model ecosystem make it relevant if you want reproducible evaluation/benchmarking muscle.   
- LAION — large open community around datasets and research collaboration; relevant if your next step is building/curating interaction datasets at scale.   

**Agent-framework communities**
- AG2 — community hub for AutoGen/AG2 (multi-agent conversation patterns).   

**Platform for collaboration and code discovery**
- GitHub remains the default place where persona-agent benchmarks and agent frameworks surface first (often with Discussions/Issues acting as “mini-communities”). 

## Cold email framework for outreach

A good outreach note for this space must do two things simultaneously: (1) make your idea sound like a **testable research program**, not a “typology app,” and (2) show you understand the **failure modes** (evaluation, boundary conditions, safety/privacy) in LLM social simulation. 

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

(If you’re writing to the HCI/social simulacra crowd, anchor on Generative Agents / Rehearsal / EGS; if you’re writing to persona-eval people, anchor on PersonaGym. )

**Novelty claim (three bullets, each testable):**
- “I represent a mind as a small committee of sub-agents with competing objectives (e.g., motivation vs emotion regulation), then learn/validate which arbitration patterns predict stable cooperation.” (Tie to the Society-of-Mind precedent without over-claiming.)  
- “I structure the agent into motive/goal/operation layers (Activity Theory), which gives a clean scaffold for long-horizon consistency tests.”   
- “I’m prepared to evaluate persona fidelity and interaction stability with benchmark-style metrics rather than only ‘vibes’.” 

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
