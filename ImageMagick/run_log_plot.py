import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import argparse
# plt.rcParams["figure.figsize"] = (20,20)
# XX_cifar10_resnet110_noshort_SGD_epochs=100_BS=128_LR=0.05_MOM=0.9_WD=0.npy
#XX_cifar10_resnet110_noshort_SGD_IKSA_epochs=100_BS=128_SEED=1234_LR=0.05_MOM=0.9_WD=0_C=2_f=x.npy
def generate_plots(args, log=False):
    dataset = args.dataset
    model = args.model
    optimizer = args.optimizer
    epochs = args.epochs
    BS = args.BS
    LR = args.LR
    MOM = args.MOM
    WD = args.WD
    LM = args.LM
    if LM == 'no':
        NAME = f"{dataset}_{model}_{optimizer}_epochs={epochs}_BS={BS}_LR={LR}_MOM={MOM}_WD={WD}"
        xx = np.load('XX_' + NAME + '.npy')
        yy = np.load('YY_' + NAME + '.npy')
        zz = np.load('ZZ_' + NAME + '.npy')
    elif LM == 'yes':
        C = args.C
        f = args.f
        SEED = args.SEED
        NAME = f"{dataset}_{model}_{optimizer}_epochs={epochs}_BS={BS}_SEED={SEED}_LR={LR}_MOM={MOM}_WD={WD}_C={C}_f={f}"
        xx = np.load('XX_' + NAME + '.npy')
        yy = np.load('YY_' + NAME + '.npy')
        zz = np.load('ZZ_' + NAME + '.npy')
        
    if log:
        zz = np.log(zz)

    ## 3D plot
    fig, ax = plt.subplots(subplot_kw={'projection' : '3d'})
    ax.set_axis_off()
    surf = ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # plt.savefig(f'results/{model}_log_surface_{dataset}.png', dpi=100, format='png', bbox_inches='tight')
    # plt.close()
    fig = plt.figure(figsize=(10, 10))
    ax = Axes3D(fig)
    ax.set_axis_off()

    def init():
        ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        return fig,

    def animate(i):
        ax.view_init(elev=(15 * (i // 15) + i % 15) + 0., azim=i)
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        return fig,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=100, interval=5, repeat=True,blit=True)

    anim.save('GIF_' + NAME + '.gif',
              fps=15,  
              writer='imagemagick')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--LM', type=str, required=True)
    parser.add_argument('--dataset', type=str, required=True)
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--optimizer', type=str, required=True)
    parser.add_argument('--epochs', type=str, required=True)
    parser.add_argument('--BS', type=str, required=True)
    parser.add_argument('--LR', type=str, required=True)
    parser.add_argument('--MOM', type=str, required=True)
    parser.add_argument('--WD', type=str, required=True)
    parser.add_argument('--C', type=str, required=False)
    parser.add_argument('--f', type=str, required=False)
    parser.add_argument('--SEED', type=str, required=False)

    args = parser.parse_args()
    generate_plots(args)