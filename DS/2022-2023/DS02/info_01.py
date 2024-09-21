from numpy import linspace,sqrt, exp, arccos, sin
import matplotlib.pyplot as plt

def s1_ind(w0,xi,K,t):
    p1=-xi*w0-w0*sqrt(xi**2-1)
    p2=-xi*w0+w0*sqrt(xi**2-1)
    return K*(1+1/(p1-p2)*(p2*exp(p1*t)-p1*exp(p2*t)))

def s2_ind(w0,xi,K,t):
    return K*(1-exp(-w0*xi*t)/sqrt(1-xi**2)*sin(w0*sqrt(1-xi**2)*t+arccos(xi)))

def s3_ind(w0,xi,K,t):
    return K*(1-(1 + t*w0)*exp(-t*w0))


K=10**(-1)
xi=0.4
w0=150
t=linspace(0,0.4,100)

if xi==1:
    st=s3_ind(w0,xi,K,t)
elif xi<1:
    st=s2_ind(w0,xi,K,t)
else:
    st=s1_ind(w0,xi,K,t)

i=0
while st[i]<0.95*st[-1]:
    i+=1
print(t[i])

i=-1
while st[i]>0.95*st[-1] and st[i]<1.05*st[-1] :
    i-=1
print(t[i])

plt.plot(t,st)
plt.grid('on')
plt.show()
