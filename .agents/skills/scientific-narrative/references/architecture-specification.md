# SNIL architecture specification

## Contents

- Provenance and intentional adaptations
- Design objective
- Twenty-two perspectives, clustered into five roles
- Scorecard and gates
- Final report template

## Provenance and intentional adaptations

This reference adapts three repository records:

- `raw/general/scientific-narrative-intelligence-layer.md` preserves the
  received 22-role architecture and numerical gating proposal;
- `protocols/scientific-narrative-intelligence-layer.md` preserves the
  platform-independent transformation sequence, five BWB inference levels,
  proposed working-memory and hazard rules, and adjacent protocol dependencies;
- Git commit `391ab10207d03bb4350472546efe75a646b044ec`, path
  `.agents/skills/scientific-narrative/SKILL.md`, is the immutable
  pre-adaptation runtime entrypoint that names `invoke_subagent`.

The current skill preserves the five runtime clusters and 22 perspectives with
these intentional deviations:

1. Nested `codex exec` and unavailable `invoke_subagent` calls are replaced by
   the collaboration mechanism available to the running Codex instance.
2. The source protocol's `lambda(s) > 0.40` rule is not used as a publication
   gate because its simulated hazard values have not been empirically
   calibrated. Use qualitative `low`/`medium`/`high` risk; label any numbers
   as uncalibrated model estimates.
3. The fixed `4±1` active-concept count is not treated as a deterministic
   threshold because the repository package does not provide evidence for that
   exact writing rule. Review working-memory and prerequisite pressure
   qualitatively and identify the concrete overload.
4. `protocols/research-bridge-builder.md` and
   `protocols/evidence-packager.md` are optional adjacent protocols for
   researcher outreach or evidence packaging. Read them only when that work is
   in scope; an ordinary SNIL audit does not require them.
5. The five-level BWB inference distinction is retained explicitly below.

## Design objective

Optimize simultaneously for:

1. scientific and epistemic correctness;
2. comprehension and durable mental models;
3. curiosity through genuine information gaps;
4. narrative momentum and reader retention.

The narrative rule is: each next thought should answer a question that has just
arisen for the reader or create a more useful question. This is a heuristic, not
a license to manufacture suspense.

## Twenty-two perspectives, clustered into five roles

### `snil_architect`

Combines:

1. Scientific Narrative Architect — cognitive route and concept graph.
2. Curiosity Architect — useful information gaps, anomalies, and paradoxes.
3. Counterintuitive Insight Agent — tests productive violations of naive models.
4. Socratic Question Agent — predicts the reader's next honest question.
5. Scientific Narrative Director — retained by the orchestrator for final
   arbitration rather than delegated as an independent vote.

Deliver:

- prerequisite map;
- proposed question-and-answer route;
- sections that arrive too early or too late;
- one concise narrative blueprint;
- risks introduced by reordering.

### `snil_explainer`

Combines:

1. Explanation Engineer.
2. Mental Model Agent.
3. Analogy and Thought Experiment Agent.
4. Concrete Example Agent.

For each hard concept, test this ladder:

1. intuition in ordinary language;
2. observable example;
3. causal or structural model, explicitly labeled;
4. technical term after the reader has a referent;
5. boundaries, counterexample, and what does not follow.

Deliver the concepts that fail the ladder, a concrete repair for each, and the
failure boundary of every proposed analogy.

### `snil_editor`

Combines:

1. Cognitive Load Agent — working-memory and prerequisite pressure.
2. Pacing Agent — cadence and tension-release balance.
3. Voice Agent — calm, respectful intellectual dialogue without imitation of a
   living or named author's exact style.
4. Compression Agent — remove repetition without deleting transitions,
   examples, qualifications, or safety limits.

Deliver section-specific notes on jargon, sentence load, transitions, pacing,
repetition, generic phrasing, and suggested cuts or bridges.

### `snil_epistemic_auditor`

Combines:

1. Epistemic Integrity Agent — may veto unsupported certainty.
2. Evidence Agent — checks citation quality and support, preferring syntheses
   and primary sources appropriate to the claim.
3. Skeptic Agent — rival explanations, circularity, and counterexamples.

Deliver a claim ledger with location, claim, current status, evidence checked,
problem, and minimal safe correction. Distinguish at least:

- observed or directly documented;
- source-attributed;
- project definition;
- research hypothesis;
- speculative extension;
- unsupported or contradicted.

When BWB typological claims are present, also keep this inference ladder
separate:

1. whole person;
2. observable trace or pattern;
3. typological-model hypothesis;
4. latent-process hypothesis;
5. natural-predisposition hypothesis.

Movement from one level to the next requires separate support; no type label or
observable pattern proves the later levels.

Do not treat the wording or metrics in this skill package as evidence about the
quality of another document.

### `snil_reader_panel`

Combines one retention meta-perspective and five reader personas:

1. Reader Retention Critic.
2. Curious Generalist.
3. Technical Reader.
4. Skeptical Reader.
5. Impatient Reader.
6. Domain Expert.

Each persona reports:

- where interest first rises;
- the first point of confusion;
- the first plausible exit point and why;
- what restores attention;
- the one change most likely to help that persona.

Aggregate these into a section-level drop-off map using qualitative risk
(`low`, `medium`, `high`). Numerical completion forecasts are optional and,
if used, must be visibly labeled as uncalibrated model estimates rather than
real analytics.

## Scorecard and gates

Score 0–10, with one or two evidence sentences for each:

- scientific accuracy;
- epistemic calibration;
- clarity;
- conceptual understanding;
- curiosity;
- narrative momentum;
- cognitive-load management;
- voice and human readability.

The director may report an overall Scientific Popularization Score (SPS) as a
transparent editorial judgment. Apply these maximums after scoring:

- accuracy under 8.0 -> SPS no higher than 60;
- epistemic calibration under 8.0 -> SPS no higher than 65;
- clarity under 7.0 -> SPS no higher than 70;
- conceptual understanding under 7.0 -> SPS no higher than 70.

Use `SPS >= 85` only as an internal publication-candidate threshold. It is not
a validated scale and must not be presented as observed reader performance.

## Final report template

1. **Verdict** — audience, mode, and publication status.
2. **Keep** — two to five strengths that should survive revision.
3. **Priority findings** — location, problem, reader impact, safe repair.
4. **Drop-off map** — section, affected personas, risk, reason, recovery.
5. **Epistemic audit** — unsupported leaps and required qualifications.
6. **Scorecard** — dimension, score, evidence; then gated SPS if useful.
7. **Revision plan** — smallest coherent set of changes in dependency order.
8. **Limits** — missing evidence, audience assumptions, and which findings are
   simulated rather than measured.
