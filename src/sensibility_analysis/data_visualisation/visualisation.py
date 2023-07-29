import matplotlib.pyplot as plt
from filtering import filter

path = './././ressources/mia.csv'
CF1,CF2,CF3,AF1,AF2,AF3 = filter(path)

def plot_distrib():
    fig, axs = plt.subplots(3,2,figsize=(5,5))
    axs[0,0].scatter(x=AF1,y=AF2,s=0.02)
    axs[0,0].set_xlabel('A_GNPS')
    axs[0,0].set_ylabel('A_SIRIUS')
    axs[0,1].scatter(x=CF1,y=CF2,s=0.02)
    axs[0,1].set_xlabel('S_GNPS')
    axs[0,1].set_ylabel('S_SIRIUS')

    axs[1,0].scatter(x=AF1,y=AF3,s=0.02)
    axs[1,0].set_xlabel('A_GNPS')
    axs[1,0].set_ylabel('A_ISDB')
    axs[1,1].scatter(x=CF1,y=CF3,s=0.02)
    axs[1,1].set_xlabel('S_GNPS')
    axs[1,1].set_ylabel('S_ISDB')

    axs[2,0].scatter(x=AF3,y=AF2,s=0.02)
    axs[2,0].set_xlabel('A_ISDB')
    axs[2,0].set_ylabel('A_SIRIUS')
    axs[2,1].scatter(x=CF3,y=CF2,s=0.02)
    axs[2,1].set_xlabel('S_ISDB')
    axs[2,1].set_ylabel('S_SIRIUS')

    for i in range(3):
        for j in range(2):
            axs[i,j].set_xticks([0,0.5,1])
            axs[i,j].set_yticks([0,0.5,1])
            axs[i,j].set(aspect='equal')
    fig.tight_layout(pad=0.1)
    plt.show()

plot_distrib()