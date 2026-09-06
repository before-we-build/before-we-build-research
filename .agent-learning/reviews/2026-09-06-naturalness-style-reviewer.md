---
title: Naturalness style reviewer — provenance and caveats review
type: agent-improvement-review
created: 2026-09-06
updated: 2026-09-06
status: approved
---

# Naturalness style reviewer review

## Proposal metadata

- Proposal: `.agent-learning/proposals/2026-09-06-naturalness-style-reviewer.md`.
- Agent draft reviewed: `/tmp/naturalness-style-reviewer.md`.
- Reviewer: Codex agent `/root/epistemic_audit`, independently delegated to review provenance and empirical caveats. This is one agent review covering two concerns, not two human expert reviews.
- Date: 2026-09-06.
- Decision: **approved** for the proposed agent instructions. Wiki semantic approval requires the two small corrections recorded below.

## Evidence reviewed

Read the proposal, agent draft, source intake register, all three `ai-text-style-evidence` language peers, review template, and relevant organization entries. Independently opened the primary publication pages and checked the attributed claims:

- [RAID, ACL 2024](https://aclanthology.org/2024.acl-long.674/): the author abstract supports twelve tested detectors and performance sensitivity to changed generation conditions and attacks. The summary does not generalize this to all detectors in all settings.
- [Liang et al., author version](https://arxiv.org/abs/2304.02819): the abstract supports false identification in the studied non-native English writing samples. No RU/UK false-positive rate is inferred.
- [Miletić and Falk, LREC 2026](https://aclanthology.org/2026.lrec-1.142/): the abstract supports the reported lexical differences and the twenty-expert reader pilot. The wiki separates that pilot from universal reader preferences.
- [NIST AI 100-4](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-4.pdf): read the relevant text in sections 3.2.2.4 and 4.2–4.2.2. The report supports context-sensitive evaluation, language limitations, short-text difficulties, and attention to false positives.

This review checked abstracts and specified report sections, not every paper in full. It did not reproduce experiments or run an authorship detector. The source register distinguishes intake metadata from empirical data and does not present prior agent output as primary evidence.

## Safety and governance checks

- [x] The role reviews located passages and their effect on reading; it does not classify authorship or fabricate an AI percentage.
- [x] It rejects detector evasion, deliberate errors, false memories, fake quotations, and invented supporting detail.
- [x] It preserves disclosures, sources, uncertainty, scientific qualifiers, and necessary repeated terminology.
- [x] It preserves BWB process hypotheses, safety/consent boundaries, universal versus worldview scope, and synchronized EN/RU/UK meanings.
- [x] It is read-only by default and returns suggestions to the editor; unresolved factual issues route to the existing provenance and caveats roles.
- [x] Its reporting line is the master orchestrator and its editorial scope fits the explanation team.
- [x] Its review rubric is labeled a project practice, not a scientifically validated scale. No statistical scoring change is introduced.
- [x] Its role is not represented as a human expert; a simulated reader panel is not represented as an empirical reader study.

## Required wiki corrections

1. In the English peer, replace “an editorial defect is not evidence of AI authorship” with “an editorial defect does not establish AI authorship.” This matches the Russian and Ukrainian claim strength and avoids confusing lack of proof with absence of any potentially informative feature.
2. In all three NIST bullets, include section 4.2 in the locator, for example `§§3.2.2.4, 4.2–4.2.2`. Matching evaluation conditions is discussed in the section 4.2 introduction, not only 4.2.2.

These corrections were sent to the implementing editor. Once applied, the triad is approved for `reviewed_semantic_version: 1` and `document_status: active`. The remaining content, claim IDs, caveats, and section topology are semantically aligned across EN/RU/UK.

## Follow-up checks

The orchestrator remains responsible for the bounded behavior exercise, manifest/skill validation, final routing changes, strict wiki checks, and generated indexes. This approval evaluates the proposed instructions and source summary; it does not claim those integration checks have already passed or that real readers benefit from the new role.
