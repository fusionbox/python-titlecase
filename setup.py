#!/usr/bin/env python

from setuptools import setup, find_packages
from titlecase import __version__


setup(
    name='titlecase',
    version=__version__,
    description='Python port of John Gruber\'s titlecase.pl',
    author='Stuart Colville, Raymond Wanyoike',
    author_email='raymond.wanyoike@gmail.com',
    long_description=open('README.rst').read(),
    url='https://github.com/raymondwanyoike/python-titlecase',
    packages=find_packages(),
    include_package_data=True,
    keywords='string, formatting, titlecase',
    tests_require=['nose'],
    test_suite='titlecase.tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Text Processing :: Filters',
    ],
    zip_safe=False,
)
