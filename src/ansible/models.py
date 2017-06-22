from django.db import models
from django.conf import settings
from django.core.validators import ValidationError
import git
import os
import shutil


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

    def get_dir_name(self):
        return os.path.join(settings.PLAYBOOK_DIR, self.repository)

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
        super(Playbook, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.rm_repository()
        super(Playbook, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "playbook"
        verbose_name_plural = "playbooks"
