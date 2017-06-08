from django import forms


class AnsibleForm1(forms.Form):
    repository = forms.CharField(label='Repository', max_length=100)
    username = forms.CharField(label='Username', max_length=39)

class AnsibleForm2(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    inventory = forms.CharField(label='Inventory', max_length=200)
    user = forms.CharField(label='Remote User', max_length=200)

