Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3]
9
>>> squares[-3:]
[9, 16, 25]
>>> squares[-2:]
[16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cubes = [1, 8, 27, 65, 125]
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> latters
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    latters
NameError: name 'latters' is not defined
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> 
