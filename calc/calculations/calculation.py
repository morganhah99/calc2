"""Calculation Class"""
from abc import ABC
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication


class Calculation(ABC):
    """ calculation abstract base class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple, op):
        """ constructor method"""
        self.op = op
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    @classmethod
    def create(cls, values: tuple, op):
        """ factory method"""
        if op == 'add':
            return cls(Addition.create(values))

        elif op == 'subtract':
            return cls(Subtraction.create(values))

        elif op == 'multiply':
            return cls(Multiplication.create(values))

        elif op == 'divide':
            return cls(Division.create(values))

    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """ standardize values to list of floats"""
        # lists can be modified and tuple cannot, tuple are faster.
        # We need to convert the tuple of potentially random data types (its raw data)
        # into a standard data format to keep things consistent so we convert it to float
        # then i make it a tuple again because i actually won't need to change the calculation
        # values. I can also use it as a list and then i would be able to edit the calculation
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)



