"""Multiplication class"""
from calc.operations.calculation import Calculation


class Multiplication(Calculation):
    """method for multiplying"""
    def getresult(self):
        return self.value_a * self.value_b
