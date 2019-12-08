#!/usr/bin/python

#ejercicio2p2.py

def revcomp (seq):
    bases = seq.split("")
    new = "";
    for n in bases:
        if n == "A":
            new = "A" + new
        elif n == "T":
            new = "T" + new 
        elif n == "G":
            new = "G" + new
        elif n == "C":
            new = "C" + new
    return new
    
seq1 = "CATGCTGATGAT"
seq2 = "ATGCGGTGAGTAAG"
print seq1, revcomp(seq1)
print seq2, recvomp(seq2)


