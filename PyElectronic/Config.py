####################################################################################################
# 
# PyElectronic - Python Electronic Tools
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

""" This module defines configuration settings. """

####################################################################################################

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

####################################################################################################

#: Defines the RGB colours associated to the bands.
COLOURS = {
    'none':Qt.transparent,
    'silver':QtGui.QColor(190, 190, 180),
    'gold':QtGui.QColor(255, 255, 200),
    'black':Qt.black,
    'brown':QtGui.QColor(128, 80, 35),
    'red':Qt.red,
    'orange':QtGui.QColor(255, 150, 50),
    'yellow':Qt.yellow,
    'green':Qt.green,
    'blue':Qt.blue,
    'violet':Qt.magenta,
    'grey':QtGui.QColor(128, 128, 128),
    'white':Qt.white,
    }

resistor_body_colour = QtGui.QColor(255, 220, 220) # pink

####################################################################################################
# 
# End
# 
####################################################################################################
