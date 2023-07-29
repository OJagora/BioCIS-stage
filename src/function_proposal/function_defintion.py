import numpy as np

def f_oct(w1,w2,w3,x,y) :
    z1 = np.sin(x)*np.sin(y)
    z2 = np.sin(x+2)*np.sin(y+2)
    z3 = np.sin(x+2)*np.sin(y)
    z4 = np.sin(x)*np.sin(y+2)
    
    z = z1 + w1*z2 + w2*z3 + w3*z4
    #mapping of z values to [1,0]
    z = np.interp(z, (z.min(),z.max()),(1,0))
    return(z)