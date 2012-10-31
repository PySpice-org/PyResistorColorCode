####################################################################################################
# 
# PyElectronic - Python Electronic Tools
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

""" This module contains the help. """

####################################################################################################

version = 'V1.0.0'

####################################################################################################

about_message = u"""
<h2>About PyElectronic</h2>
<p>PyElectronic version is %(version)s</p>
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
