# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

K=200
Kv=0.01
Ka=Kv/0.7
K1=1.7
tau1=30

K2=1
tau2=tau1/(1+K*K1*Kv)
E=1 # valeur de l'échelon de l'entrée

H=lti([K2*E],[tau2,1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti
plt.plot(t,y)
plt.grid('on')

plt.savefig('motoreduc_courbe.eps')

H=lti([K2*E],[tau2,1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti
plt.plot([0,t[-1]],[1,1])
plt.plot([0,tau2],[0,1])
plt.plot([tau2,tau2],[0,1])
plt.grid('on')


plt.savefig('motoreduc_courbe_cor.eps')


