import numpy as np

import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print (s+s)
print (s*2)
print (np.exp(2))
print (s[1:] + s[:-1])