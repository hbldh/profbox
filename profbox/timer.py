#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`timer`
==================

.. module:: timer
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-01-28, 22:04

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import time


def timefunc(f):
    """Simple Timer decorator.

    Reference:
        `https://zapier.com/engineering/profiling-python-boss/
         <https://zapier.com/engineering/profiling-python-boss/>`_

    .. code::

        @timefunc
        def expensive_function():
            for x in get_number():
                i = x ^ x ^ x
            return 'some result!'

    >> result = expensive_function()
    >> # expensive_function took 0.72583088875 seconds

    """
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'seconds')
        return result
    return f_timer


class WithTimer(object):
    """A Timer tool used directly in code.

    Reference:
    `https://zapier.com/engineering/profiling-python-boss/
     <https://zapier.com/engineering/profiling-python-boss/>`_

    .. code::

        # prints something like:
        # fancy thing done with something took 0.582462072372 seconds
        # fancy thing done with something else took 1.75355315208 seconds
        # fancy thing finished took 1.7535982132 seconds
        with WithTimer('fancy thing') as timer:
            expensive_function()
            timer.checkpoint('done with something')
            expensive_function()
            expensive_function()
            timer.checkpoint('done with something else')

    """
    def __init__(self, name=''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=''):
        print('{timer} {checkpoint} took {elapsed} seconds'.format(
            timer=self.name,
            checkpoint=name,
            elapsed=self.elapsed,
        ).strip())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')
