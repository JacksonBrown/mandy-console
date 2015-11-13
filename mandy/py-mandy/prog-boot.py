
import numpy as np
from fractions import Fraction
import matplotlib
from matplotlib.pyplot import figure, show, rc, grid

def updateThetaAxis(ax):
    thetaFractions = [Fraction.from_float(item/np.pi) for item in ax.get_xticks()]
    labels=[]
    for f in thetaFractions:
        if f.numerator==0:
            labels.append('0')
        elif f.numerator==f.denominator:
            labels.append('\\pi')
        elif f.numerator==1:
            labels.append('\\frac{{\\pi }}{'+str(f.denominator)+'}')
        else:
            labels.append('\\frac{{'+str(f.numerator)+'\\pi }}{'+str(f.denominator)+'}')
    labels = ['$\\Large'+l+'$' for l in labels]
    ax.set_xticklabels(labels,fontsize=20)

def updateRAxis(ax):
    thetaFractions = [Fraction.from_float(item) for item in ax.get_yticks()]
    labels=[]
    for f in thetaFractions:
        if f.numerator==0:
            labels.append('0')
        elif f.numerator==f.denominator:
            labels.append('1')
        elif f.denominator==1:
            labels.append(str(f.numerator))
        else:
            labels.append('\\frac{{'+str(f.numerator)+'}}{'+str(f.denominator)+'}')
    labels = ['$'+l+'$' for l in labels]
    ax.set_yticklabels(labels,fontsize=20)

def makePlot(outputFilename = r'Archimedean_spiral_polar.svg'):
    rc('grid', linewidth=1, linestyle='-') # color='#316931'
    rc('xtick', labelsize=15)
    rc('ytick', labelsize=15)
    rc('font',**{'family':'serif','serif':['Palatino'],'size':14})
    rc('text', usetex=True)

    width, height = matplotlib.rcParams['figure.figsize']
    size = min(width, height)
    fig = figure(figsize=(size, size))
    ax = fig.add_axes([0.12, 0.12, 0.76, 0.76], polar=True, )#axisbg='#d5de9c'

    r = np.arange(0, 3.0, 0.01)
    theta = 2*np.pi*r
    ax.plot(theta, r, color='#ee8d18', lw=3)
    ax.set_rmax(2.0)
    updateThetaAxis(ax)
    updateRAxis(ax)
    grid(True)
    ax.set_title('$\\rho=\\frac{1}{2\\pi}\\theta$',fontsize=20)
    fig.savefig(outputFilename)
    fig.show()

makePlot()

