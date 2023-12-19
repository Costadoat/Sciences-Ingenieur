import numpy as np
import matplotlib.pyplot as plt

a=45
b=65

theta=np.linspace(0,np.pi/2,100)
u=np.sqrt(2)/2*(a+b)/np.cos(theta-np.pi/4)
alpha=theta-np.arccos((u**2+a**2-b**2)/(2*u*a))
beta=theta-alpha+np.arccos((u**2-a**2+b**2)/(2*u*b))

x=a*np.cos(alpha)+b*np.cos(alpha+beta)
y=a*np.sin(alpha)+b*np.sin(alpha+beta)

plt.plot(x,y)
plt.show()
