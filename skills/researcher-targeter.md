# SKILL: researcher-targeter

## Purpose

Find and rank researchers, labs, and adjacent organizations most worth contacting.

## When to Use

- You need a target list for outreach
- You want to avoid generic cold emails
- You need to separate high-fit academic contacts from low-fit noise

## What This Skill Produces

- Ranked outreach list
- One-line overlap hypothesis for each target
- Suggested first ask per target

## Selection Criteria

Score each target on:
1. **Topical overlap** — persona agents, social simulation, relationship science, psychometrics, evaluation
2. **Method overlap** — LLM agents, simulation, longitudinal validation, HCI systems
3. **Practical overlap** — would they actually care about this problem
4. **Reachability** — active lab, recent papers, public contact surface
5. **Collaboration fit** — advisor, method reviewer, coauthor, pilot partner, product-intelligence source

## Output Format

```yaml
target:
  name: "..."
  type: "researcher | lab | startup"
  fit: "high | medium | low"
  why_now: "..."
  overlap: "..."
  first_ask: "..."
  risk: "..."
```

## Rules

- Prefer people with a clear method overlap over famous but vague names
- Do not mix academic, startup, and community targets into one undifferentiated list
- Always define the role: reviewer, collaborator, advisor, pilot partner, signal source
- A short high-quality list beats a long noisy list

## Dependencies

- `research-bridge-builder`
- `collaboration-ask-designer`

## Related Skills

- `outreach-personalizer`
- `objection-handler`
