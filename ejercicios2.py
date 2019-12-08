#!/usr/bin/python

#Cilalli Limpens

#ejercicio 4 tarea

#4. Dado 2 cadenas de ADN: 

print "Escribe la secuencia de ADN: ", 
cadena = raw.input();
cadena2 = ''

for ciclos in range(0, len(cadena)):
	if cadena[ciclos] == 'A':
		cadena2 += 'T'
	else if cadena[ciclos] == 'T':
		cadena2 += 'A'