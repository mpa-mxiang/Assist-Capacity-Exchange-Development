import datetime

from django.db import models
from django.utils import timezone

class Bugs(models.Model):
    description = models.CharField(max_length=200)
    report_date = models.DateTimeField("date published", default=timezone.now)
    bug_type = [
        ('error', "Error"),
        ('new_feature', "New Feature"),
        ('enhancement', "Enhancement"),
        ('good_first_bug', "Good First Bug"),
        ('others', "Others"),
    ]
    report_date = models.DateTimeField("date published")
    status = [
        ('to_do', "To Do"),
        ('in_progress', "In Progress"),
        ('done', "Done"),
        ('archive', "Archive"),
    ]
    def __str__(self):
        return self.bug_type
    def was_published_recently(self):
        return self.report_date >= timezone.now() - datetime.timedelta(days=1)