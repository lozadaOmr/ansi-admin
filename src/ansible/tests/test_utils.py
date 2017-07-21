from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.validators import ValidationError
from django.conf import settings
from ansible.models import Playbook
import utils.repository as utils
import utils.slugify as slugify
import shutil


class UtilsRepositoryTest(TestCase):

    def setUp(self):
        self.playbook = Playbook.query_set.get(id=1)

    @classmethod
    def setUpTestData(cls):
        Playbook.query_set.create(username='lozadaomr',repository='ansi-dst',
                inventory='hosts',user='ubuntu')

    def test_clone_repository(self):
        utils.clone_repository(self.playbook.username, self.playbook.repository)
        repo_path = os.path.exists(os.path.join(settings.PLAYBOOK_DIR, self.playbook.repository)
        self.assertTrue(repo_path)

    # TODO: Find a way to mock this during test
    def test_generate_command_blank_data(self):
        cmd = utils.generate_command('')
        self.assertEqual(cmd, 'ansible-playbook ')

    def test_generate_command_data(self):
        cmd = utils.generate_command('/opt/app/playbooks/ansi-dst/test.yml')
        expected = 'ansible-playbook test.yml'
        self.assertEqual(cmd, 'ansible-playbook test.yml')

    def test_get_dir_name(self):
        repository_path = utils.get_dir_name(self.playbook.repository)
        self.assertEqual(repository_path, '/opt/app/playbooks/ansi-dst')

    def test_get_remote_repo_url(self):
        repo_url = utils.get_remote_repo_url(self.playbook.username,
                self.playbook.repository)
        self.assertEqual(repo_url, 'https://github.com/lozadaomr/ansi-dst.git')

    def test_validate_repository_raise_validation_error(self):
        with self.assertRaises(ValidationError):
            utils.validate_repository(self.playbook.repository)

    def test_validate_inventory_raise_validation_error(self):
        with self.assertRaises(ValidationError):
            utils.validate_inventory(self.playbook.repository,
                    '/opt/app/playbooks/ansi-dst/none.yml')


class UtilsSlugifyTest(TestCase):

    def setUp(self):
        self.data = "Lorem ipsum dolor sit amet"
        self.expected = u'lorem-ipsum-dolor-sit-amet'

    def test_slugify_string_equal(self):
       slug = slugify.to_slug(self.data)
       self.assertEqual(slug, self.expected)
