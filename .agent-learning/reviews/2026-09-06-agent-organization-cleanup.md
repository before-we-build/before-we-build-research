# Organization cleanup review — 2026-09-06

Proposal: ../proposals/2026-09-06-agent-organization-cleanup.md

Reviewer: implementing assistant (self-review; no independent panel).
Decision: approved for bounded organizational implementation under the user's request.

- Retains all domain specialists, methods, evidence requirements and caveats.
- Separates source-doctrine coordination from empirical pipeline coordination.
- Keeps author and reviewer responsibilities distinct; an organizational parent
  is not scientific authority and does not confer runtime permissions.
- Preserves all names to avoid breaking protocol and skill references.
- Does not migrate permissions or models without runtime/version evidence.
- Does not classify inactivity from file age or fabricate usage statistics.

Post-change test evidence is recorded in the audit report. Runtime verification
remains unavailable because OpenCode is not installed in this environment.

Verification complete: 93 unit tests passed; all eight required repository checks
passed after regenerating three inventory line references. CI readability checks
passed (three existing source-text warnings); final whitespace check passed.
