import numpy as np
from distributions import sampleInput
from confidence import g

def getAB(N=100) :
    A = []
    B = []
    for i in range(N) :
        A.append(sampleInput())
        B.append(sampleInput())
    return(np.array(A),np.array(B))

def getdAi(A,B,i):
    dA = A.copy()
    dA[:,i] = B[:,i]
    return dA

def EspXi(A,B,i):
    N = len(A)
    val = 0
    dAi = getdAi(A,B,i)
    for j in range(N):
        val += (g(A[j])-g(dAi[j]))**2
    return (1/(2*N))*val

def VarXi(A,B,i):
    N = len(A)
    val = 0
    dAi = getdAi(A,B,i)
    for j in range(N):
        val += (g(A[j])-g(dAi[j]))*g(B[j])
    return (1/N)*val

def Sobols(n=1000,esp = True, var = True) :
    A,B = getAB(n)
    Esp = []
    Var = []
    for i in range(10):
        if esp :
            Esp.append(EspXi(A,B,i))
        if var :
            Var.append(VarXi(A,B,i))

    if esp :
        Esp = Esp/sum(Esp)
    if var :
        Var = Var/sum(Var)
    print('Espi : ', Esp)
    print('Vari : ', Var)
    return Esp,Var
