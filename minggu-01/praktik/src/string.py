Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'spam eggs'
'spam eggs'
>>> 'doesn\'t' # untuk menggunakan kutipan
"doesn't"
>>> "doesn't" # atau menggunakan tanda kutip ganda sebagai gantinya
"doesn't"
>>> '"Yes,"they said.'
'"Yes,"they said.'
>>> "\"Yes,\"they said."
'"Yes,"they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.' # \n merupakan baris baru
>>> s # without print (), \n termasuk dalam output
'First line.\nSecond line.'
>>> print(s) # with print(), \n menghasilkan baris baru
First line.
Second line.
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
SyntaxError: invalid syntax
>>> text
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    text
NameError: name 'text' is not defined
>>> text = ('Put several strings within parentheses '
            'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^
                
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
                   
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
>>> word = 'Python'
>>>  word[0]  # character in position 0
'P'
SyntaxError: unexpected indent
>>>  word[0]  # character in position 0
SyntaxError: unexpected indent
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[-6]
'P'
>>> word[0:2] #karakter dari posisi 0 (termasuk) hingga 2 (tidak termasuk)
'Py'
>>> word[2:5] # karakter dari posisi 2 (termasuk) hingga 5 (tidak termasuk)
'tho'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    word[42]  # the word only has 6 characters
IndexError: string index out of range
>>> word[4:42]
'on'
>>> word[42:]
''
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    word[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    word[2:] = 'py'
TypeError: 'str' object does not support item assignment
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>> s = 'supercalifragilisticexpialidocious'
>>> lens(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    lens(s)
NameError: name 'lens' is not defined
>>> len(s)
34
>>> 
