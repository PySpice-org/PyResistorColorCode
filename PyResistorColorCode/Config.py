####################################################################################################
# 
# PyResistorColorCode - Python Electronic Tools.
# Copyright (C) 2012 Salvaire Fabrice
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
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
