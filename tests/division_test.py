"""testing division function"""
from calc.operations.division import Division


def test_calculator_divide():
    """testing the divide method of the calc"""

    # arrange
    division = Division(4, 2)

    # act
    result = division.getresult()

    # assert
    assert result == 2
