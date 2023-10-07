# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np
import random as rd


plt.rcParams['text.usetex'] = True

xi=1
w0=350
K=2

A=4/350**3
B=6/350**2
C=-4/350
D=2
a=350

H=lti([K],[1/w0**2,2*xi/w0,1,0])
t,y=H.step(T=np.linspace(0,0.05,1000))


y2=C+D*t+a**2*A*(1-t*a)*np.exp(-a*t)+a**2*B*t*np.exp(-a*t)
y1=C+D*t
y0=D*t
          
plt.xlabel(r'$t\ (s)$')
plt.ylabel(r'$\omega_m(t)\ (rad\cdot s^{-1})$')

plt.plot(t,y0,'k--',label=r'$f(t)=$..................')
plt.plot(t,y1,'k-.',label=r'$g(t)=$..................')
plt.plot(t,y2,'k',label=r'$\omega_m(t)$')
plt.legend()
plt.grid('on')
plt.savefig('img/DR02.eps', format='eps')
plt.show()

plt.xlabel(r'$t\ (s)$')
plt.ylabel(r'$\omega_m(t)\ (rad\cdot s^{-1})$')

plt.plot(t,y0,'k--',label=r'$f(t)=z\cdot t$')
plt.plot(t,y1,'k-.',label=r'$g(t)=z\cdot t-w$')
plt.plot(t,y2,'k',label=r'$\omega_m(t)$')
plt.legend()
plt.grid('on')
plt.savefig('img/DR02_cor.eps', format='eps')
plt.show()
