import math
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5) 
f.read(1)