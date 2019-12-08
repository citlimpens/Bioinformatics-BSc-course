#!/usr/bin/python

#Cilalli Limpens

#ejercicio 4 tarea

#4. Dado 2 cadenas de ADN: 
seq1 = "ACCATGCTATGACGT" 
seq2 = "ACAATGCCATGTCTT" 

seq3 = ["A", "C", "C", "A", "T", "G", "C", "T", "A", "T", "G", "A", "C", "G", "T"] 
seq4 = ["A", "C", "A", "A", "T", "G", "C", "C", "A", "T", "G", "T", "C", "T", "T"] 


cuenta = 0

for ciclos in range(0,14):
	if seq3[ciclos] == seq4[ciclos]:
		cuenta += 1

print cuenta