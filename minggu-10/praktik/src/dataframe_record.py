import numpy as np

import pandas as pd

data = [(1,  2., b'Hello'), (2,  3., b'World')],
dtype= [('A', '<i4'), ('B', '<f4'), ('C', 'S10')]


print (data)
print (pd.DataFrame.from_records(data, index='C'))