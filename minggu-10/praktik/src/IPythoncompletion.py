import numpy as np

import pandas as pd

df = pd.DataFrame({'foo1' : np.random.randn(5),
					'foo2' : np.random.randn(5)})

print (df)
print (df.foo1)
