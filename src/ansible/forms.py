from django.forms import ModelForm
from django.core.validators import ValidationError
from ansible.models import Github, Playbook

class AnsibleForm1(ModelForm):
    class Meta:
        model = Github
        fields = ['repository', 'username']

    def clean_repository(self):
        if self.instance.check_repository_exists():
            raise ValidationError('Repository directory already exist')
        return self.cleaned_data

class AnsibleForm2(ModelForm):
    class Meta:
        model = Playbook
        fields = ['name', 'inventory', 'user']

