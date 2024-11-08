# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

K=2
xi=0.5
w0=100
E=12 # valeur de l'échelon de l'entrée

H=lti([K*E],[1/w0**2,2*xi/w0,1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti

fig, ax = plt.subplots()
maj_pos_x = MultipleLocator(0.02)   # major ticks for every 20 units
min_pos_x = MultipleLocator(0.01)    # minor ticks for every 5 units
maj_pos_y = MultipleLocator(5)   # major ticks for every 20 units
min_pos_y = MultipleLocator(1)    # minor ticks for every 5 units
ax.xaxis.set(major_locator=maj_pos_x, minor_locator=min_pos_x)
ax.yaxis.set(major_locator=maj_pos_y, minor_locator=min_pos_y)
ax.tick_params(axis='both', which='minor', length=0)   # remove minor tick lines
# different settings for major & minor gridlines
ax.grid(which='major', alpha=0.9)
ax.grid(which='minor', alpha=0.7, linestyle=':')
ax.plot(t,y)                       #affichage
ax.grid('on')
plt.xlabel('t (s)')
plt.ylabel('s(t)')
plt.show()

def f(x):
    return 100*np.exp(-x*np.pi/np.sqrt(1-x**2))

def f2(x):
    return 100*np.exp(-x*np.pi/np.sqrt(1-2*x**2))

x=np.linspace(0.01,10,1000)
fig, ax = plt.subplots()
maj_pos_x = MultipleLocator(0.2)   # major ticks for every 20 units
min_pos_x = MultipleLocator(0.1)    # minor ticks for every 5 units
maj_pos_y = MultipleLocator(20)   # major ticks for every 20 units
min_pos_y = MultipleLocator(5)    # minor ticks for every 5 units
ax.xaxis.set(major_locator=maj_pos_x, minor_locator=min_pos_x)
ax.yaxis.set(major_locator=maj_pos_y, minor_locator=min_pos_y)
ax.tick_params(axis='both', which='minor', length=0)   # remove minor tick lines
ax.grid(which='major', alpha=0.9)
ax.grid(which='minor', alpha=0.7, linestyle=':')
ax.grid(which='major', alpha=0.9)
ax.grid(which='minor', alpha=0.7, linestyle=':')
ax.plot(x,f(x))
ax.grid('on')
plt.xlabel(r'$\xi$')
plt.ylabel(r'$100\cdot e^{-\dfrac{\xi\pi}{\sqrt{1-\xi^2}}}$')
plt.show()


x=np.linspace(0.01,10,1000)
fig, ax = plt.subplots()
maj_pos_x = MultipleLocator(0.2)   # major ticks for every 20 units
min_pos_x = MultipleLocator(0.1)    # minor ticks for every 5 units
maj_pos_y = MultipleLocator(20)   # major ticks for every 20 units
min_pos_y = MultipleLocator(5)    # minor ticks for every 5 units
ax.xaxis.set(major_locator=maj_pos_x, minor_locator=min_pos_x)
ax.yaxis.set(major_locator=maj_pos_y, minor_locator=min_pos_y)
ax.tick_params(axis='both', which='minor', length=0)   # remove minor tick lines
ax.grid(which='major', alpha=0.9)
ax.grid(which='minor', alpha=0.7, linestyle=':')
ax.grid(which='major', alpha=0.9)
ax.grid(which='minor', alpha=0.7, linestyle=':')
ax.plot(x,f2(x))
ax.grid('on')
plt.xlabel(r'$\xi$')
plt.ylabel(r'$100\cdot e^{-\dfrac{\xi\pi}{\sqrt{1-2\xi^2}}}$')
plt.show()
