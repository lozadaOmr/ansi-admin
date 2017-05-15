from django.db import models
from django.conf import settings

class Playbook(models.Model):

    default_path = settings.PLAYBOOK_DIR

    name = models.CharField(max_length=200)
    inventory = models.CharField(max_length=200, default="hosts")
    user = models.CharField(max_length=200, default="ubuntu")

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = "playbooks"
