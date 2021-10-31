"""Testing addition function"""
from calc.operations.addition import Addition


def test_addition():
    """Testing addition method of the calc"""

    # Arrange
    addition = Addition(1, 2)

    # Act
    result = addition.getResult()

    # Assert
    assert result == 3

# or just assert addition.getResult() == 3