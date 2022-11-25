# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

fichier=open('essai_cordeuse.csv')
contenu=fichier.read()
lignes=contenu.split('\n')
tension=[]
temps=[]
vitesse_charriot=[]
t_start=3.05
t_end=4.6
for ligne in lignes[1:-1]:
    ligne=ligne.split(';')
    if float(ligne[1])>t_start and float(ligne[1])<t_end:
        temps.append(float(ligne[1])-t_start)
        tension.append(float(ligne[2]))
        vitesse_charriot.append(float(ligne[3]))


Rp=10
red=2*15/(29*55)
f=8*10**(-5)
Ke=0.025
Kt=Ke
J=1.2*10**(-4)
L=0.0011
R=1.1

K=Rp*red*Kt/(R*f+Ke*Kt)
a=(R*J+L*f)/(R*f+Ke*Kt)
b=L*J/(R*f+Ke*Kt)

E=-15 # valeur de l'échelon de l'entrée

H=lti([K*E],[b,a,1])              #creation d'une instance de la classe
t,vitesse_charriot_simu=H.step()                    #appel de la méthode step de la classe lti
tension_simu=E*np.ones(len(t))

plt.plot(t,tension_simu,label='Tension simulée (V)')                       #affichage
plt.plot(t,vitesse_charriot_simu,label='Vitesse charriot simulée (mm/s)')                       #affichage
plt.plot(temps,tension,label='Tension expérimentale (V)')                       #affichage
plt.plot(temps,vitesse_charriot,label='Vitesse charriot expérimentale (mm/s)')                       #affichage
plt.grid('on')
plt.show()

