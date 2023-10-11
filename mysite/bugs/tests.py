import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Bugs


class BugsModelTests(TestCase):
    def test_was_published_recently_with_future_bug(self):
        """
        was_published_recently() returns False for bugs whose report_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_bug = Bugs(report_date=time)
        self.assertIs(future_bug.was_published_recently(), False)
    def test_was_published_recently_with_old_bug(self):
        """
        was_published_recently() returns False for bugs whose report_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_bug = Bugs(report_date=time)
        self.assertIs(old_bug.was_published_recently(), False)


    def test_was_published_recently_with_recent_bug(self):
        """
        was_published_recently() returns True for bugs whose report_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_bug = Bugs(report_date=time)
        self.assertIs(recent_bug.was_published_recently(), True)
    def test_bug_str_method(self):
        """
        __str__() method should return a string representation of the bug's type.
        """
        bug = Bugs(bug_type="Test Bug")
        self.assertEqual(str(bug), "Test Bug")
