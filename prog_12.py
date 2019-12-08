#!/usr/bin/python

# prog_12.py

from random import choice
dna = [ "A", "C", "G", "T"]
seq = ''

for i in range(1, 20, 1):
    seq = seq + choice (dna)
    print i,  seq

