import numpy as np

import pandas as pd

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
		'Item2' : pd.DataFrame(np.random.randn(4, 2))}

print (pd.Panel(data))
print (pd.Panel.from_dict(data, orient='minor'))

df = pd.DataFrame({'a': ['foo', 'bar', 'baz'],
					'b': np.random.randn(3)})
print (df)

data = {'item1': df, 'item2': df}
panel = pd.Panel.from_dict(data, orient='minor')
print (panel['a'])
print (panel['b'])
print (panel['b'].dtypes)