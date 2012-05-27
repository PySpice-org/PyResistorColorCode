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
