####################################################################################################
# 
# PyElectronic - Python Electronic Tools
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

""" This module provides math tools. """

####################################################################################################

import math

####################################################################################################

def number_of_digits_of(x):

    """ Return the number of digits of the integer part of x.
    
    Let x an integer :math:`\geq 1`, we could rewrite it as a normalised form :math:`0.x\ 10^n`,
    where n are the number of digits of x.  The logarithm in base 10 of x is equal to :math:`n +
    \log_{10}(0.x)`.  Since :math:`0.1 \leq 0.x < 1`, we have :math:`-1 \leq \log_{10}(0.x) < 0` and
    thus :math:`n \leq \log_{10}(x) + 1 < n + 1`.  It follows the number of digits of x is equal to
    :math:`int(\log_{10}(x) + 1)`.
    """

    if x < 1:
        return 0
    else:
        return int(math.log10(x)) +1

####################################################################################################

def significant_digits_of(x, number_of_significant_digits):

    """ Return the most significant digits of a number, for example::

      significant_digits_of(1234, 2)

    will return 12.
    """

    return int(x * math.pow(10., number_of_significant_digits - number_of_digits_of(x)))

####################################################################################################
# 
# End
# 
####################################################################################################
