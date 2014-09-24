#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.2.1"

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        raise ImportError("Fix: pip install wheel")
    os.system('sudo python setup.py sdist bdist_wheel upload')
    print("Tagging now:")
    os.system("git tag -a v%s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()


readme = open('README.rst').read()


setup(
    name='one',
    version=version,
    description="""Not all nor any. Just the one.""",
    long_description=readme,
    author='Martín Gaitán',
    author_email='gaitan@gmail.com',
    url='https://github.com/mgaitan/one',
    include_package_data=True,
    py_modules=['one'],
    license="BSD",
    zip_safe=False,
    keywords='one',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

)