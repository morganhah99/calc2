"""Testing subtraction function"""
from calculator.main import Calculator


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()

    calc.subtract_number(1)

    assert calc.get_result() == -1
