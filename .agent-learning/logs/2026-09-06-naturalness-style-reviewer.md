---
title: Add a naturalness and style reviewer
type: agent-learning-log
created: 2026-09-06
updated: 2026-09-06
source: user-request
status: applied
---

# Observation

The user explicitly requested internet research followed by a new editorial
collegium specialist for text that sounds AI-generated. The previous local
readability audit found that a high static score can coexist with opaque prose.
See reports/readability-collegium-2026-09-06.md.

# Decision to review

Propose naturalness-style-reviewer: an editorial agent, not an authorship
classifier. Ground detection limits in the source intake register and keep
practical style criteria explicitly separate from validated detection features.
Use the controlled proposal → independent review → instruction patch loop.
The user's explicit implementation request supplies authorization to add and
route the role; it does not authorize external publication or detector uploads.


# Implementation record

The explicit user request authorized implementation. The independent provenance
and caveats review approved the instruction; its two wiki corrections were
applied and all three source summaries activated at reviewed version 1.
The separate behavior exercise is recorded in
.agent-learning/reviews/2026-09-06-naturalness-style-behavior.md.
The new role is registered in the master routing, organization and six-role
scientific-narrative skill. No external detector or production publication ran.
