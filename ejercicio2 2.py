#!/usr/bin/pyhton

#Ejercicio 2
#Citlalli Limpens

secuencia = "GAGAGATTTTCTCTAATCATAGCACT"

cA = 0
cT = 0
cG = 0
cC = 0
total = 26

for ciclos in range(1,26):
	if secuencia[ciclos] == "A":
		cA += 1
	elif secuencia[ciclos] == "T":
		cT += 1
	elif secuencia [ciclos] == "C":
		cC += 1
	elif secuencia [ciclos] == "G":
		cG += 1


print "total de A = ", cA
print "total de T = ", cT
print "total de G = ", cG
print "total de C = ", cC

CyG = cC + cG * 1.0 
porcentaje = CyG / total * 100

print "porcentaje GC = ", porcentaje
