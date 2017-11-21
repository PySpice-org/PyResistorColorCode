.. -*- Mode: rst -*-

.. -*- Mode: rst -*-

..
   |PyResistorColorCodeUrl|
   |PyResistorColorCodeHomePage|_
   |PyResistorColorCodeDoc|_
   |PyResistorColorCode@github|_
   |PyResistorColorCode@readthedocs|_
   |PyResistorColorCode@readthedocs-badge|
   |PyResistorColorCode@pypi|_

.. |ohloh| image:: https://www.openhub.net/accounts/230426/widgets/account_tiny.gif
   :target: https://www.openhub.net/accounts/fabricesalvaire
   :alt: Fabrice Salvaire's Ohloh profile
   :height: 15px
   :width:  80px

.. |PyResistorColorCodeUrl| replace:: https://fabricesalvaire.github.io/PyResistorColorCode

.. |PyResistorColorCodeHomePage| replace:: PyResistorColorCode Home Page
.. _PyResistorColorCodeHomePage: https://fabricesalvaire.github.io/PyResistorColorCode

.. |PyResistorColorCode@readthedocs-badge| image:: https://readthedocs.org/projects/PyResistorColorCode/badge/?version=latest
   :target: http://PyResistorColorCode.readthedocs.org/en/latest

.. |PyResistorColorCode@github| replace:: https://github.com/FabriceSalvaire/PyResistorColorCode
.. .. _PyResistorColorCode@github: https://github.com/FabriceSalvaire/PyResistorColorCode

.. |PyResistorColorCode@pypi| replace:: https://pypi.python.org/pypi/PyResistorColorCode
.. .. _PyResistorColorCode@pypi: https://pypi.python.org/pypi/PyResistorColorCode

.. |Build Status| image:: https://travis-ci.org/FabriceSalvaire/PyResistorColorCode.svg?branch=master
   :target: https://travis-ci.org/FabriceSalvaire/PyResistorColorCode
   :alt: PyResistorColorCode build status @travis-ci.org

.. |Pypi Version| image:: https://img.shields.io/pypi/v/PyResistorColorCode.svg
   :target: https://pypi.python.org/pypi/PyResistorColorCode
   :alt: PyResistorColorCode last version

.. |Pypi License| image:: https://img.shields.io/pypi/l/PyResistorColorCode.svg
   :target: https://pypi.python.org/pypi/PyResistorColorCode
   :alt: PyResistorColorCode license

.. |Pypi Python Version| image:: https://img.shields.io/pypi/pyversions/PyResistorColorCode.svg
   :target: https://pypi.python.org/pypi/PyResistorColorCode
   :alt: PyResistorColorCode python version

..  coverage test
..  https://img.shields.io/pypi/status/Django.svg
..  https://img.shields.io/github/stars/badges/shields.svg?style=social&label=Star

.. End
.. -*- Mode: rst -*-

.. |Python| replace:: Python
.. _Python: http://python.org

.. |PyPI| replace:: PyPI
.. _PyPI: https://pypi.python.org/pypi

.. |Sphinx| replace:: Sphinx
.. _Sphinx: http://sphinx-doc.org

=====================
 PyResistorColorCode
=====================

|Pypi License|
|Pypi Python Version|

|Pypi Version|

Overview
========

.. -*- Mode: rst -*-

PyResistorColorCode is a Python module that provides some tools to manage `IEC 60062
<http://webstore.iec.ch/webstore/webstore.nsf/artnum/033377!openDocument>`_ marking codes for
resistors.

.. IEC 60062 is also for "and capacitors"

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

.. The user and API documentation is hosted `here <http://fabricesalvaire.github.io/PyResistorColorCode>`_.

.. image:: https://raw.github.com/FabriceSalvaire/PyResistorColorCode/master/doc/sphinx/source/images/resistor-decoder.png

Inference Algorithm
-------------------

.. -*- Mode: rst -*-

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

.. End

Where is the Documentation ?
----------------------------

The documentation is available on the |PyResistorColorCodeHomePage|_.

How to install it ?
-------------------

Look at the `installation <@project_url@/installation.html>`_ section in the documentation.

Credits
=======

Authors: `Fabrice Salvaire <http://fabrice-salvaire.fr>`_
