import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

R=0.6
J=0.012
L=1.5*10**-3
Kt=0.06
Ke=Kt
alpha=9.

b=R*J/(Ke*Kt)

a=L*J/(Ke*Kt)

delta=b**2-4*a
print("delta",delta)

w0=np.sqrt(1/a)
xi=1/2.*b*np.sqrt(1/a)
K=1/Ke

print("K",K,"xi",xi,"w0",w0)

p1=(-b-np.sqrt(delta))/(2*a)
p2=(-b+np.sqrt(delta))/(2*a)

tau1=-1/p1
tau2=-1/p2

print("tau1",tau1,"tau2",tau2)

print(np.exp(-1))
    
t=np.linspace(0,2,1000)
s=alpha/Ke*(t-2*(1-np.exp(-t/2.)))

fig=plt.figure('Démarrage')
plt.plot(t,s)
plt.savefig("img/demarrage.png")

t=2
s=alpha/Ke*(t-2*(1-np.exp(-t/2.)))
print(s)

t1=np.arange(0,2,0.001)
t2=np.arange(2.01,20,0.001)
u1=alpha*t1
u2=u1[-1]*np.ones(len(t2))

t=np.concatenate((t1,t2))
u=np.concatenate((u1,u2))


fig2=plt.figure('Tension' )
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

offset = 60

#host.set_xlim(0, 2)
host.set_ylim(0, 20)

host.set_xlabel("Temps")
host.set_ylabel("$U_m(V)$")

p1, = host.plot([0,2,2],[18,18,0],'--',c='#1f77b4')
p1, = host.plot(t,u,c='#1f77b4',label="$U_m(V)$")
plt.yticks(np.arange(0, 20, 2))
plt.xticks(np.arange(0, 20, 2))
host.legend()

host.axis["left"].label.set_color(p1.get_color())

plt.draw()
plt.savefig("img/tension.png")
plt.plot()
wi=[]
for n in range(1,3):
    w=np.zeros(len(t))
    ww=np.zeros(len(t))
    www=np.zeros(len(t))
    for i,tt in enumerate(t[:-2]):
        www[i]=Kt/(J*L)*(u[i]/(0.1*n+0.9)-(R*J/Kt)*ww[i]-Ke*w[i])
        ww[i+1]=www[i]*(t[i+1]-t[i])+ww[i]
        w[i+1]=ww[i]*(t[i+1]-t[i])+w[i]
    i+=1
    w[i+1]=ww[i]*(t[i+1]-t[i])+w[i]
    wi.append(w)
for i in range(2):
    fig3=plt.figure('Sortie '+str(i+1))
    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()

    offset = 60
    new_fixed_axis = par1.get_grid_helper().new_fixed_axis
    par1.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par1)

    par1.axis["right"].toggle(all=True)

    #host.set_xlim(0, 2)
    host.set_ylim(0, 20)

    host.set_xlabel("Temps")
    host.set_ylabel("$U_m(V)$")
    par1.set_ylabel("$\omega_m(rad.s^{-1})$")

    p1, = host.plot(t,u, '--',label="$U_m(V)$")
    #p1, = host.plot([7.064,7.064],[0,20], '--',label="$U_m(V)$")
    p2, = par1.plot(t,wi[i]
                    , label="$\omega_m(rad.s^{-1})$")
    #p2, = par1.plot(t,wi[i][-1]*0.95*np.ones(len(t))
    #                , label="$\omega_m(rad.s^{-1})$")
    
    par1.set_ylim(0, 400)

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())

    plt.draw()  
    plt.savefig("img/rep"+str(i)+".png")
    #print(i,wi[i][-1])
    plt.show()
plt.show()

i=-1
while wi[1][i]<1.05*wi[1][-1] and wi[1][i]>0.95*wi[1][-1]:
    i+=-1

t5=t[i]
print("Le temps de réponse est %s secondes" % format(t5))
