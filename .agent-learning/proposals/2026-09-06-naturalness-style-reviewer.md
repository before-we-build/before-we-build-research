---
title: Naturalness and style review for the editorial collegium
type: agent-improvement-proposal
created: 2026-09-06
updated: 2026-09-06
status: applied
risk: moderate
target_agents: [naturalness-style-reviewer, master-orchestrator]
required_reviewers: [source-provenance-auditor, empirical-claims-caveats-reviewer]
sources: [raw/general/2026-09-06-ai-text-style-source-register.md, reports/readability-collegium-2026-09-06.md]
---

# Agent Improvement Proposal: naturalness and style review

## 1. Target agent(s)

Create .opencode/agents/naturalness-style-reviewer.md; update narrowly scoped
routing in master-orchestrator, .opencode/ORGANIZATION.md and the existing
scientific-narrative skill. Add synchronized research summaries to the wiki.

## 2. Observed failure or opportunity

Readable-looking prose can still be generic, repetitive, inflated or awkwardly
translated. The user requested a dedicated specialist after internet research.

## 3. Evidence

The dated source intake register records primary research abstracts and the
NIST technical report sections consulted. The previous editorial audit found
that static readability scores did not identify several dense introductions.

## 4. Proposed instruction change

Review observable editorial problems with exact passages and reasons, then
suggest the smallest effective revision. Separate authorship uncertainty from
style quality. Preserve BWB caveats and language peers. Never manufacture a
probability of AI authorship or optimize prose to evade a detector. Use a
read-only role by default, with fixes returned to the editor.

## 5. Risk assessment

Moderate: careless instructions could introduce false authorship accusations,
English-only stereotypes, or removal of necessary scientific qualifications.
No medical, legal, personality, compatibility or plagiarism scoring is added.
Do not bypass provenance or empirical-claims reviewers.

## 6. Required reviewers

Independent agent review covering provenance and empirical caveats, followed
by a bounded behavior exercise. Reviewer decisions are stored under reviews/.
Human authorization: explicit current user request to research and add the role.

## 7. Patch sketch

Add one explanation-team manifest and register it in the existing master and
organization listings. Add a sixth SNIL role after editing and before the final
epistemic audit and reader panel; no CLI or detector dependency is introduced.

## 8. Acceptance criteria

- Narrow role and traceable evidence; no deterministic authorship or numeric score.
- Concrete edits preserve meaning, qualifiers, safety and EN/RU/UK parity.
- Counterexamples can pass unchanged; no compulsory slang, errors or fake stories.
- Source summaries pass independent semantic review; manifests and skill validate.
- Realistic behavior exercise distinguishes quality review from origin claims.

## 9. Rollback note

Remove only this new role, its routing and sixth-role skill additions. Retain
research records and review history; do not revert unrelated editorial work.


# Implementation record

The explicit user request authorized implementation. The independent provenance
and caveats review approved the instruction; its two wiki corrections were
applied and all three source summaries activated at reviewed version 1.
The separate behavior exercise is recorded in
.agent-learning/reviews/2026-09-06-naturalness-style-behavior.md.
The new role is registered in the master routing, organization and six-role
scientific-narrative skill. No external detector or production publication ran.
