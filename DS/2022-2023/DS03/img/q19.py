import numpy as np
import matplotlib.pyplot as plt

L=0.052
L0=0.05
l=0.025
alpha=np.linspace(-35,35,100)
alpha=alpha*np.pi/180

def longueur_ressort(alpha):
    return ((L*np.cos(alpha))**2+(L*np.sin(alpha)-l)**2)**0.5-L0

Lr=longueur_ressort(alpha)

def dichotomie(L, a):
    debut = 0
    fin = len(L) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if L[m] == a:
            return m
        elif L[m] < a:
            debut = m + 1
        else:
            fin = m - 1
    return m

print(alpha[dichotomie(Lr, 0)])

plt.plot(alpha,Lr)
plt.grid('on')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$L_r-L_{r0}$')
plt.savefig("q19.pgf")
plt.show()

