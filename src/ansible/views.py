from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from formtools.wizard.views import SessionWizardView
from ansible.models import Github

def index(request):
    return HttpResponse("200")

def create(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            project = Github()
            project.repository = form.cleaned_data['repository']
            project.username = form.cleaned_data['username']
            project.save()
            # Redirect here for now
            return HttpResponseRedirect('create')
    else:
        form = RepositoryForm()
    return render(request, 'ansible/create.html', {'form': form})

class PlaybookWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('create')
