# SKILL: simulation-runner

## Purpose

Execute multi-agent simulation scenarios at scale. Manages the parallel execution of thousands of simulated interactions.

## When to Use

- Running the core simulation loop
- Executing adversarial scenarios
- Generating data for compatibility scoring

## Architecture

```
┌─────────────────────────────────────────────┐
│           Simulation Runner                  │
│                                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Agent A │  │ Agent B │  │ Agent N │    │
│  │ (Twin)  │  │ (Twin)  │  │ (Twin)  │    │
│  └────┬────┘  └────┬────┘  └────┬────┘    │
│       │              │              │         │
│       └──────────────┼──────────────┘        │
│                      ▼                         │
│              ┌─────────────┐                  │
│              │  Scenario   │                  │
│              │  Engine     │                  │
│              └─────────────┘                  │
│                      │                         │
│                      ▼                         │
│              ┌─────────────┐                  │
│              │  Decision   │                  │
│              │  Logger     │                  │
│              └─────────────┘                  │
└─────────────────────────────────────────────┘
```

## How to Use

### Configuration
```yaml
simulation:
  total_runs: 1000
  agents_per_run: 2
  max_turns: 20
  parallel_execution: true
  max_parallel: 50

scenario:
  type: "adversarial"
  pressure_level: 0.7
  duration: "short"

environment:
  platform: "text_chat"
  include_system_messages: true
  memory_persistence: "session"
```

### Process
1. **Initialize agents** — Create agent twins for simulation
2. **Load scenario** — Set up adversarial conditions
3. **Run conversation** — Execute multi-turn dialogue
4. **Capture decision** — Extract final choice from each agent
5. **Log results** — Store in choice-tracker
6. **Repeat** — Continue for N runs

### Output
```yaml
run_id: "uuid"
pair_id: "a1-b2"
scenario_id: "forced_separation"
duration_ms: 2340
turns: 12
final_state:
  agent_a:
    final_choice: "reunion_with_b"
    reasoning: "Felt authentic connection"
  agent_b:
    final_choice: "reunion_with_a"
    reasoning: "Could not imagine alternatives"
mutual_choice: true
transcript: ["Agent A: ...", "Agent B: ..."]
```

## Key Parameters

### Parallelization
```yaml
parallel_execution: true
max_parallel: 50        # Run 50 simulations at once
batch_size: 100         # Then next batch
checkpoint_interval: 100 # Save progress every 100 runs
```

### Turn Limits
```yaml
max_turns: 20           # Per conversation
timeout_ms: 30000       # Per turn
max_tokens: 500         # Per response
```

### Memory Modes
```yaml
memory_persistence:
  none:       "Fresh each run, no memory"
  session:     "Memory within single simulation"
  persistent:  "Memory across all runs for pair"  # Like Hang the DJ
```

## Scalability Targets

| Scenario | Current (CogniPair) | Target |
|----------|---------------------|--------|
| Agent count | 551 | 10,000+ |
| Runs per pair | ~20 | 1000 |
| Total simulations | ~10,000 | 1,000,000 |
| Time per run | ~30s | <5s |

## Integration Points

### With persona-cloner
```python
# Before simulation
agent_a = persona_cloner.create_twin(user_a_profile)
agent_b = persona_cloner.create_twin(user_b_profile)
```

### With adversarial-designer
```python
# Create scenario
scenario = adversarial_designer.create(
    pair=(agent_a, agent_b),
    type="forced_separation",
    pressure=0.8
)
```

### With choice-tracker
```python
# After simulation
choice_tracker.log(
    run_id=run_id,
    decisions={
        "agent_a": agent_a.final_choice,
        "agent_b": agent_b.final_choice
    }
)
```

## Dependencies

- `persona-cloner` — Generates agent twins
- `adversarial-designer` — Creates scenarios
- `choice-tracker` — Logs decisions
- `memory-persister` — Manages cross-run memory

## Related Skills

- `adversarial-designer` — Provides scenarios to run
- `choice-tracker` — Receives output
- `memory-persister` — Manages agent memory across runs
