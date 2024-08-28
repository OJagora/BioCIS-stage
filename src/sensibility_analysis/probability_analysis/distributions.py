import random
import numpy as np

def getNorm(mean,std):
    '''getNorm generates a random number from a normal distribution with mean and std
    
    :param float mean: mean of the normal distribution
    :param float std: standard deviation of the normal distribution
    
    :return: random number from a normal distribution'''

    p = -1
    while p < 0 or p > 1 :
        p = np.random.normal(mean, std)
    return p

def getBiNorm(mean1,std1,mean2,std2):
    '''getBiNorm generates a random number from a bimodal normal distribution with mean1, std1, mean2 and std2

    :param float mean1: mean of the first normal distribution
    :param float std1: standard deviation of the first normal distribution
    :param float mean2: mean of the second normal distribution
    :param float std2: standard deviation of the second normal distribution

    :return: random number from a bimodal normal distribution'''

    c = random.randint(0, 2)
    p = 0

    if c == 0 :
        p = getNorm(mean1,std1)

    elif c == 1 :
        p = getNorm(mean2,std2)

    return p
    
def sampleInput() :
    '''sampleInput generates a random input for the function

    :return: random input for the function'''

    X1 = random.uniform(0, 1)
    X2 = random.uniform(0, 1)
    X3 = random.uniform(0, 1)

    norm = X1 + X2 + X3

    X1 = X1 / norm
    X2 = X2 / norm
    X3 = X3 / norm
    X4 = random.uniform(0, 1)

    T = random.randint(0, 3)

    if T == 0 :
        X5 = getBiNorm(0.1, 0.05, 0.56, 0.05)
        X6 = random.uniform(0, 1)

        X7 = getNorm(X5, 0.021)
        X8 = getNorm(X6, 0.323)

        X9 = getNorm(X5, 0.16)
        X10 = getNorm(X6, 0.331)

    elif T == 1 :
        X7 = getBiNorm(0.11, 0.05, 0.56, 0.05)
        X8 = random.uniform(0, 1)

        X5 = getNorm(X7, 0.021)
        X6 = getNorm(X8, 0.0323)

        X9 = getNorm(X7,0.163)
        X10 = getNorm(X8, 0.253)

    else :
        X9 = getNorm(0.1, 0.05)
        X10 = getNorm(0.55, 0.1)

        X5 = getNorm(X9, 0.016)
        X6 = getNorm(X10, 0.331)

        X7 = getNorm(X9,0.163)
        X8 = getNorm(X10, 0.253)
    
    return [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]