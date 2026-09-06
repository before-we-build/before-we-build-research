# Agent pre-commit review — 2026-09-06

User authorized commit/push after comparison with internet best practices and CI monitoring.
Independent read-only subagent `adapter_review` found a read-role/write-instruction
mismatch in wiki-consistency-checker and ambiguous implementation wording in
data-pipeline-engineer. Main agent also found non-object JSON error handling and
frontmatter delimiter parsing weaknesses. No substantive domain claims changed.

Additional pre-commit finding: the staged-Markdown readability hook interpreted
prohibited examples as assertions in five roles. Each affected line now carries
its own explicit prohibition; domain caveats and the checker remain intact.
Regenerated both adapters from the revised canonical role text.
