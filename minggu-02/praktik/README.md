# Catatan Praktik Big Data Minggu 02
## Mengerjakan Tutorial Python di dokumentasi Python bab 2 sampai dengan bab 4.
### Pada link https://docs.python.org/3/tutorial/controlflow.html
## 4.1. if Statements
###
	x = int(input("Please enter an integer: "))
	if x < 0:
		x = 0 
		print('Negative changed to zero')
	elif x == 0: 
		print('Zero')
	elif x == 1: 
		print('Single')
	else:
		print('More')

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python ifstatemen.py
	Please enter an integer: 42
	More
## 4.2. for Statements
###
	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python for.py
	cat 3
	window 6
	defenestrate 12
## 4.3. The range() Function
### 
	for i in range(5):
	print(i)

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python fungsirange.py
	0
	1
	2
	3
	4
## 4.4. break and continue Statements, and else Clauses on Loops
###
	for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		print(n, 'is a prime number')

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python break.py
	2 is a prime number
	3 is a prime number
	4 equals 2 * 2
	5 is a prime number
	6 equals 2 * 3
	7 is a prime number
	8 equals 2 * 4
	9 equals 3 * 3
## 4.6. Defining Functions¶
### 
	def fib(n):
		a, b = 0, 1
		while a < n:
			print(a, end=' ')
			a, b = b, a+b
		print()
	fib(2000)

	fib
	f = fib
	f(100)

	fib(0)
	print(fib(0))

	def fib2(n):  # return Fibonacci series up to n
		result = []
		a, b = 0, 1
		while a < n:
			result.append(a)    # see below
			a, b = b, a+b
		return result
	f100 = fib2(100)    # call it
	f100
	
	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python defining.py
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
	0 1 1 2 3 5 8 13 21 34 55 89


	None
## 4.7.1. Default Argument Values
###
	i = 5

	def f(arg=i):
    	print(arg)

	i = 6
	f()

	def f(a, L=[]):
    	L.append(a)
    	return L

	print(f(1))
	print(f(2))
	print(f(3))

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python defaultargumentvalues2.py
	5
	[1]
	[1, 2]
	[1, 2, 3]

## 4.7.2. Keyword Arguments
###
	def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	    print("-- This parrot wouldn't", action, end=' ')
    	print("if you put", voltage, "volts through it.")
    	print("-- Lovely plumage, the", type)
    	print("-- It's", state, "!")

	parrot(1000)                                          # 1 positional argument
	parrot(voltage=1000)                                  # 1 keyword argument
	parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
	parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
	parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
	parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python keywordarguments.py
	-- This parrot wouldn't voom if you put 1000 volts through it.
	-- Lovely plumage, the Norwegian Blue
	-- It's a stiff !
	-- This parrot wouldn't voom if you put 1000 volts through it.
	-- Lovely plumage, the Norwegian Blue
	-- It's a stiff !
	-- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
	-- Lovely plumage, the Norwegian Blue
	-- It's a stiff !
	-- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
	-- Lovely plumage, the Norwegian Blue
	-- It's a stiff !
	-- This parrot wouldn't jump if you put a million volts through it.
	-- Lovely plumage, the Norwegian Blue
	-- It's bereft of life !
	-- This parrot wouldn't voom if you put a thousand volts through it.
	-- Lovely plumage, the Norwegian Blue
	-- It's pushing up the daisies !

## 4.7.2. Keyword Arguments
###
	def cheeseshop(kind, *arguments, **keywords):
	    print("-- Do you have any", kind, "?")
	    print("-- I'm sorry, we're all out of", kind)
	    for arg in arguments:
        	print(arg)
	    print("-" * 40)
	    for kw in keywords:
        	print(kw, ":", keywords[kw])


	cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python keywordarguments2.py
	-- Do you have any Limburger ?
	-- I'm sorry, we're all out of Limburger
	It's very runny, sir.
	It's really very, VERY runny, sir.
	----------------------------------------
	shopkeeper : Michael Palin
	client : John Cleese
	sketch : Cheese Shop Sketch

## 4.7.4. Unpacking Argument Lists
###
	def parrot(voltage, state='a stiff', action='voom'):
		print("-- This parrot wouldn't", action, end=' ')
		print("if you put", voltage, "volts through it.", end=' ')
		print("E's", state, "!")

	d = {"voltage": "four million", "state": "bleedin' demised","action": "VOOM"}
	parrot(**d)

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python unpackingargumentlist2.py
	-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

## 4.7.6. Documentation Strings
###
	def my_function():
		"""Do nothing, but document it.

		No, really, it doesn't do anything.
		"""
		pass
	print(my_function.__doc__)

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python documentationstring.py
	Do nothing, but document it.

        No, really, it doesn't do anything.

## 4.7.7. Function Annotations
###
	def f(ham: str, eggs: str = 'eggs') -> str:
		print("Annotations:", f.__annotations__)
		print("Arguments:", ham, eggs)
		return ham + ' and ' + eggs

	f('spam')

	E:\bigdatakuliah\bigdata\minggu-02\praktik\src>python annotations.py
	Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
	Arguments: spam eggs
