#!/usr/bin/python

# prog_5.py
a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c', 'd']
c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print "A[3] es ", a[3]
print "Reverso B: ", b[::-1]
print "longitud C: ", len(c)


print ':'.join(b)
b.pop()
print ':'.join(b)
b.pop(0)
print ':'.join(b)
b.insert(0,'z')
print ':'.join(b)
b.append('x')
print ':'.join(b) 

