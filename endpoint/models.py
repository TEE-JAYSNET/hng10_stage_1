from django.db import models
from .models import models
from django.utils import timezone

# Create your models here.


class Stageone(models.Model):
    slack_name = models.CharField(max_length=200)
    current_day = models.CharField(max_length=200)
    utc_time = models.DateTimeField(default=timezone.now)
    track = models.CharField(max_length=200)
    github_file_url = models.URLField(max_length=100)
    github_repo_url = models.URLField(max_length=100)
    status_code = models.IntegerField(default=0)

    def __str__(self):
        return self.slack_name + ' ' + self.track
