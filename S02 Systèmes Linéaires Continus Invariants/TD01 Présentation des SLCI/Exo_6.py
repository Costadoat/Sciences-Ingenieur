# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

K=3
theta0=7 # valeur de l'échelon de l'entrée
K=0.01
Kc=100
tau=60
taud=0.1
nb=50000
duree=180
T=np.linspace(0,duree,nb)

print(K*Kc*taud*theta0/(tau+K*Kc*taud))
print(K*Kc*theta0/(1+K*Kc))
H=lti([Kc*K*theta0*taud,K*Kc*theta0],[tau+K*Kc*taud,1+K*Kc])              #creation d'une instance de la classe
t,theta=H.step(T=T)                    #appel de la méthode step de la classe lti
thetac=theta0*np.ones(len(T))
e=thetac-theta
p=[]
for i in range(len(e)-1):
    deps=(e[i+1]-e[i])/(duree/nb)
    pi=Kc*(e[i]+taud*deps)
    p.append(pi)

plt.plot(t,theta,label=r'$\theta(t)$')                       #affichage
plt.plot(t,thetac,label=r'$\theta_c(t)$')                       #affichage
plt.plot(t[:-1],p,label=r'$p(t)$')
plt.legend()
plt.grid('on')
plt.show()

