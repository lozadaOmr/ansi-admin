from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from formtools.wizard.views import SessionWizardView
from ansible.models import Playbook
import git
import os

def index(request):
    return HttpResponse("200")


def clone_repository(username, repository):
    dir_name = get_dir_name(repository)
    remote_url = get_remote_repo_url(username, repository)

    os.mkdir(os.path.join(dir_name))
    repo = git.Repo.init(dir_name)
    origin = repo.create_remote('origin', remote_url)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)


def get_dir_name(repository):
    return os.path.join(settings.PLAYBOOK_DIR, repository)


def get_remote_repo_url(username, repository):
    return "https://github.com/{0}/{1}.git".format(
            username, repository
    )


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
            playbook = Playbook()
            playbook.username = self.prev_form_data['username']
            playbook.repository = self.prev_form_data['repository']
            playbook.inventory = form.data.dict()['1-inventory']
            playbook.user = form.data.dict()['1-user']
            playbook.save()

            clone_repository(
                    self.prev_form_data['username'],
                    self.prev_form_data['repository']
            )
        return form.data

    def done(self, form_list, form_dict, **kwargs):
        return HttpResponseRedirect('/playbooks')

