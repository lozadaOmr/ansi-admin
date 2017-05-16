from django.db import models
from django.conf import settings

class Playbook(models.Model):
    name = models.CharField(max_length=200)
    inventory = models.CharField(max_length=200, default="hosts")
    user = models.CharField(max_length=200, default="ubuntu")
    directory = models.CharField(max_length=200, editable=False, default="dir")

    def __str__(self):
        return "%s" % self.name

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
    playbook = models.ForeignKey(Playbook, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    item = models.FilePathField(path=settings.PLAYBOOK_DIR, recursive=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = "registries"
