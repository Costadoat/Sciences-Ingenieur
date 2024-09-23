# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 08:20:54 2017

@author: costa
"""
from matplotlib import rcParams
import numpy as np
import matplotlib.pyplot as plt


print 60*11*5*44*0.95


#set plot attributes
fig_width = 21  # width in inches
fig_height = 12.6  # height in inches
fig_size =  [fig_width,fig_height]
params = {'font.sans-serif' : 'Arial',
          'text.latex.preamble': [r"\usepackage{sfmath}", 
                                     r"\usepackage{amsmath}", 
                                     r"\usepackage{amstext}", 
                                     r"\renewcommand\familydefault{\sfdefault}"],
          'axes.labelsize': 14,
          'axes.titlesize': 14,
          'font.size': 20,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'figure.figsize': fig_size,
          'savefig.dpi' : 600,
          'axes.linewidth' : 1.3,
          'ytick.major.size' : 6,      # major tick size in points
          'xtick.major.size' : 6      # major tick size in points
          #'xtick.major.size' : 2,
          #'ytick.major.size' : 2,
          }
rcParams.update(params)

J=5.42*10**(-2)
pas=7*10**(-3)
k=1/6.
n=0.5
Cp=n*1500*10*pas*k/(2*np.pi)
Kc=1.6
Ke=1.6
R=5.22

dt=0.0001
tm0=0
t01=5
t02=47
t03=51
td0=tm0+t03+10
t11=3
t12=40
t13=45

omegam=104.
            
dm=(0.5*(t01)+(t02-t01)+0.5*(t03-t02))*omegam
print dm*k*pas/(2*np.pi)
omegad=-dm/(0.5*(t11)+(t12-t11)+0.5*(t13-t12))
print omegad
omegad=-120

C01=J*(omegam)/(t01)+Cp
print C01
C02=Cp
C03=-J*(omegam)/(t03-t02)+Cp
C11=J*(omegad)/(t11)+Cp

C12=Cp
C13=-J*(omegad)/(t13-t12)+Cp


t1=np.arange(tm0,tm0+t01,dt)
Cm1=C01*np.ones(len(t1))
t2=np.arange(tm0+t01,tm0+t02,dt)
Cm2=C02*np.ones(len(t2))
t3=np.arange(tm0+t02,tm0+t03,dt)
Cm3=C03*np.ones(len(t3))

tm=np.concatenate((t1,t2))
tm=np.concatenate((tm,t3))
Cm=np.concatenate((Cm1,Cm2))
Cm=np.concatenate((Cm,Cm3))

t1=np.arange(td0,td0+t11,dt)
Cd1=C11*np.ones(len(t1))
t2=np.arange(td0+t11,td0+t12,dt)
Cd2=C12*np.ones(len(t2))
t3=np.arange(td0+t12,td0+t13,dt)
Cd3=C13*np.ones(len(t3))

td=np.concatenate((t1,t2))
td=np.concatenate((td,t3))
Cd=np.concatenate((Cd1,Cd2))
Cd=np.concatenate((Cd,Cd3))

ts=np.arange(t03,td0,dt)
Cs=C02*np.ones(len(ts))

t=np.concatenate((tm,ts))
t=np.concatenate((t,td))
C=np.concatenate((Cm,Cs))
C=np.concatenate((C,Cd))

domega=(C-Cp)/J

omega=np.zeros(len(t))

for i in range(1,len(t)):
    omega[i]=omega[i-1]+domega[i]*dt

plt.figure('Sujet')
plt.plot(t,omega)
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'$\omega_m$(t) (rad.s$^{-1}$)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(-120,120,16,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/profil.pdf')
plt.show()

theta=np.zeros(len(t))

for i in range(1,len(t)):
    theta[i]=theta[i-1]+omega[i]*dt

plt.figure('Acceleration')
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'$\dot{\omega}_m$(t) (rad.s$^{-2}$)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(-50,50,11,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/accel.pdf')
plt.show()

plt.figure('Acceleration (correction)')
plt.plot(t,domega)
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'$\dot{\omega}_m$(t) (rad.s$^{-2}$)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(-50,50,11,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/accel_cor.pdf')
plt.show()

plt.figure('Coupe')
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'$C_m$(t) (N.m)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(0,5,6,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/couple.pdf')
plt.show()

plt.figure('Correction (couple)')
plt.plot(t,C)
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'$C_m$(t) (N.m)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(0,5,6,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/couple_cor.pdf')
plt.show()

plt.figure('Deplacement')
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'$d_m$(t) (m)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(-0.2,1,7,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/deplacement.pdf')
plt.show()

plt.figure('Deplacement (correction)')
plt.plot(t,theta*k*pas/(2*np.pi))
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'$d_m$(t) (m)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(-0.2,1,7,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/deplacement_cor.pdf')
plt.show()

plt.figure('Tension')
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'u(t) (V)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(-200,200,21,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/tension.pdf')
plt.show()

plt.figure('Tension (correction)')
plt.plot(t,(R/Kc)*C+Ke*omega)
plt.xlabel(r't (s)', fontsize=30)
plt.ylabel(r'u(t) (V)', fontsize=30)
plt.grid(True)
plt.xticks(np.linspace(0,108,28,endpoint=True), fontsize=20)
plt.yticks(np.linspace(-200,200,21,endpoint=True), fontsize=20)
plt.tight_layout()
plt.savefig('img/tension_cor.pdf')
plt.show()