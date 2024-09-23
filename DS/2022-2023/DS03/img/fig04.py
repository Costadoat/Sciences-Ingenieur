# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *

K=1
tau2=0.1
tau1=0.005
w0=1/tau1**0.5
xi=1

def H(w,w0,xi,k):
    return (1-w**2*tau1)/(1+1j*w*tau2-w**2*tau1),w0

fig=figure('Diagrammes Bode')
puissance_w=arange(log10(w0)-1,log10(w0)+1,0.001)
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
axes.set_ylabel('Gain (dB)')
axes.set_xscale('log')
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
subplot(212)
diag_pha1,diag_pha2=semilogx(W,phase,10,1) #Tracé en semilog du module
axes = gca()
axes.set_ylabel('Phase (deg)')
axes.set_xlabel('Pulsation $(rad.s^{-1})$')
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)

#show()

savefig("fig04.pgf")
