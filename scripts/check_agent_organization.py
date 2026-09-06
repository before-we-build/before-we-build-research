#!/usr/bin/env python3
"""Validate project reporting structure and its generated organization roster."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

START = '<!-- agent-roster:start -->'
END = '<!-- agent-roster:end -->'


def read_fields(text: str) -> dict[str, str]:
    match = re.match(r'\A---\r?\n(.*?)^---[ \t]*(?:\r?\n|\Z)', text, re.M | re.S)
    if not match:
        raise ValueError('missing or unterminated frontmatter')
    # Only scalar top-level fields used by the organizational contract.
    return {k: v.strip().strip('"\'') for k, v in
            re.findall(r'^([a-zA-Z_][\w-]*):[ \t]*([^\n]*)$', match.group(1), re.M)}


def validate(agents: dict[str, dict[str, str]], default: str) -> list[str]:
    errors = []
    roots = [name for name, f in agents.items() if f.get('mode') == 'primary']
    if roots != [default]:
        errors.append('Exactly one project primary must match default_agent')
    for name, fields in agents.items():
        if fields.get('name') != name:
            errors.append(f'{name}: filename/name mismatch')
        if fields.get('mode') != ('primary' if name == default else 'subagent'):
            errors.append(f'{name}: explicit primary/subagent mode required')
        if not fields.get('scope'):
            errors.append(f'{name}: missing scope')
        if name == default and fields.get('reportsto') != 'null':
            errors.append(f'{name}: root must report to null')
        chain, current = [], name
        while current in agents:
            if current in chain:
                errors.append(f'{name}: reporting cycle')
                break
            chain.append(current)
            parent = agents[current].get('reportsto')
            if current == default and parent == 'null':
                break
            if parent not in agents:
                errors.append(f'{name}: missing/unknown parent for {current}: {parent}')
                break
            current = parent
        if len(chain) > 3:
            errors.append(f'{name}: reporting chain exceeds three nodes')
    return errors


def roster(agents: dict[str, dict[str, str]]) -> str:
    rows = [START, '| Agent | Mode | Reports to | Responsibility |',
            '|---|---|---|---|']
    for name, f in sorted(agents.items()):
        scope = f.get('scope', '').replace('|', '\\|')
        rows.append(f'| `{name}` | {f.get("mode", "")} | `{f.get("reportsto", "")}` | {scope} |')
    return '\n'.join(rows + [END])


def load_json(path: Path) -> dict:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'Duplicate JSON key: {key}')
            result[key] = value
        return result
    value = json.loads(path.read_text(), object_pairs_hook=unique)
    if not isinstance(value, dict):
        raise ValueError(f'Expected JSON object: {path}')
    return value


def load_core(root: Path) -> tuple[str, dict]:
    registry = load_json(root / '.agents/registry.json')
    if registry.keys() != {'schema_version', 'entrypoint', 'roles'} or registry['schema_version'] != 1:
        raise ValueError('Unsupported core registry schema')
    roles = registry['roles']
    entrypoint = registry['entrypoint']
    if not isinstance(roles, dict) or not roles or entrypoint not in roles:
        raise ValueError('Registry needs roles and a valid entrypoint')
    required = {'description', 'team', 'scope', 'reports_to', 'access'}
    result = {}
    for name, fields in roles.items():
        if not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', name):
            raise ValueError(f'Unsafe role name: {name}')
        if not isinstance(fields, dict) or fields.keys() - (required | {'method'}) or not required <= fields.keys():
            raise ValueError(f'{name}: invalid neutral metadata fields')
        if any(not isinstance(fields[k], str) or not fields[k].strip() for k in ['description', 'team', 'scope']):
            raise ValueError(f'{name}: empty role metadata')
        if fields['access'] not in {'read', 'write'}:
            raise ValueError(f'{name}: unsupported intended access')
        parent = fields['reports_to']
        if parent is not None and (not isinstance(parent, str) or parent not in roles):
            raise ValueError(f'{name}: unknown parent')
        body = (root / '.agents/roles' / (name + '.md')).read_text()
        if not body.strip():
            raise ValueError(f'{name}: empty role instruction')
        result[name] = dict(fields, body=body)
    actual = {p.relative_to(root / '.agents/roles').as_posix() for p in (root / '.agents/roles').rglob('*.md')}
    if actual != {name + '.md' for name in roles}:
        raise ValueError('Unregistered or missing core role files')
    problems = validate(organization_fields(entrypoint, result), entrypoint)
    if problems:
        raise ValueError('; '.join(problems))
    return entrypoint, result


def organization_fields(entrypoint: str, roles: dict) -> dict:
    return {name: dict(name=name, mode='primary' if name == entrypoint else 'subagent',
                      reportsto=f['reports_to'] or 'null', scope=f['scope'])
            for name, f in sorted(roles.items())}


def check(root: Path = Path('.'), *, write: bool = False) -> list[str]:
    try:
        entrypoint, roles = load_core(root)
        path = root / '.agents/ORGANIZATION.md'
        text = path.read_text()
        if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
            return ['Organization must contain exactly one ordered roster marker pair']
        expected = text[:text.index(START)] + roster(organization_fields(entrypoint, roles)) + text[text.index(END) + len(END):]
        if expected != text:
            if write:
                path.write_text(expected)
            else:
                return ['Organization roster is stale; run scripts/generate_agent_adapters.py --write']
        return []
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [str(exc)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    problems = check(write=args.write)
    print('\n'.join(problems) if problems else 'Agent organization: OK')
    raise SystemExit(bool(problems))
