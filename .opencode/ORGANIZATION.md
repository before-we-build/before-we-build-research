# Agent Organization Structure

Based on best practices from McKinsey, ClawPort, and enterprise deployments (2025-2026).

## Hierarchy (3 Levels)

```
master-orchestrator (gold) ⚜
├── Research Team
│   ├── typology-researcher (purple)
│   ├── socionics-intertype-relations-expert (blue)
│   ├── psychosophy-intertype-relations-expert (green)
│   ├── temporistics-intertype-relations-expert (cyan)
│   ├── sociology-researcher (brown)
│   ├── neuroscience-researcher (indigo)
│   ├── christian-theology-researcher (sienna)
│   └── military-roles-researcher (darkgreen)
├── Typing Team  
│   ├── psychosophy-typer (green)
│   ├── socionics-typer (blue)
│   └── temporistics-typer (cyan)
├── Analysis Team
│   ├── compatibility-calculator (red)
│   ├── relation-advisor (orange)
│   ├── interaction-simulator (yellow)
│   ├── military-specialty-advisor (olive)
│   └── civilian-career-advisor (steelblue)
├── Wiki Team
│   ├── philosopher-logician (white)
│   └── wiki-consistency-checker (magenta)
└── [Reserved for future]
```

## Team Definitions

### 1. Research Team
**Lead:** typology-researcher
**Purpose:** Finding and validating information, including typological, sociological, neuroscience, and Christian-theological context. Intertype-relation experts provide mechanism-level audits of relation names and processes within their own typology.
**Crons:** military-roles-researcher (weekly)

### 2. Typing Team  
**Lead:** (any - user chooses)
**Purpose:** Typological type determination
**Agents:** 3 typing specialists

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

## Naming Conventions

| Pattern | Example |
|---------|--------|
| Role noun | researcher, typer, advisor |
| System prefix | military-, wiki-, philosophy- |
| Color per team | Unique per agent |

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

Last updated: 2026-04-24
