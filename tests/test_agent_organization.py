import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('organization', Path(__file__).resolve().parents[1] / 'scripts/check_agent_organization.py')
organization = importlib.util.module_from_spec(spec)
spec.loader.exec_module(organization)


class OrganizationTests(unittest.TestCase):
    def agents(self):
        return {
            'root': dict(name='root', mode='primary', reportsto='null', scope='route'),
            'lead': dict(name='lead', mode='subagent', reportsto='root', scope='coordinate'),
            'expert': dict(name='expert', mode='subagent', reportsto='lead', scope='review'),
        }

    def test_valid_tree(self):
        self.assertEqual(organization.validate(self.agents(), 'root'), [])

    def test_missing_mode(self):
        agents = self.agents()
        del agents['expert']['mode']
        self.assertTrue(organization.validate(agents, 'root'))

    def test_second_primary(self):
        agents = self.agents()
        agents['expert']['mode'] = 'primary'
        self.assertTrue(organization.validate(agents, 'root'))

    def test_unknown_parent(self):
        agents = self.agents()
        agents['expert']['reportsto'] = 'missing'
        self.assertTrue(organization.validate(agents, 'root'))

    def test_cycle(self):
        agents = self.agents()
        agents['lead']['reportsto'] = 'expert'
        self.assertTrue(any('cycle' in e for e in organization.validate(agents, 'root')))

    def test_depth(self):
        agents = self.agents()
        agents['leaf'] = dict(name='leaf', mode='subagent', reportsto='expert', scope='leaf')
        self.assertTrue(any('three nodes' in e for e in organization.validate(agents, 'root')))

    def test_nested_metadata_not_top_level(self):
        self.assertEqual(organization.read_fields('---\nname: real\npermissions:\n  name: nested\n---\nbody')['name'], 'real')

    def test_malformed_manifest(self):
        with self.assertRaises(ValueError):
            organization.read_fields('No manifest')

    def test_hyphens_inside_description_do_not_end_frontmatter(self):
        fields = organization.read_fields('---\ndescription: before---after\nmodel: vendor/model\n---\nbody')
        self.assertEqual(fields['model'], 'vendor/model')

    def test_repository_roster(self):
        self.assertEqual(organization.check(Path(__file__).resolve().parents[1]), [])
