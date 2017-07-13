from django.test import TestCase
from django.urls import reverse
from .models import Playbook


class QuestionViewTests(TestCase):
    def test_index_view(self):
        """
        If no playbooks exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('ansible:playbook-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No playbooks yet.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
