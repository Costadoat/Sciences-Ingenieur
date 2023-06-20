# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

fichier=open('essai_maxpid.csv')
contenu=fichier.read()
lignes=contenu.split('\n')
tension=[]
temps=[]
vitesse_moteur=[]
t_start=0
t_end=100
for ligne in lignes[1:-1]:
    ligne=ligne.split(';')
    instant=float(ligne[0])/1000
    if instant>t_start and instant<t_end:
        temps.append(instant-t_start)
        tension.append(float(ligne[1]))
        vitesse_moteur.append(float(ligne[2]))


f=0.0004
Ke=0.053
Kt=Ke
J=0.8*10**(-4)  #?
L=0.0006
R=2.07

K=Kt/(R*f+Ke*Kt)
print(K,(R*f+Ke*Kt))
print(vitesse_moteur[-1])
a=(R*J+L*f)/(R*f+Ke*Kt)
b=L*J/(R*f+Ke*Kt)

E=21.1 # valeur de l'échelon de l'entrée

H=lti([K*E],[b,a,1])              #creation d'une instance de la classe
t,vitesse_moteur_simu=H.step(t=temps)                    #appel de la méthode step de la classe lti
tension_simu=E*np.ones(len(t))

plt.plot(t,tension_simu,label='Tension simulée (V)')                       #affichage
plt.plot(t,vitesse_moteur_simu,label='Vitesse moteur simulée (mm/s)')                       #affichage
plt.plot(temps,tension,label='Tension expérimentale (V)')                       #affichage
plt.plot(temps,vitesse_moteur,label='Vitesse moteur expérimentale (mm/s)')                       #affichage
plt.grid('on')
plt.show()

