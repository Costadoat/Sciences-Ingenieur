# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:42:49 2018

@author: PROF
"""

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10,1000)
x1=np.sin(t)
x2=np.sin(t+2*np.pi/3.)
x3=np.sin(t+4*np.pi/3)

plt.plot(t,x1)
plt.plot(t,x2)
plt.plot(t,x3)
plt.show()