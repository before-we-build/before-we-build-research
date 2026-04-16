# SKILL: choice-tracker

## Purpose

Log all decisions made by agents across multiple simulation runs. Enables calculating repeated-choice metrics for compatibility analysis.

## When to Use

- Running multiple simulations with the same pair
- Calculating consistency of choice across scenarios
- Generating the final compatibility percentage

## Core Metric: Repeated Choice Score

```
Compatibility Score = (Times Chose Each Other / Total Scenarios) × 100
```

Example: 820 out of 1000 scenarios = 82.0%

## How to Use

### Input
```yaml
simulation_run: "uuid"
pair_id: "a1-b2"
scenario_id: "forced_separation"
decisions:
  agent_a:
    action: "reject_assigned_partner"
    target: "agent_b"
    reasoning: "Felt stronger connection"
  agent_b:
    action: "sought_reunion"
    target: "agent_a"
    reasoning: "Could not stop thinking about them"
mutual_choice: true
```

### Process
1. **Capture decision** — Log each agent's choice in structured format
2. **Detect mutual choice** — Both agents chose each other?
3. **Store in sequence** — Add to history for this pair
4. **Calculate rolling score** — Update compatibility percentage

### Output
```yaml
pair_id: "a1-b2"
total_runs: 1000
mutual_choices: 998
compatibility_score: 82.0
choice_sequence: [true, true, false, true, ...]
run_history:
  - run: 1
    scenario: "forced_separation"
    mutual: true
  - run: 2
    scenario: "better_option"
    mutual: true
  # ... 998 more
```

## Decision Taxonomy

### Actions
```yaml
accept_assigned: "Accepted system-assigned partner"
reject_assigned: "Rejected system-assigned partner"
seek_reunion: "Actively tried to reunite with original"
stay_loyal: "Resisted alternative attraction"
switch_partner: "Chose different partner"
express_preference: "Stated desire for specific person"
```

### Reasoning Categories
```yaml
genuine_attraction: "Felt real connection"
rebellion: "Wanted to defy system"
habit: "Comfortable, familiar"
curiosity: "New option seemed interesting"
pressure: "System/others pushed toward choice"
```

## Key Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| `compatibility_score` | mutual/total × 100 | Raw repeated choice % |
| `early_lead` | mutual_first_half - mutual_second_half | Consistency over time |
| `adversarial_strength` | mutual under high pressure / total | How strong under stress |
| `divergence_rate` | scenarios where they disagreed / total | Alignment |

## Implementation Notes

### Persistent Storage
```
pair_history/
  a1-b2/
    run_001.json
    run_002.json
    ...
    summary.json
```

### Real-time Updates
After each run, update:
1. Pair's compatibility score
2. Individual agent's choice patterns
3. Scenario-specific success rates

### Scalability
For 1000 runs × 16 types × all pairs:
- Store compact JSON per run
- Calculate summaries incrementally
- Aggregate at end for final scores

## Dependencies

- `simulation-runner` — Generates decisions to log
- `compatibility-scorer` — Uses tracked choices for final score
- `persona-cloner` — Identifies agents

## Related Skills

- `adversarial-designer` — Creates scenarios that produce tracked decisions
- `compatibility-scorer` — Computes final percentage from tracked choices
- `history-analyzer` — Examines patterns in choice sequences
