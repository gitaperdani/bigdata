Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f(ham: str, eggs: str = 'eggs') -> str:
	print("Annotations:", f.__annotations__)
	print("Arguments:", ham, eggs)
	return ham + ' and ' + eggs

>>> f('spam')
Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
>>> 
