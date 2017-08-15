from django import forms
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


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class PlaybookEditForm(forms.Form):
    playbook = forms.CharField(widget=forms.Textarea(attrs={'rows':30,'cols':80}))
