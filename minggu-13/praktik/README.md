# Catatan Praktik Big Data Minggu 13
## Di Chapter 09 ketika menjalankan import matplotlib.pyplot as plt eror
### 
	import matplotlib.pyplot as plt
	%matplotlib inline

## Hasil eror
### 
	ModuleNotFoundError Traceback (most recent call last) <ipython-input-12-76a9b0cbbe16> in <module> 2 import numpy as np 3 ----> 4 import matplotlib.pyplot as plt 5 get_ipython().run_line_magic('matplotlib', 'inline') ModuleNotFoundError: No module named 'matplotlib'

## Harus menginstall matplotlib
### 
	(name_of_my_env) C:\Users\Gita Perdani>conda install -f matplotlib
	Solving environment: done






