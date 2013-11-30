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

""" This module implements a Resistor Decoder Application. """

####################################################################################################

import os
import sys

from PyQt4 import QtGui, QtCore

####################################################################################################

from PyResistorColorCode.GuiTools import translate
from PyResistorColorCode.ResistorWidget import HypothesesTableModel, ColourMatrix, ResistorImageDelegate
import PyResistorColorCode.ConfigInstall as ConfigInstall
import PyResistorColorCode.Help as Help

####################################################################################################

class Application(QtGui.QApplication):

    """ This class implements the application. """

    ###############################################
    
    def __init__(self):

        super(Application, self).__init__(sys.argv)

        self._application_name = os.path.basename(sys.argv[0])

        self._init_main_window()
        self._main_window.show()

    ###############################################
    
    def _init_main_window(self):

        """ Initialise the main window. """

        self._main_window = QtGui.QMainWindow()
        self._main_window.setObjectName('main_window')
        self._main_window.resize(1024, 800)
        self._main_window.setWindowTitle(self._application_name)
        # translate("colour_decoder", ' - Resistor Decoder')
        svg_file = os.path.join(ConfigInstall.share_directory, 'icons/resistor.svg')
        self._main_window.setWindowIcon(QtGui.QIcon(svg_file))

        self._status_bar = QtGui.QStatusBar(self._main_window)
        self._main_window.setStatusBar(self._status_bar)

        self._init_widget()
        self._init_action()
        self._init_menu()

    ###############################################
    
    def _init_widget(self):

        """ Initialise widgets. """

        central_widget = QtGui.QWidget(self._main_window)
        self._vertical_layout = QtGui.QVBoxLayout(central_widget)
        self._main_window.setCentralWidget(central_widget)

        self._init_colour_matrix_widget()
        self._init_hypotheses_widget()
        self._colour_matrix.value_changed.connect(self._hypotheses_table_model.update_hypotheses)

        spacer_item = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self._vertical_layout.addItem(spacer_item)

    ###############################################
    
    def _init_action(self):

        """ Initialise the actions. """        

        self._about_action = QtGui.QAction(self._main_window)
        self._about_action.setText(translate('colour_decoder', 'About'))
        self._about_action.triggered.connect(self._about)

    ###############################################
    
    def _init_menu(self):

        """ Initialise the menu bar. """

        self._menu_bar = QtGui.QMenuBar(self._main_window)
        self._main_window.setMenuBar(self._menu_bar)

        self._help_menu = QtGui.QMenu(self._menu_bar)
        self._help_menu.setTitle(translate('colour_decoder', 'Help'))
        self._help_menu.addAction(self._about_action)
        self._menu_bar.addAction(self._help_menu.menuAction())

    ###############################################
    
    def _init_colour_matrix_widget(self):

        """ Initialise the colour matrix widget. """

        self._colour_code_group_box = QtGui.QGroupBox(self._main_window)
        self._colour_code_group_box.setTitle(translate("colour_decoder", 'Colour Code'))
        self._vertical_layout.addWidget(self._colour_code_group_box)

        horizontal_layout = QtGui.QHBoxLayout(self._colour_code_group_box)

        self._colour_matrix = ColourMatrix(self._colour_code_group_box)
        horizontal_layout.addLayout(self._colour_matrix.widget())

        help_label = QtGui.QLabel(self._colour_code_group_box)
        help_label.setTextFormat(QtCore.Qt.RichText)
        help_label.setTextFormat(QtCore.Qt.RichText)
        help_label.setWordWrap(True)
        help_label.setOpenExternalLinks(True)
        help_label.setMargin(25)
        help_label.setAlignment(QtCore.Qt.AlignLeading| QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        help_label.setText(translate("colour_decoder", Help.colour_matrix_help))
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        help_label.setSizePolicy(size_policy)
        horizontal_layout.addWidget(help_label)

    ###############################################
    
    def _init_hypotheses_widget(self):

        """ Initialise the hypothesis table widget. """

        self._hypotheses_group_box = QtGui.QGroupBox(self._main_window)
        self._hypotheses_group_box.setTitle(translate("colour_decoder", 'Hypotheses'))
        self._vertical_layout.addWidget(self._hypotheses_group_box)

        horizontal_layout = QtGui.QHBoxLayout(self._hypotheses_group_box)

        self._hypotheses_table_model = HypothesesTableModel()

        self._table_view = QtGui.QTableView(self._hypotheses_group_box)
        self._table_view.setAlternatingRowColors(True)
        self._table_view.setSortingEnabled(True)
        self._table_view.setModel(self._hypotheses_table_model)
        self._table_view.resizeColumnsToContents()
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self._table_view.setSizePolicy(size_policy)
        horizontal_layout.addWidget(self._table_view)

        margin = 5
        resistor_pixmap_size = QtCore.QSize(100, 50) # Fixme: no effect
        image_delegate = ResistorImageDelegate(None, margin, resistor_pixmap_size)
        column = self._hypotheses_table_model.column_index('colour code')
        self._table_view.setItemDelegateForColumn(column, image_delegate)

    ##############################################

    def _about(self):
        
        message = Help.about_message % {'version':str(Help.version)}
        QtGui.QMessageBox.about(self._main_window, 'About ' + self._application_name, message)

####################################################################################################
#
# End
#
####################################################################################################
