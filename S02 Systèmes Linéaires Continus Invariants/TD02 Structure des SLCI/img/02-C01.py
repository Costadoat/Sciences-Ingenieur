# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

K=200
Kv=0.01
Ka=Kv/0.7
K1=1.66
tau1=30

K2=K*Ka*K1/(1+K*K1*Kv)
tau2=tau1/(1+K*K1*Kv)
E=1 # valeur de l'échelon de l'entrée

H=lti([K2*E],[tau2,1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti
plt.plot(t,y)
plt.grid('on')
plt.show()

