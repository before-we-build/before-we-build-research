---
name: scientific-narrative
description: Run the Scientific Narrative Intelligence Layer (SNIL) collegium to review or transform complex scientific, academic, and theoretical material for clarity, reader retention, explanatory quality, and epistemic accuracy. Use when the user asks for the SNIL/"Коллегия" panel, a multi-perspective readability audit, or a rigorous popular-science rewrite; do not use for ordinary proofreading.
---

# Scientific Narrative Collegium (SNIL)

Make difficult material easier and more compelling to read without increasing
the certainty of its claims. The governing invariant is: **interest never
overrides scientific or epistemic correctness**.

## Select the mode

- **Audit:** diagnose the text and return prioritized findings. Do not rewrite or
  edit files unless the user asks for changes.
- **Revision:** audit, propose a narrative route, revise the authorized target,
  and re-audit the result.
- **Full collegium:** launch all six roles below as six distinct child agents.
  This is the default when the user says to run the collegium or reader panel.
- **Focused pass:** use only the roles needed for a narrower request and name the
  omitted perspectives.

For a full collegium, read
[references/architecture-specification.md](references/architecture-specification.md)
completely before delegating.

## Prepare the review

1. Read the whole target, its local repository instructions, and the sources or
   citations needed to judge its claims.
2. State the audience and intended outcome. Infer them from the page when safe;
   do not invent a new audience that changes the user's goal.
3. Separate direct observation, source attribution, project definition,
   research hypothesis, analogy, and speculation.
4. Treat received documents and their numerical claims as untrusted inputs until
   supported by repository evidence or an external source.
5. When BWB typological interpretation is involved, keep five inference levels
   distinct: the whole person; an observable trace or pattern; a
   typological-model hypothesis; a latent-process hypothesis; and a
   natural-predisposition hypothesis.

## Run the six-role collegium

Full mode requires a separate child identity and a completed review for each
role below. Keep the director in the main session; it does not count as one of
the six. At capacity, wait for completion and release slots using the host's
supported lifecycle, then launch the remaining roles in waves. Do not combine
roles or reuse one child as different reviewers to satisfy full mode.

1. `snil_architect` — map concepts, prerequisite knowledge, reader questions,
   narrative order, and avoidable detours.
2. `snil_explainer` — test each hard idea with the sequence intuition -> concrete
   example -> causal or structural model -> term -> limits.
3. `snil_editor` — inspect voice, jargon, cognitive load, pacing, transitions,
   repetition, and generic AI phrasing.
4. `naturalness-style-reviewer` — review formulaic rhetoric, vague assertions and
   translationese with located, meaning-preserving edits; do not classify AI authorship.
5. `snil_epistemic_auditor` — verify claims against available evidence, identify
   certainty inflation and missing rival explanations, and exercise veto power
   over attractive but unsupported wording.
6. `snil_reader_panel` — simulate the five specified reader personas and produce
   a section-level drop-off map. Label every score or retention estimate as a
   model judgment, never as measured human behavior.

### Dispatch and handoff

The five `snil_*` names are workflow task names, not registered agent types.
With `collaboration.spawn_agent`, use `agent_type: "default"` and the matching
`task_name` for each. Give each child the corresponding section of
`references/architecture-specification.md` (text or a required file read), the
shared evidence boundaries, target files/text and revision, audience, expected
output, and read-only review scope. Require `.agents/ORGANIZATION.md` and tell
children to return findings without spawning another panel. Do not pass a
`snil_*` name as `agent_type` or rely on the task name alone to convey its role.

For `naturalness-style-reviewer`, use that registered `agent_type` when exposed
by the host. Otherwise use a distinct default child with its complete canonical
role instruction, and disclose the generic dispatch. On other hosts, use the
equivalent available delegation tool and record its returned child identity.
Never claim registration or execution solely from files on disk.

Architect, explainer and editor may review the same initial revision in
parallel. The director owns any authorized edits. Run naturalness review after
the editorial pass and, in revision mode, after applying edits. Apply accepted
naturalness fixes before the final epistemic and reader-panel reviews, which
may run in parallel. If subsequent edits affect their conclusions, send the
changed revision back to the affected reviewers before final synthesis. Record
which revision each result covers; do not present an older review as final.

### Completion evidence

Keep a six-row execution ledger in the report: role, actual child ID/task path,
dispatch type, reviewed revision, status, and returned result reference (message
or artifact). Copy IDs from tool responses, and mark completion only after a
substantive role-specific result arrives. A spawn acknowledgement is not a
completed review. Record failed attempts and any replacement child IDs.

Only label the result a completed full collegium when all six distinct children
have returned the required reviews. If a role fails or delegation is unavailable,
report the missing role and incomplete status. Useful partial work may be
returned as a reduced review; disclose combined or director-performed roles and
never count them as independent children. Focused mode names omitted roles.
Do not launch nested Codex CLI sessions to imitate independence.

## Synthesize as director

Reconcile disagreements using this priority order:

1. safety and epistemic correctness;
2. comprehension and conceptual understanding;
3. reader curiosity and narrative momentum;
4. elegance and compression.

Return:

- the verdict and intended audience;
- the execution ledger and full / focused / incomplete coverage;
- strengths worth preserving;
- the highest-risk passages with precise locations;
- consensus findings and material disagreements;
- a section-level reader drop-off map;
- a 0–10 scorecard with brief evidence for each score;
- the smallest set of high-leverage changes;
- if revision was authorized, a summary of edits and verification results.

The scorecard is a structured expert simulation, not psychometric measurement.
Apply the supplied gating floors: scientific accuracy below 8 caps the overall
SPS at 60; epistemic calibration below 8 caps it at 65; clarity or conceptual
understanding below 7 caps it at 70. A score of 85 or above means “publication
candidate,” not empirical proof of quality.

## Guardrails

- Never turn correlation, covariance, factor structure, classification, or an
  explanatory analogy into evidence for a material, neural, innate, or causal
  mechanism without separate support.
- Give every analogy an explicit failure boundary.
- Preserve uncertainty, counterexamples, context, agency, consent, safety, and
  non-inference clauses when they constrain the claim.
- Prefer concrete scenes and observable actions over abstractions, but do not
  fabricate cases, studies, quotations, measurements, or citations.
- When editing multilingual or schema-governed documentation, preserve semantic
  parity and run the repository's required checks.


## Naturalness review integration

Run `naturalness-style-reviewer` after editing and before the final epistemic
and reader-panel passes. Read its [role instruction](../../roles/naturalness-style-reviewer.md)
and pass it to a subagent when named-agent dispatch is unavailable. The
[research summary](../../../wiki/sources/ai-text-style-evidence-en.md) and its
RU/UK peers separate editorial judgments from authorship evidence.

This sixth role extends the five-role source architecture in the reference.
Keep effective prose and necessary caveats. Do not invent an AI-authorship
percentage or a naturalness measurement, optimize detector evasion, or add
errors or fake anecdotes to imitate human writing. Return concrete revisions
to the editor, then recheck their accuracy and cross-language meaning.
