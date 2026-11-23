# On importe les bibliothèques
from matplotlib.pyplot import show, figure, subplot, gca, plot, xlabel, ylabel, grid, gca
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from numpy import log10, arange, absolute
from pylab import angle, semilogx
from matplotlib.widgets import TextBox

# Paramétrage de la fonction de transfert
K1=0.3
tau=3e-3
K2=1*100
K=K1*K2
w0=1/tau

x=arange(0.01,2,0.01)
y=log10(x)
plot(x,y)
xlabel('x')
ylabel('log(x)')
ax = gca()

# Option 1 : pas fixe (ici une graduation mineure tous les 0.05 en x, 0.1 en y)
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# Il faut aussi fixer le pas des graduations principales si on veut le contrôler
ax.xaxis.set_major_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
grid(True,which='minor', alpha=0.6)
grid(True,which='major', alpha=0.9)
show()




def H1(w,K,tau):
    return K1/(1+tau*1j*w)

def H2(w,K,tau):
    return K2/(1j*w)

def H(w,K,tau):
    return K/(1j*w*(1+tau*1j*w))

def trace(H,w0):
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
    subplot(212)
    diag_pha,val=semilogx(W,phase,10,1) #Tracé en semilog de la phase
    # Paramétrage de la grille pour le module
    axes_pha = gca()
    axes_pha.set_ylabel('Phase (deg)')
    axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
    axes_pha.grid(True,which='minor', alpha=0.2)
    axes_pha.grid(True,which='major', alpha=0.5)
    show()

trace(H1,w0)
trace(H2,w0)
trace(H,w0)
