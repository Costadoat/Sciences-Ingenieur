import matplotlib.pyplot as plt
import numpy as np

# Modèle à compléter.
b=-0.3
a=0.3
x=np.linspace(0,8,100)
y=a*x+b

# Resultats expérimentaux, texp, yexp et yErrorexp doivent avoir la même taille
xexp = [0.0,2.0,4.0,6.0,8.0]
yexp=[0.0,0.0,1.1,1.9,2.2]

# Si l'incertitude est calculée à partir d'un poucentage de la valeur
yErrorexp = [0.5, 0.5, 0.8, 0.5,0.4]
# Si l'incertitude est calculée à partir d'un poucentage de la valeur
pourcent=10
yErrorexp = [pourcent*i/100 for i in yexp]

# Tracé
plt.title("Charge d'un condensateur")
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
plt.plot(x, y, 'k', zorder = 1)
plt.grid('on')
plt.scatter(xexp, yexp, zorder = 2)
plt.errorbar(xexp, yexp, yerr = yErrorexp, fmt='none', capsize = 10, ecolor = 'red', zorder = 1)
plt.show()
