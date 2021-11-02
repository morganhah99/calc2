"""Addition Class"""
from calc.operations.calculation import Calculation


class Addition(Calculation):
    """ class for addition"""
    def getresult(self):
        """adds value_a and value_b together"""
        return self.value_a + self.value_b
