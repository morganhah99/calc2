import os

import pandas as pd

class Read:
    @staticmethod
    def DataFrameFromCSVFile(filename):
        return pd.read_csv(os.path.abspath(filename))


stuff = Read.DataFrameFromCSVFile('../input/10addition.csv')
print(stuff)