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
        DIR_NAME = self.get_dir_name()
        shutil.rmtree(DIR_NAME)

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

class Github(Repository):
    username = models.CharField(max_length=39)

    def get_remote_url(self):
        return "https://github.com/{0}/{1}.git".format(self.username, self.repository)

    class Meta:
        verbose_name = "github project"
        verbose_name_plural = "github projects"
