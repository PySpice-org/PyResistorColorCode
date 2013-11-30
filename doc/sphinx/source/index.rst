==========
 Overview
==========

.. include:: /common.txt

.. include:: /meta.txt

.. meta::
   :keywords: PyResistorColorCode, IEC 60062, resistor colour-coding, resistor colour code, electronic colour code,
       resistor color-coding, resistor color code, electronic colour code
   :description: PyResistorColorCode is a Python module that provides some tools to manage IEC 60062
       marking codes for resistors. The associated program ``resistor-decoder`` provides a graphical user
       interface to help user to decode a resistor colour-coding using an inference algorithm.

.. image:: /images/resistor-decoder.png
   :alt: resistor-decoder program's screenshot
   :scale: 70 %
   :align: right

.. itemscope:: SoftwareApplication
    :tag: p
  
    .. IEC 60062 is also for "and capacitors"

    :itemprop:`PyResistorColorCode <name>` is a Python module that provides some tools to manage `IEC 60062
    <http://webstore.iec.ch/webstore/webstore.nsf/artnum/033377!openDocument>`_ marking codes for resistors.

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
resistor colour-coding.

The user and API documentation is hosted on `GitHub <http://fabricesalvaire.github.io/PyResistorColorCode>`_.
  
.. itemscope:: SoftwareApplication
    :tag: p

    The source code is licensed under GPL V3 and is available on :itemprop:`GitHub
    <downloadUrl:https://github.com/FabriceSalvaire/Pyelectronic>`. Also a Python package is
    available on `PyPI <http://pypi.python.org/pypi/PyResistorColorCode>`_.  And the relative
    project page on |ohloh| is located `here <https://www.ohloh.net/p/PyResistorColorCode>`_.

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

===================
 Table of Contents
===================

.. toctree::
  :maxdepth: 2
  :numbered:

  api/PyResistorColorCode.rst

=========
 Indexes
=========

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

.. End
