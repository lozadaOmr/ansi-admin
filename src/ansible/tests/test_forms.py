from django.test import TestCase
from ansible.forms import AnsibleForm1, AnsibleForm2

class AnsibleCreateFormTest(TestCase):
    def test_valid_ansibleform1(self):
        form = AnsibleForm1({
            'repository': "ansi-dst",
            'username': "lozadaomr"
        })
        self.assertTrue(form.is_valid())
        form1 = form.save()
        self.assertEqual(form1.repository, "ansi-dst")
        self.assertEqual(form1.username, "lozadaomr")

    def test_valid_ansibleform2(self):
        form = AnsibleForm2({
            'inventory': "hosts",
            'user': "ubuntu"
        })
        self.assertTrue(form.is_valid())
        form2 = form.save()
        self.assertEqual(form2.inventory, "hosts")
        self.assertEqual(form2.user, "ubuntu")
