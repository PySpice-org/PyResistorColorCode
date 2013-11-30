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

""" This modules provides GUI widgets for resistors. """

####################################################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal, pyqtSlot, Qt

####################################################################################################

from PyResistorColorCode.GuiTools import translate
from PyResistorColorCode.ResistorColourCode import (
    COLOUR_NAMES, Resistor, ResistorDecoder, format_value)
import PyResistorColorCode.Config as Config

####################################################################################################

_CENTERED_ALIGNEMENT = Qt.AlignHCenter | Qt.AlignVCenter

####################################################################################################

class ResistorPixmap(object):

    """ This class implements a resistor painter. """

    ###############################################
    
    def __init__(self, resistor):

        self._resitor = resistor

    ###############################################
    
    def paint(self, painter, rect):

        """ Paint the resistor. """

        lead_size = 20
        body_line_width = 1.5
        band_width = 5
        body_corner_radius = 5
        small_band_gap = 2*band_width
        large_band_gap = 1.5*small_band_gap - small_band_gap

        resistor_width = 2*lead_size + 7*small_band_gap + large_band_gap
        if rect.width() < resistor_width:
            return

        x_left, x_right = rect.left(), rect.right()
        # x_right = x_left + resistor_width
        y_middle = rect.center().y()

        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(Qt.black, body_line_width))
        painter.setBrush(Config.resistor_body_colour)
        box_rect = rect.adjusted(lead_size, 0, -lead_size, 0)
        painter.drawLine(x_left, y_middle, x_right, y_middle)
        painter.drawRoundedRect(box_rect, body_corner_radius, body_corner_radius)
        x_band = box_rect.left() + small_band_gap
        y_band_top, y_band_bottom = box_rect.top() -1, box_rect.bottom() +1

        def paint_band(colour):
            painter.setPen(QtGui.QPen(Config.COLOURS[colour], band_width))
            painter.drawLine(x_band, y_band_top, x_band, y_band_bottom)

        for colour in self._resitor.digit_colour_iterator():
            paint_band(colour)
            x_band += small_band_gap
        x_band += large_band_gap
        for colour in self._resitor.tolerance_colour, self._resitor.temperature_coefficient_colour:
            if colour is not None:
                paint_band(colour)
                x_band += small_band_gap
           
####################################################################################################

class ResistorImageDelegate(QtGui.QStyledItemDelegate):

    """ This class implements an item delegate that paint a resistor. """

    ###############################################
 
    def __init__(self, parent, margin, size):

        super(ResistorImageDelegate, self).__init__(parent)
        
        self._margin = margin
        self._size = size

    ###############################################

    def sizeHint(self, option, index):

        """ Return the size hint. """

        print 'sizeHint'

        # Fixme: no effect

        return QtCore.QSize(100, 50)
        # return self._size + QtCore.QtQize(self._margin, self._margin)*2

    ###############################################

    def paint(self, painter, option, index):        

        """ Paint the resistor. """

        resistor_pixmap = index.data().toPyObject()
        if isinstance(resistor_pixmap, ResistorPixmap):
            # print option.rect.width(), option.rect.height()
            margin = self._margin
            rect = option.rect.adjusted(margin, margin, -margin, -margin)
            resistor_pixmap.paint(painter, rect)
        else:
            super(ResistorImageDelegate, self).paint(painter, option, index)

####################################################################################################

class ColourMatrix(QtCore.QObject):

    """ This class implements a colour matrix where the columns represents the resistor colour bands
    and the rows all the possible colours and the undefined state.  Each band column is made of a
    group of exclusive checkable buttons.
    """

    _NUMBER_OF_BANDS = 6
    _CHECKED_TEXT = 'x'
    _BAND_PIXMAP_HEIGHT, _BAND_PIXMAP_WIDTH = 30, 10

    #: Value changed signal.
    value_changed = pyqtSignal(list)
    
    ###############################################
    
    def __init__(self, parent):

        super(ColourMatrix, self).__init__()

        self._colour_names = list(COLOUR_NAMES) + ['none']
        self._colour_to_row = {colour:row for row, colour in enumerate(self._colour_names)}
        self._band_status = ['none']*self._NUMBER_OF_BANDS

        self._init_pixmaps()
        self._init_widget(parent)

    ###############################################
    
    def _band_iterator(self):

        """ Return an iterator over the band indexes. """

        return xrange(self._NUMBER_OF_BANDS)

    ###############################################
    
    def _init_pixmaps(self):

        """ Initialise the colour pixmaps that represents the resistor colour bands. """

        self._band_pixmaps = {}
        for colour in self._colour_names:
            pixmap = QtGui.QPixmap(self._BAND_PIXMAP_WIDTH, self._BAND_PIXMAP_HEIGHT)
            pixmap.fill(Config.COLOURS[colour])
            self._band_pixmaps[colour] = pixmap

    ###############################################
    
    def _init_cell(self, parent, band, row, colour):

        """ Initialise a cell. """

        button = QtGui.QToolButton(parent)
        button.setCheckable(True)
        self._grid_layout.addWidget(button, row +1, band +1, 1, 1, _CENTERED_ALIGNEMENT)
        if colour != 'none':
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(Config.COLOURS[colour])
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
            if colour in ('black', 'blue'):
                brush = QtGui.QBrush(Qt.white)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
            button.setPalette(palette)
        self._band_button_groups[band].addButton(button, row)

    ###############################################
    
    def _init_widget(self, parent):

        """ Initialise the matrix widgets. """

        self._grid_layout = QtGui.QGridLayout()
        self._grid_layout.setHorizontalSpacing(10)
        self._grid_layout.setVerticalSpacing(0)
        self._grid_layout.setRowMinimumHeight(0, int(1.5 * self._BAND_PIXMAP_HEIGHT))

        self._reset_button = QtGui.QPushButton(parent)
        self._reset_button.setText(translate("colour_decoder", "Reset"))
        self._reset_button.clicked.connect(self.reset)
        self._grid_layout.addWidget(self._reset_button, 0, 0, 1, 1, _CENTERED_ALIGNEMENT)

        self._band_labels = []
        for band in self._band_iterator():
            label = QtGui.QLabel(parent)
            self._grid_layout.addWidget(label, 0, band +1, 1, 1, _CENTERED_ALIGNEMENT)
            self._band_labels.append(label)

        self._band_button_groups = []
        for band in self._band_iterator():
            button_group = QtGui.QButtonGroup(parent)
            self._band_button_groups.append(button_group)
            button_group.setExclusive(True)
            callback = self._make_button_clicked_callback(band)
            button_group.buttonClicked.connect(callback)
        for row, colour in enumerate(self._colour_names):
            label = QtGui.QLabel(parent)
            label.setText(translate("colour_decoder", colour))
            self._grid_layout.addWidget(label, row +1, 0, 1, 1)
            for band in self._band_iterator():
                self._init_cell(parent, band, row, colour)

        self.reset()

    ###############################################
    
    def _button(self, band, colour):
        
        """ Return the button for the given band and colour. """

        return self._band_button_groups[band].button(self._colour_to_row[colour])

    ###############################################
    
    def _reset_band_button(self, band):

        """ Reset the band. """

        colour = self._band_status[band]
        button = self._button(band, colour)
        button.setText('')

    ###############################################
    
    def _set_band_status(self, band, colour):

        """ Set the colour of a band and emit the value changed signal. """

        self._reset_band_button(band)
        self._band_status[band] = colour
        button = self._button(band, colour)
        button.setChecked(True)
        button.setText(self._CHECKED_TEXT)
        self._emit_value_changed()

    ###############################################
    
    def reset(self):

        """ Reset the matrix. """

        for band in self._band_iterator():
            self._set_band_status(band, 'none')

    ###############################################
    
    def _emit_value_changed(self):

        """ Emit the value changed signal with the list of bands. """

        for band, colour in enumerate(self._band_status):
            label = self._band_labels[band]
            label.setPixmap(self._band_pixmaps[colour])

        self.value_changed.emit(self._band_status)

    ###############################################

    def _make_button_clicked_callback(self, band):

        """ Return a closure wrapper for the method :meth:`_button_clicked`. """

        # band must be a local variable

        return lambda button: self._button_clicked(band, button)

    ###############################################

    def _button_clicked(self, band, button):

        """ Handle a clicked action on a button cell. """

        button_group = self._band_button_groups[band]
        row = button_group.id(button)
        colour = self._colour_names[row]
        self._set_band_status(band, colour)

    ###############################################
    
    def widget(self):

        """ Return the grid layout of the matrix. """

        return self._grid_layout

####################################################################################################

class HypothesesTableModel(QtCore.QAbstractTableModel):

    """ This class implements a table model for the hypotheses. """

    COLUMNS = ('value',
               'series',
               'tolerance',
               'temperature coefficient',
               'value range',
               'colour code',
               )

    HEADER_DATA = ('Value [R]',
                   'Series',
                   'Tolerance [%]',
                   'Temperature Coefficient [ppm/K]',
                   'Value Range [R]',
                   'Colour Code',
                   )

    ###############################################
    
    @classmethod
    def column_index(cls, column):

        """ Return the index of the given column name. """

        return cls.COLUMNS.index(column)

    ###############################################
    
    def __init__(self):

        super(HypothesesTableModel, self).__init__()

        self._resistor_decoder = ResistorDecoder()
        self._hypotheses = []
        self._resistor_pixmaps = {}

    ###############################################
    
    @pyqtSlot(list)
    def update_hypotheses(self, bands):

        """ Slot to update the hypotheses from the given list of bands. """

        colour_names = [x for x in bands if x != 'none']
        if len(colour_names) >= 3:
            self._hypotheses = self._resistor_decoder.decode(colour_names)
            self._resistor_pixmaps = {id(resistor):ResistorPixmap(resistor)
                                      for resistor in self._hypotheses}
            self._sort_by_series()
            # print '\n', colour_names
            # for i, hypothesis in enumerate(self._hypotheses):
            #     print "hypothese %u: %s" % (i +1, hypothesis)
        else:
            self._hypotheses = ()
            self._resistor_pixmaps = {}
        self.reset()

    ###############################################

    def rowCount(self, index=QtCore.QModelIndex()):

        """ Return the number of rows. """

        return len(self._hypotheses)

    ###############################################
    
    def columnCount(self, index=QtCore.QModelIndex()):

        """ Return the number of columns. """

        return len(self.COLUMNS)

    ###############################################

    def headerData(self, section, orientation, role=Qt.DisplayRole):

        """ Return the header data. """

        if role == Qt.TextAlignmentRole:
            return QtCore.QVariant(int(Qt.AlignHCenter|Qt.AlignVCenter))
        
        elif role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return QtCore.QVariant(self.HEADER_DATA[section])
            elif orientation == Qt.Vertical:
                return QtCore.QVariant(int(section + 1))

        else:
            return QtCore.QVariant()

    ###############################################
    
    def data(self, index, role=Qt.DisplayRole):

        """ Return the cell data. """

        if not index.isValid() or not(0 <= index.row() < len(self._hypotheses)):
            return QtCore.QVariant()

        if role == Qt.TextAlignmentRole:
            return QtCore.QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
        elif role == Qt.DisplayRole:
            return self._display_role_data(index)
        else:
            return QtCore.QVariant ()

    ###############################################
    
    def _display_role_data(self, index):

        row = index.row()
        resistor = self._hypotheses[row]
        column = self.COLUMNS[index.column()]

        if column == 'value':
            return QtCore.QVariant(format_value(resistor.value))

        elif column == 'series':
            return QtCore.QVariant(str(resistor.series))

        elif column == 'tolerance':
            if resistor.tolerance is not None:
                tolerance_str = '%.2f %%' % resistor.tolerance
            else:
                tolerance_str = ''
            return QtCore.QVariant(tolerance_str)

        elif column == 'temperature coefficient':
            if resistor.temperature_coefficient is not None:
                temperature_coefficient_str = '%u ppm' % resistor.temperature_coefficient
            else:
                temperature_coefficient_str = ''
            return QtCore.QVariant(temperature_coefficient_str)

        elif column == 'value range':
            value_range = resistor.value_range()
            if value_range is not None:
                value_range_str = [format_value(x) for x in value_range]
                return QtCore.QVariant('[%s, %s]' % tuple(value_range_str))
            else:
                return QtCore.QVariant ()

        elif column == 'colour code':
            resistor_pixmap = self._resistor_pixmaps[id(resistor)]
            return QtCore.QVariant(resistor_pixmap)

    ###############################################

    def _sort(self, cmp_function, reverse):
        
        """ Sort the model with the given sort function and order. """

        self._hypotheses = sorted(self._hypotheses, cmp=cmp_function, reverse=reverse)

    ###############################################

    def _sort_by_values(self, reverse=False):

        """ Sort the resistors by values. """

        self._sort(Resistor.cmp_values(), reverse)

    ###############################################

    def _sort_by_series(self, reverse=False):

        """ Sort the resistors by series. """

        self._sort(Resistor.cmp_series(), reverse)

    ###############################################

    def sort(self, column, order=Qt.AscendingOrder):

        """ Sort the model. """

        reverse = order != Qt.AscendingOrder
        column = self.COLUMNS[column]
        if column == 'value':
            self._sort_by_values(reverse)
        elif column == 'series':
            self._sort_by_series(reverse)
        self.reset()

####################################################################################################
# 
# End
# 
####################################################################################################
