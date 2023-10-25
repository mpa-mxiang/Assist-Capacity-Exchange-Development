import datetime
from django.db import models
from django.utils import timezone

class Bugs(models.Model):
    description = models.CharField(max_length=200)
    report_date = models.DateTimeField("date published", default=timezone.now)
    BUG_TYPE_CHOICES = [
        ('error', "Error"),
        ('new_feature', "New Feature"),
        ('enhancement', "Enhancement"),
        ('good_first_bug', "Good First Bug"),
        ('others', "Others"),
    ]
    bug_type = models.CharField(max_length=20, choices=BUG_TYPE_CHOICES)
    STATUS_CHOICES = [
        ('to_do', "To Do"),
        ('in_progress', "In Progress"),
        ('done', "Done"),
        ('archive', "Archive"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.bug_type
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.report_date <= now