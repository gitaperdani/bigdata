import numpy as np

import pandas as pd

df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print (df + df2)
print (df - df.iloc[0])

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=list('ABC'))
print (df)

print (type(df['A']))
print (df - df['A'])

print (df * 5 + 2)
print (1 / df)
print (df ** 4)

df1 = pd.DataFrame({'a' : [1, 0, 1], 'b' : [0, 1, 1] }, dtype=bool)
df2 = pd.DataFrame({'a' : [0, 1, 1], 'b' : [1, 1, 0] }, dtype=bool)
print (df1 & df2)
print (df1 | df2)
print (df1 ^ df2)
print (-df1)
print (df[:5].T)
print (np.exp(df))
print (np.asarray(df))
print (df.T.dot(df))
s1 = pd.Series(np.arange(5,10))
print (s1.dot(s1))