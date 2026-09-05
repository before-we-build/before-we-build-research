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
- **Full collegium:** use all five composite roles below. This is the default when
  the user says to run the collegium or reader panel.
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

## Run the five-role collegium

Use independent subagents when collaboration tools are available. Start the
roles in parallel when useful; if capacity is limited, combine adjacent roles or
run them in waves while keeping their judgments distinguishable.

1. `snil_architect` — map concepts, prerequisite knowledge, reader questions,
   narrative order, and avoidable detours.
2. `snil_explainer` — test each hard idea with the sequence intuition -> concrete
   example -> causal or structural model -> term -> limits.
3. `snil_editor` — inspect voice, jargon, cognitive load, pacing, transitions,
   repetition, and generic AI phrasing.
4. `snil_epistemic_auditor` — verify claims against available evidence, identify
   certainty inflation and missing rival explanations, and exercise veto power
   over attractive but unsupported wording.
5. `snil_reader_panel` — simulate the five specified reader personas and produce
   a section-level drop-off map. Label every score or retention estimate as a
   model judgment, never as measured human behavior.

Do not launch a nested Codex CLI process merely to imitate independence. Use the
current collaboration mechanism or clearly disclose when a role was performed
by the orchestrator.

## Synthesize as director

Reconcile disagreements using this priority order:

1. safety and epistemic correctness;
2. comprehension and conceptual understanding;
3. reader curiosity and narrative momentum;
4. elegance and compression.

Return:

- the verdict and intended audience;
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
