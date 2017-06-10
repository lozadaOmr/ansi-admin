from django import forms
from django.forms import ModelForm
from ansible.models import Github, Playbook


class AnsibleForm1(ModelForm):
    class Meta:
        model = Github
        fields = ['repository', 'username']

class AnsibleForm2(ModelForm):
    class Meta:
        model = Playbook
        fields = ['name', 'inventory', 'user']

