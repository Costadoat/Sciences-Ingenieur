import numpy as np
import matplotlib.pyplot as plt


Ti=12
Tf=90
h=3000
S=30
m=660*1000
Cp=4185

a=h*S/(m*Cp)
b=Tf*a
c=Ti

print(a,b,c)

t=np.arange(0,2*3600,1)
T=(Ti-Tf)*np.exp(-h*S*t/(m*Cp))+Tf

plt.plot(t,T)
plt.show()
