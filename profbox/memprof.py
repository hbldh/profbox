#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`memprof`
==================

.. module:: memprof
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-01-28, 23:25

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os

import psutil
import memory_profiler


do_profile = memory_profiler.profile


def memory_usage_psutil():
    """Return the memory usage of the current process in MB."""

    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem


