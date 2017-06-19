from django.conf import settings
from django.core.validators import ValidationError
from django.forms import ModelForm
from ansible.models import Playbook
import os

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
        if not self.check_inventory_exists(self.cleaned_data['inventory']):
            raise ValidationError("Inventory not found")
        return self.cleaned_data['inventory']

    def check_inventory_exists(self, inventory):
        return os.path.exists(os.path.join(settings.PLAYBOOK_DIR, inventory))

