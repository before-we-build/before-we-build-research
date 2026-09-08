#!/usr/bin/env python3
"""
Consult Codex on Personal Account (Isolated via CODEX_HOME).

Allows Antigravity to query the personal Codex account with full reasoning
effort control without touching or invalidating the corporate work session.
"""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

CODEX_BIN = "/Applications/ChatGPT.app/Contents/Resources/codex"
PERSONAL_HOME = Path.home() / ".codex-personal"


def check_auth() -> bool:
    auth_file = PERSONAL_HOME / "auth.json"
    return auth_file.is_file() and auth_file.stat().st_size > 10


def list_models():
    if not check_auth():
        print(f"Error: Personal profile at {PERSONAL_HOME} is not authenticated.", file=sys.stderr)
        print(f"Run this one-time command in your terminal to log in:", file=sys.stderr)
        print(f"  CODEX_HOME={PERSONAL_HOME} {CODEX_BIN} login", file=sys.stderr)
        sys.exit(1)

    models_cache = PERSONAL_HOME / "models_cache.json"
    if models_cache.exists():
        import json
        try:
            with open(models_cache, "r", encoding="utf-8") as f:
                data = json.load(f)
            models = data.get("models", [])
            print("Cached models for personal account:")
            for m in models:
                slug = m.get("slug") or m.get("id") or str(m)
                desc = m.get("display_name", "")
                print(f"  - {slug} ({desc})" if desc else f"  - {slug}")
            return
        except Exception as e:
            print(f"Failed to read models cache: {e}", file=sys.stderr)

    # Fallback to running a probe command
    env = os.environ.copy()
    env["CODEX_HOME"] = str(PERSONAL_HOME)
    subprocess.run([CODEX_BIN, "login", "status"], env=env)


def consult(prompt: str, effort: str = "high", model: str | None = None, system_context: str | None = None) -> str:
    if not check_auth():
        msg = (
            f"Personal Codex account is not yet logged in!\n"
            f"Please run this one-time login command in your terminal:\n\n"
            f"  CODEX_HOME={PERSONAL_HOME} {CODEX_BIN} login\n"
        )
        raise RuntimeError(msg)

    full_prompt = prompt
    if system_context:
        full_prompt = f"{system_context}\n\n---\n\n{prompt}"

    env = os.environ.copy()
    env["CODEX_HOME"] = str(PERSONAL_HOME)

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".md", delete=False) as out_file:
        out_path = out_file.name

    try:
        cmd = [
            CODEX_BIN,
            "exec",
            "-s", "read-only",
            "--ephemeral",
            "-c", f'model_reasoning_effort="{effort}"',
            "-o", out_path,
        ]

        if model:
            cmd.extend(["-m", model])

        cmd.append(full_prompt)

        result = subprocess.run(
            cmd,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.returncode != 0:
            err_msg = result.stderr.strip() or result.stdout.strip()
            raise RuntimeError(f"Codex CLI failed (exit {result.returncode}): {err_msg}")

        if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
            with open(out_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        else:
            return result.stdout.strip()

    finally:
        if os.path.exists(out_path):
            os.remove(out_path)


def main():
    parser = argparse.ArgumentParser(description="Consult personal Codex client.")
    parser.add_argument("prompt", nargs="?", help="Prompt to send to Codex")
    parser.add_argument("-f", "--file", help="File containing prompt")
    parser.add_argument(
        "-e", "--effort",
        choices=["low", "medium", "high"],
        default="high",
        help="Reasoning effort (default: high)",
    )
    parser.add_argument("-m", "--model", help="Specific model slug to use (e.g. gpt-6, astra, etc.)")
    parser.add_argument("--list-models", action="store_true", help="List available models for personal account")
    parser.add_argument("--status", action="store_true", help="Check login status of personal profile")

    args = parser.parse_args()

    if args.status:
        env = os.environ.copy()
        env["CODEX_HOME"] = str(PERSONAL_HOME)
        res = subprocess.run([CODEX_BIN, "login", "status"], env=env, capture_output=True, text=True)
        print(f"Personal Profile ({PERSONAL_HOME}):")
        print(res.stdout or res.stderr)
        return

    if args.list_models:
        list_models()
        return

    prompt = args.prompt
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            prompt = f.read()
    elif not prompt and not sys.stdin.isatty():
        prompt = sys.stdin.read()

    if not prompt:
        parser.print_help()
        sys.exit(1)

    try:
        response = consult(prompt, effort=args.effort, model=args.model)
        print(response)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
