"""Multiplication Class"""
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """subtraction calculation object"""
    def compute(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
