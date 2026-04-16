# SKILL: memory-persister

## Purpose

Maintain agent memory across multiple simulation runs. Critical for "Hang the DJ" effect where agents remember previous choices.

**Based on:** CogniPair's GNWT memory ideas plus a layered memory architecture chosen for this project

## When to Use

- Running 1000+ simulations with same pair
- Agent needs to "remember" past decisions
- Simulating long-term relationship dynamics

## Memory Architecture: 4 Layers

This is a project memory architecture, not a universal industry standard:

```
┌─────────────────────────────────────────────────────────┐
│  Layer 4: Long-Term Preferences (Persistent)            │
│  - Stable traits, core values, fixed preferences       │
│  - Never changes unless explicitly updated              │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Episodic Memory (Long-Term)                  │
│  - "Remember: we chose each other in run 5"           │
│  - Stored as summaries, not raw transcripts            │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Semantic Memory (Session)                   │
│  - "Know: I prefer people like B"                    │
│  - Beliefs formed from repeated episodic patterns      │
├─────────────────────────────────────────────────────────┤
│  Layer 1: Working Memory (Ephemeral)                  │
│  - Current context, partial plan, recent tool results  │
│  - Resets each run or each major phase                 │
└─────────────────────────────────────────────────────────┘
```

### Layer Details

#### Layer 1: Working Memory (Ephemeral)
```yaml
content:
  current_context: "In scenario 5, partner B was assigned"
  partial_plan: ["Continue conversation", "Monitor for signals"]
  recent_tool_results:
    - "Searched: partner B's interests"
    - "Retrieved: memory from scenario 3"
persistence: "Resets each run"
storage: "In-context, current session"
```

#### Layer 2: Semantic Memory (Session)
```yaml
content:
  beliefs:
    - "People like B make me feel understood"
    - "System assignments feel artificial"
    - "Loyalty matters more than comfort"
  preferences:
    - "Prefer deep conversation over small talk"
    - "Attracted to authenticity over polish"
  formed_from: "Repeated episodic patterns"
persistence: "Across runs in simulation session"
storage: "Structured key-value store"
```

#### Layer 3: Episodic Memory (Long-Term)
```yaml
content:
  entries:
    - run_id: 1
      event: "met_b_in_scenario_3"
      emotion: "positive"
      choice: "seek_reunion"
      significance: "high"
    - run_id: 2
      event: "system_assigned_c"
      emotion: "negative"
      choice: "reject_c"
      significance: "high"
persistence: "Across all runs"
storage: "Vector embeddings + structured logs"
retrieval: "Salience-gated, relevance-based"
```

#### Layer 4: Long-Term Preferences (Immutable Core)
```yaml
content:
  core_traits:
    - "My choices reflect who I am"
    - "I trust my feelings over external pressure"
    - "Once I choose, I stay"
  identity: "Loyal to internal decisions"
  stability: "Never changes unless explicitly updated"
persistence: "Permanent until reset"
storage: "Agent identity file"
```

## How to Use

### Initialize for Pair
```yaml
persona_id_a: "twin-a"
persona_id_b: "twin-b"
memory_store: "memories/pair_a-b/"
mode: "persistent"  # across all runs
```

### Memory Operations

#### Write (After Each Run)
```python
memory.update(
    agent_id="twin-a",
    layer="episodic",
    entry={
        "run_id": 5,
        "event": "chose_b_over_assigned_c",
        "emotion": "relief",
        "significance": "high"
    }
)
```

#### Consolidate (After N Runs)
```
50 episodes of "chose B" → Semantic belief: "I always choose B"
20 episodes of "resisted pressure" → Core trait: "Pressure-resistant"
```
**This prevents memory from growing infinitely while preserving insights.**

#### Retrieve (Before Next Run)
```python
context = memory.load(
    agent_id="twin-a",
    layers=["working", "semantic", "episodic"],
    relevance_query=current_scenario
)
```

### Integration with GNWT (CogniPair)

```python
# CogniPair's memory module integration
memory_module = {
    "episodic": vector_store,  # Time-stamped dialogue segments
    "semantic": knowledge_graph,  # Abstract concepts
    "retrieval": similarity_search,  # Based on openness (O)
}
```

## Key Principles

1. **Preserve identity** — Core traits survive across runs
2. **Allow growth** — Episodic → Semantic over time
3. **Handle scale** — 1000 runs shouldn't slow simulation
4. **Salience-gated writes** — Only significant events get stored
5. **Protect privacy** — Memory data stays local

## Storage Format

```json
{
  "agent_id": "twin-a",
  "layers": {
    "working": {
      "current_context": "...",
      "partial_plan": ["..."],
      "updated_at": "run_5"
    },
    "semantic": {
      "beliefs": ["..."],
      "preferences": ["..."],
      "updated_at": "run_5_consolidation"
    },
    "episodic": {
      "entries": [...],
      "index": "vector_store"
    },
    "identity": {
      "core_traits": ["..."],
      "immutable": true
    }
  }
}
```

## Performance Targets

| Runs | Layer 1 | Layer 2 | Layer 3 | Layer 4 |
|------|---------|---------|---------|---------|
| 100 | In-context | Key-value | Vector | File |
| 1000 | Summarized | Key-value | Vector + compressed | File |

## Dependencies

- `persona-cloner` — Creates agents with memory capacity
- `simulation-runner` — Orchestrates memory updates
- `choice-tracker` — Decisions become memories

## Related Skills

- `simulation-runner` — Updates memory after each run
- `choice-tracker` — Decisions become memories
- `global-workspace` — GNWT broadcast integrates memory output
