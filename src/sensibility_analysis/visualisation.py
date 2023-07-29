import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from deltas import genDeltas,getDelta

df = pd.read_csv('C:\\Users\\octav\\Desktop\\stage\\data\\octave.csv')
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

delta_heatmap(X)