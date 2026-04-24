#!/usr/bin/env python3
"""
OpenCode Agent Manifest Linter
Validates agent markdown files against manifest schema rules.
"""

import re
import sys
from pathlib import Path

AGENTS_DIR = Path(".opencode/agents")

ERRORS = {
    "permission_singular": "Use 'permissions:' (plural) instead of 'permission:'",
    "reports_to_underscore": "Use 'reportsto:' (camelCase) instead of 'reports_to:'",
    "invalid_color": "Invalid color. Must be a quoted HEX code (e.g., '#FF0000')",
    "extra_keys": "Extra keys not allowed in frontmatter (cron, time, questions). Move to description.",
    "missing_required": "Required field '{field}' is missing",
    "invalid_model": "Invalid model. Allowed: sonnet, haiku, opus",
}

MODELS = {"sonnet", "haiku", "opus"}
REQUIRED_FIELDS = {"name", "description", "model"}

def lint_file(filepath: Path) -> list[dict]:
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
        if model_val not in MODELS:
            errors.append({"code": "invalid_model", "msg": f"Invalid model '{model_val}'. Allowed: sonnet, haiku, opus"})
    
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
        print("Run: grep -E \"permission:|reports_to:|color: [^#]\" .opencode/agents/*.md")
        sys.exit(1)
    else:
        print("OpenCode Agent Linter: OK")
        sys.exit(0)

if __name__ == "__main__":
    main()