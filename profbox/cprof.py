#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`cprof`
==================

.. module:: cprof
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2014-10-16, 13:42

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

try:
    import cProfile as profile_module
except ImportError:
    import profile as profile_module


def do_profile(func):
    """Profiling decorator that can be used for simple
    bottleneck detecting in code.

    Simply append decorator to function to profile::

        In [1]: import profbox.cprof as cprof

        In [2]:
        @cprof.do_profile
        def expensive_function(n):
            def fib(n):
                if n < 2:
                    return n
                else:
                    return fib(n-1) + fib(n-2)
            return fib(n)

        In [3]: expensive_function(25)

        242787 function calls (3 primitive calls) in 0.080 seconds

        Ordered by: standard name

        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
             1    0.000    0.000    0.080    0.080 cprof.py:57(expensive_function)
      242785/1    0.080    0.000    0.080    0.080 cprof.py:59(fib)
             1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

        Out[3]: 75025

    Reference:
    `https://zapier.com/engineering/profiling-python-boss/
     <https://zapier.com/engineering/profiling-python-boss/>`_

    """
    def profiled_func(*args, **kwargs):
        profile = profile_module.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func
