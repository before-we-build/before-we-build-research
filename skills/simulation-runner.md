# SKILL: simulation-runner

## Purpose

Execute multi-agent simulation scenarios at scale. Manages parallel execution of conversation simulations between agent twins.

**Based on:** CogniPair-style simulation architecture plus project-specific interaction phases

## When to Use

- Running the core simulation loop
- Executing adversarial scenarios
- Generating data for compatibility scoring

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              SIMULATION RUNNER (Orchestrator)                 │
│                                                              │
│  ┌─────────┐  ┌─────────┐                                   │
│  │ Agent A │  │ Agent B │   ← GNWT-Agents (from persona-cloner)
│  │ (Twin)  │  │ (Twin)  │     with Global Workspace
│  └────┬────┘  └────┬────┘                                   │
│       │              │                                       │
│       └──────────────┼──────────────┐                        │
│                      ▼              │                        │
│              ┌─────────────┐        │                        │
│              │  Scenario   │        │                        │
│              │  Engine     │        │                        │
│              └──────┬──────┘        │                        │
│                     │                │                        │
│              ┌──────▼──────┐        │                        │
│              │  Turn Loop  │        │                        │
│              │  (max_turns)│        │                        │
│              └──────┬──────┘        │                        │
│                     │                │                        │
└─────────────────────┼────────────────┘                        │
                      ▼                                        │
              ┌─────────────┐                                  │
              │  Observer   │   ← External LLM analysis        │
              │   Agent     │                                  │
              └──────┬──────┘                                  │
                     ▼                                          │
              ┌─────────────┐                                  │
              │   Reward    │   ← Compatibility scoring         │
              │   Model     │                                  │
              └─────────────┘                                  │
```

## Three Phases (from Love First)

### Phase 1: Persona Generation
```
Structured profile → persona prompt / narrative
Model: project-selected generator model
```

### Phase 2: Interaction Simulation
```
Agent A + Agent B → Multi-turn conversation
Model: Mistral-Nemo (temp=0.6)
```

### Phase 3: Compatibility Assessment
```
Transcript → LLM Participant + LLM Observer → Compatibility score
```

## How to Use

### Configuration
```yaml
simulation:
  total_runs: 1000          # For Hang the DJ effect
  agents_per_run: 2
  max_turns: 10             # Per conversation
  parallel_execution: true
  max_parallel: 50           # Concurrent runs

model:
  # Persona generation (project default)
  persona_model: "gemini-2.5-flash-lite"
  persona_temp: 0.8

  # Conversation simulation (project default)
  conversation_model: "mistral-nemo"
  conversation_temp: 0.6
  max_tokens: 200

  # Observer analysis
  observer_model: "gpt-4o"
  observer_temp: 0.3

  # CogniPair parameters
  gnwt_model: "gpt-4o"
  gnwt_temp: 0.9
  gnwt_max_tokens: 200

environment:
  platform: "text_chat"
  include_system_messages: true
  memory_persistence: "persistent"  # Critical for Hang the DJ
```

### Process
```python
async def run_simulation(pair, config):
    # 1. Initialize agents from personas
    agent_a = create_gnwt_agent(pair.persona_a, config)
    agent_b = create_gnwt_agent(pair.persona_b, config)

    # 2. For each run
    results = []
    for run_id in range(config.total_runs):
        # Load memory from previous runs
        agent_a.load_memory(pair_id)
        agent_b.load_memory(pair_id)

        # 3. Run conversation
        transcript = await run_conversation(
            agent_a, agent_b,
            max_turns=config.max_turns
        )

        # 4. Observer analysis
        observer_score = await observer.analyze(transcript)

        # 5. Participant self-rating
        participant_scores = await participants.rate(transcript)

        # 6. Calculate reward
        reward = reward_model.estimate(transcript, observer_score, participant_scores)

        # 7. Update memory
        agent_a.update_memory(run_id, reward)
        agent_b.update_memory(run_id, reward)

        # 8. Log decision
        choice_tracker.log(
            run_id=run_id,
            pair=pair,
            transcript=transcript,
            reward=reward,
            decision="mutual" if reward > threshold else "no_match"
        )

        results.append({"run_id": run_id, "reward": reward})

    return results
```

### Output per Run
```yaml
run_id: "uuid"
pair_id: "a1-b2"
run_number: 5
transcript:
  - agent: "a"
    text: "Hi! I'm Alex..."
  - agent: "b"
    text: "Hey Alex, I'm Jamie..."
  # ... more turns

observer_assessment:
  mutual_engagement: 0.8
  conversational_flow: 0.9
  overall_compatibility: 0.85

participant_ratings:
  agent_a:
    attraction: 0.85
    comfort: 0.80
  agent_b:
    attraction: 0.75
    comfort: 0.90

reward: 0.82
decision: "mutual"  # Both chose each other
```

## GNWT Integration

### Within Each Agent
```python
def gnwt_process(agent, query, history):
    """
    CogniPair's GNWT-Agent processing
    1. Parallel module processing
    2. Salience calculation
    3. Global workspace broadcast
    4. Module integration
    """
    # Each module processes in parallel
    modules = {
        "emotion": emotion_module.process(query, history, agent.personality.N),
        "memory": memory_module.process(query, history, agent.personality.O),
        "planning": planning_module.process(query, history, agent.personality.C),
        "social_norms": norms_module.process(query, history, agent.personality.A),
        "goal_tracking": goal_module.process(query, history, agent.personality.E),
    }

    # Calculate salience weights
    weights = salience_calculator.calculate(modules, agent.global_workspace)

    # Integrate into global workspace
    gw_content = global_workspace.broadcast(modules, weights)

    # Generate response
    response = llm.generate(
        prompt=build_prompt(modules, gw_content),
        model="gpt-4o",
        temperature=0.9,
        max_tokens=200
    )

    return response
```

## Scaling

### Parallel Execution
```python
async def run_parallel_batch(pairs, config):
    """
    Run multiple simulations concurrently
    CogniPair: 551 agents, we target 1000+
    """
    semaphore = asyncio.Semaphore(config.max_parallel)

    async def run_with_limit(pair):
        async with semaphore:
            return await run_simulation(pair, config)

    results = await asyncio.gather(*[
        run_with_limit(pair) for pair in pairs
    ])

    return results
```

### Performance Targets

| Metric | CogniPair | Our Target |
|--------|-----------|------------|
| Agents | 551 | 10,000+ |
| Runs per pair | ~20 | 1000 |
| Total simulations | ~10,000 | 1,000,000 |
| Time per run | ~30s | <5s |
| Parallel runs | ? | 50 |

## Memory Integration

```python
# Critical for Hang the DJ: persistent memory across runs
async def run_simulation_with_memory(pair, config):
    for run_id in range(config.total_runs):
        # Load accumulated memory
        memory_a = memory_persister.load(pair.agent_a_id)
        memory_b = memory_persister.load(pair.agent_b_id)

        # Inject into GNWT agents
        agent_a.inject_memory(memory_a)
        agent_b.inject_memory(memory_b)

        # Run conversation
        result = await run_single_conversation(agent_a, agent_b)

        # Update memory based on outcome
        memory_persister.update(pair.agent_a_id, result)
        memory_persister.update(pair.agent_b_id, result)
```

## Dependencies

- `persona-cloner` — Generates GNWT agents
- `global-workspace` — Processes agent cognition
- `memory-persister` — Maintains cross-run memory
- `observer-agent` — Analyzes conversations
- `reward-model` — Calculates compatibility reward
- `choice-tracker` — Logs final decisions

## Related Skills

- `persona-cloner` — Creates agents
- `global-workspace` — Processes cognition
- `memory-persister` — Maintains memory
- `observer-agent` — Analyzes output
- `choice-tracker` — Receives logged decisions
