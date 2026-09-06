---
title: Align reviewer instructions with read access
created: 2026-09-06
updated: 2026-09-06
status: applied
risk: moderate
target_agents: [wiki-consistency-checker, data-pipeline-engineer]
required_reviewers: []
sources: [.agents/ORGANIZATION.md]
---

## 1. Targets

Canonical wiki-consistency-checker and data-pipeline-engineer; generated adapters;
configuration loader tests and pre-commit review record.

## 2. Observed failure

Wiki reviewer demands persistent writes and bash while its adapter denies both.
Pipeline designer ambiguously demands creation of datasets despite read access.

## 3. Evidence

Independent read-only `adapter_review` findings, 2026-09-06. See matching review.

## 4. Proposed change

Use available read/search tools; return located findings, report text and proposed
paths to the authorized writer. Treat age as a review cue, not proof of staleness.
Clarify pipeline output as design/plan with persistence by the authorized owner.

## 5. Risk

Moderate organizational fix; preserves independent review, domain caveats,
consent, raw-data immutability, and confirmation requirements for external action.

## 6. Review

`adapter_review` recommended these changes. User explicitly authorized fixes before
commit and push. No clinical/theological/psychometric/statistical claim is changed.

## 7. Patch sketch

Replace forced shell snippets and Store issues imperative with read/search and
owner-write handoff. Add design-only implementation boundary to pipeline role.

## 8. Acceptance

Core/adapters synchronized; tests and strict CI checks pass; role outputs remain
usable without requiring prohibited writes. No permission expansion.

## 9. Rollback

Revert these two role refinements and regenerate; retain the audit trail.
