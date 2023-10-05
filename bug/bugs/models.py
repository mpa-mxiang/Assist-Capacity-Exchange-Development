import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Bug(models.Model):
    BUG_TYPES = (
        ('error', 'Error'),
        ('feature', 'New Feature'),
        ('enhancement', 'Enhancement'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )

    description = models.TextField()
    bug_type = models.CharField(max_length=20, choices=BUG_TYPES)
    report_date = models.DateField(auto_now_add=True)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.description[:50] 
    def was_reported_recently(self):
        return self.report_date >= timezone.now() - datetime.timedelta(days=1)
