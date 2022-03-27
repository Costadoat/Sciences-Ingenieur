# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *


K=8e-6
K=1
xi=1.1
w0=1.66

def H(w):
    return K/(1+2*1j*xi*w/w0-w**2/w0**2)

fig=figure('Diagrammes Bode')
puissance_w=arange(-2,2,0.01)
# Les pulsations w
W=10**puissance_w
# La phase en degré
phase = angle(H(W),'deg')
# Le module en dB
module = 20*log10(absolute(H(W)))
#Tracer du diagramme de Bode
subplot(211) # Perme    t d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod1,diag_mod2=semilogx(W,module,10,1) # Tracé en semilog du module
axes = gca()
axes.set_xlim(10**(-2),10**2)
axes.set_ylim(-100,10)
axes.set_ylabel('Gain (dB)')
axes.set_xscale('log')
major_ticks_y = np.arange(-100,10,10)
axes.set_yticks(major_ticks_y)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
subplot(212)
diag_pha1,diag_pha2=semilogx(W,phase,10,1) #Tracé en semilog du module
axes = gca()
axes.set_xlim(10**(-2),10**2)
axes.set_ylim(-180,0)
axes.set_ylabel('Phase (deg)')
axes.set_xlabel('Pulsation $(rad.s^{-1})$')
major_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 30)
minor_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 15)
axes.set_yticks(major_ticks_y)
axes.set_yticks(minor_ticks_y, minor=True)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
show()
