"""Testing addition function"""
from calc.operations.multiplication import Multiplication


def test_multiplication():
    """Testing addition method of the calc"""
    assert Multiplication.multiply(1, 2) == 2
