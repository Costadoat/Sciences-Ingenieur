# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:07:43 2017

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

dt=0.001

a=100.
b=150.
c=400.
d=350
e=50
p=5.

t=np.arange(0,10,dt)

l2=0.
omega76=-40.

l2_vec=[]
theta3_vec=[]
theta6_vec=[]
omega31_vec=[]
V51_vec=[]

for i in range(len(t)):
    theta3=np.arcsin(l2/(2*c))+np.pi
    theta6=np.arctan((b+d*np.sin(theta3)+e*np.cos(theta3))/(a+d*np.cos(theta3)-e*np.sin(theta3)))
    omega31=(p/(2*np.pi)/(a*np.sin(theta6)-b*np.cos(theta6)))*omega76
    V51=2*c*np.cos(theta3)*omega31
    l2+=dt*V51
    
    l2_vec.append(l2)
    theta3_vec.append(theta3*180/np.pi)
    theta6_vec.append(theta6)
    omega31_vec.append(omega31)
    V51_vec.append(V51)
    
    
plt.plot(t,theta3_vec)
plt.show()
