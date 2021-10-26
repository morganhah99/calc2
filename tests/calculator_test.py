"""Testing the Calculator"""
from calculator.main import Calculator


def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1
