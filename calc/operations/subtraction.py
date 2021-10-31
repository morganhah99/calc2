"""subtraction class"""
from calc.operations.calculation import Calculation


class Subtraction(Calculation):
    """subtracting """
    def getresult(self):
        return self.value_a - self.value_b
