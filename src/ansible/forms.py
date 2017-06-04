from django import forms


class RepositoryForm(forms.Form):
    repository = forms.CharField(label='Repository', max_length=100)
    username = forms.CharField(label='Username', max_length=39)
