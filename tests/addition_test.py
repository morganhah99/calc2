"""Testing addition function"""
from calc.operations.addition import Addition


def test_addition():
    """Testing addition method of the calc"""

    # Arrange
    addition = Addition(1, 2)

    # Act
    result = addition.getresult()

    # Assert
    assert result == 3

# or just assert Addition.getResult() == 3
