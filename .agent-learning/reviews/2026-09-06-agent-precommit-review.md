# Independent pre-commit review — 2026-09-06

Reviewer: actual read-only subagent `adapter_review`.
Decision: no proven generator/configuration blocker; correct role handoff mismatches.

- Wiki reviewer demands persistent reports and shell examples despite read-only profile.
  Recommended returning report text and intended paths to the authorized writer,
  using available read/search tools.
- Pipeline designer's dataset/exclusion-log creation wording should describe the
  proposed pipeline; the owner performs authorized persistence.
- Malformed JSON container types should return explicit validation errors.

Positive review findings: one canonical registry, generated adapters, bounded
ownership/delegation, separate model settings, duplicate-key/drift checks,
no deletion of extra outputs and protection of unowned files/symlink destinations.
This review did not claim runtime discovery or execution of all named agents.

Implementing agent applied the recommended handoff fixes and parser hardening.
Post-fix validation and primary-source comparison: reports/agent-best-practices-review-2026-09-06.md.

Independent follow-up: adapter_review rechecked the applied fixes and reported
no remaining release blocker. Final full unittest run: 110 tests passed.

Additional pre-commit finding: the staged-Markdown readability hook interpreted
prohibited examples as assertions in five roles. Each affected line now carries
its own explicit prohibition; domain caveats and the checker remain intact.
Regenerated both adapters from the revised canonical role text.
