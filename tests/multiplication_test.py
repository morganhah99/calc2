"""Testing addition function"""
from calc.calculations.multiplication import Multiplication


def test_multiplication():
    """Testing addition method of the calc"""

    my_numbers = (1.0, 2.0)
    multiplication = Multiplication(my_numbers)
    assert multiplication.get_result() == 2.0
