from django import forms
from django.core.validators import ValidationError
from django.conf import settings
from django.forms import ModelForm
from ansible.models import Playbook
import utils.playbook as playbook_utils
import os

class AnsibleForm1(ModelForm):
    class Meta:
        model = Playbook
        fields = ['repository', 'username']


class AnsibleForm2(ModelForm):
    class Meta:
        model = Playbook
        fields = ['inventory', 'user']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class PlaybookFileForm(forms.Form):
    filename = forms.CharField(label='Filename', max_length=100)
    playbook = forms.CharField(widget=forms.Textarea(attrs={'rows':30,'cols':80}))

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(PlaybookFileForm, self).__init__(*args, **kwargs)

    def clean_filename(self):
        data = playbook_utils.append_extension(self.cleaned_data['filename'])
        playbook = Playbook.query_set.get(pk=self.pk)
        playbook_dir = playbook.directory
        playbook_file_path = os.path.join(playbook_dir, data)
        if os.path.exists(playbook_file_path):
            raise forms.ValidationError("Filename already used")
        return data
