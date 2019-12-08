#!/usr/bin/python

# prog_7.py

mat = [ [1,2,3], 
        [4,5,6], 
        [7,8,9] ]
        
x = [ [0,0,0,0], 
      [0,0,0,0], 
      [0,0,0,0], 
      [0,0,0,0] ]

x[0][0] = 1
x[1][2] = 1
x[2][2] = 1
x[3][0] = 1

print mat
print mat[2][2]
print mat[1][1]
#print mat[2][5]

print x
print x[0][0]
print x[0][1]



