import numpy as np

def g(w1,w2,w3,wt,X):
    '''Calculation of g according to the paper'''
    X = np.nan_to_num(X)
    a1 = X[0,:]
    s1 = X[1,:]
    a2 = X[2,:]
    s2 = X[3,:]
    a3 = X[4,:]
    s3 = X[5,:]
    res1 = (1-wt)*s1 + wt*a1
    res2 = (1-wt)*s2 + wt*a2
    res3 = (1-wt)*s3 + wt*a3
    R = np.array([res1,res2,res3])
    R = np.transpose(R)
    R = np.sort(R)
    res = w1*R[:,2] + w2*R[:,1] + w3*R[:,0]
    return res

def getDelta(W,ind,X) :
    w1 = W[0]
    w2 = W[1]
    w3 = W[2]
    w4 = W[3]
    if ind == 1 :
        g_max = g(w1,0,1,w4,X)
        g_min = g(w1,1,0,w4,X)
    elif ind == 2 :
        g_max = g(1,w2,0,w4,X)
        g_min = g(0,w2,1,w4,X)
    elif ind == 3 :
        g_max = g(0,1,w3,w4,X)
        g_min = g(1,0,w3,w4,X)
    elif ind == 4 :
        g_max = g(w1,w2,w3,0,X)
        g_min = g(w1,w2,w3,1,X)
    else :
        return None
    diff = np.abs(g_max-g_min)
    return round(diff.mean(),2)


def genDeltas(ind,d==100,X):
    '''Calculatio of the delta with ind specifying the case test
    d is the step of our simulation'''
    deltas = np.zeros((d,d))
    W = np.linspace(0,1,d)
    W4 = np.linspace(0,1,d)
    for i in range(len(W4)):
        for j in range(len(W)):
            w4 = W4[i]
            w = W[j]
            if ind == 1 :
                g_max = g(w,0,1-w,w4,X)
                g_min = g(w,1-w,0,w4,X)
            elif ind == 2 :
                g_max = g(0,w,1-w,w4,X)
                g_min = g(1-w,w,0,w4,X)
            elif ind == 3 :
                g_max = g(0,1-w,w,w4,X)
                g_min = g(1-w,0,w,w4,X)
            elif ind == 4 :
                g_max = g(w,w4,0,0,X)
                g_min = g(w,w4,1-w,1,X)
            elif ind == 5 :
                g_max = g(w,0,w4,0,X)
                g_min = g(w,1-w,w4,1,X)
            else :
                g_max = g(0,w,w4,0,X)
                g_min = g(1-w,w,w4,1,X)
            diff = np.abs(g_max-g_min)
            deltas[i,j] = round(diff.mean(),2)
    return deltas