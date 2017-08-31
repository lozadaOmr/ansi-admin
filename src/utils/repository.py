import git
import os

from django.core.validators import ValidationError
from django.conf import settings


def check_path_exists(repository, host_inventory=None):
    if host_inventory:
        os.chdir(settings.PLAYBOOK_DIR + repository)
        current_dir = os.getcwd()
        return os.path.exists(os.path.join(current_dir, host_inventory))

    return os.path.exists(os.path.join(settings.PLAYBOOK_DIR, repository))


def clone_repository(username, repository):
    dir_name = get_dir_name(repository)
    remote_url = get_remote_repo_url(username, repository)

    os.mkdir(os.path.join(dir_name))
    repo = git.Repo.init(dir_name)
    origin = repo.create_remote('origin', remote_url)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)


def generate_command(data):
    playbook_file = os.path.basename(data)

    # TODO: check if using default host inventory
    cmd = []
    cmd.append('ansible-playbook')
    cmd.append(playbook_file)
    return ' '.join(cmd)


def get_dir_name(repository):
    return os.path.join(settings.PLAYBOOK_DIR, repository)


def get_remote_repo_url(username, repository):
    return 'https://github.com/{0}/{1}.git'.format(
        username, repository
    )


def validate_repository(repository):
    if check_path_exists(repository):
        raise ValidationError('Repository already exists')


def validate_inventory(repository, inventory):
    if not check_path_exists(repository, inventory):
        raise ValidationError('Inventory not found')
