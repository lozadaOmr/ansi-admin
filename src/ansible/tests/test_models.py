from django.test import TestCase

from ansible.models import Playbook


class PlaybookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Playbook.query_set.create(
            username='lozadaomr',
            repository='ansi-dst',
            inventory='hosts',
            user='ubuntu'
        )

    def test_username_label(self):
        playbook=Playbook.query_set.get(id=1)
        field_label = playbook._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_username_max_length(self):
        playbook=Playbook.query_set.get(id=1)
        max_length = playbook._meta.get_field('username').max_length
        self.assertEquals(max_length,39)
