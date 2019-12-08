#!/usr/bin/python

# prog_14.py

def revcomp (seq): 
    new = ""
    for i in range( len(seq) ):
        n = seq[i]
        if n == "A":
            new = "T" + new
        elif n == "T":
            new = "A" + new 
        elif n == "G":
            new = "C" + new
        elif n == "C":
            new = "G" + new
            
    return new
    
seq1 = "CATGCTGATGAT"
seq2 = "ATGCGGTGAGTAAG"
print seq1, revcomp(seq1)
print seq2, revcomp(seq2)



