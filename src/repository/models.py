from django.db import models

class Project(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repo_url = models.URLField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'projects'

