# SKILL: memory-persister

## Purpose

Maintain agent memory across multiple simulation runs. Critical for "Hang the DJ" effect where agents remember previous choices.

## When to Use

- Running 1000+ simulations with same pair
- Agent needs to "remember" past decisions
- Simulating long-term relationship dynamics

## The Memory Problem

In typical AI simulations, each run starts fresh:
```
Run 1: Agent A + Agent B → Decision
Run 2: Agent A + Agent B → Decision (NO memory of Run 1)
Run 3: Agent A + Agent B → Decision (NO memory of Run 2)
...
```

For "Hang the DJ", we need:
```
Run 1: Agent A + Agent B → Decision (stored)
Run 2: Agent A + Agent B → Decision (reads Run 1 memory)
Run 3: Agent A + Agent B → Decision (reads Runs 1-2 memory)
...
```

## Memory Architecture

### Layers

```
┌─────────────────────────────────────┐
│        Episodic Memory              │  ← "Remember: we chose each other"
├─────────────────────────────────────┤
│        Semantic Memory              │  ← "Know: I prefer people like B"
├─────────────────────────────────────┤
│        Identity Core                │  ← "Am: Loyal to my choices"
└─────────────────────────────────────┘
```

### Episodic Memory
```yaml
entries:
  - timestamp: 1
    event: "met_b_in_scenario_3"
    emotion: "positive"
    choice: "seek_reunion"
  - timestamp: 2
    event: "system_assigned_c"
    emotion: "negative"
    choice: "reject_c"
  - timestamp: 3
    event: "found_b_again"
    emotion: "relief"
    choice: "stay_with_b"
```

### Semantic Memory
```yaml
beliefs:
  - "People like B make me feel understood"
  - "System assignments feel wrong"
  - "Loyalty matters more than comfort"
preferences:
  - "Prefer deep conversation over small talk"
  - "Attracted to authenticity over polish"
```

### Identity Core (Immutable)
```yaml
core_traits:
  - "My choices reflect who I am"
  - "I trust my feelings over external pressure"
  - "Once I choose, I stay"
```

## How to Use

### Initialize for Pair
```yaml
persona_id_a: "twin-a"
persona_id_b: "twin-b"
memory_store: "pair_a-b_memory.json"
mode: "persistent"  # across all runs
```

### After Each Run
```python
memory_persister.update(
    agent_id="twin-a",
    new_memory={
        "event": "chose_b_over_assigned_c",
        "timestamp": 5,
        "significance": "high"
    }
)
```

### Before Next Run
```python
context = memory_persister.load(
    agent_id="twin-a"
)
# Returns: full memory history for context injection
```

## Memory Consolidation

After N runs, compress episodic memories into semantic generalizations:

```
50 episodes of "chose B" → Belief: "I always choose B"
20 episodes of "resisted pressure" → Trait: "Pressure-resistant"
```

This prevents memory from growing infinitely while preserving insights.

## Integration with GNWT-Agent

CogniPair's Global Workspace Theory already has memory module:
```
Memory Module:
  - episodic: stores dialogue segments
  - semantic: stores abstract knowledge
  - retrieval: vector similarity search
  
Persistent version adds:
  - cross_run_storage
  - identity_preservation
  - memory_consolidation
```

## Key Principles

1. **Preserve identity** — Core traits survive across runs
2. **Allow growth** — Episodic → Semantic over time
3. **Handle scale** — 1000 runs shouldn't slow simulation
4. **Protect privacy** — Memory data stays local

## Implementation Notes

### Storage Format
```json
{
  "pair_id": "a1-b2",
  "runs": [
    {
      "run_id": 1,
      "memories_a": [...],
      "memories_b": [...],
      "consolidated": false
    }
  ],
  "consolidated": {
    "a": {"beliefs": [...], "traits": [...]},
    "b": {"beliefs": [...], "traits": [...]}
  }
}
```

### Retrieval
```python
def get_relevant_memory(agent, current_scenario):
    # Find memories similar to current context
    memories = vector_search(
        query=current_scenario,
        memory_store=agent.memory,
        top_k=10
    )
    return memories
```

## Dependencies

- `persona-cloner` — Creates agents with memory capacity
- `simulation-runner` — Orchestrates memory updates
- `choice-tracker` — Logs decisions that become memories

## Related Skills

- `simulation-runner` — Updates memory after each run
- `choice-tracker` — Decisions become memories
- `persona-cloner` — Agents with memory modules
