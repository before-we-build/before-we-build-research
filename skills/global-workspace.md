# SKILL: global-workspace

## Purpose

Implement the Global Neuronal Workspace Theory (GNWT) for coordinating cognitive modules within an agent. This is the core mechanism that makes CogniPair's agents psychologically realistic.

**Based on:** CogniPair's GNWT-Agent architecture (Figure 5 in paper)

## When to Use

- Creating a psychologically realistic agent
- Needing modules to share information
- Simulating human-like consciousness dynamics

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT QUERY (Q)                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    COGNITIVE MODULES                         │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Emotion  │  │ Memory   │  │ Planning │  │ Social   │  │
│  │ Module   │  │ Module   │  │ Module   │  │ Norms    │  │
│  │          │  │          │  │          │  │ Module   │  │
│  │ R_Em     │  │ R_Mem    │  │ R_Plan   │  │ R_SN     │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│       │              │              │              │          │
│       └──────────────┼──────────────┼──────────────┘          │
│                      │              │                          │
│                      ▼              ▼                          │
│              ┌──────────────┐                               │
│              │   SALIENCE   │                               │
│              │  CALCULATOR  │                               │
│              │              │                               │
│              │  α = f(τ, GW) │                              │
│              └───────┬──────┘                               │
└──────────────────────┼────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  GLOBAL WORKSPACE (GW)                      │
│                                                              │
│  - Broadcasts salient information                           │
│  - Creates unified consciousness                           │
│  - Integrates competing module outputs                      │
│                                                              │
│  G(GW) = Key content from workspace                        │
└──────────────────────┬────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   MODULE INTEGRATION                         │
│                                                              │
│  Response = Σ α_M · R_M + β · G(GW)                       │
│                                                              │
│  Where:                                                     │
│    α_M = personality-weighted module importance              │
│    β = global workspace coefficient                         │
│    G(GW) = extracted workspace content                      │
└─────────────────────────────────────────────────────────────┘
```

## The Five Cognitive Modules

### 1. Emotion Module
```yaml
function: "Detects and processes emotional content"
input: "Query Q, History H, Global Workspace GW, Personality N"
output: "R_Emotion = f_E(Q, H, GW, N)"
weight_param: "Neuroticism (N)"  # N↑ → emotional processing ↑

processing:
  - "Emotion detection: identify affective markers"
  - "Valence-arousal assessment: map to 2D space"
  - "Regulation: adjust intensity based on N parameter"
```

### 2. Memory Module
```yaml
function: "Retrieves relevant memories and updates storage"
input: "Query Q, History H, Global Workspace GW, Personality O"
output: "R_Memory = f_M(Q, H, GW, O)"
weight_param: "Openness (O)"  # O↑ → broader retrieval

processing:
  - "Episodic retrieval: recent interactions"
  - "Semantic retrieval: abstract knowledge"
  - "Vector similarity search with O-adjusted breadth"
```

### 3. Planning Module
```yaml
function: "Develops strategies and next steps"
input: "Query Q, History H, Global Workspace GW, Personality C"
output: "R_Planning = f_P(Q, H, GW, C)"
weight_param: "Conscientiousness (C)"  # C↑ → deeper planning

processing:
  - "Hierarchical goal decomposition"
  - "Break complex goals into tactical steps"
  - "Strategic rigor based on C parameter"
```

### 4. SocialNorms Module
```yaml
function: "Evaluates appropriateness of responses"
input: "Query Q, History H, Global Workspace GW, Personality A"
output: "R_SocialNorms = f_SN(Q, H, GW, A)"
weight_param: "Agreeableness (A)"  # A↑ → stricter enforcement

processing:
  - "Etiquette checking: politeness, form"
  - "Boundary monitoring: self-disclosure limits"
  - "Reciprocity verification: balanced contribution"
```

### 5. GoalTracking Module
```yaml
function: "Monitors progress toward objectives"
input: "Query Q, History H, Global Workspace GW, Personality E"
output: "R_GoalTracking = f_GT(Q, H, GW, E)"
weight_param: "Extraversion (E)"  # E↑ → more assertive goals

processing:
  - "Direction monitoring: advancement tracking"
  - "Uncertainty assessment: information gaps"
  - "Direction adjustment: recalibrate based on dynamics"
```

## Module Integration Formula

```python
def integrate_modules(module_outputs, personality, global_workspace):
    """
    Combine module outputs into coherent response
    Based on CogniPair Equation (1) & (2)
    """
    response = 0
    for module_name, module_output in module_outputs.items():
        # Personality-weighted module importance
        alpha = personality[module_name]
        response += alpha * module_output

    # Global workspace integration
    beta = personality.get("beta", 0.1)
    gw_content = extract_workspace(global_workspace)
    response += beta * gw_content

    return response
```

## Implementation Reference

### LLM Parameters (from CogniPair)
```yaml
model: "gpt-4o"
temperature: 0.9
max_tokens: 200
top_p: 1.0
```

### Parallel Processing
```
All 5 modules process in parallel:
1. Each module receives: Q, H, GW, personality_param
2. Each module outputs: R_Module
3. Salience calculator determines weights
4. Global workspace broadcasts salient content
5. Integration produces final response
```

## Integration with Memory

```python
# From CogniPair: Memory.update() called after each response
memory.update_long_term(query=Q, response=R, history=H)
# Uses attention-based consolidation, highlighting:
# - Emotionally salient content
# - Goal-relevant information
```

## Preferences Update (Learning)

```python
# From CogniPair: Update personality weights based on interaction
P_t1 = P_t + η · ∇_P J(P_t, Q, Response, H)
# Learning rate η allows personality evolution while preserving core traits
```

## Dependencies

- `persona-cloner` — Initializes module weights from personality
- `memory-persister` — Provides memory to Memory Module
- `choice-tracker` — Receives final decisions

## Related Skills

- `persona-cloner` — Sets initial module weights
- `memory-persister` — Feeds Memory Module
- `simulation-runner` — Orchestrates GNWT loop
- `choice-tracker` — Receives integrated output
