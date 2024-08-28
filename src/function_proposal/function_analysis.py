import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import kendalltau, rankdata
from function_defintion import f_oct
from extract_data import get_data

#weights determined in search_weights
w1 = -0.172
w2 = 0.192
w3 = -0.434

#Read data
path = "././ressources/novelty.xlsx"
GX, GY, f, index, h_oliv = get_data(path)

def plotf(w1, w2, w3, depth = 1000, ticks = 11, showPoint = False):
    """plotf plots the novelty function f_oct for different pairs of average cosine and tanimotos

    :param float w1: first weight of f
    :param float w2: second weight of f
    :param float w3: third weight of f
    :param int depth: resolution (number of points) of each axis (Average Cosine and Average Tanimoto)
    :param int ticks: number of ticks for each axis
    :param bool showpoint: boolean to toggle wether or not to show expert's predictions overlay 
    """
    print("============================")
    print("======= Plotting of f ======")
    print("============================")
    # constrcut grid of (x,y) points to calculate f
    X, Y = np.mgrid[0:1:1000j, 0:1:1000j]
    # calculate values of novelty
    Z = f_oct(w1, w2, w3, X, Y)

    fig, ax = plt.subplots(figsize = (6, 5))
    fig.suptitle('Novelty')
    Z = np.transpose(Z)
    # plot heatmap of f values
    sns.heatmap(Z[::-1, ::], cmap = 'magma')
    labs = [str(round(x, 2)) for x in np.linspace(0, 1, ticks)]
    tk = [x for x in np.linspace(0,depth,ticks)]
    ax.set_xticks(ticks = tk, labels = labs)
    ax.set_yticks(ticks = tk, labels = labs[::-1])
    ax.set_xlabel('Average Tanimoto')
    ax.set_ylabel('Average Cosine')
    #plot expert values if wanted
    if showPoint:
        sns.scatterplot(x = GX * depth, y = GY * depth, hue = f, cmap='magma')
    plt.show()
    return

def dist(h1,h2) :
    """dist calculates the average error for the set of values

    :param numpy array h1: array of novelty values for first estimator
    :param numpy array h2: array of novelty values for second estimator
    
    :return: percentage of error
    """
    return (abs(h1 - h2)).mean()

h_oct = f_oct(w1, w2, w3, GX, GY)

def comparef(h):
    """comparef scatters the values obtained by a novelty function and compares them to our expert's truth

    :param numpy array h: list of values obtained with a novelty function for the average tanimoto and cosine of our test cases
    """
    print("============================")
    print(" Comparison of predictions  ")
    print("============================")
    fig, ax = plt.subplots()
    # scatter predictions
    plt.scatter(np.linspace(0, 1, len(f)), f, label ='Expert Values', alpha = 0.5)
    plt.scatter(np.linspace(0, 1, len(h)), h, label = 'f Values', alpha = 0.5)
    plt.title("Novelty estimation")
    ax.set_ylabel("f (novelty) value")
    ax.set_xticks([])

    # Calculate Kendall Tau coefficient
    ranked_list1 = rankdata(f)
    ranked_list2 = rankdata(h)
    tau, p_value = kendalltau(ranked_list1, ranked_list2)
    plt.text(0, 0.8, "Correlation : " + str(round(tau * 100, 1)) + "%", weight='bold')
    # calculate relative error
    err = dist(f, h)
    plt.text(0, 0.7, "Relative error : " + str(round(err * 100, 1)) + "%")

    # specify indexes of points scattered
    absi = np.linspace(0, 1, len(f))
    for i,txt in enumerate(index):
        ax.annotate(int(txt), (absi[i], f[i]))
    ax.text(0.22, 0, 'Labels over points are the indexes of the test cases', color='black', 
            bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
    
    plt.legend()
    plt.show()

    print("#Kendall Tau Coefficient:", tau)
    print("#P-value:", p_value)
    return

def plotDiff(h) :
    """plotDiff shows the error of prediction in value for each test case in the form of a scatter plot
    
    :param numpy array h: values obtained with a novelty function for our test cases
    """

    print("============================")
    print("Plotting of prediction error")
    print("============================")
    fig, ax = plt.subplots(figsize=(6, 5))
    # plot diffrence of predicitions for each data point
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
