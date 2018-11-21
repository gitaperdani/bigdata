import numpy as np

import pandas as pd

panel = pd.Panel(np.random.randn(3, 5, 4), items=['one', 'two', 'three'],
								major_axis=pd.date_range('1/1/2000', periods=5),
								minor_axis=['a', 'b', 'c', 'd'])
print (panel.to_frame())