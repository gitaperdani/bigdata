Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def my_function():
	pass

>>> print(my_function.__doc__)
None
>>> def my_function():
	"""Do nothing, but document it.

	No, really, it doesn't do anything.
	"""
	pass

>>> print(my_function.__doc__)
Do nothing, but document it.

	No, really, it doesn't do anything.
	
>>> 
