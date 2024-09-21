import math as m

R=5
L=0.0053
Ke=0.65
Ki=0.65
mu=0.001
J=8*10**-3

z=(R*J+L*mu)/(2*m.sqrt((Ke*Ki+R*mu)*L*J))
wn=m.sqrt((Ke*Ki+R*mu)/(L*J))
G=Ki/(Ke*Ki+R*mu)

print(G,wn,z)
