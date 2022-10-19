import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti    #pour l'utilisation de la classe lti

x=np.linspace(0,1,100)
plt.plot(x,np.sqrt(1-x**2),label="$\sqrt{1-x^2}$")
plt.legend()
plt.xlabel('x')
plt.grid('on')
plt.savefig('img/Figure_1.png')
plt.close()

theta = np.arange(0, 2 * np.pi+0.1, step=(np.pi / 4))
plt.plot(theta, np.exp(-theta),label="$e^{-x}$")
plt.xticks(theta, ['0', 'π/4', 'π/2', '3π/4', 'π', '5π/4', '3π/2', '7π/4', '2π'])
plt.legend()
plt.xlabel('x')
plt.grid('on')
plt.savefig('img/Figure_2.png')
plt.close()

K=17.82
xi=0.6
w0=100
E=1 # valeur de l'échelon de l'entrée

H=lti([K*E],[1/w0**2,2*xi/w0,1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti

plt.plot(t,y)                       #affichage
plt.grid('on')
plt.savefig('img/Figure_cor.png')
plt.show()
