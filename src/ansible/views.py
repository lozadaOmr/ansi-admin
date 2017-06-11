from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from formtools.wizard.views import SessionWizardView
from ansible.models import Github, Playbook
import sys


def index(request):
    return HttpResponse("200")


class PlaybookWizard(SessionWizardView):
    def get_form_initial(self, step):
        initial = {}
        if step == '1':
            prev_data = self.storage.get_step_data('0')
            initial['name'] = prev_data['0-repository']
            return self.initial_dict.get(step, initial)

        return self.initial_dict.get(step, {})


    def get_form_step_data(self, form):
        data = {}
        if self.get_form_prefix() == '0':
            github = Github()
            github.repository = form.data.dict()['0-repository']
            github.username = form.data.dict()['0-username']
            github.save()

        if self.get_form_prefix() == '1':
            playbook = Playbook()
            playbook.name = form.data.dict()['1-name']
            playbook.inventory = form.data.dict()['1-inventory']
            playbook.user = form.data.dict()['1-user']
            playbook.save()

        return form.data


    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('/ansible')

