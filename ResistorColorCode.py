####################################################################################################

from math import log, ceil

####################################################################################################

class ValuesSeries(object):

    ##############################################

    def __init__(self, name, tolerances, values):

        self.name = name
        self.number = int(name[1:])
        self.tolerances = tolerances
        self.values = values

    ##############################################

    def __cmp__(self, other):

        return cmp(self.number, other.number)

    ##############################################

    def __str__(self):

        return self.name

    ##############################################

    def __contains__(self, value):

        return value in self.values

####################################################################################################

# tolerance: 20%
E6 = ValuesSeries(name='E6',
                  tolerances=(20,),
                  values=(10, 15, 22, 33, 47, 68))

# tolerance: 10%
E12 = ValuesSeries(name='E12',
                  tolerances=(10,),
                   values=(10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82))

# tolerance: 5% 1%
E24 = ValuesSeries(name='E24',
                  tolerances=(5, 1),
                   values=(10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
                           11, 13, 16, 20, 24, 30, 36, 43, 51, 62, 75, 91))

# tolerance: 2%
E48 = ValuesSeries(name='E48',
                  tolerances=(2),
                   values=(100, 121, 147, 178, 215, 261, 316, 383, 464, 562, 681, 825,
                           105, 127, 154, 187, 226, 274, 332, 402, 487, 590, 715, 866,
                           110, 133, 162, 196, 237, 287, 348, 422, 511, 619, 750, 909,
                           115, 140, 169, 205, 249, 301, 365, 442, 536, 649, 787, 953))

# tolerance: 1%
E96 = ValuesSeries(name='E96',
                  tolerances=(1),
                   values=(100, 121, 147, 178, 215, 261, 316, 383, 464, 562, 681, 825,
                           102, 124, 150, 182, 221, 267, 324, 392, 475, 576, 698, 845,
                           105, 127, 154, 187, 226, 274, 332, 402, 487, 590, 715, 866,
                           107, 130, 158, 191, 232, 280, 340, 412, 499, 604, 732, 887,
                           110, 133, 162, 196, 237, 287, 348, 422, 511, 619, 750, 909,
                           113, 137, 165, 200, 243, 294, 357, 432, 523, 634, 768, 931,
                           115, 140, 169, 205, 249, 301, 365, 442, 536, 649, 787, 953,
                           118, 143, 174, 210, 255, 309, 374, 453, 549, 665, 806, 976))

# tolerance: 0.5% 0.25% 0.1%
E192 = ValuesSeries(name='E192',
                    tolerances=(0.5, 0.25, 0.1),
                    values=(100, 121, 147, 178, 215, 261, 316, 383, 464, 562, 681, 825,
                            101, 123, 149, 180, 218, 264, 320, 388, 470, 569, 690, 835,
                            102, 124, 150, 182, 221, 267, 324, 392, 475, 576, 698, 845,
                            104, 126, 152, 184, 223, 271, 328, 397, 481, 583, 706, 856,
                            105, 127, 154, 187, 226, 274, 332, 402, 487, 590, 715, 866,
                            106, 129, 156, 189, 229, 277, 336, 407, 493, 597, 723, 876,
                            107, 130, 158, 191, 232, 280, 340, 412, 499, 604, 732, 887,
                            109, 132, 160, 193, 234, 284, 344, 417, 505, 612, 741, 898,
                            110, 133, 162, 196, 237, 287, 348, 422, 511, 619, 750, 909,
                            111, 135, 164, 198, 240, 291, 352, 427, 517, 626, 759, 920,
                            113, 137, 165, 200, 243, 294, 357, 432, 523, 634, 768, 931,
                            114, 138, 167, 203, 246, 298, 361, 437, 530, 642, 777, 942,
                            115, 140, 169, 205, 249, 301, 365, 442, 536, 649, 787, 953,
                            117, 142, 172, 208, 252, 305, 370, 448, 542, 657, 796, 965,
                            118, 143, 174, 210, 255, 309, 374, 453, 549, 665, 806, 976,
                            120, 145, 176, 213, 258, 312, 379, 459, 556, 673, 816, 988))

####################################################################################################

COLOUR_NAMES = (
    'silver',
    'gold',
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
    )

# tolerance [%]
TOLERANCES = {
    'silver':10,
    'gold':5,
    'black':None,
    'brown':1,
    'red':2,
    'orange':None,
    'yellow':5,
    'green':0.5,
    'blue':0.25,
    'violet':0.1,
    'grey':0.05, # 10 %
    'white':None,
    'none':20,
    }

# temperature coefficient ppm/K
TEMPERATURE_COEFFICIENTS = {
    'silver':None,
    'gold':None,
    'black':250,
    'brown':100,
    'red':50,
    'orange':15,
    'yellow':25,
    'green':20,
    'blue':10,
    'violet':5,
    'grey':1,
    'white':None,
    }

####################################################################################################

def format_value(x):

    if x < 1:
        return '%g m' % (x*1e3)
    elif x < 1e3:
        return '%g' % (x)
    elif x < 1e6:
        return '%g k' % (x/1e3)
    elif x < 1e9:
        return '%g M' % (x/1e6)
    elif x < 1e12:
        return '%g G' % (x/1e9)

####################################################################################################

def significant_digits(x, number_of_significant_digits):

    # number_of_digits = int(ceil(log(x)/log(10))) + 1
    # significant_digits = int(x * 10**(number_of_significant_digits - number_of_digits))

    # print x, number_of_significant_digits
    x *= 1000
    number_of_digits = 0
    while x >= 1:
        x /= 10.
        number_of_digits += 1
    significant_digits = int(x * 10**number_of_significant_digits)
        
    # print x, number_of_digits -3, significant_digits
    return significant_digits

####################################################################################################

class ColourCode(object):

    ##############################################

    def __init__(self,
                 colour_name,
                 digit,
                 multiplier,
                 tolerance,
                 temperature_coefficient):

        self.colour_name = colour_name
        self.digit = digit
        self.multiplier = multiplier
        self.tolerance = tolerance
        self.temperature_coefficient = temperature_coefficient

    ##############################################

    def __repr__(self):

        if self.digit is not None:
            digit_str = 'd%u' % self.digit
        else:
            digit_str = ''

        if self.multiplier is not None:
            multiplier_str = 'x' + format_value(self.multiplier)
        else:
            multiplier_str = ''

        if self.tolerance is not None:
            tolerance_str = '%.2f %%' % self.tolerance
        else:
            tolerance_str = ''

        if self.temperature_coefficient is not None:
            temperature_coefficient_str = '%u ppm' % self.temperature_coefficient
        else:
            temperature_coefficient_str = ''

        return '%-6s: ' % self.colour_name + \
            ', '.join(x for x in (digit_str,
                                  multiplier_str,
                                  tolerance_str,
                                  temperature_coefficient_str)
                      if x)

####################################################################################################

COLOUR_CODES = {}
for i, colour_name in enumerate(COLOUR_NAMES):
    digit = i - 2
    multiplier = 10**digit
    # digit is defined positive
    if digit < 0:
        digit = None
    COLOUR_CODES[colour_name] = ColourCode(colour_name,
                                           digit,
                                           multiplier,
                                           TOLERANCES[colour_name],
                                           TEMPERATURE_COEFFICIENTS[colour_name])
       
####################################################################################################

class Resistor(object):

    ##############################################

    def __init__(self,
                 value=None,
                 number_of_digits=None,
                 digit1=0,
                 digit2=0,
                 digit3=None,
                 multiplier=None,
                 tolerance=None,
                 temperature_coefficient=None):

        if value is not None:
            self.value = value
            self.number_of_digits = number_of_digits
            self.digit1=None
            self.digit2=None
            self.digit3=None
            self.multiplier=None
        else:
            self.digit1=digit1
            self.digit2=digit2
            self.digit3=digit3
            self.multiplier=multiplier
            value = COLOUR_CODES[digit1].digit * 10 + COLOUR_CODES[digit2].digit
            if digit3 is not None:
                value = value * 10 + COLOUR_CODES[digit3].digit
                self.number_of_digits = 3
            else:
                self.number_of_digits = 2
            self.value = value * COLOUR_CODES[multiplier].multiplier

        if tolerance is None:
            self.tolerance = None
            self.tolerance_colour = None
        else:
            try:
                self.tolerance = COLOUR_CODES[tolerance].tolerance
                self.tolerance_colour = tolerance
            except KeyError:
                self.tolerance = float(tolerance)

        if temperature_coefficient is None:
            self.temperature_coefficient = None
            self.temperature_coefficient_colour = None
        else:
            try:
                self.temperature_coefficient = COLOUR_CODES[temperature_coefficient].temperature_coefficient
                self.temperature_coefficient_colour = temperature_coefficient
            except KeyError:
                self.temperature_coefficient = float(temperature_coefficient)

        self.series = self._guess_series()

    ##############################################

    @staticmethod
    def cmp_values():

        return lambda a, b: cmp(a.value, b.value)

    ##############################################

    @staticmethod
    def cmp_series():

        return lambda a, b: cmp(a.series, b.series)

    ##############################################

    def _guess_series(self):

        resitor_series = None
        if self.number_of_digits is not None:
            number_of_significant_digits = self.number_of_digits
            if self.number_of_digits == 2:
                list_of_series = (E6, E12, E24)
            else:
                list_of_series = (E48, E96, E192)
        else:
            list_of_series = (E6, E12, E24, E48, E96, E192)
            number_of_significant_digits = 3
        digit_value = significant_digits(self.value, number_of_significant_digits)
        for series in list_of_series:
            if resitor_series is not None:
                break
            if digit_value in series:
                if self.tolerance is None:
                    resitor_series = series
                else:
                    if self.tolerance in series.tolerances:
                        resitor_series = series

        return resitor_series

    ##############################################

    def value_range(self):

        if self.tolerance is not None:
            return [self.value * (1 + sign * self.tolerance / 100.)
                    for sign in -1, 1]
        else:
            return None

    ##############################################

    def __str__(self):

        if self.tolerance is not None:
            tolerance_str = '%.2f %%' % self.tolerance
        else:
            tolerance_str = ''

        if self.temperature_coefficient is not None:
            temperature_coefficient_str = '%u ppm' % self.temperature_coefficient
        else:
            temperature_coefficient_str = ''

        series_name = str(self.series)
        
        return ' '.join(x for x in ("%s R series %s" % (format_value(self.value), series_name),
                                    tolerance_str,
                                    temperature_coefficient_str,
                                    self.digit1,
                                    self.digit2,
                                    self.digit3,
                                    self.multiplier,
                                    str(self.number_of_digits) + 'd',
                                    )
                        if x)

    ##############################################

    def digit_iterator(self):

        return iter([digit for digit in self.digit1, self.digit2, self.digit3, self.multiplier
                     if digit is not None])
            
####################################################################################################

class ResistorDecoder(object):

    ##############################################

    def _append_hypothesis(self, **keys):

        try:
            resistor = Resistor(**keys)
            if resistor.series is not None:
                self.hypotheses.append(resistor)
        except:
            pass

    ##############################################

    def decode(self, colour_names):

        number_of_colours = len(colour_names)
        if number_of_colours < 3:
            raise ValueError("Too few bands")
        
        self.hypotheses = []
        if number_of_colours == 3:
            self._append_hypothesis(digit1=colour_names[0],
                                    digit2=colour_names[1],
                                    multiplier=colour_names[2],
                                    )
            self._append_hypothesis(digit1=colour_names[2],
                                    digit2=colour_names[1],
                                    multiplier=colour_names[0],
                                    )
        if number_of_colours == 4:
            self._append_hypothesis(digit1=colour_names[0],
                                    digit2=colour_names[1],
                                    multiplier=colour_names[2],
                                    tolerance=colour_names[3],
                                    )
            self._append_hypothesis(digit1=colour_names[3],
                                    digit2=colour_names[2],
                                    multiplier=colour_names[1],
                                    tolerance=colour_names[0],
                                    )
            self._append_hypothesis(digit1=colour_names[0],
                                    digit2=colour_names[1],
                                    digit3=colour_names[2],
                                    multiplier=colour_names[3],
                                    )
            self._append_hypothesis(digit1=colour_names[3],
                                    digit2=colour_names[2],
                                    digit3=colour_names[1],
                                    multiplier=colour_names[0],
                                    )
        if number_of_colours == 5:
            self._append_hypothesis(digit1=colour_names[0],
                                    digit2=colour_names[1],
                                    multiplier=colour_names[2],
                                    tolerance=colour_names[3],
                                    temperature_coefficient=colour_names[4],
                                    )
            self._append_hypothesis(digit1=colour_names[4],
                                    digit2=colour_names[3],
                                    multiplier=colour_names[2],
                                    tolerance=colour_names[1],
                                    temperature_coefficient=colour_names[0],
                                    )
            self._append_hypothesis(digit1=colour_names[0],
                                    digit2=colour_names[1],
                                    digit3=colour_names[2],
                                    multiplier=colour_names[3],
                                    tolerance=colour_names[4],
                                    )
            self._append_hypothesis(digit1=colour_names[4],
                                    digit2=colour_names[3],
                                    digit3=colour_names[2],
                                    multiplier=colour_names[1],
                                    tolerance=colour_names[0],
                                    )
        if number_of_colours == 6:
            self._append_hypothesis(digit1=colour_names[0],
                                    digit2=colour_names[1],
                                    digit3=colour_names[2],
                                    multiplier=colour_names[3],
                                    tolerance=colour_names[4],
                                    temperature_coefficient=colour_names[5],
                                    )
            self._append_hypothesis(digit1=colour_names[5],
                                    digit2=colour_names[4],
                                    digit3=colour_names[3],
                                    multiplier=colour_names[2],
                                    tolerance=colour_names[1],
                                    temperature_coefficient=colour_names[0],
                                    )

        return self.hypotheses

####################################################################################################
#
# Test
#
####################################################################################################

if __name__ == '__main__':

    for colour_name in COLOUR_NAMES:
        print COLOUR_CODES[colour_name]
    
    resistor_decoder = ResistorDecoder()
    
    def decode_resistor(colour_names):
        hypotheses = resistor_decoder.decode(colour_names)
        sorted_hypotheses = sorted(hypotheses, cmp=Resistor.cmp_series())
        print '\n', colour_names
        for i, hypothesis in enumerate(sorted_hypotheses):
            print "hypothese %u: %s" % (i +1, hypothesis)
        
    decode_resistor(('brown', 'black', 'red'))
    decode_resistor(('brown', 'black', 'red', 'gold'))
    decode_resistor(('brown', 'black', 'black', 'red'))
    decode_resistor(('red', 'violet', 'red', 'gold'))

####################################################################################################
#
# End
#
####################################################################################################
