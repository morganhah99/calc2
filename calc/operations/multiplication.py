"""Multiplication class"""
from calc.operations.calculation import Calculation


class Multiplication(Calculation):
    """method for multiplying"""
    def getresult(self):
        """returns value_a * value_b"""
        return self.value_a * self.value_b
