# Shared agent core and adapters — 2026-09-06

User explicitly requested a shared core with OpenCode and Codex adapters.
The prior cleanup left 53 role instructions authoritative under OpenCode, with
no native Codex agent definitions. Parallel manual copies would drift.

Preserve the current uncommitted cleanup. Extract all current role bodies,
changing only organizational/source-authoring paths and removing the repeated
organization preamble. Migration hashes are recorded in the matching review JSON.
No substantive domain method, caveat or specialist identity is removed.

Codex CLI 0.153.2 is installed. OpenCode is unavailable in this shell.
