"""testing division function"""
from calculator.main import Calculator


def test_calculator_divide():
    """testing the divide method of the calculator"""

    # arrange
    calc = Calculator()

    # act
    try:
        calc.divide_number(1)
    except ZeroDivisionError:
        calc.get_result()

    # assert
    assert calc.get_result() == 0
