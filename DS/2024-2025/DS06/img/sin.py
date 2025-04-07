import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 3))
x=np.linspace(0,90,1000)
plt.plot(x,np.sin(x*np.pi/180))
plt.xlabel(r'$\theta (\degree)$')
ax.set_xticks(np.linspace(0, 90, 10))
ax.set_yticks(np.linspace(0, 1, 11))
plt.ylabel(r'$\sin (\theta)$')
plt.grid('on')
plt.show()
