---
title: Audit-Derived Agent Hardening Batch
type: agent-improvement-proposal
created: 2026-04-25
updated: 2026-04-25
status: proposed
risk: moderate
target_agents:
  - psychosophy-researcher
  - socionics-researcher
  - temporistics-researcher
  - compatibility-calculator
  - military-specialty-advisor
  - civilian-career-advisor
  - source-provenance-auditor
  - empirical-claims-caveats-reviewer
required_reviewers:
  - empirical-claims-caveats-reviewer
  - source-provenance-auditor
  - psychometrics-methodologist
  - statistical-validation-agent
sources:
  - repo audit results from 2026-04-25 conversation
  - AGENTS.md
---

# Agent Improvement Proposal: Audit-Derived Agent Hardening Batch

## 1. Target agent(s)

- `.opencode/agents/psychosophy-researcher.md`
- `.opencode/agents/socionics-researcher.md`
- `.opencode/agents/temporistics-researcher.md`
- `.opencode/agents/compatibility-calculator.md`
- `.opencode/agents/military-specialty-advisor.md`
- `.opencode/agents/civilian-career-advisor.md`
- `.opencode/agents/source-provenance-auditor.md`
- `.opencode/agents/empirical-claims-caveats-reviewer.md`

## 2. Observed failure or opportunity

The repository audit found repeated patterns that should become agent behavior rules:

- source-backed doctrine is sometimes mixed with PsyCalc reconstruction;
- exact compatibility percentages are used without empirical calibration;
- high-stakes role-fit pages can sound assignment-like;
- Psychosophy, Socionics, and Temporistics naming/source boundaries need stronger enforcement;
- placeholder provenance such as `web research`, agent names, and bare filenames is too weak.

## 3. Evidence

- Wiki consistency audit: stale index, Cognitive Matchmaker framing drift, source-path inconsistency.
- Source provenance audit: placeholder `sources:` entries and mixed claim status.
- Caveat audit: deterministic military/compatibility claims and public-figure/theology overreach.
- System-specific audits: Socionics MBTI leakage; Psychosophy/Temporistics source drift; relation-layer reconstruction boundaries.
- Methodology audits: false precision in compatibility scoring and premature measurement claims.

## 4. Proposed instruction change

Add compact hardening rules to the target agents.

### Psychosophy researcher

```md
## Hard Boundary Rules

- Afanasyev Psychosophy uses Will, Logic, Emotion, and Physics; never describe it with Past/Present/Future/Eternity, which belongs to Temporistics.
- Treat Attitudinal Psyche as a later English adaptation/derivative tradition unless a source justifies direct equivalence.
- Mark accentuations as unofficial/community extensions unless primary evidence says otherwise.
- Distinguish Afanasyev-backed claims from community summaries and PsyCalc operational interpretation.
```

### Socionics researcher

```md
## Hard Boundary Rules

- Prefer `information elements` and `Model A function positions`; avoid uncaveated `cognitive functions` because it invites MBTI/Jung confusion.
- Treat MBTI codes as approximate external analogues, not equivalents.
- Mark relation names, Reinin signs, plus/minus signs, and subtype models as school-dependent where relevant.
- Preserve asymmetric direction for supervision/order/revision-style relations.
```

### Temporistics researcher

```md
## Hard Boundary Rules

- Separate source-backed Temporistics from PsyCalc strategic-level reconstruction.
- Treat Temporistics intertype relations as proposed reconstruction unless raw sources explicitly provide them.
- Put compatibility hypotheses on relation pages or label them clearly on entity pages.
- Check canonical alias policy before renaming codes, archetypes, or transliterations.
```

### Compatibility and role-fit agents

```md
## Calibration and Context Rules

- Do not present exact compatibility percentages as measured probabilities unless calibrated against outcome data.
- Prefer bands, uncertainty labels, and conditional language.
- For dating, career, military, or team advice, separate typology hypothesis from social context, skills, institutional feasibility, and uncertainty.
- For military roles, never frame type as assignment guidance; use conditional role-fit hypotheses only.
```

### Wiki governance agents

```md
## Provenance Rules

- Treat `web research`, `project synthesis`, agent names, and bare filenames as insufficient provenance unless normalized to concrete sources.
- Require evidence labels for mixed pages: primary-source, secondary-summary, derived-synthesis, project-hypothesis, speculative, or unverified.
- Flag places where PsyCalc is incorrectly reduced to Cognitive Matchmaker on orientation/theory pages.
```

## 5. Risk assessment

- Risk level: `moderate`
- Why: Changes touch many agents and high-stakes advice surfaces.
- Could this increase overclaiming? `no`, intended to reduce it.
- Could this bypass specialist delegation? `no`, intended to preserve it.
- Could this affect high-stakes advice? `yes`, by making it safer and more conditional.

## 6. Required reviewers

- [ ] `empirical-claims-caveats-reviewer`
- [ ] `source-provenance-auditor`
- [ ] `psychometrics-methodologist`
- [ ] `statistical-validation-agent`
- [ ] domain specialists for Socionics/Psychosophy/Temporistics if wording is expanded beyond the compact rules above
- [ ] human/project owner

## 7. Patch sketch

Patch each target agent with the relevant section from “Proposed instruction change.” Keep edits compact and avoid long theoretical duplication.

## 8. Acceptance criteria

- [ ] The new rules reduce source drift and overclaiming.
- [ ] They preserve delegation-first routing.
- [ ] They do not introduce new empirical claims.
- [ ] They are short enough not to bloat agent prompts.
- [ ] Future audits can check compliance.

## 9. Rollback note

Revert the added hardening sections from each target agent if they cause excessive refusal, loss of useful synthesis, or conflict with updated repository policy.
