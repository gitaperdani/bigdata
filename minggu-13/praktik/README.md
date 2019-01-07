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

## Chapter 8, 9, dan 10 Pandas Cookbook
#### download data yang digunakan pada (https://github.com/PacktPublishing/Pandas-Cookbook)

## Chapter 8
* Tidying variable values as column names with stack
* Tidying variable values as column names with melt
* Stacking multiple groups of variables simultaneously
* Inverting stacked data
* Unstacking after a groupby aggregation
* Replicating pivot_table with a groupby aggregation
* Renaming axis levels for easy reshaping
* Tidying when multiple variables are stored as column names
* Tidying when multiple variables are stored as column values 
* Tidying when two or more values are stored in the same cell 
* Tidying when variables are stored in column names and values 
* Tidying when multiple observational units are stored in the same table

## Chapter 9
* Appending new rows to DataFrames
* Concatenating multiple DataFrames together
* Comparing President Trump's and Obama's approval ratings
* Understanding the differences between concat, join, and merge
* Connecting to SQL databases

## Chapter 10
* Understanding the difference between Python and pandas date tools







