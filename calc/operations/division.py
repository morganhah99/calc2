"""this is the division operation"""
from calc.operations.calculation import Calculation


class Division(Calculation):
    """method for dividing"""
    def getresult(self):
        """returns value_a / value_b"""
        return self.value_a / self.value_b
