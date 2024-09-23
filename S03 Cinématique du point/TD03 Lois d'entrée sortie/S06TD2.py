# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:57:42 2017

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt


print 'Exercice 1:'

a=0.08
b=0.065

omega10=np.pi/2
dt=0.01

t=np.arange(0,1,dt)

theta1=np.zeros(len(t))
theta1[0]=0
for i in range(len(t)):
    theta1[i]=theta1[i-1]+dt*omega10

theta2=np.arccos(-l1*np.cos(theta1)/l2)


Vc=l1*omega10*(np.sin(theta1)-np.tan(theta2)*np.cos(theta1))
omega20=-omega10*(l1*np.cos(theta1))/(l2*np.cos(theta2))

Ac=l1*omega10*(omega10*np.cos(theta1)-omega20*np.cos(theta1)/np.cos(theta2)**2+omega10*np.tan(theta2)*np.sin(theta1))

plt.figure(1)
plt.subplot(221)
plt.plot(t, theta1)
plt.title('Theta1')
plt.subplot(222)
plt.plot(theta1, theta2)
plt.title('Theta2')
plt.subplot(223)
plt.plot(theta1, Vc)
plt.title('Vc')
plt.subplot(224)
plt.plot(theta1, Ac)
plt.title('Ac')

print 'Exercice 2:'

t=np.arange(0,61,0.1)
p=125-20*t/61

plt.figure(2)
plt.plot(t,p)

print np.sqrt(14**2-1)

t=np.arange(0,61,0.1)
p=125-20*t/61


o=157
theta=np.arange(0,2*np.pi,0.01)
t=theta/o
vh=2*o*np.cos(theta)

plt.figure(3)
plt.plot(t,vh)