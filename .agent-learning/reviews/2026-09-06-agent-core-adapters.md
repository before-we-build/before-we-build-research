# Shared core adapter review — 2026-09-06

Decision: approved for the user's explicit implementation request.
Reviewer: implementing assistant (self-review, not an independent expert panel).

Core content extraction preserves instructions modulo documented path changes
and the shared organization preamble. Migration hashes allow that assertion to
be checked. Permissions are explicit per runtime; intended read/write roles do
not imply universal enforcement. All existing specialist identities survive.
Generated files are not authoring sources; governance now covers core and adapter
settings. Validation: 108 tests passed; 53 normalized role-body hashes match; adapter drift
checks and strict wiki checks pass. See reports/agent-core-adapters-2026-09-06.md
for runtime limits and final inventory verification.
