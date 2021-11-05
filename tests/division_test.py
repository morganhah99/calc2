"""testing division function"""
from calc.calculations.division import Division


def test_calculator_divide():
    """testing the divide method of the calc"""

    # arrange
    my_numbers = (1.0, 2.0)

    # act
    division = Division(my_numbers)

    # assert
    assert division.get_result() == 2.0
