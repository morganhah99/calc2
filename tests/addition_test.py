"""Testing addition function"""
from calculator.main import Calculator


def test_calculator_add():
    """Testing addition method of the calculator"""
    calc = Calculator()

    calc.add_number(1)

    assert calc.result == 1
