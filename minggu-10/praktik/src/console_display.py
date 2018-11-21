import numpy as np

import pandas as pd

print (pd.DataFrame(np.random.randn(3, 12)))

pd.set_option('display.width', 40) # default is 80
print (pd.DataFrame(np.random.randn(3, 12)))

datafile={'filename': ['filename_01','filename_02'],
						'path': ["media/user_name/storage/folder_01/filename_01",
									"media/user_name/storage/folder_02/filename_02"]}
pd.set_option('display.max_colwidth',30)
print (pd.DataFrame(datafile))

pd.set_option('display.max_colwidth',100)
print (pd.DataFrame(datafile))