#!/usr/bin/pyhton


X = ['A', 'T', 'G', 'C']

from random import choice 

y = choice(X), choice(X), choice(X), choice(X)

print y

z = choice(X), choice(X), choice(X), choice(X)

while z != y:
	print z
	z = choice(X), choice(X), choice(X), choice(X)
	i = 0
	i = i + 1
	print i
	while i != 256:
		continue 
