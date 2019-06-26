|TravisLink|_ |PyupLink|_ |PyupBlocker|_

===================
Django-Tags-Steroid
===================

A collection of usefull template tags and filters for the django framework.
Take a look at the full Documentation_.

Quick Start
-----------

1. Add "django_tags_steroids" to your INSTALLED_APPS setting like this:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'django_tags_steroids',
    ]

Usage
-----

**calender filters**

.. code-block:: html

    {% load steroidscal %}

    // day_name
    <p>{{ date.day|day_name }}</p>

    // day_abbr
    <p>{{ date.day|day_abr }}</p>

    // month_name
    <p>{{ date.month|month_name }}</p>

**math filters**

.. code-block:: html

    {% load steroidsmath %}

    // get absolute
    <p>{{ -2.541|abs }}</p>

    // addition
    <p>{{ 5|add:3 }}</p>

    // substraction
    <p>{{ 10|sub:5 }}</p>

.. _Documentation: https://django-tags-steroid.readthedocs.io/en/latest/
.. |TravisLink| image:: https://travis-ci.org/pfitzer/django-tags-steroids.svg?branch=master
.. _TravisLink: https://travis-ci.org/pfitzer/django-tags-steroids
.. |PyupLink| image:: https://pyup.io/repos/github/pfitzer/django-tags-steroids/shield.svg
.. _PyupLink: https://pyup.io/account/repos/github/pfitzer/django-tags-steroids/
.. |PyupBlocker| image:: https://pyup.io/repos/github/pfitzer/django-tags-steroids/python-3-shield.svg
.. _PyupBlocker: https://pyup.io/repos/github/pfitzer/django-tags-steroids/