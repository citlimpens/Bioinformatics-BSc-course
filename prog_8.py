#!/usr/bin/python

# prog_8.py

a = {"A1" : 4, "B2" : 7, "C3" : 9}

a["D4"] = 1

print a['A1']
print a['B2']
print a["C3"]

d = "D4"
print a[d]

k = a.keys()
v = a.values()

print "keys: ", k
print "values: ", v
