import numpy as np
import matplotlib.pyplot as plt

def radian(angle):
    return np.pi*angle/180
theta1=np.arange(0,60,1)
theta2=np.arange(60,240,1)
theta3=np.arange(240,330,1)
theta4=np.arange(330,360,1)
theta=np.concatenate([theta1,theta2,theta3,theta4])

r01=45
r02=57
r03=69
e=12

r1=r01*np.ones(len(radian(theta1)))
r2=np.sqrt((e*np.cos(radian(theta2-60))-r02)**2+(e*np.sin(radian(theta2-60)))**2)
r3=r03*np.ones(len(radian(theta3)))
r4=(theta4-360)**4/(30**4/24)+45
r=np.concatenate([r1,r2,r3,r4])-r01

plt.plot(theta,r)
plt.grid('on')
plt.xticks(range(0,361,30))
plt.yticks(range(0,29,4))
plt.show()
