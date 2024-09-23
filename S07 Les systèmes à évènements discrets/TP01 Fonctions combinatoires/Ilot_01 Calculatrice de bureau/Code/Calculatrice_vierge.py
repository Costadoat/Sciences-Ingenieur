# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:51:26 2019

@author: renaud
"""
import matplotlib.pyplot as plt

# Convertir un entier en binaire
def inttobin(a):
    r=[]
    while a!=0 and a!=1:
        r.append(a%2)
        a=a//2
    r.append(a)
    while len(r)<4:
        r.append(0)
    return r

def addition(a,b):
    a=inttobin(a)
    b=inttobin(b)
    # Homogénéiser la longueur de a et b
    while len(a)!=len(b):
        if len(a)>len(b):
            b.append(0)
        else:
            a.append(0)

    n=len(a)

    #Calcul de s0 et r1 (à compléter)
    r=[0]*(n+1)
    s=[0]*n

    

    #Calcul de si et ri+1 (à compléter)
    return s


#Convertir un nombre binaire en entier
def bittoint(a):
    s=0
    for i in range(len(a)):
        s+=2**i*a[i]
    return s

#Décomposition décimale d'un nombre [unité, dixaine, centaine,...]
def decomposition_deci(d):
    rd=[]
    while d>=10:
        r=d%10
        d=d//10
        rd.append(r)
    rd.append(d)
    return rd

#Adaptateur pour 7 segments
def f(a):
    fr=[]
    fr.append(1)
    fr.append(1)
    fr.append(1)
    fr.append(1)
    fr.append(1)
    fr.append(1)
    fr.append(0)
    return fr

#Afficheur 7 segments
def seven_segments(a):
    for i in range(len(a)):
        g=f(inttobin(a[i]))
        if g[0]==1:
            plt.plot([0-i*1.5,1-i*1.5],[2,2],'b')
        if g[1]==1:
            plt.plot([1-i*1.5,1-i*1.5],[1,2],'b')
        if g[2]==1:
            plt.plot([1-i*1.5,1-i*1.5],[0,1],'b')
        if g[3]==1:
            plt.plot([0-i*1.5,1-i*1.5],[0,0],'b')
        if g[4]==1:
            plt.plot([0-i*1.5,0-i*1.5],[0,1],'b')
        if g[5]==1:
            plt.plot([0-i*1.5,0-i*1.5],[1,2],'b')
        if g[6]==1:
            plt.plot([0-i*1.5,1-i*1.5],[1,1],'b')
    plt.axis('equal')
    plt.show()


a=5
b=5
somme=bittoint(addition(a,b))
print(somme)
seven_segments(decomposition_deci(somme))

