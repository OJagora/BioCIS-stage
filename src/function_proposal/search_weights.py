import numpy as np
from function_defintion import f_oct
from scipy.stats import kendalltau, rankdata
from extract_data import get_data

path = "././ressources/novelty.xlsx"
GX,GY,f,index,h_oliv = get_data(path)

ranked_f = rankdata(f)

def get_weights(n = 100):
    w1 = np.linspace(-1,1,n)
    w2 = np.linspace(-1,1,n)
    w3 = np.linspace(-1,1,n)

    vals = []
    inds = []
    for i in range(n) :
        print(int((i/n)*100),'%')
        for j in range(n) :
            for k in range(n) :
                h = f_oct(w1[i],w2[j],w3[k],GX,GY)
                ranked_h = rankdata(h)
                tau, p_value = kendalltau(ranked_f, ranked_h)
                vals.append(tau)
                inds.append((w1[i],w2[j],w3[k]))
                
    print('maximum correlation ',max(vals))
    weights = inds[vals.index(max(vals))]
    print('With w1 : ', weights[0], ' w2 : ', weights[1], ' w3 : ', weights[2])
    return(weights)
