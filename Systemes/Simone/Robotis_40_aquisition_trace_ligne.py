## Fonctions acquisition
from initialisation import init_param
import numpy as np
import time
from datetime import datetime
import matplotlib.pyplot as plt

a=45
b=65

# Gain pid
def Reglage_gain(io,servo,PID_servo):
    servo=tuple(servo)
    PID_servo=tuple(PID_servo)
    io.set_pid_gain(dict(zip(servo,PID_servo)))
    io.set_moving_speed(dict(zip(servo,[0])))
    print('Gain pid', io.get_pid_gain(dict(zip(servo,PID_servo))))
    return io


# Essai creneau
def move(io,servo,pos):
    if len(servo)>=3:
        temps=0.02
    else:
        temps=0
    servo=tuple(servo)
    pos=tuple(pos)
    io.set_goal_position(dict(zip(servo,pos)))
    time.sleep(temps)
    return io.get_present_position(servo)

def Affichage(x_time_f,y_cons_f,y_reel_f,num_fig=0):
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Cursor
    for i in range(len(y_cons_f)):
        if num_fig==0:
            fig = plt.figure(i)
        else:
            fig = plt.figure(num_fig)
        ax = fig.add_subplot(111)
        plt.plot(x_time_f, y_cons_f[i],'r', linewidth=2,label='Consigne')
        plt.plot(x_time_f, y_reel_f[i], linewidth=2,label='Expérience')
        plt.xlabel('Temps (s)')
        plt.ylabel('Angle (°)')
        plt.title('Essai')
        plt.grid(True)
        cursor = Cursor(ax, useblit=True, color='black', linewidth=2 )
        plt.legend()
        plt.show()

def deg(rad):
    return rad*180/np.pi

def rad(deg):
    return deg*np.pi/180

def fermeture_geo(theta):
    theta=rad(theta)
    u=np.sqrt(2)/2*(a+b)/np.cos(theta-np.pi/4)
    alpha=theta-np.arccos((u**2+a**2-b**2)/(2*u*a))
    beta=theta-alpha+np.arccos((u**2-a**2+b**2)/(2*u*b))
    return alpha,beta

io,ids=init_param([2,4,6])
print(ids)
Reglage_gain(io,ids,[[4,0,0]]*len(ids))
move(io,ids,[-90]+[0]*(len(ids)-1))

kp=-1
while kp<=0 or kp>20:
    kp=int(input("kp ?"))

input('Placer le stylo ?')
move(io,[2],[-90])
input('Start ?')

lalpha=[]
lbeta=[]
lralpha=[]
lrbeta=[]
ltheta=[]
Reglage_gain(io,[4,6],[[kp,0,0]]*2)
t0=datetime.now()

for i in range(1000):
    theta=90*i/1000
    alpha,beta=fermeture_geo(theta)
    lalpha.append(alpha)
    lbeta.append(beta)
    ltheta.append(theta)
    ralpha,rbeta=move(io,[4,6],[deg(alpha),deg(beta)])
    lralpha.append(ralpha)
    lrbeta.append(rbeta)
    s=datetime.now()-t0
    lt=s.total_seconds()
    

move(io,[2],[-150])

angles=[[lalpha[i],lalpha[i]+lbeta[i]] for i in range(len(lalpha))]
x=[a*np.cos(alpha)+b*np.cos(beta) for alpha,beta in angles]
y=[a*np.sin(alpha)+b*np.sin(beta)for alpha,beta in angles]

angles=[[lralpha[i],lralpha[i]+lrbeta[i]] for i in range(len(lralpha))]
xr=[a*np.cos(rad(alpha))+b*np.cos(rad(beta)) for alpha,beta in angles]
yr=[a*np.sin(rad(alpha))+b*np.sin(rad(beta))for alpha,beta in angles]

print(lt)
plt.plot(x,y)
plt.plot(xr,yr)

plt.show()
#io.close()
