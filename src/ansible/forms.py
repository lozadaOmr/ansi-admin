from django.conf import settings
from django.core.validators import ValidationError
from django.forms import ModelForm
from ansible.models import Playbook
import os


def check_path_exists(path, inventory):
    os.chdir(settings.PLAYBOOK_DIR + path)
    current_dir = os.getcwd()
    return os.path.exists(os.path.join(current_dir, inventory))


class AnsibleForm1(ModelForm):
    class Meta:
        model = Playbook
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
        fields = ['inventory', 'user']

    def clean_inventory(self):
        inventory = self.cleaned_data['inventory']
        path = self.initial['prev_data']['repository']
        if check_path_exists(path, inventory):
            raise ValidationError("Inventory not found")
        return self.cleaned_data['inventory']

