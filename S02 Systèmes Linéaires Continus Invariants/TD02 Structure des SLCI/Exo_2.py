# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

Ka=34/57
Kb=24*10**(-4)
Kc=12
Kd=Ka
k=0.24*10**3
S=3*10**(-3)
M=500
f=10**(-10)
VB=2*2*10**(-14)

E=1 # valeur de l'échelon de l'entrée

H=lti([Ka*E/(Kd*Kc)],[M*VB/(2*S*Kb*Kc*k*Kd),M*f/(S*Kb*Kc*k*Kd),S/(Kb*Kc*k*Kd),1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti
plt.plot(t[0:len(t)//4],y[0:len(t)//4])                       #affichage

H=lti([Ka*E/(Kd*Kc)],[M*f/(S*Kb*Kc*k*Kd),S/(Kb*Kc*k*Kd),1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti
plt.plot(t[0:len(t/3)],y[0:len(t/3)])                       #affichage

H=lti([Ka*E/(Kd*Kc)],[S/(Kb*Kc*k*Kd),1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti
plt.plot(t,y)                       #affichage

print([M*VB/(2*S*Kb*Kc*k*Kd),M*f/(S*Kb*Kc*k*Kd),S/(Kb*Kc*k*Kd),1])
plt.grid('on')
plt.show()


coeff = [M*VB/(2*S*Kb*Kc*k*Kd),M*f/(S*Kb*Kc*k*Kd),S/(Kb*Kc*k*Kd),1]
coeff = [2*10**(-9),M*f/(S*Kb*Kc*k*Kd),S/(Kb*Kc*k*Kd),1]
print(np.roots(coeff))

