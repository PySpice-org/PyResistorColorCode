.. include:: common.txt

==============
 Installation
==============

You can install from `Pypy <https://pypi.python.org/pypi/PyResistorColorCode>`_::

  pip install PyResistorColorCode

but pip is unable to install `PyQt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_. If
you are on Linux then install the corresponding package else download the installer from `PyQt
download page <http://www.riverbankcomputing.co.uk/software/pyqt/download>`_.

Source Repository
-----------------

The source code is licensed under GPL V3 and is hosted on `GitHub
<https://github.com/FabriceSalvaire/PyResistorColorCode>`_.  Also a Python package is available on `PyPI
<http://pypi.python.org/pypi/PyResistorColorCode>`_. And the relative project page on |ohloh| is
located on the `ohloh project page <https://www.ohloh.net/p/PyResistorColorCode>`_.

Requirements
------------

* Python 2.7
* PyQt 4.8

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
