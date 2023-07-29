import pandas as pd
import numpy as np

def filter(path,max = 0.99, min = 0.001):
    df = pd.read_csv(path)
    C1 = df['score_gnps'].to_numpy()
    A1 = df['avrege_gnps'].to_numpy()

    C2 = df['score_sirius'].to_numpy()
    A2 = df['avrege_sirius'].to_numpy()

    C3 = df['score_isdb'].to_numpy()
    A3 = df['avrege_isdb'].to_numpy()

    CF1 = []
    CF2 = []
    CF3 = []
    AF1 = []
    AF2 = []
    AF3 = []

    for i in range(len(C1)):
        c1 = C1[i]
        c2 = C2[i]
        a1 = A1[i]
        a2 = A2[i]

        if (c1<max)*(c2<max)*(a1>min)*(a2>min) :
            CF1.append(c1)
            CF2.append(c2)
            CF3.append(C3[i])
            AF1.append(a1)
            AF2.append(a2)
            AF3.append(A3[i])

    CF1 = np.array(CF1)
    CF2 = np.array(CF2)
    CF3 = np.array(CF3)
    AF1 = np.array(AF1)
    AF2 = np.array(AF2)
    AF3 = np.array(AF3)
    return(CF1,CF2,CF3,AF1,AF2,AF3)