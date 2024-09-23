import numpy as np
import matplotlib.pyplot as plt

w=400
E=10
K=10**(0/20)
phi=-135*2*np.pi/360

t=np.linspace(0,0.1,1000)
e=E*np.sin(w*t)
s=E*K*np.sin(w*t+phi)

plt.plot(t,e)
plt.plot(t,s)
plt.grid('on')
#plt.show()

plt.savefig("q6_cor.pgf")
