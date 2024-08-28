import matplotlib.pyplot as plt
from filtering import filter
import seaborn as sns
from scipy.stats import norm
import numpy as np

path = './././ressources/mia.csv'
CF1, CF2, CF3, AF1, AF2, AF3 = filter(path)

def plot_distrib():
    """plot_distrib plots the distribution of the data"""
    fig, axs = plt.subplots(3, 2, figsize=(5, 5))
    axs[0, 0].scatter(x = AF1, y = AF2, s = 0.02)
    axs[0, 0].set_xlabel('A_GNPS')
    axs[0, 0].set_ylabel('A_SIRIUS')
    axs[0, 1].scatter(x = CF1, y = CF2, s = 0.02)
    axs[0, 1].set_xlabel('S_GNPS')
    axs[0, 1].set_ylabel('S_SIRIUS')

    axs[1, 0].scatter(x = AF1, y = AF3, s = 0.02)
    axs[1, 0].set_xlabel('A_GNPS')
    axs[1, 0].set_ylabel('A_ISDB')
    axs[1, 1].scatter(x = CF1, y = CF3, s = 0.02)
    axs[1, 1].set_xlabel('S_GNPS')
    axs[1, 1].set_ylabel('S_ISDB')

    axs[2, 0].scatter(x = AF3, y = AF2, s = 0.02)
    axs[2, 0].set_xlabel('A_ISDB')
    axs[2, 0].set_ylabel('A_SIRIUS')
    axs[2, 1].scatter(x = CF3, y = CF2, s = 0.02)
    axs[2, 1].set_xlabel('S_ISDB')
    axs[2, 1].set_ylabel('S_SIRIUS')

    for i in range(3):
        for j in range(2):
            axs[i, j].set_xticks([0, 0.5, 1])
            axs[i, j].set_yticks([0, 0.5, 1])
            axs[i, j].set(aspect = 'equal')
    fig.tight_layout(pad = 0.1)
    plt.show()
    return 

def histogram():
    """histogram plots the histogram of the data"""
    fig, axs = plt.subplots(3, 2)
    n = 0.01
    x = np.linspace(0, 1, int(1/n))

    sns.histplot(x = AF1, stat = "probability", binwidth = n, alpha = 0.2, ax = axs[0, 0])
    y10 = norm.pdf(x, loc = 0.1, scale = 0.05)
    y11 = norm.pdf(x, loc = 0.56, scale = 0.05)
    y1 = (y10 + y11) / 2
    axs[0, 0].plot(x, n * y1)

    sns.histplot(x = CF1, stat = "probability", binwidth = n, alpha = 0.2, ax = axs[0, 1])
    y2 = np.ones(len(x))
    axs[0, 1].plot(x, n * y2)

    sns.histplot(x = AF2, stat = "probability", binwidth = n, alpha = 0.2, ax = axs[1, 0])
    y20 = norm.pdf(x, loc = 0.11, scale = 0.05)
    y21 = norm.pdf(x, loc = 0.56, scale = 0.05)
    y3 = (y20 + y21) / 2
    axs[1, 0].plot(x, n * y3)

    sns.histplot(x = CF2, stat = "probability", binwidth = n, alpha = 0.2, ax = axs[1, 1])
    y4 = np.ones(len(x))
    axs[1, 1].plot(x, n * y4)

    sns.histplot(x = AF3, stat = "probability", binwidth = n, alpha = 0.2, ax = axs[2, 0])
    y5 = norm.pdf(x, loc = 0.1, scale = 0.05)
    axs[2, 0].plot(x, n * y5)

    sns.histplot(x = CF3, stat = "probability", binwidth = n, alpha = 0.2, ax = axs[2, 1])
    y6 = norm.pdf(x, loc = 0.55, scale = 0.1)
    axs[2, 1].plot(x, n * y6)
    plt.show()
    return

plot_distrib()
histogram()