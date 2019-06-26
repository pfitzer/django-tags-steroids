|TravisLink| |PyupLink| |PyupBlocker| |License| |Docs|

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

.. _Documentation: https://django-tags-steroids.readthedocs.io/en/latest/
.. |TravisLink| image:: https://travis-ci.org/pfitzer/django-tags-steroids.svg?branch=master
    :target: https://travis-ci.org/pfitzer/django-tags-steroids
    :alt: Travis-Ci
.. |PyupLink| image:: https://pyup.io/repos/github/pfitzer/django-tags-steroids/shield.svg
    :target: https://pyup.io/account/repos/github/pfitzer/django-tags-steroids/
    :alt: PyUp
.. |PyupBlocker| image:: https://pyup.io/repos/github/pfitzer/django-tags-steroids/python-3-shield.svg
    :target: https://pyup.io/repos/github/pfitzer/django-tags-steroids/
    :alt: PyUp
.. |License| image:: https://img.shields.io/github/license/pfitzer/django-tags-steroids.svg
    :target: https://github.com/pfitzer/django-tags-steroids/blob/master/LICENSE
    :alt: License
.. |Docs| image:: https://readthedocs.org/projects/django-tags-steroids/badge/?version=latest&style=flat
    :target: https://django-tags-steroids.readthedocs.io/en/latest/
    :alt: Read the Docs