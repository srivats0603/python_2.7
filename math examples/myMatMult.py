import numpy as np


def myMatMult(A,B):
    #assuming A and B are matrices:
    shapeOfA = np.shape(A)
    shapeOfB = np.shape(B)
    rowInResultMat = shapeOfA[0]
    colInResultMat = shapeOfB[1]
    if shapeOfA[1] != shapeOfB[0]:
        print "inner dimensions mismatch for the two matrices"
        return
    else:
        innerDimAB = shapeOfA[1]
    resultMat = np.zeros(rowInResultMat*colInResultMat)
    resultMat = resultMat.reshape(rowInResultMat,colInResultMat)
    for i in range(0,rowInResultMat):
        for j in range(0,colInResultMat):
            for m in range(0,innerDimAB):
                resultMat[i,j] = resultMat[i,j] + A[i,m]*B[m,j]
    return resultMat
