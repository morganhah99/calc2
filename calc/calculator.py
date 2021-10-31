from calc.operations.addition import Addition
from calc.operations.multiplication import Multiplication
from calc.operations.subtraction import Subtraction
from calc.operations.division import Division


class Calculator:
    """ This is the Calculator class"""

    history = []

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result and appends to history list"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return Addition.add(value_a, value_b)

    @staticmethod
    def multiply_number(value_a, value_b):
        """multiply number to result"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_number(value_a, value_b):
        """divides number to result"""
        return Division.divide(value_a, value_b)

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        return Subtraction.subtract(value_a, value_b)
