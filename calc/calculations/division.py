"""this is the division operation"""
import pprint
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """ calculation division class"""
    op = 'divide'

    def compute(self):
        """ gets the division results"""
        dividend_of_values = 1.0
        for value in self.values:
            dividend_of_values = value / dividend_of_values
            pprint.pprint(value)
        return dividend_of_values
