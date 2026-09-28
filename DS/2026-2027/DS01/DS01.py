from random import random
from numpy import exp, linspace
from matplotlib.pyplot import plot, show, legend, xlabel, ylabel

V0=24
R=2
Ke=0.05
Kc=0.05
Jm=0.0005
r=0.02
M=80
b=0.02
L=5*10**(-5)

J=Jm+r**2*M
J=J/100
print(J)


K=Kc/(b*R+Kc*Ke)
w0=((b*R+Kc*Ke)/(J*L))**(1/2)
xi=(b*L+R*J)/(b*R+Kc*Ke)*w0/2
print(K,w0,xi)

tau=2*xi/w0
print(tau)

bruit=0.000

erreur=[[[1,4],'A','.'],[[1.6,2],'B','--'],[[1,1],'C','+'],[[0.7,0.2],'D',':']]

t=linspace(0,0.3,30)
for data in erreur:
    v=V0*K*data[0][0]*(1-exp(-t/(tau*data[0][1])))
    p=[0]*len(t)

    for i in range(len(t)-1):
        v[i+1]=v[i+1]*(1+bruit*(2*random()-1))
        p[i+1]=p[i]+v[i+1]*(t[i+1]-t[i])

    plot(t,v,data[2],label=data[1])
xlabel('t(s)')
ylabel(r'$\omega(t)\ rad\cdot s^{-1}$')
legend()
show()
