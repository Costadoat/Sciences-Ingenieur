# On importe les bibliothèques
from matplotlib.pyplot import show, figure, subplot, gca
from numpy import log10, arange, absolute
from pylab import angle, semilogx
from matplotlib.widgets import TextBox

# Paramétrage de la fonction de transfert
K=10**-1
w0=10**3
w0=800
xi=0.2

def H(w,w0,xi,K):
    return K/(1j*w*(1+2*xi*1j*w/w0-w**2/w0**2))

fig=figure('Diagrammes Bode')
# Calcul des valeurs de l'abscisse
puissances_w=arange(log10(w0)-4,log10(w0)+3,0.01)
W=10**puissances_w
# Le module en dB
module = 20*log10(absolute(H(W,w0,xi,K)))
# La phase en degré
phase = angle(H(W,w0,xi,K),'deg')
dec=0
for i in range(len(phase)-1):
    ph=phase[i]
    phase[i]+=dec
    if abs(phase[i+1]-ph)>300:
        if ph<0:
            dec+=-360
        else:
            dec+=360
phase[-1]+=dec
    
#Tracer des diagrammes de Bode
subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod,val=semilogx(W,module,10,1) # Tracé en semilog du module
# Paramétrage de la grille pour le module
axes_mod = gca()
axes_mod.set_xlim(10**-1,10**5)
axes_mod.set_ylim(-200,0)
major_ticks_y = arange(0, -210, -20)
axes_mod.set_yticks(major_ticks_y)
axes_mod.grid(True,which='minor', alpha=0.2)
axes_mod.grid(True,which='major', alpha=0.5)
axes_mod.set_ylabel('Gain (dB)')
axes_mod.set_xscale('log')
subplot(212)
diag_pha,val=semilogx(W,phase,10,1) #Tracé en semilog de la phase
# Paramétrage de la grille pour le module
axes_pha = gca()
axes_pha.set_ylabel('Phase (deg)')
axes_pha.set_ylim(-300,-70)
axes_pha.set_xlim(10**-1,10**5)
major_ticks_y = arange(-90, -300, -30)
axes_pha.set_yticks(major_ticks_y)
axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
axes_pha.grid(True,which='minor', alpha=0.2)
axes_pha.grid(True,which='major', alpha=0.5)

show()
