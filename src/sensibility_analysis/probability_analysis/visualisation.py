import matplotlib.pyplot as plt
import seaborn as sns
from monte_carlo import Sobols,getAB

def showVari(n=1000):
    x = [1,2,3,4,5,6,7,8,9,10]
    plt.xticks(x,['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10'])
    plt.xlabel("Input variable Xi")
    plt.ylabel("first-order sensitivity index")
    plt.title("Main effect index of inputs for 1M samples")
    _,Vari = Sobols(n,esp=False)
    plt.bar(x,Vari)
    plt.show()
    return

def plot_Simulated_Distributions(n=1000):
    fig, axs = plt.subplots(3,2,figsize=(5,5))
    A,B = getAB(n)
    sns.histplot(x = A[:,4], y = A[:,6],bins=100, cmap = 'magma',ax=axs[0,0])
    sns.histplot(x = A[:,5], y = A[:,7],bins=100, cmap = 'magma',ax=axs[0,1])

    sns.histplot(x = A[:,4], y = A[:,8],bins=100, cmap = 'magma',ax=axs[1,0])
    sns.histplot(x = A[:,5], y = A[:,9],bins=100, cmap = 'magma',ax=axs[1,1])

    sns.histplot(x = A[:,8], y = A[:,6],bins=100, cmap = 'magma',ax=axs[2,0])
    sns.histplot(x = A[:,9], y = A[:,7],bins=100, cmap = 'magma',ax=axs[2,1])

    axs[0,0].set_xlabel('X5')
    axs[0,0].set_ylabel('X7')

    axs[0,1].set_xlabel('X6')
    axs[0,1].set_ylabel('X8')

    axs[1,0].set_xlabel('X5')
    axs[1,0].set_ylabel('X9')

    axs[1,1].set_xlabel('X6')
    axs[1,1].set_ylabel('X10')

    axs[2,0].set_xlabel('X9')
    axs[2,0].set_ylabel('X7')

    axs[2,1].set_xlabel('X10')
    axs[2,1].set_ylabel('X8')

    for i in range(3):
        for j in range(2):
            axs[i,j].set_xticks([0,0.5,1])
            axs[i,j].set_yticks([0,0.5,1])
            axs[i,j].set(aspect='equal')
            
    fig.tight_layout(pad=0.1)
    plt.show()
    return

showVari()
plot_Simulated_Distributions()