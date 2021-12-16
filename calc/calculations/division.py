"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """ calculation division class"""
    def get_result(self):
        """ gets the division results"""
        dividend_of_values = 1.0
        for value in self.values:
            dividend_of_values = value / dividend_of_values
        return dividend_of_values
