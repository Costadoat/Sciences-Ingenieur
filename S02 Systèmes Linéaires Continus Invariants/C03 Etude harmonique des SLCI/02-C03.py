# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *


K=10
w0=0.2
xi=1

def H(w,w0,xi,k):
    return K/(1j*w*(1+1j*w/w0)),w0

fig=figure('Diagrammes Bode')
puissance_w=arange(log10(w0)-3,log10(w0)+3,0.01)
# Les pulsations w
W=10**puissance_w
# La phase en degré
phase = angle(H(W,w0,xi,K)[0],'deg')
# Le module en dB
module = 20*log10(absolute(H(W,w0,xi,K)[0]))
#Tracer du diagramme de Bode
subplot(211) # Perme    t d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod1,diag_mod2=semilogx(W,module,10,1) # Tracé en semilog du module
axes = gca()
axes.set_xlim(w0/1000,1000*w0)
delta=(max(module)-min(module))/10
axes.set_ylim(((min(module)-delta)//10)*10, ((max(module)+delta)//10+1)*10)
axes.set_ylabel('Gain (dB)')
axes.set_xscale('log')
major_ticks_y = np.arange(((min(module)-delta)//10-1)*10, ((max(module)+delta)//10+1)*10+1, (((max(module)-min(module))/5)//5)*5)
minor_ticks_y = np.arange(((min(module)-delta)//10-1)*10, ((max(module)+delta)//10+1)*10+1, (((max(module)-min(module))/20)//5)*5)
axes.set_yticks(major_ticks_y)
axes.set_yticks(minor_ticks_y, minor=True)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
subplot(212)
diag_pha1,diag_pha2=semilogx(W,phase,10,1) #Tracé en semilog du module
axes = gca()
axes.set_xlim(w0/1000,1000*w0)
axes.set_ylim((min(phase)//30)*30-30, (max(phase)//30*30)+30)
axes.set_ylabel('Phase (deg)')
axes.set_xlabel('Pulsation $(rad.s^{-1})$')
major_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 30)
minor_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 15)
axes.set_yticks(major_ticks_y)
axes.set_yticks(minor_ticks_y, minor=True)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)

barre_z = plt.axes([0.2, 0.1, 0.4, 0.02]) # position et dimensions de la barre
choix_z = Slider(barre_z, 'Amortissement (z)', 0, 10, valinit = 0)

def update(val):
    global T
    xi = choix_z.val
    module = 20*log10(absolute(H(W,w0,xi,K)[0]))
    phase = angle(H(W,w0,xi,K)[0],'deg')
    reponse.set_data(W,module)

choix_z.on_changed(update)

show()
