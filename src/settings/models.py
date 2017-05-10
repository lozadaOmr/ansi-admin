from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    playbook_path = models.CharField(max_length=200, default="~/")
    ansible_config_path = models.CharField(max_length=200, default="~/")
    default_inventory = models.CharField(max_length=200, default="hosts")
    default_user = models.CharField(max_length=200, default="ubuntu")
