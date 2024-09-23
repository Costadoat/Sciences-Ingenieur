## Fonctions acquisition
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from pypot.dynamixel import Dxl320IO, get_available_ports
#from matplotlib.widgets import Cursor

def init_param(ids_in):
    ## Connexion
    # Scan des ports series
    ports = get_available_ports()
    
    # Affichage des ports trouvés
    if not len(ports):
        print('Aucun port detecté!')
        sys.exit(1)
    
    print('ports trouvés!', ports)
    
    # Choix du port
#num_port = int(input('taper le numero du port dans la liste? (0,1,...)'))
    num_port=0
    ## Scan des servomoteurs
    io = Dxl320IO(ports[num_port])
    ids=[]
    for i in range(3):
        ids+=io.scan(ids_in[(i*len(ids_in))//3:((i+1)*len(ids_in))//3])
        time.sleep(0.5)
    print('motors found', ids)
    return io,ids

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
    temps=0.1
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

io,ids=init_param([9,11,13,10,12,14])
Reglage_gain(io,ids,[[10,0,0]]*len(ids))
time.sleep(1)


pos0=np.array([float(i) for i in io.get_present_position(tuple(ids))])
steps=10
for i in range(steps):
    pos=pos0*(steps-i)/steps
    move(io,ids,pos)
    time.sleep(.04)

time.sleep(2)

angles=np.linspace(0,40,10)
for angle in angles:
    move(io,ids,[-angle,2*angle,angle,+angle,-2*angle,-angle])
#io.close()
