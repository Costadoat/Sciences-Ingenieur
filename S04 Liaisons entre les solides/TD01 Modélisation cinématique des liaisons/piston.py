# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:07:43 2017

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

dt=0.001

a=20.
b=100.

t=np.arange(0,10,dt)

theta1=0.
omega1=1.

theta1_vec=[]
theta2_vec=[]
omega1_vec=[]
omega2_vec=[]
omega3_vec=[]
v30_vec=[]

for i in range(len(t)):
    theta2=np.arccos(-(a/b)*np.cos(theta1))
    omega2=-(a*np.sin(theta1)+b*np.sin(theta2))/(b*np.sin(theta2))*omega1
    omega3=-omega1-omega2
    v30=-(a*np.cos(theta1)+b*np.cos(theta2))*omega3-a*np.cos(theta1)*omega2
    theta1+=omega1*dt
    
    theta1_vec.append(theta1)
    theta2_vec.append(theta2)
    omega1_vec.append(omega1)
    omega2_vec.append(omega2)
    omega3_vec.append(omega3)
    v30_vec.append(v30)

plt.plot(t,v30_vec)