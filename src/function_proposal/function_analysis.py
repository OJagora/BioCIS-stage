import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.optimize import minimize
from scipy.stats import kendalltau, rankdata
from pandas_ods_reader import read_ods

#weights determined in search_weights
w1 = -0.172
w2 = 0.192
w3 = -0.434

#Read data
path = "..\\ressources\\novelty.ods"
df = read_ods(path,columns=['id','c1','c2','c3','t(1, 2)','t(1, 3)','t(2, 3)','nouveauté','commentaire',
                            'nouv corr','a1','a2','a3','zeta1','zeta2','zeta3',
                            'r1','r2','r3','max zeta','middle zeta','min zeta','g','rc','f','est novelty'])
a1 = df['t(1, 2)'].to_numpy()
a2 = df['t(1, 3)'].to_numpy()
a3 = df['t(2, 3)'].to_numpy()
c1 = df['c1'].to_numpy()
c2 = df['c2'].to_numpy()
c3 = df['c3'].to_numpy()
GX = (a1[:19]+a2[:19]+a3[:19])/3
GY = (c1[:19]+c2[:19]+c3[:19])/3
f = df['nouveauté'].to_numpy()
index = df['id'].to_numpy()
f_oliv = df['est novelty'].to_numpy()
h_oliv = np.interp(f_oliv, (min(f_oliv), max(f_oliv)), (0,1))

f = f[:19]
index = index[:19]
h_oliv = h_oliv[:19]

#calculation of f according to paper's defintion
def f_oct(w1,w2,w3,x,y) :
    z1 = np.sin(x)*np.sin(y)
    z2 = np.sin(x+2)*np.sin(y+2)
    z3 = np.sin(x+2)*np.sin(y)
    z4 = np.sin(x)*np.sin(y+2)
    
    z = z1 + w1*z2 + w2*z3 + w3*z4
    #mapping of z values to [1,0]
    z = np.interp(z, (z.min(),z.max()),(1,0))
    return(z)

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
