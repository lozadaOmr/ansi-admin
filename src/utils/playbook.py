from django.conf import settings
from ansible.models import Playbook
import os


def content_loader(pk, slug):
    playbook = Playbook.query_set.get(pk=pk)
    playbook_dir = playbook.directory
    # TODO: for now assume without validation
    playbook_file = os.path.join(playbook_dir, slug + '.yml')

    with open(playbook_file, 'r') as f:
        content = f.read()

    return content
