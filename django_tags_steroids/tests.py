from __future__ import unicode_literals

from django.test import TestCase
from django_tags_steroids.templatetags.steroidscal import *
from django_tags_steroids.templatetags.steroidsmath import *

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

class MathTestCase(TestCase):

    def test_absolute(self):
        self.assertEqual(1.25, absolute('-1.25'))
        self.assertEqual(1.587, absolute(-1.587))

    def test_sub(self):
        self.assertEqual(2, sub(8, 6))
        self.assertEqual(5, sub('8', '3'))

    def test_add(self):
        self.assertEqual(5, add(2, 3))
        self.assertEqual(8, add('5', '3'))

    def test_multiply(self):
        self.assertEqual(20, mul(4, 5))
        self.assertEqual(16, mul('4', '4'))

    def test_divide(self):
        self.assertEqual(4.00, div(20, 5))
        self.assertEqual(6.85, div(27.4, 4))