# Shared agent core

Edit roles once; generate adapters for each supported runtime.

| Authoritative input | Purpose |
|---|---|
| `registry.json` | Stable role IDs, descriptions, accountability and intended read/write access |
| `roles/<id>.md` | Vendor-independent role instructions and domain caveats |
| `ORGANIZATION.md` | Shared task ownership and handoff rules; roster generated from registry |
| `adapters/opencode.json` | OpenCode V1 model IDs and optional colors |
| `adapters/codex.json` | Codex concurrency and optional per-role model/reasoning settings |
| `skills/` | Reusable skills; these are workflows, not additional permanent agents |

All paths in role instructions are relative to the repository root unless an
explicit Markdown link says otherwise. Legacy `.opencode/data/` and
`.opencode/skills/` files remain shared resources at their stable paths; they
are not executable dependencies on OpenCode. Historical governance records
retain the old authoring paths as evidence of the system at that time.

## Authoring

1. Follow `.agent-learning/` for an authorized instruction/configuration change.
2. Edit metadata in `registry.json` and prose in `roles/<id>.md`. A new role needs
   a distinct responsibility and a registered parent. Change vendor-specific
   settings only in the relevant `adapters/*.json` file.
3. Run `python3 scripts/generate_agent_adapters.py --write`.
4. Run `python3 scripts/generate_agent_adapters.py --check` and the repository checks.

Both commands are deterministic and need no network, credentials or model calls.
The checker fails for missing, extra or edited outputs. `--write` does not delete
obsolete roles or overwrite an unowned adapter file. Review and archive obsolete
outputs explicitly; then update the generated manifest. `--adopt-existing` is an
explicit initial-migration option, not a routine way to suppress conflicts.

`generated-files.json` lists managed outputs, not additional role definitions.
Do not hand-edit `.opencode/agents/*.md`, `.codex/agents/*.toml`,
`.codex/config.toml`, or the compatibility `.opencode/ORGANIZATION.md` stub.
The existing `opencode.json` remains host configuration; its default_agent must
match the registry entrypoint. Global user configuration is never generated.

## Runtime adapters

| Runtime | Generated integration | Models and permissions |
|---|---|---|
| OpenCode V1 schema | 53 Markdown agents, one primary | Existing provider/model IDs; read roles deny edit and shell, write roles permit edit; other permissions inherit host policy |
| Current Codex standalone-agent schema | 52 TOML custom subagents and project config | Models/reasoning inherit session unless explicitly set; read roles request read-only sandbox, writers workspace-write |
| Other hosts | Canonical Markdown/JSON is available | Requires a host adapter or explicit assignment to a generic subagent; no automatic discovery is claimed |

Codex's **main session** owns `master-orchestrator` via root `AGENTS.md`; it is
not emitted as another custom subagent. This avoids a redundant coordinator.
Codex defaults to three concurrent child threads in the generated project config.
No model/provider, credential, global config, approval mode or network setting is
changed by this adapter. OpenCode V2 uses a different permission schema and needs
an additional adapter; do not load the V1 outputs as if compatibility were proven.

The core `access` field describes intended role access, not a universal security
mechanism. Runtime overrides, sandbox implementation, external tools and account
permissions can differ. OpenCode's read profile denies shell entirely; Codex's
read-only sandbox can permit read-only shell operations. They are not identical
permission sets. Writing files does not authorize publication or data collection.

## Verification and use

Start a new trusted Codex session in the repository so project configuration is
loaded. Ask for a bounded task and identify specialists when useful, for example:
“Use source-provenance-auditor to check these sources; return findings without edits.”
The main session reads the shared routing contract. No simultaneous launch of all
roles is needed. A host with generic subagents can receive the same canonical
role text explicitly; disclose when named registration is unavailable.

Test at four levels: source/adapter synchronization; TOML and metadata validation;
actual runtime discovery; representative delegated tasks. Static checks only prove
the first two. See `../reports/agent-core-adapters-2026-09-06.md` for tested limits.

Primary documentation (checked 2026-09-06):
[Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[OpenCode agents and V1 permissions](https://opencode.ai/docs/agents/).
