# Tutorial Python di dokumentasi Python Minggu 04

## BAB 7
## 7.1. Fancier Output Formatting
###
	s = 'Hello, world.'
	str(s)
	repr(s)
	print(s)
	str(1/7)
	x = 10 * 3.25
	y = 200 * 200
	s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
	print(s)
	# The repr() of a string adds string quotes and backslashes: 
	hello = 'hello, world\n'
	hellos = repr(hello)
	print(hellos)
	# The argument to repr() may be any Python object:
	repr((x, y, ('spam', 'eggs')))
	"The sum of 1 + 2 is {0}".format(1+2)

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-04\praktik\src>python fancierOutput.py
	Hello, world.
	The value of x is 32.5, and y is 40000...
	'hello, world\n'

## 7.1.1. Formatted String Literals
###
	table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
	for name, phone in table.items():
		print(f'{name:10} ==> {phone:10d}')
	animals = 'eels'
	print(f'My hovercraft is full of {animals}.')
	print(f'My hovercraft is full of {animals!r}.')

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-04\praktik\src>python StringLiteral.py
	Sjoerd     ==>       4127
	Jack       ==>       4098
	Dcab       ==>       7678
	My hovercraft is full of eels.
	My hovercraft is full of 'eels'.

## 7.1.2. The String format() Method
###
	print('We are the {} who say "{}!"'.format('knights', 'Ni'))
	print('{0} and {1}'.format('spam', 'eggs'))
	print('{1} and {0}'.format('spam', 'eggs'))
	print('This {food} is {adjective}.'.format(
		food='spam', adjective='absolutely horrible'))
	print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
		other='Georg'))
	table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
	print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
		'Dcab: {0[Dcab]:d}'.format(table))
	table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
	print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
	for x in range(1, 11):
		print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-04\praktik\src>python StringMethod.py
	We are the knights who say "Ni!"
	spam and eggs
	eggs and spam
	This spam is absolutely horrible.
	The story of Bill, Manfred, and Georg.
	Jack: 4098; Sjoerd: 4127; Dcab: 8637678
	Jack: 4098; Sjoerd: 4127; Dcab: 8637678
	 1   1    1
	 2   4    8
	 3   9   27
	 4  16   64
	 5  25  125
	 6  36  216
	 7  49  343
	 8  64  512
	 9  81  729
	10 100 1000

## BAB 8
## 8.3. Handling Exceptions
###
	while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")
	except (RuntimeError, TypeError, NameError):
		pass
	class B(Exception):
	    pass

	class C(B):
	    pass

	class D(C):
	    pass

	for cls in [B, C, D]:
	    try:
	        raise cls()
	    except D:
	        print("D")
	    except C:
	        print("C")
	    except B:
	        print("B")

	import sys

	try:
	    f = open('myfile.txt')
	    s = f.readline()
	    i = int(s.strip())
	except OSError as err:
	    print("OS error: {0}".format(err))
	except ValueError:
	    print("Could not convert data to an integer.")
	except:
	    print("Unexpected error:", sys.exc_info()[0])
	    raise
	for arg in sys.argv[1:]:
	    try:
	        f = open(arg, 'r')
	    except OSError:
	        print('cannot open', arg)
	    else:
	        print(arg, 'has', len(f.readlines()), 'lines')
	        f.close()
	try:
		raise Exception('spam', 'eggs')
	except Exception as inst:
			print(type(inst))    # the exception instance
			print(inst.args)     # arguments stored in .args
			print(inst)          # __str__ allows args to be printed directly,
			                     # but may be overridden in exception subclasses
			x, y = inst.args     # unpack args
			print('x =', x)
			print('y =', y)
	def this_fails():
		x = 1/0

	try:
			this_fails()
	except ZeroDivisionError as err:
		print('Handling run-time error:', err)

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-04\praktik\src>python HandlingExceptions.py
	Please enter a number: 23
	B
	C
	D
	OS error: [Errno 2] No such file or directory: 'myfile.txt'
	<class 'Exception'>
	('spam', 'eggs')
	('spam', 'eggs')
	x = spam
	y = eggs
	Handling run-time error: division by zero
