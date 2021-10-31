"""this is the division operation"""
from calc.operations.calculation import Calculation


class Division(Calculation):
    """method for dividing"""
    def getresult(self):
        return self.value_a / self.value_b
