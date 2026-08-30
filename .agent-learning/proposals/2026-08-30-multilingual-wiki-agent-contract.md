---
title: Align Agents and Skills with the Multilingual Evidence Contract
type: agent-improvement-proposal
created: 2026-08-30
updated: 2026-08-30
status: approved
risk: moderate
target_agents: [master-orchestrator, typology-researcher, wiki-contributor, wiki-consistency-checker]
required_reviewers: [human-project-owner, provenance-source-traceability-agent, empirical-claims-caveats-reviewer]
sources: [user-approved-repository-clarity-plan-2026-08-30, AGENTS.md]
---

# Agent Improvement Proposal: Multilingual Wiki and Evidence Contract

## Observed failure

Active instructions could recreate unsuffixed pages, incomplete translations, stale hand-edited indexes, ambiguous source references, and verdict-style cross-system mappings after the repository migration.

## Approved change

- Require complete equal EN/RU/UK groups and current frontmatter.
- Generate, never hand-edit, `index.md`.
- Run strict schema, section, link, claim, inventory, and agent checks.
- Treat MBTI, Socionics, Psychosophy, Temporistics, and Big Five as non-equivalent systems; compare constructs and attributed source claims instead of translating a type code.
- Replace determination and confidence arbitration language with provisional hypotheses, rival explanations, and evidence limits.

## Acceptance criteria

- [x] Wiki agents cannot create a single active locale.
- [x] Research instructions use the generated catalog and append-only log.
- [x] Cross-system output contains no fixed threshold conversion or final verdict.
- [x] Example paths resolve to current suffixed pages.

## Rollback

Do not restore the legacy single-language workflow. Any schema change requires a new migration, tests, owner approval, and an updated generated manifest.
