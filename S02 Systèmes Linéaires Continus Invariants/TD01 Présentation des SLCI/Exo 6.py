# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

K=0.01
Kc=100
tau=60
taud=60
theta0=7
t=np.linspace(0,30*tau,100)

H1=lti([theta0*K*Kc*taud,theta0*K*Kc],[tau+K*Kc*taud,1+K*Kc])              #creation d'une instance de la classe
H2=lti([theta0*Kc*taud*tau,theta0*Kc*(taud+tau),theta0*Kc],[tau*(tau+K*Kc*taud),tau*(1+K*Kc)+tau+K*Kc*taud,1+K*Kc])              #creation d'une instance de la classe
t,y1=H1.step(T=t)                    #appel de la méthode step de la classe lti
t,y2=H2.step(T=t)                    #appel de la méthode step de la classe lti

plt.plot(t,np.ones(len(t))*theta0,label=r'$\theta_c(t)$')                       #affichage
plt.plot(t,y1,label=r'$\theta(t)$')                       #affichage
plt.plot(t,y2,label=r'$p(t)$')                       #affichage
plt.grid('on')
plt.legend()
plt.show()

