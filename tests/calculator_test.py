"""Testing the Calculator"""
from calc.calculator import Calculator


def test_calculator_result():
    """testing calc result is 0"""
    calc = Calculator()
    assert calc.add_number(1, 2) == 3


def test_calculator_history_static_property():
    """testing the history function of the calculator"""
    calc = Calculator()
    calc.add_number(1, 2)
    assert len(calc.history) == 2


def test_calculator_get_result():
    """Testing the Get result method of the calc"""
    calc = Calculator()
    result = calc.add_number(1, 2)
    assert result == 3


def test_calculator_history_get_calc():
    """ test to see if get_last_calculator_result works"""
    calc = Calculator()
    result = calc.add_number(2, 4)
    assert result.get_last_calculator_result == 6
