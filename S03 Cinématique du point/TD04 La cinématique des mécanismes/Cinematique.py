# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:05:00 2015

@author: Renaud
"""
import math
import matplotlib.pyplot as plt
import csv
c = csv.writer(open("MONFICHIER.csv", "wb"))

l1=0.025
l2=0.05
dt=0.001
wm=[]
thetam=[]
theta6=[]
ym=[]
w6=[]
Vm=[]
t=[]

for i in range(0,2000):
    t.append(i*dt)
    wm.append(3*math.pi)
    thetam.append(wm[i]*t[i])
    theta6.append(math.acos(-l1*math.cos(thetam[i])/l2))
    ym.append(l1*math.sin(thetam[i])+l2*math.sin(theta6[i]))
    w6.append((-l1*math.sin(thetam[i])/(l2*math.sin(theta6[i])))*wm[i])
    Vm.append(l1*wm[i]*math.cos(thetam[i])+l2*w6[i]*math.cos(theta6[i]))

#plt.plot(t,Vm)
#plt.ylabel(r'$\theta_1$')
#plt.xlabel(r'$\theta_2$')
#plt.show()

m=3*math.pi
wm4=0
wm21=3*math.pi
wm2=[]
thetam2=[]
theta62=[]
ym2=[]
w62=[]
Vm2=[]
t2=[]

for i in range(0,2000):
    if i==0:
        thetam2.append(0)
        theta62.append(math.acos(-l1/l2))
    t2.append(i*dt)
    Vm2.append(10*l1*math.cos(m*t2[i]))
    wm3=Vm2[i]/(l1*math.cos(thetam2[i])+l2*(-l1*math.sin(thetam2[i])/(l2*math.sin(theta62[i])))*math.cos(theta62[i]))
    c.writerow([i*dt,wm3],)
    wm2.append(wm3)
    wm4=wm4+wm3
    w62.append((-l1*math.sin(thetam2[i])/(l2*math.sin(theta62[i])))*wm2[i])
    if i!=1999:
        theta62.append(theta62[i-1]+w62[i]*dt)
        thetam2.append(thetam2[i-1]+wm2[i]*dt)

plt.plot(t2,wm2)
plt.ylabel(r'$\theta_1$')
plt.xlabel(r'$\theta_2$')
plt.show()