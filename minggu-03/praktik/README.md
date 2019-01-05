# Tutorial Python di dokumentasi Python bab 3

## 5.1. More on Lists
###
	fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
	print(fruits.count('apple'))

	print(fruits.count('tangerine'))

	print(fruits.index('banana'))

	print(fruits.index('banana', 4))  # Find next banana starting a position 4

	print(fruits.reverse())
	print(fruits)

	print(fruits.append('grape'))
	print(fruits)

	print(fruits.sort())
	print(fruits)

	print(fruits.pop())

	E:\bigdatakuliah\bigdata\minggu-03\praktik\src>python moreonlist.py
	2
	0
	3
	6
	None
	['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
	None
	['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
	None
	['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
	pear

## 5.1.1. Using Lists as Stacks
###
	stack = [3, 4, 5]
	stack.append(6)
	stack.append(7)
	print (stack)

	print (stack.pop())

	print (stack)

	print (stack.pop())

	print (stack.pop())

	print (stack)

	E:\bigdatakuliah\bigdata\minggu-03\praktik\src>python lists-as-stacks.py
	[3, 4, 5, 6, 7]
	7
	[3, 4, 5, 6]
	6
	5
	[3, 4]

## 5.1.2. Using Lists as Queues
###
	from collections import deque
	queue = deque(["Eric", "John", "Michael"])
	queue.append("Terry")           # Terry arrives
	queue.append("Graham")          # Graham arrives
	print (queue.popleft())                 # The first to arrive now leaves

	print (queue.popleft())                 # The second to arrive now leaves

	print (queue)                           # Remaining queue in order of arrival

	E:\bigdatakuliah\bigdata\minggu-03\praktik\src>python lists-as-queues.py
	Eric
	John
	deque(['Michael', 'Terry', 'Graham'])
	
## 5.4. Sets
###
	basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
	print(basket)                      # show that duplicates have been removed

	'orange' in basket                 # fast membership testing

	'crabgrass' in basket

	E:\bigdatakuliah\bigdata\minggu-03\praktik\src>python sets.py
	{'pear', 'apple', 'banana', 'orange'}

## 5.6. Looping Techniques
###
	knights = {'gallahad': 'the pure', 'robin': 'the brave'}
	for k, v in knights.items():
   	 print(k, v)

	for i, v in enumerate(['tic', 'tac', 'toe']):
  	  print(i, v)

	questions = ['name', 'quest', 'favorite color']
	answers = ['lancelot', 'the holy grail', 'blue']
	for q, a in zip(questions, answers):
    	print('What is your {0}?  It is {1}.'.format(q, a))

	for i in reversed(range(1, 10, 2)):
   	 print(i)

	basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
	for f in sorted(set(basket)):
 	   print(f)

	import math
	raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
	filtered_data = []
	for value in raw_data:
   	 if not math.isnan(value):
        filtered_data.append(value)

	filtered_data
	
	E:\bigdatakuliah\bigdata\minggu-03\praktik\src>python looping.py
	gallahad the pure
	robin the brave
	0 tic
	1 tac
	2 toe
	What is your name?  It is lancelot.
	What is your quest?  It is the holy grail.
	What is your favorite color?  It is blue.
	9
	7
	5
	3
	1
	apple
	banana
	orange
	pear
