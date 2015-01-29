#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`lineprof`
==================

.. module:: lineprof
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2014-10-16, 13:56

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

try:
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        """Profiling decorator that can be used for simple
        bottleneck detecting in code.

        Simply append decorator to function to profile::

            In [1]: import mtblack.utils.profiling.lineprof as lprof

            In [2]: def fib(n):
                if n < 2:
                    return n
                else:
                    return fib(n-1) + fib(n-2)

            In [3]: @lprof.do_profile(follow=[fib, ])
            def expensive_function(n):
                return fib(n)

            In [3]: expensive_function(25)

            Timer unit: 4.27653e-07 s

            Total time: 0.281137 s
            File: path/to/file.py
            Function: fib at line 72

            Line #      Hits         Time  Per Hit   % Time  Line Contents
            ==============================================================
                72                                           def fib(n):
                73    242785       309324      1.3     47.1      if n < 2:
                74    121393       139890      1.2     21.3          return n
                75                                               else:
                76    121392       208180      1.7     31.7          return fib(n-1) + fib(n-2)

            Total time: 0.610332 s
            File: path/to/file.py
            Function: expensive_function at line 78

            Line #      Hits         Time  Per Hit   % Time  Line Contents
            ==============================================================
                78                                           @do_profile(follow=[fib,])
                79                                           def expensive_function(n):
                80         1      1427165 1427165.0    100.0      return fib(n)

            Out[3]: 75025

        Reference:
        `https://zapier.com/engineering/profiling-python-boss/
         <https://zapier.com/engineering/profiling-python-boss/>`_

        """
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner
except ImportError:
    def do_profile(follow=[]):
        """Ensures that nothing breaks if decorator is accidentally
        left in production code.
        """
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner
