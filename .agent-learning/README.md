# Agent Learning Loop

This directory stores the controlled self-improvement loop for PsyCalc agents.

The goal is inspired by systems like Hermes Agent: agents should learn from experience. In this repository, agent learning is **proposal-first and review-gated** because PsyCalc touches high-stakes domains such as typology, compatibility, theology, neuroscience, clinical boundaries, public figures, and military role-fit.

## Directory structure

```text
.agent-learning/
├── logs/        # observed failures, lessons, and task retrospectives
├── proposals/   # proposed changes to .opencode/agents/*.md
├── reviews/     # review decisions and safety checks
└── templates/   # proposal/review templates
```

## Default workflow

```text
Experience / audit finding
→ learning log entry
→ improvement proposal
→ specialist review if needed
→ human approval or explicit implementation request
→ patch to agent instructions
→ post-change verification
```

## Rules

1. Do not silently self-modify agents.
2. Do not weaken caveats without specialist review.
3. Do not treat generated agent output as primary evidence.
4. Preserve delegation-first routing.
5. Prefer small enforceable instruction patches over broad rewrites.

## Steward agent

Use `.opencode/agents/agent-improvement-steward.md` for creating and reviewing improvement proposals.
