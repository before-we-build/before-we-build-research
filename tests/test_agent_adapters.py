import json
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from generate_agent_adapters import render, sync, prompt, MARKER
from check_agent_organization import load_core


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for path in ['.agents/roles', '.agents/adapters']:
            (self.root / path).mkdir(parents=True)
        self.registry = {'schema_version': 1, 'entrypoint': 'root', 'roles': {
            'root': {'description': 'Route', 'scope': 'route', 'team': 'main', 'reports_to': None, 'access': 'write'},
            'reviewer': {'description': 'Review', 'scope': 'review', 'team': 'review', 'reports_to': 'root', 'access': 'read'},
            'writer': {'description': 'Write', 'scope': 'edit', 'team': 'edit', 'reports_to': 'root', 'access': 'write'},
        }}
        self.save_registry()
        for name in self.registry['roles']:
            (self.root / f'.agents/roles/{name}.md').write_text(f'# {name}\nPreserve evidence.\n')
        self.save('.agents/adapters/opencode.json', {'schema_version': 1, 'format': 'opencode-v1', 'default_model': 'vendor/model', 'roles': {}})
        self.save('.agents/adapters/codex.json', {'schema_version': 1, 'format': 'standalone-toml', 'max_concurrent_threads_per_session': 3, 'roles': {}})
        self.save('opencode.json', {'default_agent': 'root'})
        (self.root / '.agents/ORGANIZATION.md').write_text('# Shared\n<!-- agent-roster:start -->\n<!-- agent-roster:end -->\n')

    def save(self, path, data):
        (self.root / path).write_text(json.dumps(data))

    def save_registry(self):
        self.save('.agents/registry.json', self.registry)

    def test_generate_and_check_idempotent(self):
        self.assertEqual(sync(self.root, write=True), [])
        before = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(sync(self.root), [])
        self.assertEqual(sync(self.root, write=True), [])
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_codex_has_no_duplicate_root_and_inherits_models(self):
        outputs = render(self.root)
        self.assertNotIn('.codex/agents/root.toml', outputs)
        cfg = tomllib.loads(outputs['.codex/agents/reviewer.toml'])
        self.assertNotIn('model', cfg)
        self.assertNotIn('model_reasoning_effort', cfg)
        self.assertEqual(cfg['sandbox_mode'], 'read-only')
        self.assertEqual(tomllib.loads(outputs['.codex/agents/writer.toml'])['sandbox_mode'], 'workspace-write')

    def test_native_opencode_permissions(self):
        outputs = render(self.root)
        read = outputs['.opencode/agents/reviewer.md']
        self.assertIn('permission: {"edit": "deny", "bash": "deny"}', read)
        self.assertNotIn('tool_use:', read)
        self.assertNotIn('\npermissions:', read)
        self.assertIn('permission: {"edit": "allow"}', outputs['.opencode/agents/writer.md'])

    def test_role_change_propagates_to_both_runtimes(self):
        sync(self.root, write=True)
        p = self.root / '.agents/roles/reviewer.md'
        p.write_text(p.read_text()+'Check counterexamples.\n')
        errors = sync(self.root)
        self.assertTrue(any('.codex/agents/reviewer.toml' in e for e in errors))
        self.assertTrue(any('.opencode/agents/reviewer.md' in e for e in errors))
        self.assertEqual(sync(self.root, write=True), [])

    def test_prompt_roundtrip_with_quotes_unicode_and_backslashes(self):
        body = '# Українська\n""" and \'\'\' and \\path\\file\n$HOME is literal.\n'
        (self.root / '.agents/roles/reviewer.md').write_text(body)
        outputs = render(self.root)
        cfg = tomllib.loads(outputs['.codex/agents/reviewer.toml'])
        _, roles = load_core(self.root)
        self.assertEqual(cfg['developer_instructions'], prompt(roles['reviewer']))
        self.assertTrue(outputs['.opencode/agents/reviewer.md'].endswith(cfg['developer_instructions']))

    def test_refuses_unowned_config_before_any_write(self):
        (self.root / '.codex').mkdir()
        cfg = self.root / '.codex/config.toml'
        cfg.write_text('user_setting = true\n')
        self.assertTrue(any('unowned' in e for e in sync(self.root, write=True)))
        self.assertEqual(cfg.read_text(), 'user_setting = true\n')
        self.assertFalse((self.root / '.opencode/agents').exists())

    def test_detects_manual_generated_edit(self):
        sync(self.root, write=True)
        path = self.root / '.codex/agents/reviewer.toml'
        path.write_text(path.read_text()+'# drift\n')
        self.assertTrue(any('reviewer.toml' in e for e in sync(self.root)))

    def test_extra_adapter_is_not_deleted(self):
        sync(self.root, write=True)
        path = self.root / '.codex/agents/extra.toml'
        path.write_text('# personal\n')
        self.assertTrue(sync(self.root, write=True))
        self.assertTrue(path.exists())

    def test_missing_role_and_unknown_override_fail(self):
        (self.root / '.agents/roles/reviewer.md').unlink()
        self.assertTrue(sync(self.root))
        (self.root / '.agents/roles/reviewer.md').write_text('# Review\n')
        self.save('.agents/adapters/codex.json', {'schema_version': 1, 'format': 'standalone-toml', 'max_concurrent_threads_per_session': 3, 'roles': {'unknown': {'model': 'x'}}})
        self.assertTrue(sync(self.root))

    def test_cycles_and_vendor_metadata_rejected(self):
        self.registry['roles']['reviewer']['reports_to'] = 'reviewer'
        self.save_registry()
        self.assertTrue(sync(self.root))
        self.registry['roles']['reviewer']['reports_to'] = 'root'
        self.registry['roles']['reviewer']['model'] = 'vendor/model'
        self.save_registry()
        self.assertTrue(sync(self.root))

    def test_unsafe_role_name_rejected(self):
        self.registry['roles']['../escape'] = self.registry['roles'].pop('reviewer')
        self.save_registry()
        self.assertTrue(sync(self.root))

    def test_symlink_output_refused(self):
        (self.root / '.codex').mkdir()
        target = self.root / 'user.toml'
        target.write_text('untouched')
        (self.root / '.codex/config.toml').symlink_to(target)
        self.assertTrue(sync(self.root, write=True, adopt_existing=True))
        self.assertEqual(target.read_text(), 'untouched')

    def test_native_overrides_are_separate(self):
        self.save('.agents/adapters/codex.json', {'schema_version': 1, 'format': 'standalone-toml', 'max_concurrent_threads_per_session': 3, 'roles': {'reviewer': {'model': 'explicit-model', 'model_reasoning_effort': 'high'}}})
        outputs = render(self.root)
        cfg = tomllib.loads(outputs['.codex/agents/reviewer.toml'])
        self.assertEqual(cfg['model'], 'explicit-model')
        self.assertNotIn('explicit-model', outputs['.opencode/agents/reviewer.md'])

    def test_duplicate_json_role_is_rejected(self):
        path = self.root / '.agents/registry.json'
        path.write_text('{"schema_version": 1, "entrypoint": "root", "roles": {}, "roles": {}}')
        self.assertTrue(any('Duplicate JSON key' in e for e in sync(self.root)))

    def test_non_object_configs_fail_without_writes(self):
        for relative in ('.agents/registry.json', '.agents/adapters/opencode.json',
                         '.agents/adapters/codex.json', 'opencode.json',
                         '.agents/generated-files.json'):
            with self.subTest(path=relative):
                path = self.root / relative
                previous = path.read_text() if path.exists() else None
                path.write_text('[]')
                self.assertTrue(any('Expected JSON object' in e for e in sync(self.root, write=True)))
                self.assertFalse((self.root / '.opencode/agents').exists())
                if previous is None:
                    path.unlink()
                else:
                    path.write_text(previous)

    def test_actual_repository_is_synchronized(self):
        self.assertEqual(sync(Path(__file__).resolve().parents[1]), [])
