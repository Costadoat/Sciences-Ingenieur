# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:33:40 2018

@author: PROF
"""

import numpy as np
import matplotlib.pyplot as plt

xmin1, xmax1, resol = 0, 2, 0.01
xmin2, xmax2 = 2, 6
xmin3, xmax3 = 6, 8
l=1

def integrale(x,y):
    nbi = nbx - 1 # nombre d’intervalles
    int = np.linspace(1, 1, nbx)
    int[0]=0
    for i in range(nbi):
        int[i+1] = int[i] + y[i]*(x[i+1]-x[i])
    return int

x1 = np.arange(xmin1, xmax1, resol)
y1=(1/12.)*np.ones(np.shape(x1)[0])
x2 = np.arange(xmin2, xmax2, resol)
y2=0*np.ones(np.shape(x2)[0])
x3 = np.arange(xmin3, xmax3, resol)
y3=-(1/12.)*np.ones(np.shape(x3)[0])
x=np.concatenate((x1,x2,x3))
y=np.concatenate((y1,y2,y3))
nbx=np.shape(x)[0]

z=integrale(x,y)
u=integrale(x,z)

plt.figure(1)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.xlabel(r'$t\ (s)$')
plt.ylabel(r'$\lambda(t)\ (m)$, $\dot{\lambda}(t)\ (m.s^{-1})$, $\ddot{\lambda}(t)\ (m.s^{-2})$')

plt.plot(x,y,'-.',label='$\ddot{\lambda}(t)$')
plt.plot(x,z,'--',label='$\dot{\lambda}(t)$')
plt.plot(x,u,'-',label='$\lambda(t)$')
plt.ylim(-0.2,1.1)
plt.legend()
plt.savefig('lambda.pdf')

plt.figure(2)
alpha=np.arccos(u/(2*l))
beta=np.pi/2.-np.arccos(u/(2*l))
gamma=np.arccos(u/(2*l))-x*1./8.
delta=np.pi/2.-np.arccos(u/(2*l))+x*1./8.


plt.plot(x,beta,'-',label='courbe 1')
plt.plot(x,alpha,':',label='courbe 2')
plt.plot(x,gamma,'-.',label='courbe 3')
plt.plot(x,delta,'--',label='courbe 4')
plt.xlabel(r'$t\ (s)$')
plt.ylabel(r'$\alpha(t)\ (rad)$')
plt.legend()
plt.savefig('alpha.pdf')

