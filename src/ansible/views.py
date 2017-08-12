from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from formtools.wizard.views import SessionWizardView
from ansible.models import Playbook
from .forms import LoginForm, PlaybookEditForm
import utils.repository as utils
import utils.playbook as playbook_utils
import os
import subprocess
import sys


def index(request):
    return HttpResponse("200")


class Login(View):
    # TODO: This needs work
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


class PlaybookListView(ListView):
    model = Playbook

    def get_context_data(self, **kwargs):
        context = super(PlaybookListView, self).get_context_data(**kwargs)
        return context


class PlaybookDetailView(DetailView):
    model = Playbook

    def get_context_data(self, **kwargs):
        context = super(PlaybookDetailView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST.get("playbook_file")
        current_dir = os.path.dirname(data)
        cmd = utils.generate_command(data)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                cwd=current_dir)
        while True:
            line = proc.stdout.readline()
            if line != '':
                print line
            else:
                break
        proc.wait()

        result = proc.stdout.read()
        return HttpResponse(result)


class PlaybookFileView(View):
    template_name = "ansible/playbookfile_detail.html"

    def get(self, request, *args, **kwargs):
        playbook_file = playbook_utils.content_loader(
                self.kwargs['pk'], self.kwargs['slug']
        )
        with open(playbook_file, 'r') as f:
            content = f.read()

        return HttpResponse(content, content_type='text/plain')


class PlaybookFileEditView(View):
    form_class = PlaybookEditForm
    template_name = "ansible/playbookfile_edit.html"
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        playbook_file = playbook_utils.content_loader(
                self.kwargs['pk'], self.kwargs['slug']
        )
        with open(playbook_file, 'r') as f:
            content =  f.read()
        # TODO: Pass content to Form
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
