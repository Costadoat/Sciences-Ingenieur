# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *
from matplotlib.widgets import TextBox

K=1
w0=100
xi=1
xi_init=[0.001, 10]
w0_init=[1, 1000]
K_init=[1, 10]

def H(w,w0,xi,K):
    return K/(1+2*xi*1j*w/w0-w**2/w0**2)

def plage_w(w0,xi):
    if xi>1:
        w1=w0*(xi+(xi**2-1)**(1/2))
        w2=w0*(xi-(xi**2-1)**(1/2))
        return log10(w2)-3,log10(w1)+3
    else:
        return log10(w0)-3,log10(w0)+3

def plage_mod(module):
    global axes_mod
    delta=(max(module)-min(module))/10
    axes_mod.set_ylim(((min(module)-delta)//10)*10, ((max(module)+delta)//10+1)*10)
    major_ticks_y = np.arange(((min(module)-delta)//10-1)*10, ((max(module)+delta)//10+1)*10+1, (((max(module)-min(module))/5)//5)*5)
    minor_ticks_y = np.arange(((min(module)-delta)//10-1)*10, ((max(module)+delta)//10+1)*10+1, (((max(module)-min(module))/20)//5)*5)
    axes_mod.set_yticks(major_ticks_y)
    axes_mod.set_yticks(minor_ticks_y, minor=True)
    axes_mod.grid(True,which='minor', alpha=0.2)
    axes_mod.grid(True,which='major', alpha=0.5)


fig=figure('Diagrammes Bode')
bornes_w=plage_w(w0,xi)
puissances_w=arange(bornes_w[0],bornes_w[1],0.01)
W=10**puissances_w
# La phase en degré
phase = angle(H(W,w0,xi,K),'deg')
# Le module en dB
module = 20*log10(absolute(H(W,w0,xi,K)))
#Tracer du diagramme de Bode
subplot(311) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod,val=semilogx(W,module,10,1) # Tracé en semilog du module
axes_mod = gca()
axes_mod.set_ylabel('Gain (dB)')
axes_mod.set_xscale('log')
plage_mod(module)
subplot(312)
diag_pha,val=semilogx(W,phase,10,1) #Tracé en semilog du module
axes_pha = gca()
axes_pha.set_ylim((min(phase)//30)*30-30, (max(phase)//30*30)+30)
axes_pha.set_ylabel('Phase (deg)')
axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
major_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 30)
minor_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 15)
axes_pha.set_yticks(major_ticks_y)
axes_pha.set_yticks(minor_ticks_y, minor=True)
axes_pha.grid(True,which='minor', alpha=0.2)
axes_pha.grid(True,which='major', alpha=0.5)
barre_xi = plt.axes([0.2, 0.11, 0.3, 0.02]) # position et dimensions de la barre
choix_xi = Slider(barre_xi, 'Amortissement (z)', xi_init[0], xi_init[1], valinit = xi)
axbox_xi = fig.add_axes([0.8, 0.11, 0.1, 0.05])
text_xi = TextBox(axbox_xi, "Evaluate", textalignment="center")
barre_w0 = plt.axes([0.2, 0.2, 0.3, 0.02]) # position et dimensions de la barre
choix_w0 = Slider(barre_w0, 'Pulsation propre (w0)', w0_init[0], w0_init[1], valinit = w0)
axbox_w0 = fig.add_axes([0.8, 0.2, 0.1, 0.05])
text_w0 = TextBox(axbox_w0, "Evaluate", textalignment="center")
barre_K = plt.axes([0.2, 0.02, 0.3, 0.02]) # position et dimensions de la barre
choix_K = Slider(barre_K, 'Gain (K)', K_init[0], K_init[1], valinit = K)
axbox_K = fig.add_axes([0.8, 0.02, 0.1, 0.05])
text_K = TextBox(axbox_K, "Evaluate", textalignment="center")


def update(val):
    global T
    K = choix_K.val
    w0 = choix_w0.val
    xi = choix_xi.val
    bornes_w=plage_w(w0,xi)
    puissances_w=arange(bornes_w[0],bornes_w[1],0.01)
    W=10**puissances_w
    axes_mod.set_xlim(w0/1000,1000*w0)
    axes_pha.set_xlim(w0/1000,1000*w0)
    module = 20*log10(absolute(H(W,w0,xi,K)))
    phase = angle(H(W,w0,xi,K),'deg')
    diag_mod.set_data(W,module)
    diag_pha.set_data(W,phase)
    plage_mod(module)


def update_K(expression):
    if expression:
        K = float(eval(expression))
        choix_K.set_val(K)
        if choix_K.valmax<K:
            choix_K.ax.set_xlim(K_init[0],K)
        elif choix_K.valmin>K:
            choix_K.ax.set_xlim(K,K_init[1])
        bornes_w=plage_w(w0,xi)
        puissances_w=arange(bornes_w[0],bornes_w[1],0.01)
        W=10**puissances_w
        axes_mod.set_xlim(10**bornes_w[0],10**bornes_w[1])
        axes_pha.set_xlim(10**bornes_w[0],10**bornes_w[1])
        module = 20*log10(absolute(H(W,w0,xi,K)))
        phase = angle(H(W,w0,xi,K),'deg')
        diag_mod.set_data(W,module)
        diag_pha.set_data(W,phase)

def update_xi(expression):
    if expression:
        xi = float(eval(expression))
        choix_xi.set_val(xi)
        if choix_xi.valmax<xi:
            choix_xi.ax.set_xlim(xi_init[0],xi)
        elif choix_xi.valmin>xi:
            choix_xi.ax.set_xlim(xi,xi_init[1])
        bornes_w=plage_w(w0,xi)
        puissances_w=arange(bornes_w[0],bornes_w[1],0.01)
        W=10**puissances_w
        axes_mod.set_xlim(10**bornes_w[0],10**bornes_w[1])
        axes_pha.set_xlim(10**bornes_w[0],10**bornes_w[1])
        module = 20*log10(absolute(H(W,w0,xi,K)))
        phase = angle(H(W,w0,xi,K),'deg')
        diag_mod.set_data(W,module)
        diag_pha.set_data(W,phase)

def update_w0(expression):
    if expression:
        w0 = float(eval(expression))
        choix_w0.set_val(w0)
        if choix_w0.valmax<w0:
            choix_w0.ax.set_xlim(w0_init[0],w0)
        elif choix_w0.valmin>w0:
            choix_w0.ax.set_xlim(w0,w0_init[1])
        bornes_w=plage_w(w0,xi)
        puissances_w=arange(bornes_w[0],bornes_w[1],0.01)
        W=10**puissances_w
        axes_mod.set_xlim(10**bornes_w[0],10**bornes_w[1])
        axes_pha.set_xlim(10**bornes_w[0],10**bornes_w[1])
        module = 20*log10(absolute(H(W,w0,xi,K)))
        phase = angle(H(W,w0,xi,K),'deg')
        diag_mod.set_data(W,module)
        diag_pha.set_data(W,phase)

    
choix_K.on_changed(update)
choix_w0.on_changed(update)
choix_xi.on_changed(update)
text_K.on_submit(update_K)
text_w0.on_submit(update_w0)
text_xi.on_submit(update_xi)

show()
