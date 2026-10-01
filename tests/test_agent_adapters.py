import json
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch

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
            (self.root / f'.agents/roles/{name}.md').write_text(f'# {name}\nPreserve evidence.\n', encoding='utf-8')
        self.save('.agents/adapters/opencode.json', {'schema_version': 1, 'format': 'opencode-v1', 'default_model': 'vendor/model', 'roles': {}})
        self.save('.agents/adapters/codex.json', {'schema_version': 1, 'format': 'standalone-toml', 'max_concurrent_threads_per_session': 3, 'roles': {}})
        self.save('opencode.json', {'default_agent': 'root'})
        (self.root / '.agents/ORGANIZATION.md').write_text('# Shared\n<!-- agent-roster:start -->\n<!-- agent-roster:end -->\n', encoding='utf-8')

    def save(self, path, data):
        (self.root / path).write_text(json.dumps(data), encoding='utf-8')

    def save_registry(self):
        self.save('.agents/registry.json', self.registry)

    def symlink(self, link, target, *, directory=False):
        try:
            link.symlink_to(target, target_is_directory=directory)
        except OSError as exc:
            if sys.platform == 'win32' and getattr(exc, 'winerror', None) == 1314:
                self.skipTest('Windows requires Developer Mode or symlink privilege for this test')
            raise

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
        p.write_text(p.read_text(encoding='utf-8')+'Check counterexamples.\n', encoding='utf-8')
        errors = sync(self.root)
        self.assertTrue(any('.codex/agents/reviewer.toml' in e for e in errors))
        self.assertTrue(any('.opencode/agents/reviewer.md' in e for e in errors))
        self.assertEqual(sync(self.root, write=True), [])

    def test_prompt_roundtrip_with_quotes_unicode_and_backslashes(self):
        body = '# ������쪠\n""" and \'\'\' and \\path\\file\n$HOME is literal.\n'
        (self.root / '.agents/roles/reviewer.md').write_text(body, encoding='utf-8')
        outputs = render(self.root)
        cfg = tomllib.loads(outputs['.codex/agents/reviewer.toml'])
        _, roles = load_core(self.root)
        self.assertEqual(cfg['developer_instructions'], prompt(roles['reviewer']))
        self.assertTrue(outputs['.opencode/agents/reviewer.md'].endswith(cfg['developer_instructions']))

    def test_unicode_and_crlf_sources_generate_utf8_lf_artifacts(self):
        path = self.root / '.agents/roles/reviewer.md'
        path.write_bytes('# ������쪠 - ���᪨�\r\n�ਬ��: \\path\\file\r\n'.encode('utf-8'))
        self.registry['roles']['reviewer']['description'] = '��ॢ?ઠ - �஢�ઠ'
        self.save_registry()
        self.assertEqual(sync(self.root, write=True), [])
        for relative, expected in render(self.root).items():
            with self.subTest(path=relative):
                actual = (self.root / relative).read_bytes()
                self.assertEqual(actual, expected.encode('utf-8'))
                self.assertNotIn(b'\r\n', actual)
        self.assertEqual(sync(self.root), [])

    def test_refuses_unowned_config_before_any_write(self):
        (self.root / '.codex').mkdir()
        cfg = self.root / '.codex/config.toml'
        cfg.write_text('user_setting = true\n', encoding='utf-8')
        self.assertTrue(any('unowned' in e for e in sync(self.root, write=True)))
        self.assertEqual(cfg.read_text(encoding='utf-8'), 'user_setting = true\n')
        self.assertFalse((self.root / '.opencode/agents').exists())

    def test_detects_manual_generated_edit(self):
        sync(self.root, write=True)
        path = self.root / '.codex/agents/reviewer.toml'
        path.write_text(path.read_text(encoding='utf-8')+'# drift\n', encoding='utf-8')
        self.assertTrue(any('reviewer.toml' in e for e in sync(self.root)))

    def test_extra_adapter_is_not_deleted(self):
        sync(self.root, write=True)
        path = self.root / '.codex/agents/extra.toml'
        path.write_text('# personal\n', encoding='utf-8')
        self.assertTrue(sync(self.root, write=True))
        self.assertTrue(path.exists())

    def test_missing_role_and_unknown_override_fail(self):
        (self.root / '.agents/roles/reviewer.md').unlink()
        self.assertTrue(sync(self.root))
        (self.root / '.agents/roles/reviewer.md').write_text('# Review\n', encoding='utf-8')
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
        target.write_text('untouched', encoding='utf-8')
        self.symlink(self.root / '.codex/config.toml', target)
        self.assertTrue(sync(self.root, write=True, adopt_existing=True))
        self.assertEqual(target.read_text(encoding='utf-8'), 'untouched')

    def test_host_symlink_ancestor_above_repository_is_allowed(self):
        # Exercise real host aliases like macOS /var -> /private/var.
        with tempfile.TemporaryDirectory() as directory:
            alias = Path(directory) / 'host-alias'
            self.symlink(alias, self.root.parent, directory=True)
            aliased_root = alias / self.root.name
            self.assertEqual(sync(aliased_root, write=True), [])
            self.assertEqual(sync(aliased_root), [])
            self.assertEqual(sync(self.root), [])

    def test_symlink_guard_stops_at_repository_root(self):
        checked = []

        def is_symlink(path):
            checked.append(path)
            return path == self.root.parent.parent

        with patch.object(Path, 'is_symlink', is_symlink):
            self.assertEqual(sync(self.root, write=True), [])
        self.assertIn(self.root, checked)
        self.assertTrue(all(path.is_relative_to(self.root) for path in checked))

    def test_symlinked_repository_root_is_refused(self):
        with patch.object(Path, 'is_symlink', lambda path: path == self.root):
            self.assertTrue(any('symlink output' in e for e in sync(self.root, write=True)))
        self.assertFalse((self.root / '.opencode/agents').exists())

    def test_symlinked_output_parent_is_refused_before_any_write(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            sentinel = target / 'config.toml'
            sentinel.write_text('untouched', encoding='utf-8')
            self.symlink(self.root / '.codex', target, directory=True)
            self.assertTrue(any('symlink output' in e for e in
                                sync(self.root, write=True, adopt_existing=True)))
            self.assertEqual(sentinel.read_text(encoding='utf-8'), 'untouched')
            self.assertEqual(list(target.iterdir()), [sentinel])
            self.assertFalse((self.root / '.opencode/agents').exists())

    def test_native_overrides_are_separate(self):
        self.save('.agents/adapters/codex.json', {'schema_version': 1, 'format': 'standalone-toml', 'max_concurrent_threads_per_session': 3, 'roles': {'reviewer': {'model': 'explicit-model', 'model_reasoning_effort': 'high'}}})
        outputs = render(self.root)
        cfg = tomllib.loads(outputs['.codex/agents/reviewer.toml'])
        self.assertEqual(cfg['model'], 'explicit-model')
        self.assertNotIn('explicit-model', outputs['.opencode/agents/reviewer.md'])

    def test_duplicate_json_role_is_rejected(self):
        path = self.root / '.agents/registry.json'
        path.write_text('{"schema_version": 1, "entrypoint": "root", "roles": {}, "roles": {}}', encoding='utf-8')
        self.assertTrue(any('Duplicate JSON key' in e for e in sync(self.root)))

    def test_non_object_configs_fail_without_writes(self):
        for relative in ('.agents/registry.json', '.agents/adapters/opencode.json',
                         '.agents/adapters/codex.json', 'opencode.json',
                         '.agents/generated-files.json'):
            with self.subTest(path=relative):
                path = self.root / relative
                previous = path.read_text(encoding='utf-8') if path.exists() else None
                path.write_text('[]', encoding='utf-8')
                self.assertTrue(any('Expected JSON object' in e for e in sync(self.root, write=True)))
                self.assertFalse((self.root / '.opencode/agents').exists())
                if previous is None:
                    path.unlink()
                else:
                    path.write_text(previous, encoding='utf-8')

    def test_actual_repository_is_synchronized(self):
        self.assertEqual(sync(Path(__file__).resolve().parents[1]), [])
