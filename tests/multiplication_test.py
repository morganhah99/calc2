"""Testing multiplication function"""
from calculator.main import Calculator


def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    calc = Calculator()

    calc.multiply_number(1)

    assert calc.get_result() == 0
