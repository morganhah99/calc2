"""Class for the Calculator object that contains all the methods"""
from calc.operations.addition import Addition
from calc.operations.multiplication import Multiplication
from calc.operations.subtraction import Subtraction
from calc.operations.division import Division


class Calculator:
    """ This is the Calculator class"""

    history = []
    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result and appends to history list"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.getresult

    @staticmethod
    def multiply_number(value_a, value_b):
        """multiply number to result"""
        multiplication = Multiplication(value_a, value_b)
        Calculator.history.append(multiplication)
        return Multiplication.getresult

    @staticmethod
    def divide_number(value_a, value_b):
        """divides number to result"""
        division = Division(value_a, value_b)
        Calculator.history.append(division)
        return division.getresult

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return Subtraction.getresult
