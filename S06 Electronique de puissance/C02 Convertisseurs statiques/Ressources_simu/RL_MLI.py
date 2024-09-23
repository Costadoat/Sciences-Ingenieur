import numpy as np
import matplotlib.pyplot as plt

fh=10**6
Vin=0.5
R=30
L=1*10**(-3)
ttot=0.5*10**(-1)
w=200*np.pi
dt=10**(-8)
nt=ttot/dt
t=np.linspace(0,ttot,nt)
triangle=[-1.]
p=4*fh
pr=p
for i in range (1,len(t)):
    tri=triangle[i-1]+pr*dt
    if tri>1:
        pr=-p
    elif tri<-1:
        pr=p
    triangle.append(tri)
modulant=np.sin(w*t)
module=[]
for i in range(len(t)):
    if triangle[i]>modulant[i]:
        module.append(0)
    else:
        module.append(Vin)
        
plt.figure(1)
plt.plot(t,module,t,triangle,t,modulant)
    
def F(y,t,i):
    return (module[i]-R*y)/L

def euler(F,y0,t):
    y=[0]*len(t)
    y[0]=y0
    for i in range(len(t)-1):
        y[i+1]=y[i]+(t[i+1]-t[i])*F(y[i],t[i],i)
    return y

courant=euler(F,0,t)

plt.figure(2)
plt.plot(t,courant)