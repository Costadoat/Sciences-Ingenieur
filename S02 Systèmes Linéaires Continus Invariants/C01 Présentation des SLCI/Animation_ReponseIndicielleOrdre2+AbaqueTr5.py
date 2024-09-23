# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Animation de la réponse indicielle d'un système d'ordre 2 en fonction de 
# l'amortissement (pour un système normé, K = 1, omega0 = 1)
# et correspondance avec l'abaque du temps de réponse adimensionnel
# Jean-Philippe COSTES - Lycée LESAGE - Vannes - Septembre 2014
#-------------------------------------------------------------------------------
import pylab as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.patches import Polygon

#-------------------------------------------------------------------------------
# Réponse indicielle normée adimensionnelle d'un ordre 2: s(t,z)
#-------------------------------------------------------------------------------
def s(t, z):
    """ fonction qui retourne la valeur de s(t) en fonction de s(t, z)
        (fonction vectorisable car les opérateurs sont tous issus de numpy """
    
    b = z**2-1
    
    if z > 1:
        a = np.sqrt(b)
        return 1+np.exp(-t*(z+a))/2/(z*a+b)-np.exp(-t*(z-a))/2/(z*a-b)
    
    elif z < 1:
        a = np.sqrt(-b)
        return 1-np.exp(-z*t)/a*np.sin(t*a+np.arcsin(a))

    else:                           # cas où z == 1
        return 1-(1+t)*np.exp(-t)
    
#-------------------------------------------------------------------------------
# définition d'un intervalle de temps réduit T = t * wo
#-------------------------------------------------------------------------------
tmin  = 0    # borne minimale (incluse)
tmax  = 15.  # borne maximale (incluse)
delta = 0.01 # choix d'un incrément pour les valeurs discrètes de T

T = np.arange(tmin, tmax+delta, delta)

#-------------------------------------------------------------------------------
# Construction d'une bande rectangulaire pour faire apparaitre les +/- 5%
#-------------------------------------------------------------------------------
eps = 0.05
rectangle = [(0,1-eps), (0,1+eps), (tmax,1+eps), (tmax,1-eps)]
bande5    = Polygon(rectangle, facecolor='0.8', edgecolor='0.5')

#-------------------------------------------------------------------------------
# définition d'une fonction qui permet de savoir si une valeur (v)
# est dans l'intervalle [1-epsilon, 1+epsilon]
# en pratique epsilon = 0.05 pour l'abaque du temps de réponse à +/-5%
#-------------------------------------------------------------------------------
def est_dans_bande(v, eps = 0.05):
    """ fonction qui renvoie True(~1) si v est dans l'intervalle [1 +/-eps] """
    return abs(v-1) <= eps

#-------------------------------------------------------------------------------
# fonction pour la recherche du temps de réponse à 5%
#-------------------------------------------------------------------------------
def recherche_tr5(z, tm = 20, delta = 0.01):
    tr5 = tm
    while est_dans_bande(s(tr5, z), eps):
        tr5 -= delta

    return tr5

#-------------------------------------------------------------------------------
# Tracé de l'abaque en échelle linéaire
# stratégie: on balaye les z par valeur croissante
# pour chaque z, on teste la sortie de bande en partant d'une valeur de Tr
# suffisamment grande (Trmax pour commencer) mais pour la suite,
# on ne repart pas de Trmax (gain de temps),
# mais de Tr5[i-1] auquel on rajoute 1% (arbitrairement),
# car Tr5% n'est pas strictement décroissant sur z = [0, 0.69],
# et pour z = [0.69 , +infini], les variations de Tr5% sont faibles
#-------------------------------------------------------------------------------
# définition d'une discrétisation en z et en Tr(temps de réponse)
#-------------------------------------------------------------------------------
zmin  = 0.1    # borne minimale pour l'amortissement (incluse)
zmax  = 2      # borne maximale (incluse)
pas_z = 0.001  # choix d'un incrément pour les valeurs de z

Z     = np.arange( zmin , zmax+pas_z , pas_z)
Tr5   = []    # initialisation de la liste des valeurs de tr5

#-------------------------------------------------------------------------------
# recherche du temps de réponse à 5%
#-------------------------------------------------------------------------------
t = tmax

for z in Z:
    Tr5.append(recherche_tr5(z, tm = t, delta = delta))
    t = Tr5[-1]*1.05 # on repart de Tr5 précédent auquel on ajoute 5%


#-------------------------------------------------------------------------------
# Tracé de la réponse paramétrable (en z) et de l'abaque 
#-------------------------------------------------------------------------------
T = np.arange(tmin, tmax+delta, delta)

fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (16, 8))
plt.subplots_adjust(left = 0.10, bottom = 0.2, wspace = 0.15)

fs = 14 # fontsize pour les textes (titres, labels, etc)

# dans le 1er dessin (gauche)
plt.subplot(121)
plt.xticks(np.linspace(0, int(tmax), int(tmax)+1))
plt.yticks(np.arange(0, 2.25, 0.25))
plt.grid(True, color = '0.5', linestyle = '-')
plt.title(r'$Réponse\ indicielle\ (système\ du\ 2^{ième}\ ordre\ normé:\ \omega_0=1)$', fontsize = fs)
plt.ylabel('$Réponse$', fontsize = fs)
plt.text(tmax-1, -0.15, '$t(s)$', fontsize = fs)


z0 = 1
plt.axis([0,tmax,0,2])

tr5_0 = recherche_tr5(z0)   # temps de réponse pour z = z0
s0    = s(tr5_0,z0)         # valeur de s(t, z) pour t = tr5_0 et z = z0

plt.plot(T, s(T,1), '--k', lw = 1.)       # réponse critique (z = 1)
plt.plot([0,tmax], [1,1], '-k', lw = 1.)  # asymptote y = 1
plt.plot(tr5_0, s0, 'ow')                # marker pour tr5 pour z = 1
plt.plot([tr5_0, tr5_0], [0, s0], '--k')   # ligne de rappel de tr5% pour z = 1

plt.fill([tmin, tmax, tmax, tmin, tmin], [1-eps, 1-eps, 1+eps, 1+eps, 1-eps],\
         '-g', alpha = 0.3)

Xline5 = [tr5_0, tr5_0]
Yline5 = [0, s(tr5_0, z0)]
Xtext5, Ytext5 = tr5_0, 0

reponse, = plt.plot(T, s(T, z0), '-b', linewidth = 1.5)
mark_t5, = plt.plot(tr5_0, s0, 'or')
line_t5, = plt.plot(Xline5, Yline5, '-r')


# dans le second dessin (droite)
plt.subplot(122)
plt.axis([0, zmax, 0, tmax])
plt.xticks(np.arange(0, zmax+0.2, 0.2))
plt.yticks(np.arange(0, tmax+1, 1))
plt.grid(True, color = '0.5', linestyle = '-')
plt.title(r'$Abaque\ du\ temps\ de\ réponse\ à\ 5\% \ (normé).$', fontsize = fs)
plt.ylabel('$T_{R5\%}\ \cdot\ \omega_0$', fontsize = fs)
plt.text(zmax*.75, -1.2, '$Amortissement\ z$', fontsize = fs)

plt.plot(Z, Tr5, '-', color = 'grey')   # courbe continue (trame)

# puis tracé de la courbe de l'abaque comme étant une courbe discontinue !
# on commence par identifier les indices qui correspondent à une discontinuité
# on en crée une liste I (qui comporte comme premier indice 0),
# la recherche consiste à chercher les indices i tels que:
# Tr5[i] et Tr5[i+1] sont distants de plus de 1
I = [0]
for i in range(len(Tr5)-1):
    if Tr5[i] - Tr5[i+1] > 1: I.append(i)
I.append(len(Tr5)-1)

for k in range(len(I)-1):
    plt.plot(Z[I[k]+1: I[k+1]+1], Tr5[I[k]+1: I[k+1]+1], '-k', lw = 2.) # abaque réel (discontinu)
    
#plt.plot(Z, Tr5, '.b', markersize = 1.) # abaque réel (discontinu)
plt.plot(z0,tr5_0,'ow')                 # marqueur pour z = 1
plt.plot([z0, z0],[0, tr5_0], '--k')    # ligne de rappel de tr5% pour z = 1

mark_zt, = plt.plot(z0, tr5_0, 'or')

zmax = 2 # redéfinition de zmax

barre_z = plt.axes([0.2, 0.1, 0.4, 0.02]) # position et dimensions de la barre
choix_z = Slider(barre_z, 'Amortissement (z)', 0, zmax, valinit = z0)

def update(val):
    global T
    z = choix_z.val
        
    reponse.set_data(T, s(T,z))
    tr5 = recherche_tr5(z)
    mark_t5.set_data(tr5, s(tr5,z))

    mark_zt.set_data(z, tr5)

    Xline5 = [tr5, tr5]
    Yline5 = [0, s(tr5, z)]
    line_t5.set_data(Xline5, Yline5)

choix_z.on_changed(update)

plt.show()
