# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *


K=80000
tau=0.5
w0=1/tau
def H(w,K,tau):
    w0=1/tau
    return K/(1j*w*(1+1j*w*tau)),w0

fig=figure('Diagrammes Bode')
puissance_w=arange(-2,3,0.01)
# Les pulsations w
W=10**puissance_w
# La phase en degré
phase = angle(H(W,K,tau)[0],'deg')
# Le module en dB
module = 20*log10(absolute(H(W,K,tau)[0]))
#Tracer du diagramme de Bode
subplot(211) # Perme    t d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod1,diag_mod2=semilogx(W,module,10,1) # Tracé en semilog du module
axes = gca()
axes.set_xlim(10**-2,10**3)
axes.set_ylim(-20,161)
axes.set_ylabel('Gain (dB)')
axes.set_xscale('log')
major_ticks_y = np.arange(-20,161,20)
axes.set_yticks(major_ticks_y)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
subplot(212)
diag_pha1,diag_pha2=semilogx(W,phase,10,1) #Tracé en semilog du module
axes = gca()
axes.set_xlim(10**-2,10**3)
axes.set_ylim(-180,-90)
axes.set_ylabel('Phase (deg)')
axes.set_xlabel('Pulsation $(rad.s^{-1})$')
major_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 30)
minor_ticks_y = np.arange((min(phase)//30*30)-30, ((max(phase)//30+1)*30)+30, 15)
axes.set_yticks(major_ticks_y)
axes.set_yticks(minor_ticks_y, minor=True)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
show()
