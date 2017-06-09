from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from formtools.wizard.views import SessionWizardView
from ansible.models import Github

def index(request):
    return HttpResponse("200")

class PlaybookWizard(SessionWizardView):
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Github()
        return self.instance

    def get_form_initial(self, step):
        initial = {}

        if step == '1':
            prev_data = self.storage.get_step_data('0')
            initial['name'] = prev_data['0-repository']
            return self.initial_dict.get(step, initial)
        return self.initial_dict.get(step, {})


    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('ansible/create')
