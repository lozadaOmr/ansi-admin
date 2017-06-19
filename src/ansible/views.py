from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from formtools.wizard.views import SessionWizardView
from ansible.models import Playbook

def index(request):
    return HttpResponse("200")


class PlaybookWizard(SessionWizardView):
    def get_form_initial(self, step):
        initial = {}
        return self.initial_dict.get(step, {})

    def done(self, form_list, form_dict,**kwargs):
        for form in form_list:
            form.save()
        return HttpResponseRedirect('/playbooks')

