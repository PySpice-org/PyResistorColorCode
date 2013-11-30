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

####################################################################################################

import unittest

####################################################################################################

from PyResistorColorCode.Math import *

####################################################################################################

class TestMath(unittest.TestCase):
 
    ##############################################
    
    def test_number_of_digits_of(self):

        for i in xrange(6):
            for x in 0.1, 0.123456:
                y = x*10**i
                # print i, y
                self.assertEqual(number_of_digits_of(y), i)

    ##############################################
    
    def test_significant_digits_of(self):
 
        digits = (1, 2, 3, 4)
        number = 0
        for i, d in enumerate(reversed(digits)):
            number += d * 10**i
        for i in xrange(1,5):
            output_number = 0
            for j, d in enumerate(reversed(digits[:i])):
                output_number += d * 10**j
            # print number, i, output_number
            self.assertEqual(significant_digits_of(number, i), output_number)

####################################################################################################

if __name__ == '__main__':

    unittest.main()

####################################################################################################
# 
# End
# 
####################################################################################################
