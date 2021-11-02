"""Testing the Calculator"""
from calc.calculator import Calculator


def test_calculator_result():
    """testing calc result is 0"""
    calc = Calculator()
    assert calc.get_result == 0


def test_calculator_history_static_property():
    """testing the history function of the calculator"""
    calc = Calculator()
    calc.add_number(1, 2)
    assert len(Calculator.history) == 1


def test_calculator_get_result():
    """Testing the Get result method of the calc"""
    calc = Calculator()
    result = calc.add_number(1, 2)
    assert result == 3


def test_calculator_history_getAdditionCalc():
    """ tests to see if you can get an individual history result"""
    calculation = Calculator.history[0]
    assert calculation.getresult() == 3

