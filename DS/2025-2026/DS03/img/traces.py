import numpy as np
import matplotlib.pyplot as plt

a1=2
a2=-3
t1=3
t2=5

tl1=np.linspace(0,t1,100)
tl2=np.linspace(t1,t2,100)
t=np.concatenate([tl1,tl2])

ax1=a1*np.ones(len(tl1))
ax2=a2*np.ones(len(tl2))
ax=np.concatenate([ax1,ax2])

vx1=a1*tl1
vx2=-a2*t2+a2*tl2
vx=np.concatenate([vx1,vx2])


x1=1/2*a1*tl1**2
x2=1/2*a2*tl2**2-a2*t2*tl2-1/2*a2*t1**2+a2*t2*t1+1/2*a1*t1**2
x=np.concatenate([x1,x2])

plt.plot(t,x)
plt.show()
