"""Testing Addition"""
from calc.calculations.addition import Addition
import pandas as pd
from Fileutilities.absolutepath import absolutepath
path = absolutepath(r'C:\Users\imabe\PycharmProjects\calc3\input\10addition.csv')

data = pd.read_csv(path)
print(data)
def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
