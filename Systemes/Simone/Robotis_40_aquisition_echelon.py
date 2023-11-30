## Fonctions acquisition
from initialisation import init_param
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#from matplotlib.widgets import Cursor

# Gain pid
def Reglage_gain(io,servo,PID_servo):
    servo=tuple(servo)
    PID_servo=tuple(PID_servo)
    io.set_pid_gain(dict(zip(servo,PID_servo)))
    return io

def update(val):
    global x_time_f
    K = choix_K.val
    w0 = choix_w0.val
    z = choix_z.val
        
    reponse.set_data(x_time_f, 90*s(np.array(x_time_f),K,w0,z))

def s(t, K,w0,z):
    """ fonction qui retourne la valeur de s(t) en fonction de s(t, z)
        (fonction vectorisable car les opérateurs sont tous issus de numpy """
    
    b = z**2-1
    
    if z > 1:
        a = np.sqrt(b)
        return K*(1+np.exp(-t*w0*(z+a))/2/(z*a+b)-np.exp(-t*w0*(z-a))/2/(z*a-b))
    
    elif z < 1:
        a = np.sqrt(-b)
        return K*(1-np.exp(-z*t*w0)/a*np.sin(t*w0*a+np.arcsin(a)))

    else:                           # cas où z == 1
        return K*(1-(1+t)*np.exp(-t*w0))


# Mise en mouvement du bras
def move(io,servo,pos):
    temps=0.03
    servo=tuple(servo)
    pos=tuple(pos)
    io.set_goal_position(dict(zip(servo,pos)))
    time.sleep(temps)
    return io.get_present_position(servo)

# Essai creneau
def Essai_creneau(io,servo,pos_init,amplitude,t_debut,t_fin,duree):
    temps=0.02
    AMP = amplitude
    servo=tuple(servo)
    pos_init=tuple(pos_init)
    io.set_goal_position(dict(zip(servo,pos_init)))
    time.sleep(2)
    
    pos_init_vrai = io.get_present_position(servo)

    
    T1 = t_debut
    T2 = t_fin
    
    def f(t,pos_ini,AMP,T1,T2):
        if T1 <= t < T2:
            return pos_ini+AMP
        else:
            return pos_ini
    
    
    
    x_time_f = []
    y_cons_f = []
    y_reel_f = []
    load_f = []
    
    
    
    
    t0 = time.time()
    while True:
        poss=[]
        t = time.time()
        if (t - t0) > duree:
            break
        for i in range(len(servo)):
            poss.append(f(t-t0,pos_init[i],AMP[i],T1,T2))
            
        io.set_goal_position(dict(zip(servo, poss)))
        x_time_f.append(t-t0)
        y_cons_f.append(poss)
        time.sleep(temps)
        y_reel_f.append(io.get_present_position(servo))
        
    
    consigne=[]
    position_reelle=[]
    for i in range(len(servo)):
        liste_c=[]
        liste_p=[]
        for j in range(len(x_time_f)):
            liste_c.append(y_cons_f[j][i])
            liste_p.append(y_reel_f[j][i])
        consigne.append(liste_c)
        position_reelle.append(liste_p)
            
    return x_time_f,consigne,position_reelle

io,ids=init_param([4,6])
Reglage_gain(io,ids,[[5,0,0]]*2)

axe=0
while axe!=1 and axe!=2:
    axe=int(input("Epaule-1, Coude-2 ?"))

kp=-1
while kp<=0 or kp>20:
    kp=int(input("kp ?"))

Reglage_gain(io,ids,[[kp,0,0]]*2)
move(io,ids,[0,0])
time.sleep(1)
x_time_f,y_cons_f,y_reel_f=Essai_creneau(io,[2*axe+2],[0],[90],0,0.5,0.5)

plt.subplots_adjust(bottom=0.4)
plt.xticks(np.linspace(0, int(max(x_time_f)), int(max(x_time_f))+1))
plt.yticks(np.arange(0, int(max(y_cons_f[0])), int(max(y_cons_f[0])/10)))
plt.grid(True, color = '0.5', linestyle = '-')
plt.plot(x_time_f, y_cons_f[0],'r', linewidth=2,label='Consigne')
plt.plot(x_time_f, y_reel_f[0], linewidth=2,label='Expérience')
reponse, = plt.plot(x_time_f, 90*s(np.array(x_time_f), 1,20,0.6), '-b', linewidth = 1.5)
plt.xlabel('Temps (s)')
plt.ylabel('Angle (°)')
plt.title('Essai')
plt.grid(True)
plt.legend()
barre_K = plt.axes([0.2, 0.3, 0.4, 0.02]) # position et dimensions de la barre
choix_K = Slider(barre_K, 'Gain (K)', 0.5, 3, valinit = 1)
barre_w0 = plt.axes([0.2, 0.2, 0.4, 0.02]) # position et dimensions de la barre
choix_w0 = Slider(barre_w0, 'Pulsation propre (w0)', 1, 100, valinit = 20)
barre_z = plt.axes([0.2, 0.1, 0.4, 0.02]) # position et dimensions de la barre
choix_z = Slider(barre_z, 'Amortissement (z)', 0.2, 3, valinit = 0.6)

choix_K.on_changed(update)
choix_w0.on_changed(update)
choix_z.on_changed(update)

plt.show()
#io.close()
