"""Testing Addition"""
from calc.calculations.addition import Addition
import pandas as pd
import os

outname = '10addition.csv'

outdir = r'C:\Users\imabe\PycharmProjects\calc3\input\10addition.csv'
if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname = os.path.join(outdir, outname)

df.to_csv(fullname)
df = pd.read_csv(r'C:\Users\imabe\PycharmProjects\calc3\input\10addition.csv')
print(df)

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
