#!/usr/bin/python

# prog_13.py

from random import choice
dna = [ "A", "C", "G", "T"]
seq = ''

i = 0
while i <= 20:
    i = i + 1
    seq = seq + choice (dna)
    if i >= 10 and i <= 15:
        continue 
    print i, seq    
    
print "final del programa"
