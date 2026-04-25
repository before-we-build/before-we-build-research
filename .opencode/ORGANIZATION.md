# Agent Organization Structure

Based on best practices from McKinsey, ClawPort, and enterprise deployments (2025-2026).

## Hierarchy (3 Levels)

```
master-orchestrator (gold) ⚜
├── Orchestration Governance
│   └── agent-improvement-steward (mediumpurple)
├── Research Team
│   ├── typology-researcher (purple)
│   ├── socionics-intertype-relations-expert (blue)
│   ├── psychosophy-intertype-relations-expert (green)
│   ├── temporistics-intertype-relations-expert (cyan)
│   ├── sociology-researcher (brown)
│   ├── neuroscience-researcher (indigo)
│   ├── clinical-neurologist-expert (darkslategray)
│   ├── christian-theology-researcher (sienna)
│   └── military-roles-researcher (darkgreen)
├── Typing Team  
│   ├── psychosophy-interview-typer (green)
│   ├── psychosophy-test-typer (green)
│   └── psychosophy-quick-typer (green)
├── Analysis Team
│   ├── compatibility-calculator (red)
│   ├── interaction-simulator (yellow)
│   ├── military-specialty-advisor (olive)
│   └── civilian-career-advisor (steelblue)
├── Wiki Team
│   ├── wiki-contributor (white)
│   └── wiki-consistency-checker (magenta)
├── Explanation Team
│   └── type-explain (gray)
└── [Reserved for future]
```

## Team Definitions

### 1. Research Team
**Lead:** typology-researcher
**Purpose:** Finding and validating information, including typological, sociological, neuroscience, clinical-neurology, and Christian-theological context. Intertype-relation experts provide mechanism-level audits of relation names and processes within their own typology.
**Crons:** military-roles-researcher (weekly)

### 0. Orchestration Governance
**Lead:** agent-improvement-steward
**Purpose:** Controlled self-improvement of `.opencode/agents/*.md`, including learning logs, improvement proposals, review-gated instruction patches, and preservation of delegation-first behavior.
**Storage:** `.agent-learning/`

### 2. Typing Team  
**Lead:** (no dedicated lead yet)
**Purpose:** Psychosophy type determination
**Agents:** 3 Psychosophy typing specialists

### 3. Analysis Team
**Lead:** compatibility-calculator
**Purpose:** Multi-type analysis and recommendations

### 4. Wiki Team
**Lead:** wiki-consistency-checker
**Purpose:** Quality assurance

## Principles Applied

| Principle | Implementation |
|-----------|-------------|
| **One root** | master-orchestrator only |
| **Max depth 3** | orchestrator → team → specialist |
| **Least privilege** | Each agent has minimal tools |
| **One job** | Each agent specializes |
| **Team memory** | Shared files in .opencode/data/ |
| **Controlled self-improvement** | Agent changes go through `.agent-learning/` proposals and reviews |

## Memory Architecture

| Tier | Scope | Agent |
|------|-------|-------|
| Short-term | Current conversation | All |
| Long-term | Personal patterns | Typing agents |
| Team | Shared knowledge | Team leads |

## Workflows

### User Flow: "What's my military role?"

```
1. User → master-orchestrator
2. Orchestrator → (route to typing team)
3. Typing team → get all 3 types
4. Types → military-specialty-advisor
5. Advisor → recommendation
```

### Update Flow: "Update military roles"

```
1. User → master-orchestrator  
2. Orchestrator → military-roles-researcher
3. Researcher → web search → updates data
4. Notify military-specialty-advisor
```

### Quality Flow: "Check wiki"

```
1. Cron/Manual → master-orchestrator
2. Orchestrator → wiki-consistency-checker
3. Checker → scan → report issues
```

### Agent Improvement Flow: "Improve our agents"

```
1. User/audit → master-orchestrator
2. Orchestrator → agent-improvement-steward
3. Steward → learning log + proposal in .agent-learning/
4. Relevant specialist reviewers → approve/request changes
5. Human approval or explicit implementation request → patch agent instructions
```

## Naming Conventions

| Pattern | Example |
|---------|--------|
| Role noun | researcher, typer, advisor |
| System prefix | military-, wiki-, philosophy- |
| Color per team | Unique per agent |
| Governance suffix | steward for meta-governance agents |

## Tool Allocation

| Tier | Tools |
|------|-------|
| Orchestrator | Full (routes) |
| Team leads | read + tool_use |
| Specialists | Minimal (job only) |

## Future Expansion

Reserved slots for:
- Date/socionics matching system
- Content generation team
- External API integrations

---

Last updated: 2026-04-25
