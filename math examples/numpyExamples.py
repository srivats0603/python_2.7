import numpy as np
from numpy import linalg as mathfunc
import cmath
from myMatMult import myMatMult as MM

A = np.matrix('1 2;3 4')
print A
print "determinant of A",'\n', mathfunc.det(A)
print "inverse of A",'\n', mathfunc.inv(A)
print "rank of matrix",'\n', mathfunc.matrix_rank(A)
print "sum of second row of A =", np.sum(A[1,:])
print "sum of first column of A =", np.sum(A[:,0])

Anew = np.matrix('1 2;3 -4')
print "Anew is =",'\n',Anew
print "sum of of second row of Anew =", np.sum(Anew[1,:])
print "sum of abs val of second row of Anew =", np.sum(abs(Anew[1,:]))
print "all elements of Anew divided by 5 = ", '\n' ,np.divide(Anew,5,dtype=float)
print "second of Anew divided by 4= ",'\n',np.divide(Anew[1,:],4,dtype=float)
print "logical result when elements of Anew compared with 0",'\n',np.greater(Anew,0)
print "the elements which exceed zero",'\n',Anew[Anew>0]
print "the indices of elements which exceed zero",'\n',np.argwhere(Anew>0)
print "the elements in Anew which are lesser than 0",'\n',Anew[Anew<0]
print "the indices of elements in the second row are lesser than zero",'\n',np.argwhere(Anew[1,:]<0)
print "the indices of elements in the first row are greater than zero",'\n',np.argwhere(Anew[0,:]>0)
print "the indices of elements in the second row whose absolute value is greater than three",'\n',np.argwhere(abs(Anew[1,:])>3)[:,1]



B = np.matrix('10 2 23 4.3 5 6.5 7 8.2 9 10.1; \
101 21 231 41.3 52 61.5 71 81.2 91 101.1;\
110 22 123 14.3 15 161.5 17 18.2 19 110.1;\
12 25 283 4.3 5 6.5 7 8.2 9 10.1;\
14 26 237 4.3 5 6.5 7 8.2 9 10.1;\
15 28 523 4.3 5 6.5 17 60.2 9 10.1;\
80 22 213 42.3 5 6.15 72 81.2 94 13.1;\
102 51 237 4.23 52 6.25 72 28.2 92 101.1;\
105 212 223 41.3 53 63.5 71 82.2 91 101.1;\
102 22 232 42.3 52 262.5 72 28.2 92 102.1')

print "inverse of B",'\n', mathfunc.inv(B)

Bsqaured = np.matmul(B,B)
print "Square of B", '\n', Bsqaured

B2great50 = np.argwhere(B[1,:]>50.0)
b2list =  B2great50[:,1]
print "the indices of elements in the second row of B greater than 50",'\n',b2list+1


y13 = complex(1,-4)
y12 = complex(2,-4)

Y11 = y13+y12+0.1j
print Y11

"""delete a row and column from B matrix, example: 4"""
Breduced = np.delete(B,3,axis = 0)  #row
Breduced = np.delete(Breduced,3,axis = 1) #column
print "reduced B matrix =",'\n', Breduced

"example zero matrix"
zeroExampleMatrix = np.zeros(3*4)
zeroExampleMatrix = zeroExampleMatrix.reshape(3,4)
print "zero example matrix =",'\n',zeroExampleMatrix


