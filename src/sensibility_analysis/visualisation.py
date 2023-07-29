import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from deltas import genDeltas,getDelta
from matplotlib.collections import LineCollection
from confidence import g

path = '././ressources/mia.csv'
df = pd.read_csv(path)
X = np.array([df['avrege_gnps'],df['score_gnps'],
     df['avrege_sirius'],df['score_sirius'],
     df['avrege_isdb'],df['score_isdb']])

def delta_heatmap(X,n=100,p=11):
    fig, axs = plt.subplots(2,3,figsize=(5,5))
    fig.suptitle('Deltas')

    labs = [str(round(x,2)) for x in np.linspace(0,1,p)]
    tk = [x for x in np.linspace(0,n,p)]

    sns.heatmap(genDeltas(X,1,n),ax = axs[0,0])
    axs[0,0].set_xticks(ticks = tk, labels = labs)
    axs[0,0].set_yticks(ticks = tk, labels = labs[::-1])
    axs[0,0].set_xlabel('W1')
    axs[0,0].set_ylabel('Wt')

    sns.heatmap(genDeltas(X,2,n),ax = axs[0,1])
    axs[0,1].set_xticks(ticks = tk, labels = labs)
    axs[0,1].set_yticks(ticks = tk, labels = labs[::-1])
    axs[0,1].set_xlabel('W2')
    axs[0,1].set_ylabel('Wt')

    sns.heatmap(genDeltas(X,3,n),ax = axs[0,2])
    axs[0,2].set_xticks(ticks = tk, labels = labs)
    axs[0,2].set_yticks(ticks = tk, labels = labs[::-1])
    axs[0,2].set_xlabel('W3')
    axs[0,2].set_ylabel('Wt')

    sns.heatmap(genDeltas(X,4,n),ax = axs[1,0])
    axs[1,0].set_xticks(ticks = tk, labels = labs)
    axs[1,0].set_yticks(ticks = tk, labels = labs[::-1])
    axs[1,0].set_xlabel('W2')
    axs[1,0].set_ylabel('W1')

    sns.heatmap(genDeltas(X,5,n),ax = axs[1,1])
    axs[1,1].set_xticks(ticks = tk, labels = labs)
    axs[1,1].set_yticks(ticks = tk, labels = labs[::-1])
    axs[1,1].set_xlabel('W3')
    axs[1,1].set_ylabel('W1')

    sns.heatmap(genDeltas(X,6,n),ax = axs[1,2])
    axs[1,2].set_xticks(ticks = tk, labels = labs)
    axs[1,2].set_yticks(ticks = tk, labels = labs[::-1])
    axs[1,2].set_xlabel('W2')
    axs[1,2].set_ylabel('W3')
    plt.show()
    return

def plotWt(X,n=1000,w=10) :
    W = np.linspace(0,1,n)
    G = []
    col = []
    for i in range(n):
        G.append(g(0.7,0.2,0.1,W[i],X))
        col.append('g'+str(i))
    inds = G[int(n/2)].argsort()
    for i in range(n) :
        #inds = G[i].argsort()
        G[i] = G[i][inds[::-1]]

    G = np.transpose(G)
    df = pd.DataFrame(G, columns = col)
    for lab in col :
        df[lab] = df[lab].rolling(w).mean()

    df.dropna(inplace=True)

    GS = df.to_numpy()

    GS = np.transpose(GS)
    
    x = np.linspace(0,1,len(GS[-1]))
    xs = np.tile(x,(n,1))

    fig,ax = plt.subplots()
    #np.interp(y, (y.min(), y.max()), (0,1))

    segments = [np.column_stack([x, y]) for x, y in zip(xs, GS)]
    lc = LineCollection(segments,cmap = "coolwarm")
    lc.set_array(np.asarray(W))
    ax.add_collection(lc)
    ax.autoscale()

    axcb = fig.colorbar(lc)
    plt.suptitle("g rolling mean distribution in function of the value of wt")
    plt.title("rolling frame of size 10")
    axcb.set_label("wt")
    plt.xticks([])
    plt.show()
    return

def plotW(ax,X,W,p,n) :
    if p == 1 :
        ind = 2
        W1 = W*np.ones(n)
        W2 = np.linspace(0,1-W,n)
        W3 = np.linspace(1-W,0,n)
    elif p == 2 :
        ind = 3
        W2 = W*np.ones(n)
        W3 = np.linspace(0,1-W,n)
        W1 = np.linspace(1-W,0,n)
    else :
        ind = 1
        W3 = W*np.ones(n)
        W1 = np.linspace(0,1-W,n)
        W2 = np.linspace(1-W,0,n)
        
    G = []
    col = []
    for i in range(n):
        G.append(g(W1[i],W2[i],W3[i],0.5,X))
        col.append('g'+str(i))
    inds = G[int(n/2)].argsort()
    for i in range(n) :
        G[i] = G[i][inds[::-1]]

    G = np.transpose(G)
    df = pd.DataFrame(G, columns = col)
    for lab in col :
        df[lab] = df[lab].rolling(100).mean()

    df.dropna(inplace=True)
    GS = df.to_numpy()
    GS = np.transpose(GS)
    
    x = np.linspace(0,1,len(GS[-1]))
    xs = np.tile(x,(n,1))
    #fig,ax = plt.subplots()
    segments = [np.column_stack([x, np.interp(y, (y.min(), y.max()), (0,1))]) for x, y in zip(xs, GS)]
    lc = LineCollection(segments,cmap = "coolwarm")
    
    if p == 1 :
        lc.set_array(np.asarray(W2))
    elif p == 2 :
        lc.set_array(np.asarray(W3))
    else :
        lc.set_array(np.asarray(W1))
        
    ax.add_collection(lc)
    ax.autoscale()
    #axcb = fig.colorbar(lc)
    #axcb.set_label("w"+str(ind))

def visualize_weights_enveloppes(W = [0.1,0.3,0.5,0.7,0.9],n=1000):
    fig, axs = plt.subplots(3,5)
    for j in range(3) :
        for i in range(len(W)) :
            plotW(axs[j,i],X,W[i],j+1,n)
            axs[j,i].set_xticks([])
            if i != 0 :
                axs[j,i].set_yticks([])
            if i == 0 :
                axs[j,i].set_ylabel("Wi = W"+str(j+1))
            if j == 0 :
                axs[j,i].set_title("Wi = " + str(W[i]))
    plt.show()

visualize_weights_enveloppes()
