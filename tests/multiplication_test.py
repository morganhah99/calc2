"""Testing addition function"""
from calc.operations.multiplication import Multiplication


def test_multiplication():
    """Testing addition method of the calc"""

    multiplication = Multiplication(1, 2)

    result = multiplication.getresult()

    assert result == 2
