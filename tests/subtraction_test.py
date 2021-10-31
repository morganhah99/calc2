"""Testing subtraction function"""
from calc.operations.subtraction import Subtraction


def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    subtraction = Subtraction(1, 2)

    result = subtraction.getresult()

    assert result == -1
