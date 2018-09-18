Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def function(a):
	pass

>>> function(0, a=0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    function(0, a=0)
TypeError: function() got multiple values for argument 'a'
>>> function(0, a=3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    function(0, a=3)
TypeError: function() got multiple values for argument 'a'
>>> 
