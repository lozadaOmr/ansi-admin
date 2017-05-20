from django.db import models
import git, os

class Github (models.Model):
    username = models.CharField(max_length=39)
    repository = models.CharField(max_length=100)

    def __str__(self):
        return self.repository

    def clone_repository(self):
        DIR_NAME = self.repository
        REMOTE_URL = "https://github.com/{0}/{1}.git".format(self.username, self.repository)

        os.mkdir(DIR_NAME)

        repo = git.Repo.init(DIR_NAME)
        origin = repo.create_remote('origin', REMOTE_URL)
        origin.fetch()
        origin.pull(origin.refs[0].remote_head)

    def save(self, *args, **kwargs):
        self.clone_repository()
        super(Github, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "projects"
