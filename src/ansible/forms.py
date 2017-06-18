from django.conf import settings
from django.core.validators import ValidationError
from django.forms import ModelForm
from ansible.models import Github, Playbook
import os

class AnsibleForm1(ModelForm):
    class Meta:
        model = Github
        fields = ['repository', 'username']

    def clean_repository(self):
        if self.check_repository_exists(self.cleaned_data['repository']):
            raise ValidationError("Repository Exists")
        return self.cleaned_data['repository']

    def check_repository_exists(self, repository):
        return os.path.exists(os.path.join(settings.PLAYBOOK_DIR, repository))

class AnsibleForm2(ModelForm):
    class Meta:
        model = Playbook
        fields = ['name', 'inventory', 'user']

