from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from formtools.wizard.views import NamedUrlSessionWizardView
from ansible.models import Github, Playbook


def index(request):
    return HttpResponse("200")


class PlaybookWizard(NamedUrlSessionWizardView):
    def get_form_initial(self, step):
        initial = {}
        if step == '2':
            prev_data = self.storage.get_step_data('1')
            initial['name'] = prev_data['1-repository']
            return self.initial_dict.get(step, initial)
        return self.initial_dict.get(step, {})

    def get_form_step_data(self, form):
        data = {}
        if self.get_form_prefix() == '1':
            github = Github()
            github.repository = form.data.dict()['1-repository']
            github.username = form.data.dict()['1-username']
            github.save()

        if self.get_form_prefix() == '2':
            playbook = Playbook()
            playbook.name = form.data.dict()['2-name']
            playbook.inventory = form.data.dict()['2-inventory']
            playbook.user = form.data.dict()['2-user']
            playbook.save()
        return form.data

    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('/ansible')

