f = open('workfile', 'w')
with open('workfile') as f:
	read_data = f.read()
f.closed
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')