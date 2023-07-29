import pandas as pd
import numpy as np

#Read data
def get_data(path) :
    df = pd.read_excel(path, usecols='A,B,C,D,E,F,G,H,Z',skiprows=0,nrows=19)
    data = df.to_numpy()
    a1 = data[:,4]
    a2 = data[:,5]
    a3 = data[:,6]
    c1 = data[:,1]
    c2 = data[:,2]
    c3 = data[:,3]
    GX = (a1+a2+a3)/3
    GY = (c1+c2+c3)/3
    f = data[:,7]
    index = data[:,0]
    f_oliv = data[:,8]
    h_oliv = np.interp(f_oliv, (min(f_oliv), max(f_oliv)), (0,1))
    return(GX,GY,f,index,h_oliv)
