from django.db import models
from django.conf import settings
from django.core.validators import ValidationError
import git, os, shutil

class QuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            obj.delete()
        super(QuerySet, self).delete(*args, **kwargs)

class Playbook(models.Model):
    username = models.CharField(max_length=39, default="")
    repository = models.CharField(max_length=100, default="")
    inventory = models.CharField(max_length=200, default="hosts")
    user = models.CharField(max_length=200, default="ubuntu")
    directory = models.CharField(max_length=200, editable=False, default="dir")

    query_set = QuerySet.as_manager()

    def __str__(self):
        return self.repository

    def get_remote_url(self):
        return "https://github.com/{0}/{1}.git".format(
                self.username, self.repository
        )

    def get_dir_name(self):
        return os.path.join(settings.PLAYBOOK_DIR, self.repository)

    def clone_repository(self):
        DIR_NAME = self.get_dir_name()
        REMOTE_URL = self.get_remote_url()

        os.mkdir(os.path.join(DIR_NAME))
        repo = git.Repo.init(DIR_NAME)
        origin = repo.create_remote('origin', REMOTE_URL)
        origin.fetch()
        origin.pull(origin.refs[0].remote_head)

    def check_repository_exists(self):
        return os.path.exists(self.get_dir_name())

    def check_inventory_exists(self):
        inventory = self.inventory
        repo_name = self.format_directory()

        os.chdir(settings.PLAYBOOK_DIR + repo_name)
        current_dir = os.getcwd()

        if not os.path.exists(os.path.join(current_dir, inventory)):
            raise ValidationError('Inventory file does not exist')

    def format_directory(self):
        directory = self.repository.lower()
        directory = directory.replace(" ","-")
        return directory

    def rm_repository(self):
        try:
            DIR_NAME = self.get_dir_name()
            shutil.rmtree(DIR_NAME)
        except OSError:
            pass

    def clean(self, *args, **kwargs):
        super(Playbook, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.directory = self.format_directory()
        self.clone_repository()
        self.check_inventory_exists()
        super(Playbook, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.rm_repository()
        super(Playbook, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "playbook"
        verbose_name_plural = "playbooks"

