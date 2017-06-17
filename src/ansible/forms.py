from django.forms import ModelForm
from django.core.validators import ValidationError
from ansible.models import Github, Playbook
from django.conf import settings
import os

class AnsibleForm1(ModelForm):
    class Meta:
        model = Github
        fields = ['repository', 'username']

    def clean_repository(self):
        # TODO: move validation to validators.py
        if self.check_repository_exists():
            raise ValidationError('Repository directory already exist')
        return self.cleaned_data

    def check_repository_exists(self):
        return os.path.exists(os.path.join(settings.PLAYBOOK_DIR, self.cleaned_data['repository']))

class AnsibleForm2(ModelForm):
    class Meta:
        model = Playbook
        fields = ['name', 'inventory', 'user']

