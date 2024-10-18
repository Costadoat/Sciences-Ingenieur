# On importe les bibliothèques
from matplotlib.pyplot import show, figure, subplot, gca
from numpy import log10, arange, absolute
from pylab import angle, semilogx
from matplotlib.widgets import TextBox

# Paramétrage de la fonction de transfert
K=0.1
tau=0.05
w0=1/tau

def H(w,K,tau):
    return K/(1+tau*1j*w)

fig=figure('Diagrammes Bode')
# Calcul des valeurs de l'abscisse
puissances_w=arange(log10(w0)-3,log10(w0)+3,0.01)
W=10**puissances_w
# Le module en dB
module = 20*log10(absolute(H(W,K,tau)))
# La phase en degré
phase = angle(H(W,K,tau),'deg')
#Tracer des diagrammes de Bode
subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod,val=semilogx(W,module,10,1) # Tracé en semilog du module
# Paramétrage de la grille pour le module
axes_mod = gca()
axes_mod.grid(True,which='minor', alpha=0.2)
axes_mod.grid(True,which='major', alpha=0.5)
axes_mod.set_ylabel('Gain (dB)')
axes_mod.set_xscale('log')
axes_mod.plot([0.02,20,20000],[-20,-20,-80])
subplot(212)
diag_pha,val=semilogx(W,phase,10,1) #Tracé en semilog de la phase
# Paramétrage de la grille pour le module
axes_pha = gca()
axes_pha.set_ylabel('Phase (deg)')
axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
axes_pha.grid(True,which='minor', alpha=0.2)
axes_pha.grid(True,which='major', alpha=0.5)
axes_pha.plot([0.02,20,20,20000],[0,0,-90,-90])

show()
