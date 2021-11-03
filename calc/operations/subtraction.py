"""subtraction class"""
from calc.operations.calculation import Calculation


class Subtraction(Calculation):
    """subtracting """
    def getresult(self):
        """returns value_a - value_b"""
        return self.value_a - self.value_b
