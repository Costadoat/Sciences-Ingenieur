import matplotlib.pyplot as plt
import numpy as np
a=4
t0=2
T=2

#Exercice 1:

t1=np.linspace(0,t0,100)
thetapp1=a*np.sin(np.pi*t1/t0)
thetap1=-a*np.cos(np.pi*t1/t0)*t0/np.pi+a*t0/np.pi
theta1=-a*np.sin(np.pi*t1/t0)*(t0/np.pi)**2+a*t0*t1/np.pi

t2=np.linspace(t0,t0+T,100)
thetapp2=0*t2
thetap2=2*a*t0/np.pi*t2/t2
theta2=2*a*t0/np.pi*t2-a*t0**2/np.pi

t3=np.linspace(t0+T,2*t0+T,100)
thetapp3=-a*np.sin((np.pi/t0)*(t3-(t0+T)))
thetap3=a*np.cos((np.pi/t0)*(t3-(t0+T)))*t0/np.pi-a*np.cos((np.pi/t0)*(-T))*t0/np.pi
theta3= a*np.sin((np.pi/t0)*(t3-(t0+T)))*(t0/np.pi)**2-a*np.cos(-(np.pi/t0)*T)*t0/np.pi*(t3-(t0+T))+2*a*t0/np.pi*(t0+T)-a*t0**2/np.pi

t=np.concatenate((t1,t2,t3))
thetapp=np.concatenate((thetapp1,thetapp2,thetapp3))
thetap=np.concatenate((thetap1,thetap2,thetap3))
theta=np.concatenate((theta1,theta2,theta3))

plt.plot(t,thetapp)
plt.plot(t,thetap)
plt.plot(t,theta)
plt.show()

