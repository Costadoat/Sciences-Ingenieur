# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

K=1
tau=0.4
E=-30 # valeur de l'échelon de l'entrée

H=lti([K*E],[tau,1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti

plt.plot(t,y+30*np.ones(len(t)))                       #affichage
plt.grid('on')
plt.show()

