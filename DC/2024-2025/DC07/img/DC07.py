# On importe les bibliothèques
from matplotlib.pyplot import show, figure, subplot, gca
from numpy import log10, arange, absolute
from pylab import angle, semilogx
from matplotlib.widgets import TextBox

# Paramétrage de la fonction de transfert
K=2
xi=0.5
w0=100

def H(w,K,xi,w0):
    return K/(1+2*xi*1j*w/w0+(1j*w)**2/w0**2)

fig=figure('Diagrammes Bode')
# Calcul des valeurs de l'abscisse
puissances_w=arange(log10(w0)-3,log10(w0)+3,0.01)
W=10**puissances_w
# Le module en dB
module = 20*log10(absolute(H(W,K,xi,w0)))
# La phase en degré
phase = angle(H(W,K,xi,w0),'deg')
#Tracer des diagrammes de Bode
subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod,val=semilogx(W,module,10,1) # Tracé en semilog du module
# Paramétrage de la grille pour le module
axes_mod = gca()
axes_mod.grid(True,which='minor', alpha=0.2)
axes_mod.grid(True,which='major', alpha=0.5)
axes_mod.set_ylabel('Gain (dB)')
axes_mod.set_xscale('log')
axes_mod.plot([0.02,w0,1000*w0],[20*log10(2),20*log10(2),20*log10(2)-120])
subplot(212)
diag_pha,val=semilogx(W,phase,10,1) #Tracé en semilog de la phase
# Paramétrage de la grille pour le module
axes_pha = gca()
axes_pha.set_ylabel('Phase (deg)')
axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
axes_pha.grid(True,which='minor', alpha=0.2)
axes_pha.grid(True,which='major', alpha=0.5)
axes_pha.plot([0.02,w0,w0,1000*w0],[0,0,-180,-180])

show()
