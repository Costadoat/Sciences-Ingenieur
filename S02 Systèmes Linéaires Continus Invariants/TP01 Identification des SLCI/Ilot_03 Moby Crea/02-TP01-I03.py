# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

###Lecture des données du TP#######
temps=[]
vitesse=[]
tension=[]
courant=[]
fichier=open('data.csv')
contenu=fichier.read()
lignes=contenu.split('\n')
for ligne in lignes[:800]:
    data=ligne.split(';')
    temps.append(float(data[0]))
    vitesse.append(float(data[3]))
##############Fin##################

# Tracé de la vitesse expérimentale
plt.plot(temps,vitesse)

# Données numériques
Ke=0.022
Kt=Ke
R=1.21
J=4.16e-6
U0=7.5
red=44/12
vis=20
f=4*10e-6

# Modèle premier ordre simple
K=Kt/(Ke*Kt+R*f)
tau=R*J/(Kt*Ke+R*f)

# Calcul réponse temporelle
t=np.linspace(0,temps[-1],1000)
omega=K/U0*(1-np.exp(-t/tau))

# Tracé
#plt.plot(t,omega)

# Prise en compte du couple résistant
K2=-K*R/Kt
tau2=tau

# Nouvelles valeurs numériques
wp=U0*K/(red*vis)
Cr0=6*10e-5
Cs0=4*10e-5

# Calcul des coefficients de la décomposition en éléments simples
A=-K2*Cr0*tau2/(1+tau2**2*wp**4)-tau2*K2*Cs0
B=K2*Cr0/(1+tau2**2*wp**4)-tau2*K2*Cs0
C=K2*Cr0*tau2*wp**2/(1+tau2**2*wp**4)
D=K2*Cs0

# Calcul réponse temporelle
omega2=A*np.exp(-t/tau2)+B*np.cos(wp*t)+(C/wp)*np.sin(wp*t)+D
omega=omega+omega2

# Décalage de la réponse temporelle pour synchroniser avec expérimental
dt=0.2
t=np.linspace(dt,temps[-1]+dt,1000)

# Tracé de la courbe
plt.plot(t,omega)
plt.show()


