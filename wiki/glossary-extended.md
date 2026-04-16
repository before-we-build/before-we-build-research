---
title: Glossary Extended
type: reference
tags: [glossary, terminology, disambiguation]
created: 2026-04-16
updated: 2026-04-16
sources: []
---

# Glossary Addendum: Extended Ambiguity Disambiguation

## Purpose

This addendum extends the glossary with additional ambiguous terms identified through systematic review of all project documents. Each term is analyzed for domain-specific meanings and provided with explicit disambiguation.

---

## Critical Disambiguation Section

### CRITICAL-1: "Model" — Four Distinct Meanings

| # | Term | Domain | Definition | In Our Project |
|---|------|--------|------------|----------------|
| 1 | **Formal Model** | Epistemological | Simplified representation for prediction/explanation | Persona, Digital Twin, Unified Compatibility Model |
| 2 | **Information Model** | Socionics/Kępiński | Mental construct for processing information | Psychic function information model |
| 3 | **Model A** | Socionics | Structural diagram of 8 psychic functions | Specific Socionics artifact |
| 4 | **Mathematical Model** | Computer Science | Set of equations/functions | Not used directly |

**Rule:** When "model" appears without qualifier:
- In Epistemological context → Formal Model (Section 1.5 of main glossary)
- In Socionics context → "information model" or "Model A" explicitly
- In Software context → Data model or ML model explicitly

---

### CRITICAL-2: "Function" — Three Distinct Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Psychic Function** | Socionics | Unit of information processing (8 aspects: Te, Ti, Fe, Fi, Se, Si, Ne, Ni) |
| 2 | **Mathematical Function** | Computer Science | Mapping from inputs to outputs: f(x) |
| 3 | **Software Function** | Programming | Named subroutine or method |

**Rule:** 
- Always write "psychic function" or specify by aspect name (e.g., "Te function")
- Mathematical functions are used in formulas without conflict
- Software functions are used in technical documentation

---

### CRITICAL-3: "Type" — Two Distinct Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Socionic Type** | Socionics | 16 information metabolism types (e.g., ILE, SEI, LIE) |
| 2 | **Data Type** | Computer Science | Classification of data (int, string, etc.) |

**Rule:** Use "socionic type" when discussing personality, never just "type" in that context.

---

### CRITICAL-4: "Reasoning" — Two Distinct Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Deductive Reasoning** | Epistemological | Deriving conclusions from premises |
| 2 | **LLM Reasoning** | AI | Emergent inferencing in language models |

**Rule:** 
- In epistemological context → deductive reasoning (Section 1.2)
- In AI context → LLM reasoning or emergent inference
- Never use "reasoning" alone; specify context

---

### CRITICAL-5: "Representation" — Two Distinct Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Mental Representation** | Psychology | Cognitive encoding of external reality |
| 2 | **Formal Representation** | Computer Science | Data structure encoding information |

**Rule:** 
- In Persona context → formal structured representation
- In psychological context → "mental representation" or "cognitive representation"
- In Socionics context → "information representation"

---

### CRITICAL-6: "Prediction" — Must Always Be Qualified

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Simulation Prediction** | Our project | Hypothesis generated from digital twin simulation |
| 2 | **Statistical Prediction** | ML | Point estimate from trained model |
| 3 | **Forecast** | General | Future projection (weather, financial) |

**Rule:** ALL predictions in our system are hypotheses, not certain forecasts. Always phrase as "predicted behavior hypothesis" or "simulation-derived hypothesis."

---

### CRITICAL-7: "Mapping" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Type Mapping** | Socionics | Mapping between elements and functions |
| 2 | **Feature Mapping** | ML | Transformation of input features |
| 3 | **Conceptual Mapping** | Our project | Binding Activity Theory layers to typologies |
| 4 | **Memory Mapping** | Computer Science | Address translation |

**Rule:** Use qualifiers: "conceptual mapping" (our binding), "type mapping" (Socionics)

---

## High-Priority Disambiguation

### HIGH-1: "Schema" — Two Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Schema (Feature Language)** | Our project | Typology as feature generation language |
| 2 | **Database Schema** | Database | Structure definition |

**Rule:** In typology context, always "typological schema" or "schema language"

---

### HIGH-2: "Embedding" — Three Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Vector Embedding** | ML | Numerical vector representation |
| 2 | **Psychological Embedding** | Psychology | Attachment or internalization |
| 3 | **Code Embedding** | Software | Including external code |

**Rule:** Vector embeddings are NOT how we represent personas. We use structured representations.

---

### HIGH-3: "Decomposition" — Two Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Analytical Decomposition** | Epistemological | Breaking down for analysis (Section 1.3) |
| 2 | **Functional Decomposition** | Software | Breaking down into functions/modules |

**Rule:** In Analysis section → epistemological decomposition. In software design → functional decomposition.

---

### HIGH-4: "Integration" — Two Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Synthesis Integration** | Epistemological | Combining elements (Section 1.4) |
| 2 | **System Integration** | Software | Connecting systems |

**Rule:** In typology/synthesis context → epistemological. In infrastructure context → system.

---

### HIGH-5: "State" — Three Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Dialog State** | Conversation | Current context of conversation |
| 2 | **Workflow State** | Orchestration | Execution state of workflow |
| 3 | **Psychic State** | Psychology | Current mental/emotional state |

**Rule:** Always specify: "dialog state," "workflow state," "psychic state"

---

### HIGH-6: "Memory" — Three Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Short-Term Memory** | Conversation | Recent turns in dialog |
| 2 | **Long-Term Memory** | Vector DB | Persistent semantic storage |
| 3 | **Cognitive Memory** | Psychology | Human memory systems |

**Rule:** Always specify layer or use full term from glossary

---

### HIGH-7: "Pattern" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Behavioral Pattern** | Our project | Recurring behavior regularities |
| 2 | **Communication Pattern** | Socionics | Typical interaction styles |
| 3 | **Search Pattern** | ML | Retrieval query patterns |
| 4 | **Design Pattern** | Software | Reusable solution templates |

**Rule:** Use qualifiers: "behavioral pattern," "communication pattern," etc.

---

### HIGH-8: "Signal" — Two Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Diagnostic Signal** | Our project | Compatibility indicator from analysis |
| 2 | **Digital Signal** | Electronics | Information in signal form |

**Rule:** In compatibility context → always "diagnostic signal" or "compatibility signal"

---

### HIGH-9: "Output" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Simulation Output** | Our project | Simulation transcript |
| 2 | **Model Output** | ML | Prediction from model |
| 3 | **System Output** | General | Result of computation |

**Rule:** In context of Love Observer → "compatibility assessment" or "structured assessment"

---

### HIGH-10: "Outcome" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Relationship Outcome** | Our project | Real-world result of dating interaction |
| 2 | **Simulation Outcome** | Our project | Result of scenario simulation |
| 3 | **Medical Outcome** | Medicine | Result of treatment |

**Rule:** Always specify: "relationship outcome," "simulation outcome"

---

### HIGH-11: "Engagement" — Three Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Dialog Engagement** | Our project | Mutual responsiveness in conversation |
| 2 | **User Engagement** | Product | App usage metrics |
| 3 | **Labor Engagement** | HR | Employee involvement |

**Rule:** In Love Observer context → "dialog engagement" or "mutual engagement"

---

### HIGH-12: "Conflict" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Value Conflict** | Our project | Mismatch in strategic values |
| 2 | **Intertype Conflict** | Socionics | Specific Socionics relation type |
| 3 | **System Conflict** | Software | Resource contention |

**Rule:** In compatibility context → "strategic value conflict" or "operational conflict"

---

### HIGH-13: "Attitude" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Psychosophy Attitude** | Our project | One of 4 domains (Logic, Emotion, Volition, Physics) |
| 2 | **General Attitude** | Psychology | Disposition toward something |

**Rule:** In Psychosophy context → always capitalized: "attitude toward Logic"

---

### HIGH-14: "Intuition" — Two Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Jungian Intuition** | Socionics | Information aspect (Ni, Ne) |
| 2 | **General Intuition** | Everyday | Gut feeling |

**Rule:** In Socionics context → "intuitive function" or specify (Ne/Ni)

---

### HIGH-15: "Logic" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Extraverted Logic** | Socionics | Te function (business, efficiency) |
| 2 | **Introverted Logic** | Socionics | Ti function (formal, structure) |
| 3 | **Formal Logic** | Philosophy | Deductive systems |
| 4 | **Informal Logic** | Critical Thinking | Argument analysis |

**Rule:** In Socionics context → specify "extraverted logic (Te)" or "introverted logic (Ti)"

---

### HIGH-16: "Emotion" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Extraverted Emotion** | Socionics | Fe function (emotional expression) |
| 2 | **Introverted Emotion** | Socionics | Fi function (values, relationships) |
| 3 | **General Emotion** | Psychology | Affective states |

**Rule:** In Socionics context → specify Fe or Fi

---

### HIGH-17: "Sensation" — Two Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Extraverted Sensation** | Socionics | Se function (physical reality) |
| 2 | **Introverted Sensation** | Socionics | Si function (bodily comfort) |
| 3 | **General Sensation** | Physiology | Physical sensory input |

**Rule:** In Socionics context → specify Se or Si

---

### HIGH-18: "Action" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Activity Theory Action** | Our project | Goal-directed behavior (Operational level) |
| 2 | **Physical Action** | Physics | Movement |
| 3 | **Software Action** | Programming | Method call |

**Rule:** In Activity Theory context → "goal-directed action" or "conscious action"

---

### HIGH-19: "Activity" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Activity Theory Activity** | Our project | Motive-driven behavior (Strategic level) |
| 2 | **General Activity** | Physics | State of being active |
| 3 | **Software Activity** | Android | UI component |

**Rule:** In Activity Theory context → "activity (motive-driven)" or "Activity with capital A"

---

### HIGH-20: "Operation" — Multiple Meanings

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Activity Theory Operation** | Our project | Automatic habitual behavior (Tactical level) |
| 2 | **Mathematical Operation** | Math | Addition, multiplication, etc. |
| 3 | **Software Operation** | DevOps | Running service |

**Rule:** In Activity Theory context → "automatic operation" or "Tactical-level operation"

---

## Medium-Priority Disambiguation

### MED-1: "Trajectory"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Life Trajectory** | Biography | Life course |
| 2 | **Simulation Trajectory** | Our project | Sequence of simulation steps |
| 3 | **Learning Trajectory** | ML | Optimization path |

---

### MED-2: "Orientation"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Temporal Orientation** | Our project | Relationship to Past/Present/Future |
| 2 | **Information Orientation** | Socionics | EI/SN dimension |
| 3 | **Sexual Orientation** | Psychology | Sexual preference |

---

### MED-3: "Trait"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Personality Trait** | Psychology | Consistent behavior pattern |
| 2 | **Character Trait** | Literature | Personality quality |
| 3 | **ML Trait** | Software | Object property |

---

### MED-4: "Factor"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Personality Factor** | Psychometrics | Big Five factors |
| 2 | **Risk Factor** | Our project | Compatibility risk indicator |
| 3 | **Mathematical Factor** | Math | Multiplicand |

---

### MED-5: "Dimension"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Personality Dimension** | Psychometrics | Trait axis |
| 2 | **Mathematical Dimension** | Geometry | Spatial extent |
| 3 | **Data Dimension** | ML | Feature count |

---

### MED-6: "Risk"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Compatibility Risk** | Our project | Strategic/Operational/Tactical flags |
| 2 | **Financial Risk** | Finance | Monetary loss potential |
| 3 | **Technical Risk** | Engineering | System failure potential |

---

### MED-7: "Depth"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Profile Depth** | Our project | Richness of Persona |
| 2 | **Relationship Depth** | Psychology | Intimacy level |
| 3 | **Analysis Depth** | General | Thoroughness |

---

### MED-8: "Quality"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Dialog Quality** | Our project | Love Observer metric |
| 2 | **System Quality** | Engineering | Non-functional requirements |
| 3 | **Life Quality** | Economics | Standard of living |

---

### MED-9: "Stability"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Relationship Stability** | Our project | Predictability of relationship |
| 2 | **System Stability** | Engineering | Reliability |
| 3 | **Emotional Stability** | Psychology | Trait measure |

---

### MED-10: "Counterfactual"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Philosophical Counterfactual** | Philosophy | "What if" reasoning |
| 2 | **ML Counterfactual** | XAI | Explanation generation |
| 3 | **Simulation Counterfactual** | Our project | "What would this twin do in scenario X" |

---

### MED-11: "Retrieval"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Vector Retrieval** | RAG | Similarity search |
| 2 | **Memory Retrieval** | Psychology | Recall |
| 3 | **Document Retrieval** | IR | Search engine |

---

### MED-12: "Reflection"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Philosophical Reflection** | Philosophy | Self-examination |
| 2 | **Software Reflection** | Programming | Introspection |
| 3 | **RAG Reflection** | AI | Query rewriting |

---

### MED-13: "Compilation"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Scenario Compilation** | Our project | Creating parameterized scenarios |
| 2 | **Code Compilation** | Programming | Building executable |

---

### MED-14: "Rehearsal"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Mental Rehearsal** | Psychology | Visualization practice |
| 2 | **Simulation Rehearsal** | Our project | Dry run before production |

---

### MED-15: "Channel"

| # | Term | Domain | Definition |
|---|------|--------|------------|
| 1 | **Communication Channel** | Our project | Information exchange pathway |
| 2 | **Information Channel** | Socionics | EI/SN or TF/FJ dimension |

---

## Low-Priority (Clarified When Needed)

### LOW-1: "Alignment"

| Primary Meaning | Alternative |
|-----------------|-------------|
| Value alignment (our project) | Model alignment (AI safety) |

---

### LOW-2: "Fidelity"

| Primary Meaning | Alternative |
|-----------------|-------------|
| Simulation fidelity (realism) | Model fidelity (accuracy) |

---

### LOW-3: "Profiling"

| Primary Meaning | Alternative |
|-----------------|-------------|
| User profiling (GDPR concern) | Performance profiling (engineering) |

---

### LOW-4: "Diagnosis"

| Primary Meaning | Alternative |
|-----------------|-------------|
| Psychological diagnosis (not our claim) | System diagnosis (technical) |

---

### LOW-5: "Compensation"

| Primary Meaning | Alternative |
|-----------------|-------------|
| Reimbursement (Socionics reimbursement) | Financial compensation |

---

## Summary Table of All Critical Terms

| Term | Meanings Count | Primary Project Meaning | Always Write As |
|------|----------------|------------------------|-----------------|
| Model | 4 | Formal representation | "formal model" or specify type |
| Function | 3 | Psychic function (Socionics) | "psychic function" or "Te/Ti/Fe/Fi/Se/Si/Ne/Ni" |
| Type | 2 | Socionic type | "socionic type" |
| Reasoning | 2 | Deductive reasoning | "deductive reasoning" |
| Representation | 2 | Formal representation | "formal representation" |
| Prediction | 3 | Simulation hypothesis | "simulation-derived hypothesis" |
| Mapping | 4 | Conceptual mapping | "conceptual mapping" |
| Schema | 2 | Typological schema | "typological schema" |
| Embedding | 3 | Vector embedding (NOT our use) | "vector embedding" (if used) |
| Decomposition | 2 | Analytical decomposition | "analytical decomposition" |
| Integration | 2 | Synthesis integration | "synthesis integration" |
| State | 3 | Dialog/Workflow state | specify: "dialog state" |
| Memory | 3 | Vector/Short-term/Long-term | specify layer |
| Pattern | 4 | Behavioral pattern | "behavioral pattern" |
| Signal | 2 | Diagnostic signal | "diagnostic signal" |
| Output | 3 | Simulation/Model output | "structured assessment" |
| Outcome | 3 | Relationship outcome | "relationship outcome" |
| Engagement | 3 | Dialog engagement | "dialog engagement" |
| Conflict | 3 | Value conflict | "strategic value conflict" |
| Attitude | 2 | Psychosophy attitude | "attitude toward X" |
| Intuition | 2 | Jungian intuition | "intuitive function" |
| Logic | 4 | Extraverted/Introverted | "Te" or "Ti" |
| Emotion | 3 | Extraverted/Introverted | "Fe" or "Fi" |
| Sensation | 3 | Extraverted/Introverted | "Se" or "Si" |
| Action | 3 | Goal-directed action | "goal-directed action" |
| Activity | 3 | Motive-driven activity | "Activity (motive-driven)" |
| Operation | 3 | Automatic operation | "automatic operation" |

---

## Naming Conventions for Disambiguation

### When Writing About Typologies

✅ CORRECT:
- "The extraverted logic function (Te)"
- "Psychic function of type Fe"
- "Information model of sensation"

❌ INCORRECT:
- "The logic function"
- "A function"

### When Writing About Simulation

✅ CORRECT:
- "Simulation-derived behavioral hypothesis"
- "Predicted response trajectory"

❌ INCORRECT:
- "Prediction of what will happen"
- "Guaranteed outcome"

### When Writing About System

✅ CORRECT:
- "Workflow state machine"
- "Dialog state context"
- "Vector retrieval system"

❌ INCORRECT:
- "The system is in a state"

### When Writing About Compatibility

✅ CORRECT:
- "Strategic value conflict"
- "Operational goal misalignment"
- "Tactical communication friction"

❌ INCORRECT:
- "They will conflict"
- "Incompatible personalities"

---

## Cross-System Terminology

For terminology conflicts between typological systems (different definitions of Extraversion, Function, Intuition, etc.), see [[cross-typology-terminology-conflicts]].

## Typology Attribution

For correct attribution of who developed which system and when, see [[typology-authors-timeline]].
