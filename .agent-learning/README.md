# Agent Learning Loop

This directory stores the controlled self-improvement loop for Before We Build agents.

The goal is inspired by systems like Hermes Agent: agents should learn from experience. In this repository, agent learning is **proposal-first and review-gated** because Before We Build touches high-stakes domains such as typology, compatibility, theology, neuroscience, clinical boundaries, public figures, and military role-fit.

## Directory structure

```text
.agent-learning/
├── logs/        # observed failures, lessons, and task retrospectives
├── proposals/   # proposed changes to canonical specs in governance/agent-system/ or .agents/roles/
├── reviews/     # review decisions and safety checks
├── skill-drafts/ # inactive reusable skill drafts generated from repeated workflows
├── approved-skills/ # approved reusable skills conforming to Agent Skills specification
└── templates/   # proposal/review templates
```

## Default workflow

```text
Experience / audit finding / user feedback
→ learning log entry (logs/)
→ improvement proposal (proposals/) targeting canonical contracts (governance/agent-system/)
→ specialist review if needed (reviews/)
→ human approval or explicit implementation request
→ patch to canonical specifications
→ compile projections across targets (scripts/agent_system.py build / scripts/generate_agent_adapters.py --write)
→ post-change drift verification (scripts/agent_system.py check-drift / scripts/generate_agent_adapters.py --check)
```

## Supported Harness Targets

Projections are compiled from canonical contracts into:
- **Google Antigravity**: `.agents/agents/*.md`, `.agents/skills/`
- **Anthropic Claude Code**: `.claude/agents/*.md`, `CLAUDE.md`
- **OpenAI Codex**: `.codex/agents/*.toml`
- **OpenCode**: `.opencode/agents/*.md`

Direct manual edits to projection files are prohibited and flagged by CI drift checks.

## Rules

1. Do not silently self-modify agents.
2. Do not weaken caveats without specialist review.
3. Do not treat generated agent output as primary evidence.
4. Preserve delegation-first routing.
5. Prefer small enforceable instruction patches over broad rewrites.
6. Proposals must target canonical specifications in `governance/agent-system/`, `.agents/roles/`, or `.agent-learning/approved-skills/`.
7. Skills must not replace specialist review in high-risk domains.

## Steward agent

Use `governance/agent-system/roles/agent-improvement-steward.yaml` and `.agents/roles/agent-improvement-steward.md` for creating and reviewing improvement proposals.
Compile and verify all projections via `python3 scripts/agent_system.py build` and `python3 scripts/generate_agent_adapters.py --write`.
