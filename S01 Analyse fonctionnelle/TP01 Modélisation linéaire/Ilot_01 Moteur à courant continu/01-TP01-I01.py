import matplotlib.pyplot as plt
import numpy as np

def regression_lineaire_eq_normale(x,y):
    X_b = np.c_[np.ones((len(x), 1)), x]
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    return theta_best

def regression_lineaire_descente_gradient(x,y):
    X_b = np.c_[np.ones((len(x), 1)), x]
    eta = 0.1 # taux d’apprentissage
    n_iterations = 1000
    m = 100
    theta = np.random.randn(2,1)
    # initialisation aléatoire
    for iteration in range(n_iterations):
        gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
        theta = theta - eta * gradients
    return theta

# Modèle à compléter.
b=-1
a=0.3
x=np.linspace(0,8,100)
y=a*x+b

# Resultats expérimentaux, texp, yexp et yErrorexp doivent avoir la même taille
xexp = [0.0,2.0,4.0,6.0,8.0]
yexp = [0.0,0.0,1.1,1.9,2.2]
xexprl=np.array(xexp).reshape(len(xexp),1)
yexprl=np.array(yexp).reshape(len(yexp),1)
brl,arl=regression_lineaire_eq_normale(xexprl,yexprl)
print(brl,arl)
brl2,arl2=regression_lineaire_descente_gradient(xexprl,yexprl)
print(brl2,arl2)

# Si l'incertitude est calculée à partir d'un poucentage de la valeur
yErrorexp = [0.5, 0.5, 0.8, 0.5,0.4]
# Si l'incertitude est calculée à partir d'un poucentage de la valeur
pourcent=10
yErrorexp = [pourcent*i/100 for i in yexp]

# Tracé
plt.title("Modélisation moteur")
plt.xlabel('Tension (V)')
plt.ylabel('Vitesse (rad/s)')
plt.plot(x, y, 'r', zorder = 1)
plt.plot(x, brl+arl*x, 'k', zorder = 1)
plt.grid('on')
plt.scatter(xexp, yexp, zorder = 2)
plt.errorbar(xexp, yexp, yerr = yErrorexp, fmt='none', capsize = 10, ecolor = 'red', zorder = 1)
plt.show()
