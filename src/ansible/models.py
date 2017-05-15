from django.db import models

class Playbook(models.Model):

    class Meta:
        verbose_name_plural = "playbooks"

    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200, default="~/")
    ansible_config = models.CharField(max_length=200, default="~/")
    inventory = models.CharField(max_length=200, default="hosts")
    user = models.CharField(max_length=200, default="ubuntu")

    def __str__(self):
        return "Playbook name: %s" % self.playbook.name
