===================
PyElectronic V0.1.0
===================

:Info: The home page of PyElectronic is located at http://fabricesalvaire.github.com/PyElectronic

About
-----

PyElectronic is a Python module that provide some tools to manage resistor colour codes. The
associated program “resistor-decoder” provides a graphical user interface to help user to decode a
resistor colour code using an inference algorithm. This feature is an enhancement compared to a
program like gresistor which is only a colour code calculator.

.. image:: https://raw.github.com/FabriceSalvaire/PyElectronic/master/doc/sphinx/source/images/resistor-decoder.png

Source Repository
-----------------

The PyElectronic project is hosted at github
http://github.com/FabriceSalvaire/PyElectronic

Requirements
------------

* Python 2.7
* PyQt 4.9

Building & Installing
---------------------

Download and unpack the source, then run the following commands in a terminal::

  python setup.py build
  python setup.py install

Running
-------

Set the terminal environment using::

  source setenv.sh

then run the command::

  bin/resistor-decoder

Packages for Linux
------------------

RPM *.spec* files are provided for Fedora (up to F18), see *spec* directory in the sources.

.. End
