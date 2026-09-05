# Scientific Narrative Runtime Adaptation

Date: 2026-09-05
Actor: Codex primary agent
Type: controlled skill correction

## Observation

The user explicitly requested installation and execution of the received SNIL
collegium and later requested that the work be committed and pushed. During the
pre-commit review, the active repository skill at
`.agents/skills/scientific-narrative/SKILL.md` was found to prescribe
`invoke_subagent` and a nested `codex exec` audit even though those are not the
available collaboration mechanism in this runtime. The entrypoint also did not
route to enough detail to reproduce its five-role review and scoring gates.

## Evidence

- Active skill before adaptation: commit
  `391ab10207d03bb4350472546efe75a646b044ec`, path
  `.agents/skills/scientific-narrative/SKILL.md`
- Preserved architecture:
  `raw/general/scientific-narrative-intelligence-layer.md`
- Platform-independent operational protocol:
  `protocols/scientific-narrative-intelligence-layer.md`
- First governance review:
  `.agent-learning/reviews/2026-09-05-scientific-narrative-runtime-adaptation-review.md`

## Proposed correction

Keep the same SNIL purpose and five composite roles while:

- using the available collaboration/subagent mechanism;
- defining audit, revision, full-collegium, and focused modes;
- routing detailed role definitions to one supporting reference;
- labeling reader-retention estimates and scorecards as model judgments;
- retaining the five-level BWB inference distinction;
- preserving epistemic vetoes, uncertainty, safety, and multilingual checks.

## Safety notes

- This is a runtime and documentation correction, not a new compatibility model.
- It adds no empirical, psychometric, clinical, theological, or typological
  claim.
- It strengthens the prohibition on certainty inflation and fabricated evidence.
- Activation is covered by the user's explicit request to install and run the
  collegium.
- The unvalidated numerical hazard threshold and fixed working-memory count are
  retained as provenance notes, not executable publication gates.

## Verification

Require structural skill validation, independent behavioral review, the
repository agent linter, the scientific-narrative strict check, and the complete
wiki CI suite before push.

All checks passed after application: 74 unit tests, the strict wiki contract,
section synchronization, wikilinks, claim-language audit, generated artifacts,
agent lint, the scientific-narrative gate, structural skill validation, and
whitespace checks. The scientific-narrative gate reported three non-blocking
warnings in the preserved source exposition and zero errors.
