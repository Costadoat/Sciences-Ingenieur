import numpy as np
import matplotlib.pyplot as plt

Ke=52.5*10**(-3)
Kt=Ke
R=2.07
L=0.62*10**(-3)
f=0.125
J=0.01

w0=np.sqrt((Ke*Kt+R*f)/(L*J))
xi=(L*f+R*J)/(2*np.sqrt(L*J*(Ke*Kt+R*f)))
K=Kt/(Ke*Kt+R*f)

print("K",K,"w0",w0,"xi",xi)

J=5*10**-4

w0=np.sqrt((Ke*Kt+R*f)/(L*J))
xi=(L*f+R*J)/(2*np.sqrt(L*J*(Ke*Kt+R*f)))
K=Kt/(Ke*Kt+R*f)

print(L*f,R*J)
print("K",K,"w0",w0,"xi",xi)

