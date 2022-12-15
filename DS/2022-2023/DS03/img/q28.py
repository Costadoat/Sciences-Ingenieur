# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

K=1
tau=1/441
E=1 # valeur de l'échelon de l'entrée

t=np.linspace(0,0.5,1000)
H=lti([K*E],[tau,0,1])              #creation d'une instance de la classe
t,y=H.step(T=t)                    #appel de la méthode step de la classe lti

plt.plot(t,y)                       #affichage
plt.grid('on')
#plt.show()

plt.savefig("q27.pgf")
