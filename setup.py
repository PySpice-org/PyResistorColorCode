#! /usr/bin/env python

####################################################################################################
#
# PyElectronic
# Copyright (C) 2012 Salvaire Fabrice
#
####################################################################################################

####################################################################################################

import os
from distutils.core import setup
#from setuptools import setup

####################################################################################################

# Utility function to read the README file.
# Used for the long_description.
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

####################################################################################################

setup(name='PyElectronic',
      version='1.0',
      author='Fabrice Salvaire',
      author_email='fabrice.salvaire@orange.fr',
      description='Simple Morpho-Mathematics',
      license = "GPLv3",
      keywords = "electronic tools",
      url='http://fabrice-salvaire.pagesperso-orange.fr/software/index.html',
      scripts=['bin/colour-resistor-decoder'],
      packages=['PyElectronic'],
      long_description=read('README'),
      # cf. http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Topic :: Scientific/Engineering",
          "Intended Audience :: Education",
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          ],
          install_requires=[
              'pyqt>=4.8',
              ],
              )

####################################################################################################
#
# End
#
####################################################################################################
