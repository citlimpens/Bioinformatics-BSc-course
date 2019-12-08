#!/usr/bin/python

# prog_10.py

from random import choice
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = choice(a) 

if num > 5:
    print num, " es mayor  a 5"

elif num == 5:
    print num, " igual a 5"

else:
    print num, " es menor que 5"

