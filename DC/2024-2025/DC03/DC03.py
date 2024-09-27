# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np
import random as rd

H=lti([6],[1/3,1,0])
t,y1=H.step(T=np.linspace(0,1,1000))

y2=-2+6*t+2*np.exp(-3*t)

plt.plot(t,y1)
plt.plot(t,y2)
plt.grid('on')
plt.show()


print(y1-y2)
