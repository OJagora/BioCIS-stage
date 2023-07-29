import numpy as np

def g(X):
    X1 = X[0]
    X2 = X[1]
    X3 = X[2]
    X4 = X[3]
    X5 = X[4]
    X6 = X[5]
    X7 = X[6]
    X8 = X[7]
    X9 = X[8]
    X10 = X[9]

    res1 = (1-X4)*X5 + X4*X6
    res2 = (1-X4)*X7 + X4*X8
    res3 = (1-X4)*X9 + X4*X10

    R = [res1,res2,res3]
    R.sort()
    res = X3*R[2] + X2*R[1] + X1*R[0]
    
    return res