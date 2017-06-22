from django.conf import settings
from django.forms import ModelForm
from ansible.models import Playbook

class AnsibleForm1(ModelForm):
    class Meta:
        model = Playbook
        fields = ['repository', 'username']


class AnsibleForm2(ModelForm):
    class Meta:
        model = Playbook
        fields = ['inventory', 'user']

