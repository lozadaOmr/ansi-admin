from django.test import TestCase
from ansible.models import Playbook
from django.core.urlresolvers import reverse

class PlaybookListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Playbook.query_set.create(username='lozadaomr',repository='ansi-dst',
                inventory='hosts',user='ubuntu')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/playbooks/')
        self.assertEqual(resp.status_code, 200)

    def test_view_playbook_list_url_accessible_by_name(self):
        resp = self.client.get(reverse('ansible:playbook-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_playbook_detail_url_accessible_by_name(self):
        resp = self.client.get(reverse(
            'ansible:playbook-detail', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('ansible:playbook-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'ansible/playbook_list.html')

