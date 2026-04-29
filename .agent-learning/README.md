# Agent Learning Loop

This directory stores the controlled self-improvement loop for PsyCalc agents.

The goal is inspired by systems like Hermes Agent: agents should learn from experience. In this repository, agent learning is **proposal-first and review-gated** because PsyCalc touches high-stakes domains such as typology, compatibility, theology, neuroscience, clinical boundaries, public figures, and military role-fit.

## Directory structure

```text
.agent-learning/
├── logs/        # observed failures, lessons, and task retrospectives
├── proposals/   # proposed changes to .opencode/agents/*.md
├── reviews/     # review decisions and safety checks
├── skill-drafts/ # inactive reusable skill drafts generated from repeated workflows
├── approved-skills/ # approved reusable skills; activation still depends on runtime support
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

## Skill generation workflow

Agents may draft reusable skills when they notice repeated, stable workflows. Drafting is allowed; silent activation is not.

```text
Repeated task / recurring failure
→ learning log entry
→ inactive skill draft in skill-drafts/
→ proposal describing purpose, risks, and reviewers
→ review and human approval
→ approved skill copied to approved-skills/ or runtime skill directory
→ post-change verification
```

Drafts in `skill-drafts/` are not active instructions. Approved skills in `approved-skills/` are governance artifacts unless explicitly connected to a runtime skill system.

## Rules

1. Do not silently self-modify agents.
2. Do not weaken caveats without specialist review.
3. Do not treat generated agent output as primary evidence.
4. Preserve delegation-first routing.
5. Prefer small enforceable instruction patches over broad rewrites.
6. Agents may auto-draft skills, but must not auto-apply or activate skills without explicit approval.
7. Skills must not replace specialist review in high-risk domains.

## Steward agent

Use `.opencode/agents/agent-improvement-steward.md` for creating and reviewing improvement proposals.
