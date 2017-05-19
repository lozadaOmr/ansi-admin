from django.db import models
from django.conf import settings

class Github (models.Model):
    username = models.CharField(max_length=39)
    repository = models.CharField(max_length=100)

    def __str__(self):
        return self.repository

    class Meta:
        verbose_name_plural = "projects"
