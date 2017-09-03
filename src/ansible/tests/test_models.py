from django.test import TestCase

from ansible.models import Playbook


class PlaybookModelTest(TestCase):
    fixtures = ['initial_data.json']

    def test_username_label(self):
        playbook=Playbook.query_set.get(id=1)
        field_label = playbook._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_username_max_length(self):
        playbook=Playbook.query_set.get(id=1)
        max_length = playbook._meta.get_field('username').max_length
        self.assertEquals(max_length,39)
