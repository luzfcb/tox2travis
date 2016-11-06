========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |codecov|
        | |landscape|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/tox2travis/badge/?style=flat
    :target: https://readthedocs.org/projects/tox2travis
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/luzfcb/tox2travis.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/luzfcb/tox2travis

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/luzfcb/tox2travis?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/luzfcb/tox2travis

.. |codecov| image:: https://codecov.io/github/luzfcb/tox2travis/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/luzfcb/tox2travis

.. |landscape| image:: https://landscape.io/github/luzfcb/tox2travis/master/landscape.svg?style=flat
    :target: https://landscape.io/github/luzfcb/tox2travis/master
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/tox2travis.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/tox2travis

.. |downloads| image:: https://img.shields.io/pypi/dm/tox2travis.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/tox2travis

.. |wheel| image:: https://img.shields.io/pypi/wheel/tox2travis.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/tox2travis

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tox2travis.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/tox2travis

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tox2travis.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/tox2travis


.. end-badges

Read tox.ini and generate 'matriz' section of .travis.yml

* Free software: BSD license

Installation
============

::

    pip install tox2travis

Documentation
=============

https://tox2travis.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
