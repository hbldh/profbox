#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The setup script for the Mt. Black library.

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>

Created on 2014-02-14, 16:20

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from setuptools import setup, find_packages

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='profbox',
    version="0.1.0",
    author='Henrik Blidh',
    author_email='henrik.blidh@nedomkull.com',
    maintainer='Henrik Blidh',
    maintainer_email='henrik.blidh@nedomkull.com',
    description='Toolbox fo simple profiling in Python.',
    long_description=LONG_DESCRIPTION,
    license='GPLv2',
    url='',
    download_url='',
    platforms=['Linux', 'Mac OSX', 'Windows XP/Vista/7/8'],
    keywords=['Python 2.7', 'Profiling', 'Timing', ],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    packages=find_packages(),
    install_requires=[
        'psutil>=2.0.0',
        'memory_profiler>=0.32',
        'line_profiler>=1.0',
    ],
    dependency_links=[],
    ext_modules=[],
)
