# On importe les bibliothèques
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,90,100)
fig=plt.figure()
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.xticks(np.arange(0, 91, step=5))
plt.yticks(np.arange(0, np.pi/2+0.1, step=0.1))
plt.plot(t,np.sin(t*np.pi/180))

plt.grid('on')
#plt.show()

plt.savefig("fig07.pgf")
