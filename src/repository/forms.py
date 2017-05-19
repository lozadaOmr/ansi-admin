from django import forms

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        widgets = {
            'password': forms.PasswordInput(),
        }
