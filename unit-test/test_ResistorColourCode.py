####################################################################################################
# 
# PyElectronic - Python Electronic Tools
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

####################################################################################################

import unittest

####################################################################################################

from PyElectronic.ResistorColourCode import *

####################################################################################################

class TestResistorColourCode(unittest.TestCase):

    ##############################################
    
    def test_Series(self):
 
        self.assertEqual(len(E6), 6)
        self.assertEqual(len(E12), 12)
        self.assertEqual(len(E24), 24)
        self.assertEqual(len(E48), 48)
        self.assertEqual(len(E96), 96)
        self.assertEqual(len(E192), 192)

        eia_series = (E6, E12, E24, E48, E96, E192)
        for i in xrange(len(eia_series) -1):
            for j in xrange(i +1, len(eia_series)):
                self.assertTrue(eia_series[i] < eia_series[j])
                self.assertFalse(eia_series[i] > eia_series[j])

        self.assertTrue(10 in E6)

    ##############################################
    
    def test_Resistor(self):

        resistor = Resistor(digit1='brown', digit2='black', multiplier='red')
        self.assertEqual(resistor.value, 1000)
        self.assertEqual(resistor.series, E6)
        self.assertEqual(resistor.number_of_digits, 2)
        self.assertEqual(resistor.digit1, 1)
        self.assertEqual(resistor.digit2, 0)
        self.assertEqual(resistor.significant_digits, 10)
        self.assertEqual(resistor.multiplier, 100)

        resistor = Resistor(digit1='brown', digit2='red', digit3='orange', multiplier='yellow',
                            tolerance='violet')
        resistance = 1230000
        self.assertEqual(resistor.value, resistance)
        self.assertEqual(resistor.series, E192)
        self.assertEqual(resistor.number_of_digits, 3)
        self.assertEqual(resistor.digit1, 1)
        self.assertEqual(resistor.digit2, 2)
        self.assertEqual(resistor.digit3, 3)
        self.assertEqual(resistor.significant_digits, 123)
        self.assertEqual(resistor.multiplier, 10000)
        self.assertEqual(resistor.tolerance, .1)
        self.assertTupleEqual(resistor.value_range(), (resistance*0.999, resistance*1.001))

####################################################################################################

if __name__ == '__main__':

    unittest.main()

####################################################################################################
# 
# End
# 
####################################################################################################
