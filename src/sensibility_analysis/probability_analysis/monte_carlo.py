import numpy as np
from distributions import sampleInput
from confidence import g

def getAB(N = 100) :
    '''Get A and B for the Sobol indices calculation

    :param int N: number of samples

    :return: A and B arrays
    '''

    A = []
    B = []

    for i in range(N) :
        A.append(sampleInput())
        B.append(sampleInput())

    return(np.array(A), np.array(B))

def getdAi(A, B, i):
    '''Get dAi for the Sobol indices calculation
    
    :param numpy array A: array of values
    :param numpy array B: array of values
    :param int i: index
    
    :return: dAi array'''

    dA = A.copy()
    dA[:, i] = B[:, i]
    return dA

def EspXi(A, B, i):
    '''Calculation of EspXi for the Sobol indices calculation
    
    :param numpy array A: array of values
    :param numpy array B: array of values
    :param int i: index
    
    :return: EspXi value'''

    N = len(A)

    val = 0
    dAi = getdAi(A, B, i)

    for j in range(N):
        val += (g(A[j]) - g(dAi[j]))**2

    return (1 / (2 * N)) * val

def VarXi(A, B, i):
    '''Calculation of VarXi for the Sobol indices calculation

    :param numpy array A: array of values
    :param numpy array B: array of values
    :param int i: index

    :return: VarXi value'''
    
    N = len(A)
    val = 0
    dAi = getdAi(A, B, i)

    for j in range(N):
        val += (g(A[j]) - g(dAi[j])) * g(B[j])

    return (1 / N) * val

def Sobols(n = 1000, esp = True, var = True) :
    A, B = getAB(n)
    Esp = []
    Var = []

    for i in range(10):
        if esp :
            Esp.append(EspXi(A, B, i))
        if var :
            Var.append(VarXi(A, B, i))

    if esp :
        Esp = Esp / sum(Esp)
    if var :
        Var = Var / sum(Var)
    print('Espi : ', Esp)
    print('Vari : ', Var)
    return Esp, Var
