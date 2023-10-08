from django.db import models


class Bugs(models.Model):
    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=200)
    report_date = models.DateTimeField("date published")
    status = models.CharField(max_length=200)
