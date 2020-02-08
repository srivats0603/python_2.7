"""
author: srivats

solves for Ax = b

uses Gaussian Elimination
"""


import numpy as np
from numpy import matrix as mat
import datetime
from datetime import datetime as dt

def doElimination(Afun,bfun,dimAfun,dimbfun):
    for i in range(1,dimAfun[0]):
       this_m = Afun[i,0]/Afun[0,0]
       #print "m for this row=",this_m
       Afun[i,0] = this_m
       #do elimination on each row of B
       bfun[i,0] = bfun[i,0] - Afun[i,0] * bfun[0,0]
       #do elimination on each row of A
       for j in range(1,dimAfun[1]):
           Afun[i,j] = Afun[i,j] - Afun[i,0] * Afun[0,j]
    #print Afun
    #print bfun
    newdimA = (dimAfun[0]-1,dimAfun[1]-1)
    newdimb = (dimbfun[0]-1,dimbfun[1])
    if newdimA[0] > 1:
        newA = Afun[1:dimAfun[0],1:dimAfun[1]]
        newb = bfun[1:dimbfun[0],0]
        doElimination(newA,newb,newdimA,newdimb)
    return

def doBackSubst(A,b):
    dimx = A.shape[1]
    x = np.zeros((dimx,1))
    x[dimx-1,0] = b[dimx-1,0]/A[dimx-1,dimx-1]
    while dimx>0:
        dimx = dimx-1
        sumThis = 0
        for j in range(dimx+1,x.shape[0]):
            sumThis = sumThis+A[dimx,j]*x[j,0]
        x[dimx,0] = (b[dimx,0]-sumThis)/A[dimx,dimx]
    return x

def GaussElim(A,b):
    dimA = A.shape
    #print dimA
    dimb = b.shape
    #print dimb
    if dimA[0] != dimb[0]:
        print "dimension mismatch"
        print "dimension of A=",dimA,"while dimension of b=",dimb
        return
    else:
        x = np.ones(dimA[1])
        doElimination(A,b,dimA,dimb)
        x = doBackSubst(A,b)
        return x


if __name__ == '__main__':
    #A = np.matrix('2 1 -1 3; -2 0 0 0; 4 1 -2 6;-6 -1 2 -3')
    #b = np.matrix('13;-2;24;-14')
    A = np.random.rand(750,750)
    b = np.random.rand(750,1)
    A = np.asmatrix(A)
    b = np.asmatrix(b)
    #print "A is", A
    #print "b is", b
    st_inv = dt.now()
    x_inv=np.linalg.inv(A)*b
    #print "x calculated by inverting=\n", x_inv
    en_inv = dt.now()
    print "time taken by inverting method=", en_inv-st_inv
    st_ga = dt.now()
    x = GaussElim(A,b)
    en_ga = dt.now()
    #print "x calculated by Gauss Elimination=\n", x
    print "time taken by Gauss Elimination method=", en_ga-st_ga
    
