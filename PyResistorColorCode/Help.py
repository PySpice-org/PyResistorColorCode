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

""" This module contains the help. """

####################################################################################################

version = 'V1.0.0'

####################################################################################################

about_message = u"""
<h2>About PyResistorColorCode</h2>
<p>PyResistorColorCode version is %(version)s</p>
<p>Copyright &copy; 2012 Fabrice Salvaire</p>
"""

####################################################################################################

colour_matrix_help = """
<h3>Inference Algorithm</h3>
<ul>
<li>Code orientation (LR or RL) doesn't matter,</li>
<li>Bands set to none are skipped,</li>
<li>At least 3 colours must be provided (2 digits and the multiplier),</li>
<li>Colours are interpreted by priority as resistance value, then tolerance and finally temperature
coefficient,</li>
<li>The resistance value must exists in a series and its tolerance must be defined if there is a
colour assigned to it.</li>
</ul>
"""

####################################################################################################
# 
# End
# 
####################################################################################################
