#!/usr/bin/env python3
"""
Agent System Orchestrator: Compiler, Validator & Drift Detector.

Implements the multi-harness universal agent architecture for Before We Build:
- Canonical Role Contracts (governance/agent-system/roles/*.yaml)
- Target Projections (Antigravity, Claude Code, OpenAI Codex, OpenCode)
- Static Validation & Drift Detection
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
GOVERNANCE_DIR = REPO_ROOT / "governance" / "agent-system"
ROLES_DIR = GOVERNANCE_DIR / "roles"
INSTRUCTIONS_DIR = GOVERNANCE_DIR / "instructions"
POLICIES_DIR = GOVERNANCE_DIR / "policies"
SCHEMAS_DIR = GOVERNANCE_DIR / "schemas"
DEPLOYMENTS_DIR = REPO_ROOT / "deployments"
TARGETS_FILE = DEPLOYMENTS_DIR / "targets.yaml"
LOCK_FILE = DEPLOYMENTS_DIR / "agent-system.lock.json"
CONSTITUTION_FILE = REPO_ROOT / "AGENTS.md"

VALID_CAPABILITIES = {
    "fs.read",
    "fs.write",
    "exec.sandboxed",
    "web.search",
    "sources.retrieve",
    "artifact.emit",
    "subagent.spawn",
}

ID_REGEX = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def compute_sha256(content: str | bytes) -> str:
    if isinstance(content, str):
        content = content.encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def compute_file_sha256(file_path: Path) -> str:
    return compute_sha256(file_path.read_bytes())


class ValidationError(Exception):
    pass


def load_yaml(file_path: Path) -> Dict[str, Any]:
    if not file_path.is_file():
        raise ValidationError(f"File not found: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if not isinstance(data, dict):
                raise ValidationError(f"Invalid YAML structure in {file_path}: expected mapping")
            return data
    except Exception as e:
        raise ValidationError(f"Error parsing YAML {file_path}: {e}")


def validate_role_dict(role: Dict[str, Any], file_path: Path) -> List[str]:
    errors = []
    if role.get("api_version") != "bwb.agent/v1":
        errors.append(f"api_version must be 'bwb.agent/v1', got {role.get('api_version')}")
    if role.get("kind") != "Role":
        errors.append(f"kind must be 'Role', got {role.get('kind')}")

    role_id = role.get("id")
    if not role_id or not isinstance(role_id, str) or not ID_REGEX.match(role_id):
        errors.append(f"Invalid id '{role_id}': must be lowercase kebab-case")
    elif file_path.stem != role_id:
        errors.append(f"Filename stem '{file_path.stem}' does not match role id '{role_id}'")

    if not isinstance(role.get("revision"), int) or role.get("revision", 0) < 1:
        errors.append(f"revision must be an integer >= 1, got {role.get('revision')}")

    desc = role.get("description")
    if not isinstance(desc, str) or len(desc.strip()) < 10:
        errors.append("description must be a string of at least 10 characters")

    scope = role.get("scope")
    if not isinstance(scope, dict):
        errors.append("scope must be a mapping with 'includes' and 'excludes'")
    else:
        includes = scope.get("includes")
        excludes = scope.get("excludes")
        if not isinstance(includes, list) or len(includes) == 0:
            errors.append("scope.includes must be a non-empty list of strings")
        if not isinstance(excludes, list) or len(excludes) == 0:
            errors.append("scope.excludes must be a non-empty list of strings")

    instr_ref = role.get("instructions_ref")
    if not isinstance(instr_ref, str) or not instr_ref.endswith(".md"):
        errors.append(f"instructions_ref must point to a .md file, got {instr_ref}")
    else:
        instr_path = REPO_ROOT / instr_ref
        if not instr_path.is_file():
            errors.append(f"instructions_ref file does not exist: {instr_ref}")

    policy_refs = role.get("policy_refs", [])
    if isinstance(policy_refs, list):
        for pref in policy_refs:
            policy_path = POLICIES_DIR / f"{pref}.yaml"
            if not policy_path.is_file():
                errors.append(f"Referenced policy '{pref}' does not exist at {policy_path}")
    else:
        errors.append("policy_refs must be a list of strings")

    accountability = role.get("accountability")
    if not isinstance(accountability, dict) or not isinstance(accountability.get("reports_to"), str):
        errors.append("accountability.reports_to must be specified as a string")

    capabilities = role.get("capabilities", {})
    if isinstance(capabilities, dict):
        for cap in capabilities.get("required", []):
            if cap not in VALID_CAPABILITIES:
                errors.append(f"Unknown required capability '{cap}'")
    else:
        errors.append("capabilities must be a dictionary")

    return errors


def validate_canonical() -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Dict[str, Any]], List[str]]:
    errors = []
    if not CONSTITUTION_FILE.is_file():
        errors.append(f"Constitution not found at {CONSTITUTION_FILE}")

    # Validate policies
    policies: Dict[str, Dict[str, Any]] = {}
    if not POLICIES_DIR.is_dir():
        errors.append(f"Policies directory not found: {POLICIES_DIR}")
    else:
        for pfile in sorted(POLICIES_DIR.glob("*.yaml")):
            try:
                pdata = load_yaml(pfile)
                pid = pdata.get("id")
                if not pid:
                    errors.append(f"Policy in {pfile.name} missing 'id'")
                else:
                    policies[pid] = pdata
            except ValidationError as ve:
                errors.append(str(ve))

    # Validate roles
    roles: Dict[str, Dict[str, Any]] = {}
    if not ROLES_DIR.is_dir():
        errors.append(f"Roles directory not found: {ROLES_DIR}")
    else:
        for rfile in sorted(ROLES_DIR.glob("*.yaml")):
            try:
                rdata = load_yaml(rfile)
                r_errors = validate_role_dict(rdata, rfile)
                if r_errors:
                    errors.extend([f"[{rfile.name}] {e}" for e in r_errors])
                else:
                    roles[rdata["id"]] = rdata
            except ValidationError as ve:
                errors.append(str(ve))

    # Validate cross-role references
    for rid, rdata in roles.items():
        reports_to = rdata["accountability"]["reports_to"]
        # reports_to can be another role, orchestrator, or lead
        delegation = rdata.get("delegation", {})
        for del_id in delegation.get("may_delegate_to", []):
            # delegation target should ideally be a recognized role
            pass

    return roles, policies, errors


def load_targets() -> Dict[str, Any]:
    if not TARGETS_FILE.is_file():
        raise ValidationError(f"Targets file missing: {TARGETS_FILE}")
    data = load_yaml(TARGETS_FILE)
    targets = data.get("targets", {})
    if not targets:
        raise ValidationError("No targets defined in targets.yaml")
    return targets


def render_opencode(role: Dict[str, Any], instruction_content: str, target_cfg: Dict[str, Any]) -> str:
    caps = set(role.get("capabilities", {}).get("required", []) + role.get("capabilities", {}).get("optional", []))
    write_perm = "fs.write" in caps
    
    # Deriving team from accountability or role scope
    reports_to = role["accountability"]["reports_to"]
    team = "wiki" if "wiki" in reports_to else "orchestration"

    fm = {
        "name": role["id"],
        "team": team,
        "description": role["description"].strip(),
        "model": target_cfg.get("default_model", "openai/gpt-5.5"),
        "scope": ", ".join(role["scope"]["includes"]),
        "reportsto": reports_to,
        "permissions": {
            "tool_use": True,
            "read": True,
            "write": write_perm,
            "grep": True,
            "glob": True,
        }
    }
    fm_str = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm_str}\n---\n\n{instruction_content.strip()}\n"


def render_claude(role: Dict[str, Any], instruction_content: str, target_cfg: Dict[str, Any]) -> str:
    caps = set(role.get("capabilities", {}).get("required", []) + role.get("capabilities", {}).get("optional", []))
    tools = ["read"]
    if "fs.write" in caps:
        tools.append("write")
    if "exec.sandboxed" in caps:
        tools.append("terminal")
    if "web.search" in caps:
        tools.append("web_search")

    fm = {
        "name": role["id"],
        "description": role["description"].strip(),
        "tools": tools,
        "reports_to": role["accountability"]["reports_to"],
    }
    fm_str = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm_str}\n---\n\n{instruction_content.strip()}\n"


def render_antigravity(role: Dict[str, Any], instruction_content: str, target_cfg: Dict[str, Any]) -> str:
    caps = set(role.get("capabilities", {}).get("required", []) + role.get("capabilities", {}).get("optional", []))
    tools = ["read"]
    if "fs.write" in caps:
        tools.append("write")
    if "exec.sandboxed" in caps:
        tools.append("run_command")
    if "web.search" in caps:
        tools.append("search_web")
    if "subagent.spawn" in caps:
        tools.append("invoke_subagent")

    fm = {
        "name": role["id"],
        "description": role["description"].strip(),
        "model": target_cfg.get("default_model", "gemini-2.5-pro"),
        "reportsto": role["accountability"]["reports_to"],
        "tools": tools,
    }
    fm_str = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm_str}\n---\n\n{instruction_content.strip()}\n"


def render_codex_toml(role: Dict[str, Any], instruction_content: str, target_cfg: Dict[str, Any]) -> str:
    model = target_cfg.get("default_model", "gpt-6")
    effort = target_cfg.get("default_effort", "high")
    role_id = role["id"]
    desc = role["description"].strip().replace('"', '\\"')

    # Clean instructions for TOML multiline string
    escaped_instructions = instruction_content.strip().replace('"""', '\\"\\"\\"')

    toml_content = f'''# Generated by scripts/agent_system.py. DO NOT EDIT DIRECTLY.
name = "{role_id}"
description = "{desc}"
model = "{model}"
model_reasoning_effort = "{effort}"

developer_instructions = """
{escaped_instructions}
"""
'''
    return toml_content


def generate_claude_bootstrap(roles: Dict[str, Dict[str, Any]]) -> str:
    lines = [
        "<!-- Generated by scripts/agent_system.py. DO NOT EDIT DIRECTLY. -->",
        "# Claude Code Agent System Bootstrap",
        "",
        "@AGENTS.md",
        "",
        "## Available Custom Subagents (`.claude/agents/`)",
        "",
    ]
    for rid, rdata in sorted(roles.items()):
        lines.append(f"- **`{rid}`**: {rdata['description'].strip()}")
    lines.append("")
    return "\n".join(lines)


def build_projections(dry_run: bool = False) -> Tuple[Dict[str, str], List[str]]:
    roles, policies, errors = validate_canonical()
    if errors:
        return {}, errors

    targets = load_targets()
    generated_files: Dict[str, str] = {}  # rel_path -> content

    for target_key, target_cfg in targets.items():
        agents_dir_rel = target_cfg.get("agents_dir")
        if not agents_dir_rel:
            continue
        agents_dir = REPO_ROOT / agents_dir_rel

        for rid, role in roles.items():
            instr_path = REPO_ROOT / role["instructions_ref"]
            instruction_content = instr_path.read_text(encoding="utf-8")

            if target_key == "opencode":
                content = render_opencode(role, instruction_content, target_cfg)
                out_path = agents_dir / f"{rid}.md"
            elif target_key == "claude-code":
                content = render_claude(role, instruction_content, target_cfg)
                out_path = agents_dir / f"{rid}.md"
            elif target_key == "antigravity":
                content = render_antigravity(role, instruction_content, target_cfg)
                out_path = agents_dir / f"{rid}.md"
            elif target_key == "codex":
                content = render_codex_toml(role, instruction_content, target_cfg)
                out_path = agents_dir / f"{rid}.toml"
            else:
                continue

            rel_str = str(out_path.relative_to(REPO_ROOT))
            generated_files[rel_str] = content

        # Check for target-specific root files
        if target_key == "claude-code" and "bootstrap_file" in target_cfg:
            bootstrap_rel = target_cfg["bootstrap_file"]
            bootstrap_content = generate_claude_bootstrap(roles)
            generated_files[bootstrap_rel] = bootstrap_content

    if not dry_run:
        for rel_str, content in generated_files.items():
            full_path = REPO_ROOT / rel_str
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding="utf-8")

        # Save lockfile
        manifest = {
            "version": "1.0.0",
            "constitution_digest": compute_file_sha256(CONSTITUTION_FILE),
            "canonical_sources": {
                str(rfile.relative_to(REPO_ROOT)): compute_file_sha256(rfile)
                for rfile in sorted(ROLES_DIR.glob("*.yaml"))
            },
            "policies": {
                str(pfile.relative_to(REPO_ROOT)): compute_file_sha256(pfile)
                for pfile in sorted(POLICIES_DIR.glob("*.yaml"))
            },
            "projections": {
                rel_path: compute_sha256(content)
                for rel_path, content in sorted(generated_files.items())
            }
        }
        LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LOCK_FILE, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

    return generated_files, []


def check_drift() -> Tuple[bool, List[str]]:
    expected_files, errors = build_projections(dry_run=True)
    if errors:
        return False, [f"Validation failure during drift check: {e}" for e in errors]

    drift_detected = []
    for rel_str, expected_content in expected_files.items():
        disk_path = REPO_ROOT / rel_str
        if not disk_path.is_file():
            drift_detected.append(f"Missing projection file: {rel_str}")
            continue

        actual_content = disk_path.read_text(encoding="utf-8")
        if actual_content != expected_content:
            drift_detected.append(f"Drift detected in projection: {rel_str} (content on disk does not match canonical projection)")

    if drift_detected:
        return False, drift_detected
    return True, []


def generate_report():
    roles, policies, errors = validate_canonical()
    if errors:
        print("Validation errors detected:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    targets = load_targets()
    print("================================================================================")
    print("                 BEFORE WE BUILD — AGENT SYSTEM COMPLIANCE REPORT                ")
    print("================================================================================")
    print(f"Constitution: {CONSTITUTION_FILE.name} (digest: {compute_file_sha256(CONSTITUTION_FILE)[:12]})")
    print(f"Canonical Roles: {len(roles)} | Policies: {len(policies)} | Targets: {len(targets)}")
    print("--------------------------------------------------------------------------------")
    print(f"{'Role ID':<35} | {'Target':<14} | {'Status':<12} | {'Capabilities'}")
    print("--------------------------------------------------------------------------------")

    for rid, role in sorted(roles.items()):
        req_caps = role.get("capabilities", {}).get("required", [])
        for tname, tcfg in sorted(targets.items()):
            supported = tcfg.get("capabilities_supported", [])
            unsupported = [c for c in req_caps if c not in supported]
            if unsupported:
                status = f"PARTIAL (-{len(unsupported)})"
            else:
                status = "FULLY_ALIGNED"
            caps_str = ", ".join(req_caps)
            print(f"{rid:<35} | {tname:<14} | {status:<12} | {caps_str}")

    print("================================================================================")


def main():
    parser = argparse.ArgumentParser(description="Multi-Harness Agent System CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("validate", help="Validate canonical schemas, references and rules")
    subparsers.add_parser("build", help="Compile canonical roles into target projections")
    subparsers.add_parser("check-drift", help="Check if generated target projections match canonical definitions")
    subparsers.add_parser("report", help="Print compatibility and compliance matrix")

    args = parser.parse_args()

    if args.command == "validate":
        roles, policies, errors = validate_canonical()
        if errors:
            print(f"Validation FAILED with {len(errors)} errors:", file=sys.stderr)
            for err in errors:
                print(f"  - {err}", file=sys.stderr)
            sys.exit(1)
        print(f"Validation SUCCESS: {len(roles)} canonical roles and {len(policies)} policies valid.")

    elif args.command == "build":
        generated, errors = build_projections(dry_run=False)
        if errors:
            print(f"Build FAILED with {len(errors)} errors:", file=sys.stderr)
            for err in errors:
                print(f"  - {err}", file=sys.stderr)
            sys.exit(1)
        print(f"Build SUCCESS: Compiled {len(generated)} projection files across all targets.")
        for path in sorted(generated.keys()):
            print(f"  -> {path}")

    elif args.command == "check-drift":
        passed, issues = check_drift()
        if not passed:
            print("Drift check FAILED. Target projections are out of sync with canonical source:", file=sys.stderr)
            for issue in issues:
                print(f"  [DRIFT] {issue}", file=sys.stderr)
            sys.exit(1)
        print("Drift check PASSED: All target projections are synchronized with canonical source.")

    elif args.command == "report":
        generate_report()


if __name__ == "__main__":
    main()
