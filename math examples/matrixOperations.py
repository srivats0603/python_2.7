import numpy as np
from numpy import linalg as mathfunc


A = np.random.rand(3,3)
print A

D = np.diagonal(A)
print D

G = np.zeros(9).reshape(3,3)

for indx in range(0,3):
    G[indx,indx] = D[indx]

print G

Dinv = mathfunc.inv(G)
print Dinv

resMat = Dinv*A
print resMat

q,r = mathfunc.qr(A)
print q
print r

