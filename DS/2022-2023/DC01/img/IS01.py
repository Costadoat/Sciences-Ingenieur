import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1,100)
plt.plot(x,np.sqrt(1-x**2),label="$\sqrt{1-x^2}$")
plt.legend()
plt.xlabel('x')
plt.grid('on')
plt.show()

theta = np.arange(0, 2 * np.pi+0.1, step=(np.pi / 4))
plt.plot(theta, np.exp(-theta),label="$e^{-x}$")
plt.xticks(theta, ['0', 'π/4', 'π/2', '3π/4', 'π', '5π/4', '3π/2', '7π/4', '2π'])
plt.legend()
plt.xlabel('x')
plt.grid('on')
plt.show()
