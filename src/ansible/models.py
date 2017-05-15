from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    playbook_path = models.CharField(max_length=200, default="~/")
    ansible_config_path = models.CharField(max_length=200, default="~/")
    default_inventory = models.CharField(max_length=200, default="hosts")
    default_user = models.CharField(max_length=200, default="ubuntu")


class Registry(models.Model):
    class Meta:
        verbose_name_plural = "registries"


    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return "project name: %s" % self.project.project_name
