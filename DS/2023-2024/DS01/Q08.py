# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np
import random as rd


plt.rcParams['text.usetex'] = True

R=2
L=6*10**(-4)
Ke=44*10**(-3)
Kc=44*10**(-3)
f=1*10**(-2)
J=3*10**(-4)    
K=Kc/(R*f+Ke*Kc)
w0=((R*f+Ke*Kc)/(L*J))**(1/2)
xi=(R*J+L*f)/(2*(L*J*(R*f+Ke*Kc))**(1/2))
print(K,w0,xi)

E=12.5

H=lti([K*E],[1/w0**2,2*xi/w0,1])
t,y=H.step()
y2=[]
for yi in y:
    y2.append(yi+rd.randrange(-5,5,1)/8)

plt.xlabel(r'$t\ (s)$')
plt.ylabel(r'$\omega_m(t)\ (rad\cdot s^{-1})$')

plt.plot(t,y2)
plt.grid('on')
plt.show()

