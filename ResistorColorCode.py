####################################################################################################

import math

####################################################################################################

def number_of_digits_of(x):

    if x <= 1:
        return 0
    else:
        return int(math.log10(x)) +1

####################################################################################################

def significant_digits_of(x, number_of_significant_digits):

    return int(x * math.pow(10., number_of_significant_digits - number_of_digits_of(x)))

####################################################################################################

class ValuesSeries(object):

    ##############################################

    def __init__(self, name, number_of_digits, tolerances, values):

        self.name = name
        self.number_of_digits = number_of_digits
        self.number = int(name[1:])
        self.tolerances = tolerances
        self.values = sorted(values)

    ##############################################

    def __cmp__(self, other):

        return cmp(self.number, other.number)

    ##############################################

    def __str__(self):

        return self.name

    ##############################################

    def __contains__(self, value):

        return value in self.values

    ##############################################

    def tolerance_min(self):

        return min(self.tolerances)

    ##############################################

    def tolerance_max(self):

        return max(self.tolerances)

####################################################################################################

E6 = ValuesSeries(name='E6',
                  number_of_digits=2,
                  tolerances=(20,),
                  values=(10, 15, 22, 33, 47, 68))

E12 = ValuesSeries(name='E12',
                   number_of_digits=2,
                   tolerances=(10,),
                   values=(10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82))

E24 = ValuesSeries(name='E24',
                   number_of_digits=2,
                   tolerances=(5, 1),
                   values=(10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
                           11, 13, 16, 20, 24, 30, 36, 43, 51, 62, 75, 91))

E48 = ValuesSeries(name='E48',
                   number_of_digits=3,
                   tolerances=(2,),
                   values=(100, 121, 147, 178, 215, 261, 316, 383, 464, 562, 681, 825,
                           105, 127, 154, 187, 226, 274, 332, 402, 487, 590, 715, 866,
                           110, 133, 162, 196, 237, 287, 348, 422, 511, 619, 750, 909,
                           115, 140, 169, 205, 249, 301, 365, 442, 536, 649, 787, 953))

E96 = ValuesSeries(name='E96',
                   number_of_digits=3,
                   tolerances=(1,),
                   values=(100, 121, 147, 178, 215, 261, 316, 383, 464, 562, 681, 825,
                           102, 124, 150, 182, 221, 267, 324, 392, 475, 576, 698, 845,
                           105, 127, 154, 187, 226, 274, 332, 402, 487, 590, 715, 866,
                           107, 130, 158, 191, 232, 280, 340, 412, 499, 604, 732, 887,
                           110, 133, 162, 196, 237, 287, 348, 422, 511, 619, 750, 909,
                           113, 137, 165, 200, 243, 294, 357, 432, 523, 634, 768, 931,
                           115, 140, 169, 205, 249, 301, 365, 442, 536, 649, 787, 953,
                           118, 143, 174, 210, 255, 309, 374, 453, 549, 665, 806, 976))

E192 = ValuesSeries(name='E192',
                    number_of_digits=3,
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

def series_iterator(number_of_digits_min=2,
                    number_of_digits_max=3,
                    tolerance_min=1,
                    tolerance_max=5):

    for series in E6, E12, E24, E48, E96, E192:
        if (number_of_digits_min <= series.number_of_digits <= number_of_digits_max and
            series.tolerance_min() >= tolerance_min and
            series.tolerance_max() <= tolerance_max):
            yield series

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
            # Not implemented
            self.digit1 = None
            self.digit2 = None
            self.digit3 = None
            self.multiplier = None
            self.digit1_colour = None
            self.digit2_colour = None
            self.digit3_colour = None
            self.multiplier_colour = None
            self.significant_digits  =  None
        else:
            self.digit1_colour = digit1
            self.digit2_colour = digit2
            self.digit3_colour = digit3
            self.multiplier_colour = multiplier
            self._compute_value_from_colours()

        self._init_tolerance(tolerance)
        self._init_temperature_coefficient(temperature_coefficient)
        self.series = self._guess_series()

    ##############################################

    def _init_tolerance(self, tolerance):

        if tolerance is None:
            self.tolerance = None
            self.tolerance_colour = None
        else:
            try:
                self.tolerance = COLOUR_CODES[tolerance].tolerance
                self.tolerance_colour = tolerance
            except KeyError:
                self.tolerance = float(tolerance)

    ##############################################

    def _init_temperature_coefficient(self, temperature_coefficient):

        if temperature_coefficient is None:
            self.temperature_coefficient = None
            self.temperature_coefficient_colour = None
        else:
            try:
                self.temperature_coefficient = COLOUR_CODES[temperature_coefficient].temperature_coefficient
                self.temperature_coefficient_colour = temperature_coefficient
            except KeyError:
                self.temperature_coefficient = float(temperature_coefficient)

    ##############################################

    def _compute_value_from_colours(self):

        try:
            self.digit1 = COLOUR_CODES[self.digit1_colour].digit
            self.digit2 = COLOUR_CODES[self.digit2_colour].digit
        except:
            raise ValueError("Forbidden digit")
        self.multiplier = COLOUR_CODES[self.multiplier_colour].multiplier
        self.significant_digits = self.digit1 * 10 + self.digit2
        if self.digit3_colour is not None:
            self.digit3 = COLOUR_CODES[self.digit3_colour].digit
            self.significant_digits = self.significant_digits * 10 + self.digit3
            self.number_of_digits = 3
        else:
            self.number_of_digits = 2
        self.value = self.significant_digits * self.multiplier

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

        if self.number_of_digits is not None:
            if self.number_of_digits == 2:
                list_of_series = (E6, E12, E24)
            else:
                list_of_series = (E48, E96, E192)
        else:
            list_of_series = (E6, E12, E24, E48, E96, E192)

        resitor_series = None
        for series in list_of_series:
            # print '  ', self.significant_digits, self.tolerance, series.name, series.tolerances
            if resitor_series is not None:
                break
            if self.significant_digits in series:
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
                                    self.digit1_colour,
                                    self.digit2_colour,
                                    self.digit3_colour,
                                    self.multiplier_colour,
                                    str(self.number_of_digits) + 'd',
                                    )
                        if x)

    ##############################################

    def digit_colour_iterator(self):

        return iter([digit for digit in (self.digit1_colour,
                                         self.digit2_colour,
                                         self.digit3_colour,
                                         self.multiplier_colour)
                     if digit is not None])
            
####################################################################################################

class ResistorDecoder(object):

    ##############################################

    def _append_hypothesis(self, **keys):

        print 'Try:', keys
        try:
            resistor = Resistor(**keys)
            # print resistor.value, resistor.series
            # Resistor value must exists in a series and
            # its tolerance must be defined if there is a band for it
            if (resistor.series is not None and
                not (resistor.tolerance_colour is not None  and resistor.tolerance is None) and
                # remove doublon for symetric cases
                resistor.value not in [x.value for x in self.hypotheses]):
                self.hypotheses.append(resistor)
        except:
            # raise
            pass

    ##############################################

    def decode(self, colour_names):

        number_of_colours = len(colour_names)
        if number_of_colours < 3:
            raise ValueError("Too few bands")
        
        self.hypotheses = []
        if number_of_colours == 3:
            # 2 digits
            self._append_hypothesis(digit1=colour_names[0],
                                    digit2=colour_names[1],
                                    multiplier=colour_names[2],
                                    )
            self._append_hypothesis(digit1=colour_names[2],
                                    digit2=colour_names[1],
                                    multiplier=colour_names[0],
                                    )
        if number_of_colours == 4:
            # 2 digits + m + %
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
            # 3 digits + m
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
            # 2 digits + m + % + T
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
            # 3 digits + m + %
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
            # 3 digits + m + % + T
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
        
    # decode_resistor(('brown', 'black', 'red'))
    # decode_resistor(('brown', 'black', 'red', 'gold'))
    # decode_resistor(('brown', 'black', 'black', 'red'))
    # decode_resistor(('red', 'violet', 'red', 'gold'))
    # decode_resistor(('brown', 'black', 'black', 'orange', 'brown')) # 100k E96 1%
    # decode_resistor(('brown', 'black', 'black', 'black', 'brown')) # 100R E96 1%
    # decode_resistor(('orange', 'orange', 'silver', 'gold'))
    # decode_resistor(('orange', 'orange', 'gold', 'gold'))
    # decode_resistor(('brown', 'red', 'black', 'orange', 'brown'))

    value_min = 10.
    value_max = 80.
    number_of_digits_min = 2
    number_of_digits_max = 3
    tolerance_min = 1
    tolerance_max = 5

    for series in series_iterator(number_of_digits_min=number_of_digits_min,
                                  number_of_digits_max=number_of_digits_max,
                                  tolerance_min=tolerance_min,
                                  tolerance_max=tolerance_max):

        significant_digits_min, significant_digits_max = \
            sorted([significant_digits_of(value, series.number_of_digits)
                    for value in value_min, value_max])
        print 'Significant digits:', significant_digits_min, significant_digits_max
        for value in series.values:
            if significant_digits_min <= value <= significant_digits_max:
                ratio = value_min / value
                # print series.name, value, ratio
                if ratio >= 1e-3: # check GR
                    for multiplier in xrange(-2, 9):
                        if ratio <= 10**multiplier:
                            break
                    # print series.name, value, ratio, 10**multiplier, COLOUR_NAMES[multiplier +2]
                    if series.number_of_digits == 2:
                        digit1 = int(value / 10)
                        digit2 = value - digit1 * 10
                        digits = [digit1, digit2]
                    else:
                        digit1 = int(value / 100)
                        digit2 = int((value - digit1 * 100) / 10)
                        digit3 = value - (digit1 * 10 + digit2) * 10
                        digits = [digit1, digit2, digit3]
                    colours = [COLOUR_NAMES[digit +2] for digit in digits]
                    print series.name, value, 10**multiplier, format_value(value * 10**multiplier), colours, COLOUR_NAMES[multiplier +2]

####################################################################################################
#
# End
#
####################################################################################################
