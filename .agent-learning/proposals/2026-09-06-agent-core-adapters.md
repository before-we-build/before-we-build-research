---
title: Shared agent core and runtime adapters
type: agent-improvement-proposal
created: 2026-09-06
updated: 2026-09-06
status: applied
risk: moderate
target_agents: [all-project-agents]
required_reviewers: []
sources: [AGENTS.md, .agents/ORGANIZATION.md]
---

## 1. Targets

53 existing roles; shared registry, organization, role bodies; generated OpenCode
Markdown and Codex standalone TOML; active governance pointers and CI checks.

## 2. Observed failure

OpenCode storage is being mistaken for portable agent registration. Maintaining
independent copies for each runtime would recreate the duplication just removed.

## 3. Evidence

Previous organization audit; 53 current manifests; Codex CLI 0.153.2;
official https://learn.chatgpt.com/docs/agent-configuration/subagents and
https://opencode.ai/docs/agents/ (accessed 2026-09-06).

## 4. Proposed change

Use `.agents/registry.json` for neutral identity, responsibility and intended
read/write role; `.agents/roles/*.md` for instructions; `.agents/adapters/*.json`
for vendor configuration. Generate adapters, fail CI on drift, preserve role names.
Codex's main session reads the entrypoint through AGENTS.md; only 52 delegate
roles become custom subagents. Codex models inherit the current session unless
explicitly configured. OpenCode model IDs remain unchanged.

Replace undocumented boolean permission/tool_use declarations with documented
OpenCode V1 permission syntax. Read roles deny edit/bash; write roles permit edit
and inherit the host's shell policy. Codex read roles request read-only sandbox;
writers request workspace-write. Host live overrides and external-tool policies
remain authoritative; the adapters do not claim identical enforcement.

## 5. Risk

Moderate: storage, registration and permissions change. No doctrine, empirical
warrant, instrument, public release authorization or domain safety gate changes.
No external publishing or collection is authorized by role access settings.

## 6. Review

Implementing assistant self-review; user explicitly authorized implementation.
No independent domain review is claimed or needed for a content-preserving move.
Any subsequent substantive domain change retains the existing review requirement.

## 7. Patch sketch

Extract role bodies → neutral registry → deterministic renderer → generated
OpenCode/Codex outputs. Update active authoring guidance; preserve historical logs.

## 8. Acceptance

53 canonical roles, 53 OpenCode adapters, 52 Codex subagents; no duplicate Codex
entrypoint. Byte-equivalent generated instructions across adapters. Parse TOML,
check structural invariants, detect missing/extra/stale outputs, preserve unknown
files on writes, test escaping and propagation. Run required repository checks.
Verify actual Codex discovery if a read-only local endpoint supports it.

## 9. Rollback

Restore the pre-migration cleanup state from the reviewed diff, preserving other
uncommitted work and historical learning records. No automatic deletion mode.
