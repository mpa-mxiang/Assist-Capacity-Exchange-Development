import datetime

from django.db import models
from django.utils import timezone

class Bugs(models.Model):
    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=200)
    report_date = models.DateTimeField("date published", default=timezone.now)
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.bug_type
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.report_date <= now