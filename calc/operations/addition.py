"""Addition Class"""
from calc.operations.calculation import Calculation


class Addition(Calculation):
    """ class for addition"""
    def getresult(self):
        return self.value_a + self.value_b

