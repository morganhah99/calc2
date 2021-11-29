"""Testing Multiplication function"""
from calc.calculations.multiplication import Multiplication


def test_multiplication():
    """Testing multiplication method of the calc"""

    my_numbers = (1.0, 2.0)
    multiplication = Multiplication(my_numbers)
    assert multiplication.compute() == 2.0
