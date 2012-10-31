####################################################################################################
# 
# PyElectronic - Python Electronic Tools
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

####################################################################################################

import unittest

####################################################################################################

from PyElectronic.Math import *

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
