import matplotlib.pyplot as plt
import numpy as np

fr=10*10**3
kf=1/16.
t=np.linspace(0,2*10**-3,10000)

def f(x):
    return np.sin(2*np.pi*fr*x)*np.sin(2*np.pi*fr*kf*x)

def g(x):
    return np.sin(2*np.pi*fr*x)*np.cos(2*np.pi*fr*kf*x)
    
plt.plot(t,f(t))

plt.show()

plt.plot(t,g(t))

plt.show()
