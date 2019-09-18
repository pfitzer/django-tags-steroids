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

    // divide
    <p>{{ 10|div:5 }}</p>

    // multiply
    <p>{{ 2|mul:5 }}</p>

**parameter filter**

.. code-block:: html

    {% load steroidsparameters %}

    /**
    * example for usage of param_replace in pagination
    *
    * useful for paginated sites with filters for example
    */
    <nav aria-label="Page navigation example">
        <ul class="pagination">
            {% if page_obj.has_previous %}
                <li class="page-item"><a class="page-link"
                                         href="?{% param_replace page=1 %}">{% trans 'first' %}</a>
                </li>
                <li class="page-item"><a class="page-link"
                                         href="?{% param_replace page=page_obj.previous_page_number %}">{{ page_obj.previous_page_number }}</a>
                </li>
            {% endif %}
            <li class="page-item active"><a class="page-link"
                                            href="?{{ page_obj.number }}">{{ page_obj.number }}</a>
            </li>
            {% if page_obj.has_next %}
                <li class="page-item"><a class="page-link"
                                         href="?{% param_replace page=page_obj.next_page_number %}">{{ page_obj.next_page_number }}</a>
                </li>
                <li class="page-item"><a class="page-link"
                                         href="?{% param_replace page=page_obj.paginator.num_pages %}">{% trans 'last' %}</a>
                </li>
            {% endif %}
        </ul>
    </nav>
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