from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import View
from formtools.wizard.views import SessionWizardView
from ansible.models import Playbook
from .forms import LoginForm
import utils.repository as utils


def index(request):
    return HttpResponse("200")


class Login(View):
    form_class = LoginForm
    template_name = 'login_template.html'

    def get(self, request, *args, **kwargs):
        self.form_class()
        return render(request, self.template_name, {'form': form})


class PlaybookWizard(SessionWizardView):
    prev_form_data = {}

    def get_form_initial(self, step):
        initial = {}

        if step == '1':
            prev_data = self.get_cleaned_data_for_step('0')
            result = super(PlaybookWizard, self).get_form_initial(step)
            result['prev_data'] = {}
            result['prev_data']['repository'] = prev_data['repository']
            return result
        return self.initial_dict.get(step, {})

    def get_form_step_data(self, form):
        if self.get_form_prefix() == '0':
            self.prev_form_data['repository'] = form.data.dict()['0-repository']
            self.prev_form_data['username'] = form.data.dict()['0-username']

        if self.get_form_prefix() == '1':
            utils.validate_repository(self.prev_form_data['repository'])
            utils.clone_repository(
                    self.prev_form_data['username'],
                    self.prev_form_data['repository']
            )
            utils.validate_inventory(
                    self.prev_form_data['repository'],
                    form.data.dict()['1-inventory']
            )
            playbook = Playbook()
            playbook.username = self.prev_form_data['username']
            playbook.repository = self.prev_form_data['repository']
            playbook.inventory = form.data.dict()['1-inventory']
            playbook.user = form.data.dict()['1-user']
            playbook.save()
        return form.data

    def done(self, form_list, form_dict, **kwargs):
        return HttpResponseRedirect('/playbooks')

