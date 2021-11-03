""" calculation class"""


class Calculation:
    """Default Constructor for calculation object"""
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b


@classmethod
def create(cls, value_a, value_b):
    """cls represents the class that it is"""
    return cls(value_a, value_b)
