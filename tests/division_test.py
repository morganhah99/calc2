"""testing division function"""
from calculator.main import Calculator


def test_calculator_divide():
    """testing the divide method of the calculator"""

    # arrange
    calc = Calculator()

    # act
    calc.add_number(2)
    calc.divide_number(2)

    # assert
    assert calc.get_result() == 1
