---
name: codex-personal-consultant
description: >-
  Consult the user's personal Codex account (Astra / GPT-6 flagship models) with
  task-adaptive reasoning effort (low, medium, high) via isolated CODEX_HOME. Use for
  deep conceptual peer reviews, cross-validating architectural hypotheses, or comparing
  Antigravity's analysis with OpenAI's frontier models without disturbing the corporate work session.
---

# Codex Personal Consultant Skill

This skill enables Antigravity to consult the user's personal Codex account (equipped with Astra / GPT-6 and deep reasoning modes) as an external expert / second opinion, completely isolated from the corporate EIS session.

## Architecture

- **Isolation**: Uses `CODEX_HOME=~/.codex-personal`. The corporate session in `~/.codex` (with Jira/Confluence tokens and enterprise SSO) remains 100% untouched.
- **CLI Runner**: Script [`scripts/consult_codex_personal.py`](file:///Users/oprotsenko/projects/self-education/before-we-build-research/scripts/consult_codex_personal.py).
- **Execution Mode**: Runs non-interactively via `codex exec` with `-s read-only` and `--ephemeral` for safety and clean history.

## Selecting Reasoning Effort (`model_reasoning_effort`)

Always adapt the reasoning effort to the epistemic and structural complexity of the query:

| Effort Level | When to Use | Typical Topics |
| :--- | :--- | :--- |
| **`high`** | Deep ontology, epistemic boundaries, trade-offs, rival hypotheses | Shifting from typologies to latent processes; multi-level compatibility; falsification design; philosophical foundations. |
| **`medium`** | Structured analysis, document review, synthesis of 2-3 sources | Reviewing section flow, checking claim caveats, refactoring draft pages, evaluating prompt engineering. |
| **`low`** | Quick sanity checks, formatting, factual lookups | Grammar, quick schema validation, listing options. |

## How to Consult Personal Codex

### 1. Direct Command

Run the consultation script via `run_command`:

```bash
python3 scripts/consult_codex_personal.py -e high "Твой концептуальный промпт для Codex"
```

### 2. Passing Complex Prompts via File

For rich prompts or text passages (e.g. from `wiki/`):

```bash
python3 scripts/consult_codex_personal.py -e high -f path/to/prompt.md
```

### 3. Using Specific Model (e.g. Astra / GPT-6)

If a specific model slug is required:

```bash
python3 scripts/consult_codex_personal.py -m <model_slug> -e high "Промпт"
```

To view available models on the personal account:
```bash
python3 scripts/consult_codex_personal.py --list-models
```

## First-Time Authentication Gate

If `~/.codex-personal` is not yet authenticated, `consult_codex_personal.py` will report `Not logged in`.
In that case, guide the user to execute the one-time interactive login in their terminal:

```bash
CODEX_HOME=~/.codex-personal /Applications/ChatGPT.app/Contents/Resources/codex login
```

Once completed in the browser, all subsequent calls work seamlessly and headless.

## Synthesis & Collegium Workflow

When comparing Antigravity's advice with Codex's advice:
1. **Frame the core question** with clean epistemic boundaries.
2. **Consult Codex** at the appropriate reasoning effort level.
3. **Analyze convergence & divergence**:
   - Where do Antigravity and Codex agree?
   - Where do they offer distinct angles or complementary tools?
   - What unaddressed caveats or blind spots did either side reveal?
4. **Deliver a synthesized, actionable summary** to the user.
