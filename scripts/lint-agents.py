#!/usr/bin/env python3
"""
OpenCode Agent Manifest Linter.

Validates agent markdown files against manifest schema rules and checks that
agent model IDs point to реально доступные модели в текущем OpenCode setup.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

AGENTS_DIR = Path(".opencode/agents")

ERRORS = {
    "permission_singular": "Use 'permissions:' (plural) instead of 'permission:'",
    "reports_to_underscore": "Use 'reportsto:' (camelCase) instead of 'reports_to:'",
    "invalid_color": "Invalid color. Must be a quoted HEX code (e.g., '#FF0000')",
    "extra_keys": "Extra keys not allowed in frontmatter (cron, time, questions). Move to description.",
    "missing_required": "Required field '{field}' is missing",
    "invalid_model_format": "Model must use provider/model format (e.g., openai/gpt-5.4)",
    "unknown_provider": "Model provider '{provider}' is not available via opencode models",
    "unavailable_model": "Model '{model}' is not available for provider '{provider}'",
    "opencode_unavailable": "Could not query available models from opencode CLI",
}

REQUIRED_FIELDS = {"name", "description", "model"}


def load_available_models() -> tuple[dict[str, set[str]], str | None]:
    try:
        providers_proc = subprocess.run(
            ["opencode", "providers"],
            capture_output=True,
            text=True,
            check=False,
        )
        provider_output = (providers_proc.stdout or "") + (providers_proc.stderr or "")
        providers = set(re.findall(r"^\s*([a-zA-Z0-9_-]+)\s", provider_output, re.MULTILINE))

        # Fallback for setups where `opencode providers` is noisy or not parseable.
        providers.update({"openai"})

        available: dict[str, set[str]] = {}
        for provider in sorted(providers):
            proc = subprocess.run(
                ["opencode", "models", provider],
                capture_output=True,
                text=True,
                check=False,
            )
            if proc.returncode != 0:
                continue

            models = set()
            for line in proc.stdout.splitlines():
                line = line.strip()
                if not line or "/" not in line:
                    continue
                line_provider, model_name = line.split("/", 1)
                if line_provider == provider:
                    models.add(model_name)

            if models:
                available[provider] = models

        if not available:
            return {}, ERRORS["opencode_unavailable"]

        return available, None
    except Exception as exc:
        return {}, f"{ERRORS['opencode_unavailable']}: {exc}"


AVAILABLE_MODELS, MODEL_LOAD_ERROR = load_available_models()


def lint_file(filepath: Path) -> list[dict[str, str]]:
    errors = []
    content = filepath.read_text()
    
    if not content.startswith("---"):
        return errors
    
    frontmatter_end = content[3:].find("---")
    if frontmatter_end == -1:
        return errors
    
    frontmatter = content[3:frontmatter_end]
    lines = frontmatter.strip().split("\n")
    
    fields = {}
    for line in lines:
        if ":" in line:
            key = line.split(":", 1)[0].strip()
            value = line.split(":", 1)[1].strip()
            fields[key] = value
    
    if re.search(r"^permission:", content, re.MULTILINE):
        errors.append({"code": "permission_singular", "msg": ERRORS["permission_singular"]})
    
    if re.search(r"^reports_to:", content, re.MULTILINE):
        errors.append({"code": "reports_to_underscore", "msg": ERRORS["reports_to_underscore"]})
    
    if "color" in fields:
        color_val = fields["color"].strip().strip('"').strip("'")
        if not re.match(r"^#[0-9A-Fa-f]{6}$", color_val):
            errors.append({"code": "invalid_color", "msg": ERRORS["invalid_color"]})
    
    extra_keys = {"cron", "time", "questions"}
    for key in extra_keys:
        if key in fields:
            errors.append({"code": "extra_keys", "msg": ERRORS["extra_keys"]})
    
    for field in REQUIRED_FIELDS:
        if field not in fields:
            errors.append({"code": "missing_required", "msg": ERRORS["missing_required"].format(field=field)})
    
    if "model" in fields:
        model_val = fields["model"].strip().strip('"').strip("'")
        if "/" not in model_val:
            errors.append({
                "code": "invalid_model_format",
                "msg": f"{ERRORS['invalid_model_format']}: '{model_val}'",
            })
        elif MODEL_LOAD_ERROR:
            errors.append({"code": "opencode_unavailable", "msg": MODEL_LOAD_ERROR})
        else:
            provider, model_name = model_val.split("/", 1)
            if provider not in AVAILABLE_MODELS:
                errors.append({
                    "code": "unknown_provider",
                    "msg": ERRORS["unknown_provider"].format(provider=provider),
                })
            elif model_name not in AVAILABLE_MODELS[provider]:
                known = ", ".join(sorted(AVAILABLE_MODELS[provider]))
                errors.append({
                    "code": "unavailable_model",
                    "msg": f"{ERRORS['unavailable_model'].format(model=model_name, provider=provider)}. Available: {known}",
                })

    return errors

def main():
    if not AGENTS_DIR.exists():
        print("No .opencode/agents directory found")
        sys.exit(0)
    
    all_errors = {}
    for md_file in AGENTS_DIR.glob("*.md"):
        errors = lint_file(md_file)
        if errors:
            all_errors[md_file] = errors
    
    if all_errors:
        print("OpenCode Agent Linter: ERRORS FOUND\n")
        for file, errors in all_errors.items():
            print(f"  {file.name}:")
            for e in errors:
                print(f"    - {e['msg']}")
            print()
        print("Run: python3 scripts/lint-agents.py")
        sys.exit(1)
    else:
        print("OpenCode Agent Linter: OK")
        sys.exit(0)

if __name__ == "__main__":
    main()
