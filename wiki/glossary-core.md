---
title: Glossary Core
type: reference
tags: [glossary, terminology]
created: 2026-04-15
updated: 2026-04-24
sources: []
---

# Glossary of Terms: PsyCalc and Cognitive Matchmaker

## Purpose

This glossary provides authoritative working definitions for the PsyCalc research framework and its downstream applications, including Cognitive Matchmaker. PsyCalc is the broader ontology and latent-process compatibility framework; Cognitive Matchmaker is one implementation of that framework in AI-assisted dating and relationship matching.

The glossary should preserve the central PsyCalc distinction: type labels are not final explanations. They are structured hypotheses about latent processes inferred from observable traces and revised through evidence.

Core formula:

- **Socionics → latent processes of information modeling**
- **Psychosophy → latent processes of synthesis and analysis in action**
- **Temporistics → latent processes of induction and deduction in temporal/existential experience**

---

## Part I: Epistemological Operations

These terms are used in their **technical epistemological sense**, distinct from their everyday meaning.

### 1.1 Induction

**Definition:** The cognitive operation of deriving general principles or structured representations from particular observations.

**In Cognitive Matchmaker:** The process by which the system constructs a structured Persona from responses gathered during the onboarding interview. It infers latent behavioral regularities (motives, goals, automatic reactions) from explicit descriptions of past experiences and hypothetical scenarios.

**Formula:** `Persona = Induction(OnboardingResponses)`

**NOT:** Casual reasoning or intuition. NOT the collection of stated preferences. NOT the application of predefined typological labels to raw data.

---

### 1.2 Deduction

**Definition:** The cognitive operation of deriving specific predictions from general principles or models.

**In Cognitive Matchmaker:** The process by which a Persona (general model) is used to generate specific predicted behaviors in specific scenario conditions. The Simulation Engine takes a Persona and a Scenario as input and produces a Simulation Transcript.

**Formula:** `SimulationTranscript = Deduction(Persona, Scenario)`

**NOT:** Logical proof. NOT the assertion of certain truth. The output is a **hypothesis** about how the modeled person would likely behave, not a guaranteed prediction.

---

### 1.3 Analysis

**Definition:** The cognitive operation of decomposing a complex phenomenon into its constituent elements for examination.

**In Cognitive Matchmaker:** The process by which the Love Observer module decomposes a Simulation Transcript into component signals. Compatibility is not assessed as a single monolithic score but as a structured vector of signals across different dimensions and layers.

**NOT:** The creation of new information. Analysis reveals patterns that exist in the transcript; it does not invent them.

---

### 1.4 Synthesis

**Definition:** The cognitive operation of combining elements into a unified whole.

**In Cognitive Matchmaker:** The process of integrating multiple typological frameworks (Temporistics, Psychosophy, Socionics) into a Unified Compatibility Model. The synthesis produces outputs traceable to any constituent framework while maintaining internal consistency.

**NOT:** Reduction to a single framework. Synthesis preserves the distinct contributions of each framework rather than forcing a consensus.

---

### 1.5 Modeling

**Definition:** The construction of a simplified, formal representation that captures essential features of a phenomenon for purposes of prediction, explanation, or control.

**In Cognitive Matchmaker:** The entire process of creating, instantiating, and maintaining Digital Twins. The Digital Twin is the primary modeling construct; the Persona is its core representation.

**NOT:** An assertion of completeness or perfect accuracy. A model is always a simplification; its value lies in its predictive utility, not its ontological status.

---

## Part II: Person Constructs

### 2.1 Persona

**Definition:** A structured, three-layer representation of an individual, induced from onboarding interview responses. The Persona is the output of the Induction operation.

**Structure:**
```
Persona = {
  Strategic: { values, worldview, temporalOrientation },
  Operational: { goals, rolePreferences, decisionStrategies },
  Tactical: { automaticReactions, communicationStyle, infoProcessing }
}
```

**NOT:** A profile with explicit attributes. A collection of stated preferences. An embedding vector. An opaque score.

**Lifecycle:** Created during onboarding → Updated via feedback from real-world interactions.

---

### 2.2 Digital Twin

**Definition:** An agentic instantiation of a Persona, capable of maintaining state, generating contextually appropriate responses, and exhibiting consistent behavior across multiple simulation turns.

**Structure:**
```
DigitalTwin = {
  Persona: Persona,
  PolicyConstraints: { stablePreferences, nonNegotiables },
  ActionPolicy: { behavioralTendencies },
  CommunicationStyle: { linguisticPatterns, repairStrategies }
}
```

**NOT:** A perfect copy of a person. A consciousness or identity. A static profile.

**Analogy:** A computational actor that behaves according to the rules encoded in its Persona, similar to how a game NPC behaves according to its programmed AI.

---

### 2.3 User Twin / Candidate Twin

**Definition:** Specific instances of Digital Twin. A User Twin represents the primary user of the system; a Candidate Twin represents a potential match.

**Relationship:** Compatibility is assessed by running simulations between User Twin and Candidate Twin.

---

## Part III: Activity Theory Terms

These terms are borrowed from Activity Theory (Leontiev) and mapped to the three-layer Persona structure.

### 3.1 Activity (Strategic Level)

**Definition:** The highest level of analysis in Activity Theory, concerned with motives—the "why" of behavior. At this level, we ask: What does this person fundamentally value? What are their long-term orientations?

**Mapping:** Corresponds to the Strategic layer of Persona.

**Typology:** Operationalized via Temporistics (relationship to Past/Present/Future/Eternity).

---

### 3.2 Action (Operational Level)

**Definition:** The middle level of analysis in Activity Theory, concerned with conscious goals—the "what" of behavior. At this level, we ask: What is this person trying to achieve? What roles do they prefer?

**Mapping:** Corresponds to the Operational layer of Persona.

**Typology:** Operationalized via Psychosophy/Attitudinal Psyche (attitudes toward Logic, Emotion, Volition, Physics).

---

### 3.3 Operation (Tactical Level)

**Definition:** The lowest level of analysis in Activity Theory, concerned with automatic, habitual execution under specific conditions—the "how" of behavior. At this level, we ask: How does this person automatically react? How do they process and communicate information?

**Mapping:** Corresponds to the Tactical layer of Persona.

**Typology:** Operationalized via Socionics (information metabolism, communication styles).

---

### 3.4 Motive

**Definition:** The underlying drive that initiates Activity. Something a person values for its own sake, as opposed to as a means to an end.

**Example:** "Security in relationships" is a motive; "having a shared apartment" is a goal that may serve that motive.

---

### 3.5 Goal

**Definition:** A conscious target that an Action is directed toward. Goals are the objects of Actions.

**Example:** "Own a home by age 35" is a goal.

---

### 3.6 Condition

**Definition:** The specific circumstance under which an Operation is executed. Conditions determine which automatic behaviors are triggered.

**Example:** "When stressed, this person withdraws."

---

## Part IV: Typological Frameworks

These are **schema languages** used to generate features for simulation and scoring. They are NOT treated as validated psychometric instruments.

### 4.1 Temporistics (Темпористика)

**Definition:** A typological framework describing how a person relates to temporal categories: Past, Present, Future, and Eternity, as value-orienting categories.

**Status:** Niche typology. Used as a feature schema for the Strategic layer.

**Epistemic Status:** Heuristic. Outputs are hypotheses to test, not definitive assessments.

---

### 4.2 Psychosophy / Attitudinal Psyche (Психософия)

**Definition:** A typological framework centered on a person's attitudes toward four domains: Logic, Emotion, Volition/Will, and Physics/Body. It describes which functions a person leads with versus holds in reserve.

**Status:** Niche typology. Used as a feature schema for the Operational layer.

**Epistemic Status:** Heuristic. Outputs are hypotheses to test, not definitive assessments.

---

### 4.3 Socionics (Соционика)

**Definition:** A Jung-inspired typology developed by Aušra Augustinavičiūtė, describing information metabolism types and interpersonal dynamics. Influenced by Jung's psychological types and Antoni Kępiński's information metabolism theory.

**Status:** Widely characterized as pseudoscientific in mainstream contexts. Used as a feature schema for the Tactical layer.

**Epistemic Status:** Heuristic with extra caution. Outputs are explicitly framed as hypotheses to validate in real-world interactions.

---

## Part IV-B: Socionics-Specific Terminology

⚠️ **CRITICAL DISAMBIGUATION:** The term "modeling" has **two fundamentally different meanings** in this project:

| Term | Domain | Meaning |
|------|--------|---------|
| **Modeling** ( epistemological ) | This project (Section 1.5) | Constructing formal representations for prediction/explanation |
| **Information Modeling** (информационное моделирование) | Socionics/Kępiński | The cognitive process by which a person's mind processes and represents information |

### 4.3.1 Information Metabolism (информационный метаболизм)

**Definition (Kępiński):** The theory that the psyche processes information analogous to how an organism metabolizes substances. Different psychic types metabolize different aspects of reality (logic, emotions, sensations, intuitions) differently.

**In Socionics:** The foundational concept that each personality type has a characteristic way of perceiving and processing information.

**NOT:** Biological metabolism. A literal metabolic process.

---

### 4.3.2 Information Model (информационная модель)

**Definition (Kępiński):** A mental construct formed by the psyche to represent and process a specific aspect of reality. Each psychic function has its corresponding information model.

**Example:** The "logic" information model represents abstract causal relationships. The "ethics" information model represents interpersonal emotional states.

**⚠️ CONFLICT RESOLVED:** This is **NOT** the same as "Model" in Section 1.5. When Socionics literature mentions "model," it refers to the cognitive representation of information, not to our formal computational representation.

---

### 4.3.3 Psychic Function (психическая функция)

**Definition (Socionics):** A unit of information processing corresponding to a specific aspect of reality (aspect) and a specific orientation (EI/SN, TF/FJ).

**Aspects:**
- **Extraverted Logic (Te):** Business logic, efficiency, pragmatics
- **Introverted Logic (Ti):** Formal logic, classification, structure
- **Extraverted Ethics (Fe):** Emotions, feelings, emotional communication
- **Introverted Ethics (Fi):** Moral values, relationships, feelings about people
- **Extraverted Sensing (Se):** Physical reality, force, tangible presence
- **Introverted Sensing (Si):** Physical sensations, comfort, health
- **Extraverted Intuition (Ne):** Possibilities, meanings, connections
- **Introverted Intuition (Ni):** Time, system development, predictions

**NOT:** A psychological defense mechanism. A personality trait in the trait-based sense.

---

### 4.3.4 Model A (Модель А)

**Definition (Socionics):** The structural model describing how the 8 psychic functions are arranged in a personality type. Functions are assigned to positions:

| Position | Name | Properties |
|----------|------|------------|
| 1 | Leading (A) | Strongest, most developed |
| 2 | Creative (B) | Strong, used for output |
| 3 | Role (C) | Weak, used situationally |
| 4 | Vulnerable (D) | Weakest, creates anxiety |
| 5 | Suggestive (PoLR) | Desired but undeveloped |
| 6 | Mobilizing | Activated under stress |
| 7 | Ignoring | Overlooked or suppressed |
| 8 | Demonstrative | Shown without awareness |

**NOT:** A computational model in our sense. Model A is a structural diagram of personality, not a formal predictive representation.

---

### 4.3.5 Intertype Relations (межтиповые отношения)

**Definition (Socionics):** Predicted interaction patterns between different socionic types, derived from the structure of Model A.

**Types of relations:**
- **Dual (дуал):** Complementary, comfortable (e.g., ILE ↔ SEI)
- **Activation (активация):** Energizing but potentially exhausting
- **Benefit:** One-sided advantage
- **Conflict:** High tension, potential for misunderstanding
- **Mirror:** Apparent similarity with hidden differences
- **Supervision:** One monitors the other
- **Super-ego:** Similar values, different methods

**NOT:** Guaranteed predictions. The strength of these relations varies empirically.

---

### 4.3.6 Reimbursement (компенсация)

**Definition (Kępiński):** The psychological mechanism by which a weak psychic function attempts to compensate for its limitations, often leading to characteristic neurotic patterns.

**In our project:** Tactical layer behaviors may show "reimbursement patterns"—compensatory strategies for weak information processing aspects.

---

### 4.3.7 Information Accumulation vs. Information Metabolism

**Information Accumulation:** The cognitive process of storing and recalling information (memory-based).

**Information Metabolism:** The process of transforming incoming information through psychic functions (process-based).

**Critical distinction:** Socionics is about the **process** (how information is transformed), not the **content** (what information is stored).

---

## Part V: System Components

### 5.1 Simulation Engine / Text World Engine

**Definition:** The core computational component that runs scenario-based simulations. Instantiates Text-World environments parameterized by scenario type, stakes, time pressure, ambiguity, and value conflict axis.

**Input:** Two Digital Twins (User Twin, Candidate Twin) + Scenario
**Output:** Simulation Transcript (pairwise interaction record)

**NOT:** A game engine. A chatbot. A simple question-answering system.

---

### 5.2 Scenario Compiler

**Definition:** A component that generates parameterized "critical event" scenarios for simulation. Scenarios are defined by:

- Scenario type (relocation, financial crisis, etc.)
- Stakes (magnitude of consequences)
- Time pressure (urgency)
- Ambiguity (information availability)
- Value conflict axis (primary tension point)
- Required joint decision

**NOT:** A random scenario generator. A conversation starter library.

---

### 5.3 Love Observer

**Definition:** The analysis module that consumes Simulation Transcripts and produces structured compatibility assessments.

**Output:**
```
Assessment = {
  dialogQuality: Score,
  complementarity: Score,
  strategicRiskFlags: [Flag],
  operationalRiskFlags: [Flag],
  tacticalRiskFlags: [Flag],
  explanationGraph: Graph
}
```

**NOT:** A human psychologist. A definitive diagnostic tool. A single compatibility number.

---

### 5.4 Concierge Action Layer

**Definition:** The user-facing component responsible for delivering weekly digests, pre-date coaching, and scheduling/logistics support.

**Output:** Weekly shortlist (1-5 candidates) + evidence packets + coaching

---

### 5.5 Digital Twin Builder

**Definition:** The component that transforms a Persona into a controllable agent (Digital Twin). In practice, this is the "agent prompt + memory + policy constraints" layer.

**NOT:** A cloning system. A consciousness transfer mechanism.

---

## Part VI: Outputs and Artifacts

### 6.1 Simulation Transcript

**Definition:** A textual record generated by the Simulation Engine, documenting the simulated reasoning, emotional responses, and behavioral choices of one or more Digital Twins in a scenario.

**Content:** Timestamped exchanges, decision points, internal monologue (optional), outcome state.

**NOT:** A real conversation. A definitive prediction. A transcript of actual events.

---

### 6.2 Evidence Packet

**Definition:** A user-facing artifact accompanying each candidate recommendation. Contains plain-language explanation referencing simulation outcomes and suggested questions for the first date.

**Format:** "In a [scenario type] scenario, [User Twin] and [Candidate Twin] showed [behavior pattern]. Here are questions to validate this assumption: [list]."

**NOT:** A certainty. A psychological diagnosis. A guarantee of relationship success.

---

### 6.3 Compatibility Score

**Definition:** A numerical or categorical value representing a specific aspect of predicted compatibility. Scores are produced by the Love Observer per layer and per dimension.

**Types:**
- Dialog Quality Score
- Complementarity Score
- Layer-specific Risk Flags (not scores, but indicators)

**NOT:** A single universal number. A definitive judgment. A score that replaces human judgment.

---

### 6.4 Weekly Shortlist

**Definition:** The curated list of 1-5 candidate recommendations delivered to the user on a weekly cadence, each accompanied by an Evidence Packet.

---

## Part VII: Algorithmic Concepts

### 7.1 Sparse Reward Principle

**Definition:** The principle (borrowed from reinforcement learning) that high-frequency, low-information interactions are less valuable for prediction than low-frequency, high-information interactions.

**Application:** The Simulation Engine focuses on "critical events" (stressors, conflicts, major decisions) rather than routine daily chat. Routine interactions are poor predictors of compatibility; responses to high-stakes scenarios are diagnostically superior.

---

### 7.2 Critical Event / Critical Incident

**Definition:** A scenario involving high stakes, potential value conflict, or major life decisions, designed to elicit diagnostic behavioral signals.

**Examples:** Relocation for career, family budget crisis, reaction to partner's sudden failure.

---

### 7.3 Cognitive Offload

**Definition:** The design goal of reducing the user's cognitive burden by delegating the labor of searching, reading, triaging, and shortlisting candidates to the AI agent.

---

## Part VIII: Epistemological Terms

### 8.1 Hypothesis

**Definition:** In the scientific method, a proposed explanation made on the basis of limited evidence as a starting point for further investigation.

**In Cognitive Matchmaker:** Every typological output, simulation prediction, and compatibility assessment is a hypothesis to be validated. Nothing is treated as definitive truth.

**Counter:** Hypothesis ≠ Fact. Hypothesis ≠ Assumption without evidence.

---

### 8.2 Validation

**Definition:** The process of testing predictions against real-world outcomes to assess the accuracy and utility of a model.

**In Cognitive Matchmaker:** User feedback (date outcomes, relationship progress) is used to refine Persona models and improve simulation quality.

**NOT:** Proof. Confirmation bias. Cherry-picking favorable outcomes.

---

### 8.3 Evidence Packet as Evidence

**Definition:** An "evidence packet" contains evidence in the scientific sense: a traceable basis for a claim, not the claim itself. It shows which simulation moments drove which conclusions.

**Counter:** Evidence ≠ Truth. Evidence is the basis for belief, subject to revision.

---

## Part IX: Potential Ambiguities Resolved

| Ambiguous Term | Resolution |
|----------------|------------|
| "Model" (epistemological) | Formal representation for prediction (Section 1.5): Persona, Digital Twin, Unified Compatibility Model |
| "Model" (Socionics/Kępiński) | Information model = cognitive mental construct; NOT the same as our formal representations |
| "Modeling" (epistemological) | Constructing formal representations |
| "Modeling" (Socionics) | Information modeling = cognitive process of processing information |
| "Simulation" could mean real conversation vs. synthetic | Always synthetic scenario runs, never actual user conversations |
| "Score" could mean single number vs. vector | Compatibility is always a structured assessment vector, not a single number |
| "Framework" could mean Activity Theory vs. typology | Activity Theory = theoretical skeleton. Typologies = feature schema languages |
| "Prediction" could imply certainty | All predictions are hypotheses to be validated, not certainties |
| "Twin" could imply perfect copy | Digital Twin is a simplified computational model, not a perfect copy |
| "Typology" could imply validated science | Typologies are explicitly framed as heuristics, not validated psychometrics |
| "Function" could mean Socionics function vs. mathematical function | Always specify: "psychic function" (Socionics) vs. "mathematical function" (epistemological/logical) |
| "Type" could mean Socionics type vs. data type | Always specify context; in Socionics context, use "socionic type" or "information metabolism type" |
| "System" could mean multiple things | Specify: Activity System, Information System (Socionics), or Software System |
| "Metabolism" could mean biological vs. information | "Information metabolism" (Кепиньский) is specific; not biological |
| "Layer" could mean Persona layer vs. network layer | Always specify: Strategic/Operational/Tactical (Persona) vs. "software layer" |
| "Persona" vs. "Personality" | Persona = our induced representation. Personality = general psychological concept |
| "Synthesis" (epistemological) | Combining elements into unified whole |
| "Synthesis" (chemical) | Chemical combination; NOT applicable here |

---

## Part X: Document Cross-Reference

### Core Epistemological Terms

| Term | Defined Here | Used In |
|------|--------------|---------|
| Induction | Section 1.1 | scientific-contribution-statement.md |
| Deduction | Section 1.2 | scientific-contribution-statement.md |
| Analysis | Section 1.3 | scientific-contribution-statement.md |
| Synthesis | Section 1.4 | scientific-contribution-statement.md |
| Modeling | Section 1.5 | scientific-contribution-statement.md |

### Person Constructs

| Term | Defined Here | Used In |
|------|--------------|---------|
| Persona | Section 2.1 | project-requirements.md, scientific-contribution-statement.md |
| Digital Twin | Section 2.2 | project-requirements.md, scientific-contribution-statement.md |
| User Twin / Candidate Twin | Section 2.3 | project-requirements.md |

### Activity Theory

| Term | Defined Here | Used In |
|------|--------------|---------|
| Activity (Strategic) | Section 3.1 | project-requirements.md |
| Action (Operational) | Section 3.2 | project-requirements.md |
| Operation (Tactical) | Section 3.3 | project-requirements.md |
| Motive | Section 3.4 | - |
| Goal | Section 3.5 | - |
| Condition | Section 3.6 | - |

### Typological Frameworks

| Term | Defined Here | Used In |
|------|--------------|---------|
| Temporistics | Section 4.1 | project-requirements.md |
| Psychosophy | Section 4.2 | project-requirements.md |
| Socionics | Section 4.3 | project-requirements.md |

### Socionics-Specific (Part IV-B)

| Term | Defined Here | Note |
|------|--------------|------|
| Information Metabolism | Section 4.3.1 | Kępiński concept |
| Information Model | Section 4.3.2 | ⚠️ NOT our "Model" |
| Psychic Function | Section 4.3.3 | 8 aspects |
| Model A | Section 4.3.4 | Structural diagram |
| Intertype Relations | Section 4.3.5 | Compatibility predictions |
| Reimbursement | Section 4.3.6 | Compensatory mechanism |

### System Components

| Term | Defined Here | Used In |
|------|--------------|---------|
| Text World Engine | Section 5.1 | project-requirements.md |
| Scenario Compiler | Section 5.2 | project-requirements.md |
| Love Observer | Section 5.3 | project-requirements.md, scientific-contribution-statement.md |
| Concierge Action Layer | Section 5.4 | project-requirements.md |
| Digital Twin Builder | Section 5.5 | project-requirements.md |

### Outputs

| Term | Defined Here | Used In |
|------|--------------|---------|
| Simulation Transcript | Section 6.1 | project-requirements.md, scientific-contribution-statement.md |
| Evidence Packet | Section 6.2 | project-requirements.md |
| Compatibility Score | Section 6.3 | project-requirements.md |
| Weekly Shortlist | Section 6.4 | project-requirements.md |

### Algorithmic

| Term | Defined Here | Used In |
|------|--------------|---------|
| Sparse Reward Principle | Section 7.1 | scientific-contribution-statement.md |
| Critical Event | Section 7.2 | - |
| Cognitive Offload | Section 7.3 | - |

### Epistemological

| Term | Defined Here | Note |
|------|--------------|------|
| Hypothesis | Section 8.1 | Applied to all outputs |
| Validation | Section 8.2 | - |
| Evidence | Section 8.3 | Scientific sense |
