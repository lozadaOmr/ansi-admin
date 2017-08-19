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


def write_content(pk, slug, data):
   playbook = Playbook.query_set.get(pk=pk)

   #TODO: assume for now file ends with '.yml'
   playbook_file = slug + '.yml'
   playbook_file = os.path.join(playbook.get_dir_name(), playbook_file)
   f = open(playbook_file, "w")
   f.write(data)
   f.close
