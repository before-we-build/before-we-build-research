---
title: Integrate Socionics Reality-Modeling Ontology into Agent Instructions
type: agent-improvement-proposal
created: 2026-08-30
updated: 2026-08-30
status: approved
risk: moderate
target_agents: [socionics-researcher, socionics-intertype-relations-expert, typology-test-evaluation-expert, master-orchestrator, research-orchestrator]
required_reviewers: [human-project-owner, source-provenance-auditor, psychometrics-methodologist, empirical-claims-caveats-reviewer]
sources: [user-approved-socionics-reality-modeling-plan-2026-08-30, AGENTS.md, raw/socionics/augustinaviciute-information-metabolism-provenance.md]
---

# Agent Improvement Proposal: Socionics reality-modeling ontology

## 1. Target agents

- `.opencode/agents/socionics-researcher.md`
- `.opencode/agents/socionics-intertype-relations-expert.md`
- `.opencode/agents/typology-test-evaluation-expert.md`
- `.opencode/agents/master-orchestrator.md`
- `.opencode/agents/research-orchestrator.md`

## 2. Observed failure or opportunity

The agents identify Socionics with “information modeling” but do not define
what is modeled, distinguish aspect content from aspect operation, or separate
the operation from its Model A position. This permits theme-only typing and
ability-like interpretations of position labels.

## 3. Approved instruction change

- Treat each Socionics aspect as a BWB hypothesis about a class of distinctions
  in one shared reality plus an operation that selects, compresses, organizes,
  infers from, and updates a partial representation.
- Keep the source axes attributed to classical sources and the eight operation
  definitions explicitly revisable BWB reconstructions.
- Separate aspect content, aspect operation, Model A position mode, and
  observable trace.
- Require evidence for aspect operations and position modes separately before
  ranking Model A hypotheses.
- Forbid ability scores, innateness scores, theme-only typing, neural-module
  claims, and relationship-fate conclusions.
- Require rival explanations including learning, role, culture, health, stress,
  state, and context.

## 4. Risk assessment

- Risk level: `moderate`
- Main risk: presenting a useful reconstruction as historical doctrine or
  established cognitive science.
- Overclaiming risk is reduced by explicit attribution and falsifiability.
- Specialist routing remains required for provenance, psychometrics,
  statistics, and empirical caveat review.

## 5. Acceptance criteria

- [x] Source claims and BWB reconstruction are visibly separated.
- [x] Aspect operation and position mode are not collapsed.
- [x] No position is interpreted as an ability or deficit by itself.
- [x] Test guidance requires selection, compression, inference, and updating.
- [x] Type and relation outputs remain provisional and context-sensitive.
- [x] Natural origin remains an unestablished further hypothesis.

## 6. Rollback

Revert the instruction paragraphs and retain the prior generic “information
modeling” formula. Do not remove existing caveats about non-determinism,
innateness, or high-stakes use.
