from django.test import TestCase

from ansible.forms import AnsibleForm1, AnsibleForm2


class AnsibleCreateFormTest(TestCase):

    def test_valid_ansibleform1(self):
        form = AnsibleForm1({
            'repository':'ansi-dst',
            'username':'lozadaomr'
        })
        self.assertTrue(form.is_valid())
        form1 = form.save()
        self.assertEqual(form1.repository, 'ansi-dst')
        self.assertEqual(form1.username, 'lozadaomr')

    def test_valid_ansibleform2(self):
        form = AnsibleForm2({
            'inventory':'hosts',
            'user':'ubuntu'
        })
        self.assertTrue(form.is_valid())
        form2 = form.save()
        self.assertEqual(form2.inventory, 'hosts')
        self.assertEqual(form2.user, 'ubuntu')

    def test_blank_ansibleform1(self):
        form = AnsibleForm1({
            'repository':'',
            'username':''
        })
        self.assertFalse(form.is_valid())

    def test_blank_ansibleform2(self):
        form = AnsibleForm2({
            'inventory':'',
            'user':''
        })
        self.assertFalse(form.is_valid())

    def test_blank_error_message_ansibleform1(self):
        error_msg = [u'This field is required.']
        form = AnsibleForm1({
            'repository':'',
            'username':''
        })
        self.assertEqual(form.errors.get('repository', None), error_msg)
        self.assertEqual(form.errors.get('username', None), error_msg)

    def test_blank_error_message_ansibleform2(self):
        error_msg = [u'This field is required.']
        form = AnsibleForm2({
            'inventory':'',
            'user':''
        })
        self.assertEqual(form.errors.get('inventory', None), error_msg)
        self.assertEqual(form.errors.get('user', None), error_msg)
