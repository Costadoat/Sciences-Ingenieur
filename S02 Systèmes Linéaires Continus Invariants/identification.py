## Fonctions acquisition
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np
from math import ceil
from os import path

if not path.exists("data.csv"):
    print("Le fichier data.csv n'existe pas, il a été créé avec la sortie s(p)=1/(1+p), vous pouvez le modifier.")
    K=1
    tau=1
    E=1 # valeur de l'échelon de l'entrée

    H=lti([K*E],[tau,1])              #creation d'une instance de la classe
    t,y=H.step()                    #appel de la méthode step de la classe lti

    file=open('data.csv','w')
    file.write('x;y\n')
    for i in range(len(t)):
        file.write(str(t[i])+';'+str(y[i])+'\n')

    file.close()


def update(val):
    global x_in,status
    if val=='2nd ordre':
        barre_z.set_visible(True)
        barre_w0.set_visible(True)
        barre_tau.set_visible(False)
        status=2
    elif val=='1er ordre':
        barre_z.set_visible(False)
        barre_w0.set_visible(False)
        barre_tau.set_visible(True)
        status=1
    if status==1:
        K = choix_K.val
        tau = choix_tau.val
        s = s1(np.array(x_th),K,tau)
    else:
        K = choix_K.val
        w0 = choix_w0.val
        z = choix_z.val
        s = s2(np.array(x_th),K,w0,z)
    reponse.set_data(x_th, s)
    fig.axes[0].axis(ymin=0,ymax=ceil(max(s))+0.5)
    plt.yticks(np.arange(0, ceil(max(s))+0.5, (ceil(max(s))+0.5)/10))
    fig.canvas.draw()


def s1(t, K,tau):
    """ fonction qui retourne la valeur de s(t) en fonction de s(t, z)
        (fonction vectorisable car les opérateurs sont tous issus de numpy """
    
    return K*(1-np.exp(-t/tau))
    
def s2(t, K,w0,z):
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

file=open('data.csv','r')
lignes=file.read().split('\n')
x_in,y_in=[],[]
for ligne in lignes[1:-1]:
    x,y=[float(i) for i in ligne.split(';')]
    x_in.append(x)
    y_in.append(y)
x_th=[]
interv=100
for i in range(len(x_in)-1):
    x_th+=[x_in[i]+(x_in[i+1]-x_in[i])*j/interv for j in range(interv)]
file.close()

fig=plt.figure(figsize=(12,10))
plt.subplots_adjust(bottom=0.5)
plt.grid(True, color = '0.5', linestyle = '-')
plt.plot(x_in, y_in, linewidth=2,label='Expérience')
s=s1(np.array(x_th), 1,0.6)
reponse,= plt.plot(x_th, s, '-b', linewidth = 1.5,label='Identification')
plt.xlabel('Temps (s)')
plt.ylabel('Angle (°)')
plt.title('Essai')
plt.grid(True)
plt.legend()
bouton_ordre = plt.axes([0.7, 0.25, 0.2, 0.1]) # position et dimensions de la barre
choix_ordre = RadioButtons(bouton_ordre,labels=['1er ordre','2nd ordre'])
barre_K = plt.axes([0.2, 0.3, 0.4, 0.02]) # position et dimensions de la barre
choix_K = Slider(barre_K, 'Gain (K)', 0.5, 3, valinit = 1)
barre_tau = plt.axes([0.2, 0.2, 0.4, 0.02]) # position et dimensions de la barre
choix_tau = Slider(barre_tau, 'Constante de temps (s)', 10**(-3), 10, valinit = 1)
barre_w0 = plt.axes([0.2, 0.2, 0.4, 0.02]) # position et dimensions de la barre
choix_w0 = Slider(barre_w0, 'Pulsation propre (w0)', 1, 100, valinit = 20)
barre_z = plt.axes([0.2, 0.1, 0.4, 0.02]) # position et dimensions de la barre
choix_z = Slider(barre_z, 'Amortissement (z)', 0.2, 3, valinit = 0.6)
barre_w0.set_visible(False)
barre_z.set_visible(False)

status=1
choix_K.on_changed(update)
choix_w0.on_changed(update)
choix_z.on_changed(update)
choix_tau.on_changed(update)
choix_ordre.on_clicked(update)
fig.axes[0].axis(ymin=0,ymax=ceil(max(s))+0.5)
plt.yticks(np.arange(0, ceil(max(s))+0.5, (ceil(max(s))+0.5)/10))

plt.show()
