from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    playbook_path = models.CharField(max_length=200)
