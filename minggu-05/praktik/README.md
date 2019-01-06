# Tutorial Python di dokumentasi Python Minggu-05

## BAB 10
## 10.5. String Pattern Matching
###
	import re
	print (re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
	print (re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

	print ('tea for too'.replace('too', 'two'))

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-05\praktik\src>python string-pattern-matching.py
	['foot', 'fell', 'fastest']
	cat in the hat
	tea for two

## 10.6. Mathematics
### 
	import math
	print (math.cos(math.pi / 4))
	print (math.log(1024, 2))

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-05\praktik\src>python mathematics.py
	0.7071067811865476
	10.0

### 
	import random
	print (random.choice(['apple', 'pear', 'banana']))

	print (random.sample(range(100), 10))   # sampling without replacement

	print (random.random())   # random float

	print (random.randrange(6))    # random integer chosen from range(6)

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-05\praktik\src>python mathematics2.py
	apple
	[46, 43, 71, 80, 90, 20, 3, 36, 32, 65]
	0.44743336794558186
	2

## 10.8. Dates and Times
###
	from datetime import date
	now = date.today()
	print (now)
	now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
	'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

	# dates support calendar arithmetic
	birthday = date(1964, 7, 31)
	age = now - birthday
	print (age.days)

	(name_of_my_env) E:\bigdatakuliah\bigdata\minggu-05\praktik\src>python date-and-times.py
	2019-01-06
	19882