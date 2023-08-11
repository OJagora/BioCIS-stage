import numpy as np

def f_oct(w1,w2,w3,x,y) :
    """f_oct calculates the novelty of a molecule based on it's average tool tanimotos and cosines
    
    :param float w1: first weight of novelty function
    :param float w2: second weight of novelty function
    :param float w3: third weight of novelty function
    :param float x: average Tanimoto
    :param float y: average Cosine

    :return: float value of f (number in [0,1])
    """
    z1 = np.sin(x)*np.sin(y)
    z2 = np.sin(x+2)*np.sin(y+2)
    z3 = np.sin(x+2)*np.sin(y)
    z4 = np.sin(x)*np.sin(y+2)
    
    z = z1 + w1*z2 + w2*z3 + w3*z4
    #mapping of z values to [1,0]
    z = np.interp(z, (z.min(),z.max()),(1,0))
    return(z)