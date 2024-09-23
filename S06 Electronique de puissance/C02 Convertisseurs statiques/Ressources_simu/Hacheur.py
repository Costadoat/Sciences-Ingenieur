# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:03:11 2018

@author: renaud
"""
import numpy as np
import matplotlib.pyplot as plt

def trace_courant(C,Vin,f,ttotal,R,L):
    P=1/f
    t=0
    d=0
    lt=[]
    lV=[]

    deltat=P/100.
    temps=np.linspace(0,ttotal,ttotal/deltat)
    
    for t in temps:
        lt.append(t)
        if t<P*C+d:
            E=Vin
        else:
            E=0
        lV.append(E)
        t+=deltat
        if t>P+d:
            d+=P
    
    
    def F(y,i):
        return lV[i]/L-R*y/L
    
    
    def euler(F,y0,t):
        N = len(t)
        y = [0]*N
        y[0] = y0
        for i in range(N-1):
            y[i+1] = y[i]+(t[i+1]-t[i])*F(y[i],i)
        return y
    
    
    i=euler(F,0.,temps)
    plt.plot(temps,lV,temps,i)

plt.figure(10)
C=0.5
Vin=200.
f=20.
ttotal=0.1
R=2.84
L=12.8*10**(-3)

trace_courant(C,Vin,f,ttotal,R,L)

plt.figure(100)
C=0.5
Vin=200.
f=100.
ttotal=0.1
R=2.84
L=12.8*10**(-3)
    
trace_courant(C,Vin,f,ttotal,R,L)

plt.figure(1000)
C=0.5
Vin=200.
f=1000.
ttotal=0.1
R=2.84
L=12.8*10**(-3)
    
trace_courant(C,Vin,f,ttotal,R,L)

plt.figure(10000)
C=0.5
Vin=200.
f=10000.
ttotal=0.1
R=2.84
L=12.8*10**(-3)
    
trace_courant(C,Vin,f,ttotal,R,L)