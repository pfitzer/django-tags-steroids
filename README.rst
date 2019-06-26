.. figure:: https://travis-ci.org/pfitzer/django-tags-steroids.svg?branch=master

===================
Django-Tags-Steroid
===================

A collection of usefull template tags and filters for the django framework.
Take a look at the full Documentation_.

Quick Start
-----------

1. Add "django_tags_steroids" to your INSTALLED_APPS setting like this:

::

    INSTALLED_APPS = [
        ...
        'django_tags_steroids',
    ]

Usage
-----

**calender filters**

::

    {% load steroidscal %}

    # day_name
    <p>{{ date.day|day_name }}</p>

    # day_abbr
    <p>{{ date.day|day_abr }}</p>

    # month_name
    <p>{{ date.month|month_name }}</p>

**math filters**

::

    {% load steroidsmath %}

    # get absolute
    <p>{{ -2.541|abs }}</p>

    # addition
    <p>{{ 5|add:3 }}</p>

    # substraction
    <p>{{ 10|sub:5 }}</p>

.. _Documentation: https://django-tags-steroid.readthedocs.io/en/latest/