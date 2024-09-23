# On importe les bibliothèques
from matplotlib.pyplot import show, figure, subplot, gca
from numpy import log10, arange, absolute, concatenate,ones
from pylab import angle, semilogx
from matplotlib.widgets import TextBox

# Paramétrage de la fonction de transfert
K=16
tau_2=0.00428
tau_1=0.000291

def H(w,w0,xi,K):
    return K/((1+tau_1*1j*w)*(1+tau_2*1j*w))

w0=1/(tau_1*tau_2)**0.5
xi=4
fig=figure('Diagrammes Bode')
# Calcul des valeurs de l'abscisse
puissances_w_1=arange(log10(w0)-2,log10(1/tau_2),0.01)
W_1=10**puissances_w_1
puissances_w_2=arange(log10(1/tau_2),log10(1/tau_1),0.01)
W_2=10**puissances_w_2
puissances_w_3=arange(log10(1/tau_1),log10(w0)+2,0.01)
W_3=10**puissances_w_3
W=concatenate([W_1,W_2,W_3])

# Le module en dB
module = 20*log10(absolute(H(W,w0,xi,K)))
module_1 = 20*log10(K)*ones(len(W_1))
module_2 = 20*log10(K/tau_2)-20*log10(W_2)
module_3 = 20*log10(K/(tau_1*tau_2))-40*log10(W_3)
module_as=concatenate([module_1,module_2,module_3])
# La phase en degré
phase = angle(H(W,w0,xi,K),'deg')
phase_1 = 0*ones(len(W_1))
phase_2 = -90*ones(len(W_2))
phase_3 = -180*ones(len(W_3))
phase_as=concatenate([phase_1,phase_2,phase_3])
#Tracer des diagrammes de Bode
subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod,val=semilogx(W,module,10,1) # Tracé en semilog du module
diag_mod,val=semilogx(W,module_as,10,1) # Tracé en semilog du module
# Paramétrage de la grille pour le module
axes_mod = gca()
axes_mod.grid(True,which='minor', alpha=0.2)
axes_mod.grid(True,which='major', alpha=0.5)
axes_mod.set_ylabel('Gain (dB)')
axes_mod.set_xscale('log')
subplot(212)
diag_pha,val=semilogx(W,phase,10,1) #Tracé en semilog de la phase
diag_pha,val=semilogx(W,phase_as,10,1) #Tracé en semilog de la phase
# Paramétrage de la grille pour le module
axes_pha = gca()
axes_pha.set_ylabel('Phase (deg)')
axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
axes_pha.grid(True,which='minor', alpha=0.2)
axes_pha.grid(True,which='major', alpha=0.5)


show()
