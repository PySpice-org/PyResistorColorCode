####################################################################################################
# 
# PyElectronic - Python Electronic Tools
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

####################################################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal, pyqtSlot, Qt

####################################################################################################

from PyElectronic.Config import COLOURS
from PyElectronic.GuiTools import translate
from PyElectronic.ResistorColorCode import COLOUR_NAMES, Resistor, ResistorDecoder, format_value

####################################################################################################

class ResistorPixmap(object):

    ###############################################
    
    def __init__(self, resistor):

        self._resitor = resistor

    ###############################################
    
    def paint(self, painter, rect):

        lead_size = 20
        small_band_gap = 10
        large_band_gap = 10

        x_left, x_right = rect.left(), rect.right()
        y_middle = rect.center().y()

        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(Qt.black, 1.5))
        painter.setBrush(QtGui.QColor(255, 220, 220)) # pink
        box_rect = rect.adjusted(lead_size, 0, -lead_size, 0)
        painter.drawLine(x_left, y_middle, x_right, y_middle)
        painter.drawRoundedRect(box_rect, 5, 5)
        x_band = box_rect.left() + small_band_gap
        y_band_top, y_band_bottom = box_rect.top() -1, box_rect.bottom() +1

        def paint_band(colour):
            painter.setPen(QtGui.QPen(COLOURS[colour], 4.))
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

class ImageDelegate(QtGui.QStyledItemDelegate):

    ###############################################
 
    def __init__(self, parent, margin, size):

        super(ImageDelegate, self).__init__(parent)
        
        self._margin = margin
        self._size = size

    ###############################################

    def sizeHint(self, option, index):

        return QtCore.QSize(100, 50)
        # return self._size + QtCore.QtQize(self._margin, self._margin)*2

    ###############################################

    def paint(self, painter, option, index):        

        resistor_pixmap = index.data().toPyObject()
        if isinstance(resistor_pixmap, ResistorPixmap):
            # print option.rect.width(), option.rect.height()
            margin = self._margin
            rect = option.rect.adjusted(margin, margin, -margin, -margin)
            resistor_pixmap.paint(painter, rect)
        else:
            super(ImageDelegate, self).paint(painter, option, index)

####################################################################################################

class ColourMatrix(QtCore.QObject):

    NUMBER_OF_BANDS = 6
    CHECKED_TEXT = 'x'
    BAND_PIXMAP_HEIGHT, BAND_PIXMAP_WIDTH = 30, 10

    value_changed = pyqtSignal(list)
    
    ###############################################
    
    def __init__(self, parent):

        super(ColourMatrix, self).__init__()

        self._colour_names = list(COLOUR_NAMES) + ['none']
        self._colour_to_row = {colour:row for row, colour in enumerate(self._colour_names)}
        self._band_status = ['none']*self.NUMBER_OF_BANDS

        self._init_pixmaps()
        self._init_widget(parent)

    ###############################################
    
    def _band_iterator(self):

        return xrange(self.NUMBER_OF_BANDS)

    ###############################################
    
    def _init_pixmaps(self):

        self._band_pixmaps = {}
        for colour in self._colour_names:
            pixmap = QtGui.QPixmap(self.BAND_PIXMAP_WIDTH, self.BAND_PIXMAP_HEIGHT)
            pixmap.fill(COLOURS[colour])
            self._band_pixmaps[colour] = pixmap

    ###############################################
    
    def _init_widget(self, parent):

        self._grid_layout = QtGui.QGridLayout()
        self._grid_layout.setHorizontalSpacing(10)
        self._grid_layout.setVerticalSpacing(0)
        self._grid_layout.setRowMinimumHeight(0, int(1.5 * self.BAND_PIXMAP_HEIGHT))
        alignement = Qt.AlignHCenter | Qt.AlignVCenter

        self._reset_button = QtGui.QPushButton(parent)
        self._reset_button.setText(translate("colour_decoder", "Reset"))
        self._reset_button.clicked.connect(self.reset)
        self._grid_layout.addWidget(self._reset_button, 0, 0, 1, 1, alignement)

        self._band_labels = []
        for band in self._band_iterator():
            label = QtGui.QLabel(parent)
            self._grid_layout.addWidget(label, 0, band +1, 1, 1, alignement)
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
                button = QtGui.QToolButton(parent)
                button.setCheckable(True)
                self._grid_layout.addWidget(button, row +1, band +1, 1, 1, alignement)
                if colour != 'none':
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(COLOURS[colour])
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
                    if colour in ('black', 'blue'):
                        brush = QtGui.QBrush(Qt.white)
                        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
                    button.setPalette(palette)
                self._band_button_groups[band].addButton(button, row)

        self.reset()

    ###############################################
    
    def _button(self, band, colour):

        return self._band_button_groups[band].button(self._colour_to_row[colour])

    ###############################################
    
    def _reset_band_button(self, band):

        colour = self._band_status[band]
        button = self._button(band, colour)
        button.setText('')

    ###############################################
    
    def _set_band_status(self, band, colour):

        self._reset_band_button(band)
        self._band_status[band] = colour
        button = self._button(band, colour)
        button.setChecked(True)
        button.setText(self.CHECKED_TEXT)
        self._emit_value_changed()

    ###############################################
    
    def reset(self):

        for band in self._band_iterator():
            self._set_band_status(band, 'none')

    ###############################################
    
    def _emit_value_changed(self):

        for band, colour in enumerate(self._band_status):
            label = self._band_labels[band]
            label.setPixmap(self._band_pixmaps[colour])

        self.value_changed.emit(self._band_status)

    ###############################################

    def _make_button_clicked_callback(self, band):

        # band must be a local variable

        return lambda button: self._button_clicked(band, button)

    ###############################################

    def _button_clicked(self, band, button):

        button_group = self._band_button_groups[band]
        row = button_group.id(button)
        colour = self._colour_names[row]
        self._set_band_status(band, colour)

    ###############################################
    
    def widget(self):

        return self._grid_layout

####################################################################################################

class HypothesesTableModel(QtCore.QAbstractTableModel):

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

        return cls.COLUMNS.index(column)

    ###############################################
    
    def __init__(self):

        super(HypothesesTableModel, self).__init__()

        self._resistor_decoder = ResistorDecoder()
        self._hypotheses = []
        self._resistor_pixmaps = {}

    ###############################################
    
    @pyqtSlot(list)
    def _update_hypotheses(self, bands):

        colour_names = [x for x in bands if x != 'none']
        if len(colour_names) >= 3:
            self._hypotheses = self._resistor_decoder.decode(colour_names)
            self._resistor_pixmaps = {id(resistor):ResistorPixmap(resistor)
                                      for resistor in self._hypotheses}
            self._sort_by_series()
            print '\n', colour_names
            for i, hypothesis in enumerate(self._hypotheses):
                print "hypothese %u: %s" % (i +1, hypothesis)
        else:
            self._hypotheses = ()
            self._resistor_pixmaps = {}
        self.reset()

    ###############################################

    def rowCount(self, index=QtCore.QModelIndex()):

        return len(self._hypotheses)

    ###############################################
    
    def columnCount(self, index=QtCore.QModelIndex()):

        return len(self.COLUMNS)

    ###############################################

    def headerData(self, section, orientation, role=Qt.DisplayRole):

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

        row = index.row()

        if not index.isValid() or not(0 <= row < len(self._hypotheses)):
            return QtCore.QVariant()

        resistor = self._hypotheses[row]

        if role == Qt.TextAlignmentRole:
            return QtCore.QVariant(int(Qt.AlignRight|Qt.AlignVCenter))

        elif role == Qt.DisplayRole:
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
            elif column == 'colour code':
                resistor_pixmap = self._resistor_pixmaps[id(resistor)]
                return QtCore.QVariant(resistor_pixmap)
                
        # else:
        return QtCore.QVariant ()

    ###############################################

    def _sort(self, cmp_function, reverse):

        self._hypotheses = sorted(self._hypotheses, cmp=cmp_function, reverse=reverse)

    ###############################################

    def _sort_by_values(self, reverse=False):

        self._sort(Resistor.cmp_values(), reverse)

    ###############################################

    def _sort_by_series(self, reverse=False):

        self._sort(Resistor.cmp_series(), reverse)

    ###############################################

    def sort(self, column, order=Qt.AscendingOrder):

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
