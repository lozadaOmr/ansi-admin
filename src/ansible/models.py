from django.db import models
from django.conf import settings
import git, os, shutil

class QuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            obj.delete()
        super(QuerySet, self).delete(*args, **kwargs)

class Repository(models.Model):
    repository = models.CharField(max_length=100)

    objects = QuerySet.as_manager()

    def __str__(self):
        return self.repository

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

    def rm_repository(self):
        try:
            DIR_NAME = self.get_dir_name()
            shutil.rmtree(DIR_NAME)
        except OSError:
            pass


    def save(self, *args, **kwargs):
        self.clone_repository()
        super(Repository, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.rm_repository()
        super(Repository, self).delete(*args, **kwargs)

    class Meta:
        abstract = True
        verbose_name = "project"
        verbose_name_plural = "projects"

class Playbook(models.Model):
    name = models.CharField(max_length=200)
    inventory = models.CharField(max_length=200, default="hosts")
    user = models.CharField(max_length=200, default="ubuntu")
    directory = models.CharField(max_length=200, editable=False, default="dir")

    def __str__(self):
        return self.name

    def format_directory(self):
        directory = self.name.lower()
        directory = directory.replace(" ","-")
        return directory

    def save(self, *args, **kwargs):
        self.directory = self.format_directory()
        super(Playbook, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "playbooks"


class Registry(models.Model):
    playbook = models.ForeignKey("Playbook", default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    file_path = models.FilePathField(path=settings.PLAYBOOK_DIR, recursive=True)

    def __str__(self):
        return self.name

    def modify_item_file_path(self):
        return self.item

    def save(self, *args, **kwargs):
        self.item = self.modify_item_file_path()
        super(Registry, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "registries"

class Github(Repository):
    username = models.CharField(max_length=39)

    def get_remote_url(self):
        return "https://github.com/{0}/{1}.git".format(self.username, self.repository)

    class Meta:
        verbose_name = "github project"
        verbose_name_plural = "github projects"

class Gitlab(Repository):
    username = models.CharField(max_length=255)
    repository_owner = models.CharField(max_length=255)

    def get_remote_url(self):
        return "https://{0}@gitlab.com/{1}/{2}.git".format(
                self.username, self.repository_owner, self.repository)

    class Meta:
        verbose_name = "gitlab project"
        verbose_name_plural = "gitlab projects"
