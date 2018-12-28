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

