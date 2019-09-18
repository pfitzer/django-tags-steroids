import os
from setuptools import find_packages, setup

from __version__ import version

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tags-steroids',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Django template tags and filter library.',
    long_description=README,
    url='https://github.com/pfitzer/django-tags-steroids',
    author='Michael Pfister',
    author_email='michael@mp-development.de',
    setup_requires=['Django>=2.2'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
)