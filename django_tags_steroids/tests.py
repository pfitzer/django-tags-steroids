from __future__ import unicode_literals

from django.test import TestCase
from django_tags_steroids.templatetags.tagssteroids import *

class CalendarTestCase(TestCase):

    def test_day_name(self):
        self.assertEqual('Monday', day_name(0))
        self.assertRaises(AssertionError, lambda:
            self.assertEqual('Monday', day_name('foo')))

    def test_day_abbr(self):
        self.assertEqual('Fri', day_abbr(4))
        self.assertRaises(AssertionError, lambda:
            self.assertEqual('Monday', day_abbr('foo')))

    def test_month_name(self):
        self.assertEqual('April', month_name(4))
        self.assertRaises(AssertionError, lambda:
            self.assertEqual('April', month_name('foo')))