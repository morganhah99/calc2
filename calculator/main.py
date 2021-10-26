"""this is the calculator class"""


class Calculator:
    """ methods of calculator"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result

    def multiply_number(self, value_a):
        """multiply number by value_a"""
        self.result = self.result * value_a
        return self.result

    def divide_number(self, value_a):
        """divides number by value_a"""
        self.result = self.result / value_a
        return self.result
