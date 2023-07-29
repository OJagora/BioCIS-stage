import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import kendalltau, rankdata
import pandas as pd
from function_defintion import f_oct

#weights determined in search_weights
w1 = -0.172
w2 = 0.192
w3 = -0.434

#Read data
path = "././ressources/novelty.xlsx"
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

def plotf(w1,w2,w3,depth=1000,ticks = 11,showPoint = False):
    print("============================")
    print("======= Plotting of f ======")
    print("============================")
    #constrcut grid of (x,y) points to calculate f
    X, Y = np.mgrid[0:1:1000j, 0:1:1000j]
    Z = f_oct(w1,w2,w3,X,Y)

    fig, ax = plt.subplots(figsize=(6, 5))
    fig.suptitle('Novelty')
    Z = np.transpose(Z)
    #plot heatmap of f values
    sns.heatmap(Z[::-1,::],cmap='magma')
    labs = [str(round(x,2)) for x in np.linspace(0,1,ticks)]
    tk = [x for x in np.linspace(0,depth,ticks)]
    ax.set_xticks(ticks = tk, labels = labs)
    ax.set_yticks(ticks = tk, labels = labs[::-1])
    ax.set_xlabel('Average Tanimoto')
    ax.set_ylabel('Average Cosine')
    #plot expert values if wanted
    if showPoint:
        sns.scatterplot(x = GX*depth, y = GY*depth, hue = f, cmap='magma')
    plt.show()
    return

def dist(h1,h2) :
    return (abs(h1-h2)).mean()

h_oct = f_oct(w1,w2,w3,GX,GY)

def comparef(h):
    print("============================")
    print(" Comparison of predictions  ")
    print("============================")
    fig, ax = plt.subplots()
    #scatter predictions
    plt.scatter(np.linspace(0,1,len(f)),f,label ='Expert Values',alpha = 0.5)
    plt.scatter(np.linspace(0,1,len(h)),h, label = 'f Values',alpha = 0.5)
    plt.title("Novelty estimation")
    ax.set_ylabel("f (novelty) value")
    ax.set_xticks([])

    # Calculate Kendall Tau coefficient
    ranked_list1 = rankdata(f)
    ranked_list2 = rankdata(h)
    tau, p_value = kendalltau(ranked_list1, ranked_list2)
    plt.text(0,0.8,"Correlation : "+str(round(tau*100,1))+"%", weight='bold')
    #calculate relative error
    err = dist(f,h)
    plt.text(0,0.7,"Relative error : "+str(round(err*100,1))+"%")

    #specify indexes of points scattered
    absi = np.linspace(0,1,len(f))
    for i,txt in enumerate(index):
        ax.annotate(int(txt), (absi[i],f[i]))
    ax.text(0.22, 0, 'Labels over points are the indexes of the test cases', color='black', 
            bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
    
    plt.legend()
    plt.show()

    print("#Kendall Tau Coefficient:", tau)
    print("#P-value:", p_value)
    return

def plotDiff(h) :
    print("============================")
    print("Plotting of prediction error")
    print("============================")
    fig, ax = plt.subplots(figsize=(6, 5))
    #plot diffrence of predicitions for each data point
    sns.scatterplot(x = GX, y = GY, hue = h-f, palette = 'bwr',s = 100)
    fig.suptitle('Difference of estimations')
    ax.set_xlabel('Average Tanimoto')
    ax.set_ylabel('Average Cosine')

    for i,txt in enumerate(index):
        ax.annotate(int(txt), (GX[i],GY[i]))
    ax.text(0.07, 0, 'Labels over points are the indexes of the test cases', color='black', 
            bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
    
    plt.show()
    return 

plotf(w1,w2,w3)
comparef(h_oct)
plotDiff(h_oct)
