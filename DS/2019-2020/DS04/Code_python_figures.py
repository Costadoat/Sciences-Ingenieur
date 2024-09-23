# -*- coding: utf-8 -*-
"""
MP - DS 02 - 2/12/2016
Merci à Lionel Grillet pour le code
"""

""" BIBLIOTHEQUE """
import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as op

""" CONSTANTES """
L0=50
L1=25
L2=62.5

""" Paramètres """
#liste de valeur pour Theta1
Theta1=np.linspace(-np.pi,np.pi,360)

# Création des listes Theta2 et Theta3
Theta2=[]
Theta3=[]

#Initialisation des valeur de Theta2 et Theta3 pour la résolution
Theta20=2*np.pi/3
Theta30=-2*np.pi/3
init=[Theta20,Theta30]

""" FONCTIONS """
# Système d'équation à résoudre
def Sys(X,arg):
    t2,t3=X
    t1=arg
    f1=L0+L1*np.cos(t1)-L2*np.cos(t2)-L2*np.cos(t3)
    f2=L1*np.sin(t1)-L2*np.sin(t2)-L2*np.sin(t3)
    return [f1,f2]

""" PROGRAMME PRINCIPAL"""
for angle in Theta1:
    sol=op.fsolve(Sys,init,angle)
    Theta2.append(sol[0])
    Theta3.append(sol[1])
    init=[sol[0],sol[1]]

""" Position du point E """
XE=L0+L1*np.cos(Theta1)-2*L2*np.cos(Theta3)
YE=L1*np.sin(Theta1)-2*L2*np.sin(Theta3)

""" Dérivation """
n=len(XE)
dYE=[]
for i in range(n-1):
    dYE.append((YE[i+1]-YE[i])/(XE[i+1]-XE[i]))
dYE.append(dYE[0])


""" Calcul du rapport Cm/F """
CmF=[]
for i in range(len(Theta1)):
    CmF.append(L1*(np.sin(Theta1[i])*np.sin(Theta3[i]-Theta2[i])+2*np.sin(Theta3[i])*np.sin(Theta2[i]-Theta1[i]))/np.sin(Theta3[i]-Theta2[i]))

""" Courbe YE=f(XE) """

pl.xlim(-60,60)
#pl.ylim(95,125)
pl.xlabel('$X_E (mm)$')
pl.ylabel('$Y_E (mm)$')
pl.grid()
pl.plot(XE,YE,'black')
pl.show()

""" Courbe dYE/dXE=f(XE) """

#pl.ylim(-8,8)
pl.xlim(-60,60)
pl.xlabel(r'$X_E (mm)$')
pl.ylabel(r'$\frac{dY_E}{dX_E}$')
pl.grid()
pl.plot(XE,dYE, 'black')
pl.show()


""" Courbe XE=f(theta1) """

pl.xlim(-90,180)
pl.xlabel(r'$\theta_1 (deg)$')
pl.ylabel(r'$X_E (mm)$')
#pl.xticks([-90,-45,0,45,90])
pl.grid()
pl.plot(np.rad2deg(Theta1),XE, 'black')
pl.show()

""" Courbe Cm/F=f(XE) """

pl.xlim(-40,40)
pl.ylim(32,34)
pl.xlabel(r'$X_E (mm)$')
pl.ylabel(r'$\frac{Cm}{F}$')
#pl.xticks([-90,-45,0,45,90])
pl.grid()
pl.plot(XE,CmF,'black')
pl.show()
