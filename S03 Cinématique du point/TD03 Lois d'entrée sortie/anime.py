from numpy import pi,sin,cos,sqrt,cross,array,arccos
import matplotlib.pyplot as plt
import matplotlib.animation as animation

wm = pi
dt = 0.01
a=0.02
b=0.05
thetam=0

fig = plt.figure() # initialise la figure
AB, = plt.plot([], []) 
BC, = plt.plot([], []) 
VB, = plt.plot([], []) 
VC, = plt.plot([], []) 
plt.xlim(-0.05, 0.05)
plt.ylim(-0.05, 0.1)
plt.axis('scaled')

def init():
    AB.set_data([], [])
    BC.set_data([], [])
    VB.set_data([], [])
    VC.set_data([], [])
    return AB,BC,VB,VC

def animate(i):
    global thetam
    t = i * dt
    thetam += wm * dt
    theta6=arccos(-a*cos(thetam)/b)
    v=-a*wm*sin(thetam-theta6)/sin(theta6)
    v=v/2
    xA,yA=0,0
    xB,yB=a*cos(thetam),a*sin(thetam)
    delta=(2*a*sin(thetam))**2-4*(a**2-b**2)
    y=a*sin(thetam)+(sqrt(delta)/2)
    xC,yC=0,y
    AB.set_data([xA,xB], [yA,yB])
    BC.set_data([xB,xC], [yB,yC])
    vb=cross(array([xA-xB,yA-yB,0]),array([0,0,wm/2]))+array([xB,yB,0])
    VB.set_data([xB,vb[0]], [yB,vb[1]])
    VC.set_data([xC,0], [yC,yC+v])
    return AB,BC,VB,VC
 
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=20, 
                              interval=1, blit=True, repeat=False)


plt.show()
