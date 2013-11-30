===================
PyResistorColorCode V0.1.0
===================

:Info: The user and API documentation is hosted `here <http://fabricesalvaire.github.io/PyResistorColorCode>`_.

About
-----

PyResistorColorCode is a Python module that provides some tools to manage `IEC 60062
<http://webstore.iec.ch/webstore/webstore.nsf/artnum/033377!openDocument>`_ marking codes for
resistors.

The associated program **resistor-decoder** provides a graphical user interface to help user to
decode a resistor colour-coding using an inference algorithm. This feature is an enhancement
compared to a program like **gresistor** which is only a colour-coding calculator.

I started to develop this software a day where I had to sort a lot of unsorted resistors in a
jumble. Resistors colour-coding using no more than 3 bands (2 digits and a multiplier) are no too
difficult to decode when a person is experienced. But for more accurate resistors, it is more
tricky. Another difficulty arises when it is difficult to recognise the colour of a band, due to an
inappropriate colour contrast or tone. For strange colour-coding we can in last resort use an
Ohmmeter to measure the resistance value. But it doesn't respond to the question what is the
specification of this resistor: tolerance, temperature coefficient, etc. For all theses reasons, I
developed an inference algorithm coupled to an graphical user interface to help user to decode

.. image:: https://raw.github.com/FabriceSalvaire/PyResistorColorCode/master/doc/sphinx/source/images/resistor-decoder.png

Inference Algorithm
-------------------

The inference algorithm works as follow:

* code orientation (left-right or right-left) doesn't matter,
* unset bands are not take into account,
* at least 3 colours must be provided: 2 digits and the multiplier,
* colour band are interpreted by priority as:

 #. resistance value,
 #. resistance tolerance,
 #. temperature coefficient,

* the resistance value must exists in a IEC 60063 series: E6, E12, E48, E96, E192,
* the resistance tolerance must be defined if there is a colour band assigned to it. 

When there is more than one hypothesis for the given input, the hypotheses are sorted by ascending
precision (series).

Source Repository
-----------------

.. |ohloh| image:: https://www.ohloh.net/accounts/230426/widgets/account_tiny.gif
   :target: https://www.ohloh.net/accounts/fabricesalvaire
   :alt: Fabrice Salvaire's Ohloh profile
   :height: 15px
   :width:  80px

The source code is licensed under GPL V3 and is available on `GitHub
<https://github.com/FabriceSalvaire/Pyelectronic>`_.  And the relative project page on |ohloh| is
located `here <https://www.ohloh.net/p/PyResistorColorCode>`_.

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
