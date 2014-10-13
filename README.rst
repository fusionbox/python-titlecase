================
Python TitleCase
================

Titlecase is a port of John Gruber's titlecase.pl:
`http://daringfireball.net/2008/05/title_case <http://daringfireball.net/2008/05/title_case>`_

This filter changes all words to Title Caps, and attempts to be clever about
*un*\capitalizing SMALL words like a/an/the in the input.

The list of "SMALL words" which are not capped comes from the New York Times
Manual of Style, plus 'vs' and 'v'.

Installation
============

Using ``pip``::

    pip install "git+https://github.com/raymondwanyoike/python-titlecase"

Usage
=====

To use it is as simple as::

    >>> from titlecase import titlecase
    >>> titlecase('it\'s a beautiful thing, the destruction of words')
    "It's a Beautiful Thing, the Destruction of Words"
