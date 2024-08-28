import numpy as np

def g(w1, w2, w3, wt, X):
    '''Calculation of g according to the paper
    
    :param float w1: first weight of g
    :param float w2: second weight of g
    :param float w3: third weight of g
    :param float wt: weight of the average
    :param numpy array X: array of values
    
    :return: g value
    '''
    X = np.nan_to_num(X)
    
    a1 = X[0, :]
    s1 = X[1, :]
    a2 = X[2, :]
    s2 = X[3, :]
    a3 = X[4, :]
    s3 = X[5, :]

    res1 = (1 - wt) * s1 + wt * a1
    res2 = (1 - wt) * s2 + wt * a2
    res3 = (1 - wt) * s3 + wt * a3

    R = np.array([res1, res2, res3])
    R = np.transpose(R)
    R = np.sort(R)

    res = w1*R[:, 2] + w2*R[:, 1] + w3*R[:, 0]

    return res

