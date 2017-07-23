from django.test import TestCase
from django.conf import settings
import utils.repository as utils
import utils.slugify as slugify
import mock


class UtilsRepositoryTest(TestCase):

    def setUp(self):
        self.playbook = {
            'username' : 'lozadaomr',
            'repository' : 'ansi-dst',
            'hosts' : 'hosts',
            'user' : 'ubuntu',
        }

    # TODO: Find a way to mock this during test
    def test_generate_command_blank_data(self):
        cmd = utils.generate_command('')
        self.assertEqual(cmd, 'ansible-playbook ')

    def test_generate_command_data(self):
        cmd = utils.generate_command('/opt/app/playbooks/ansi-dst/test.yml')
        expected = 'ansible-playbook test.yml'
        self.assertEqual(cmd, 'ansible-playbook test.yml')

    def test_get_dir_name(self):
        repository_path = utils.get_dir_name(self.playbook['repository'])
        self.assertEqual(repository_path, '/opt/app/playbooks/ansi-dst')

    def test_get_remote_repo_url(self):
        repo_url = utils.get_remote_repo_url(self.playbook['username'],
                self.playbook['repository'])
        self.assertEqual(repo_url, 'https://github.com/lozadaomr/ansi-dst.git')


class UtilsSlugifyTest(TestCase):

    def setUp(self):
        self.data = "Lorem ipsum dolor sit amet"
        self.expected = u'lorem-ipsum-dolor-sit-amet'

    def test_slugify_string_equal(self):
       slug = slugify.to_slug(self.data)
       self.assertEqual(slug, self.expected)
