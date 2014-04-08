.. include:: common.txt

==============
 Installation
==============

You can install from `Pypy <https://pypi.python.org>`_::

  pip install PyResistorColorCode

Source Repository
-----------------

The source code is licensed under GPL V3 and is hosted on `GitHub
<https://github.com/FabriceSalvaire/Pyelectronic>`_.  Also a Python package is available on `PyPI
<http://pypi.python.org/pypi/PyResistorColorCode>`_. And the relative project page on |ohloh| is
located `here <https://www.ohloh.net/p/PyResistorColorCode>`_.

Requirements
------------

* Python 2.7
* PyQt 4.9

Manual Installation
-------------------

Alternatively you can download the source from Github or Pypi and run the following commands in a
terminal within the source directory::

  python setup.py build
  python setup.py install

Running
-------

Set the terminal environment using::

  source setenv.sh

then run the command::

  bin/resistor-decoder

Package for Linux
-----------------

RPM *.spec* files are provided for Fedora (up to F18), see *spec* directory in the sources.

.. End
