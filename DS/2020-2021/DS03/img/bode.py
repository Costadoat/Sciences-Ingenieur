# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *

tau=6*10**(-5)
def H(w):
    return 6*10**(-5)*1j*w/(1+tau*1j*w)

def trace(zoom,ordre,H):
    # Découpage régulier des puissances en base 10 de la pulsation ici de 10^-2 à 10^3
    if ordre==1:
        fig=figure('Diagrammes Bode')
        w0=1/tau
        puissance_w=arange(log10(w0)-5,log10(w0)+4,0.01)
    else:
        w0=100
        if zoom==False:
            fig=figure('Diagrammes Bode')
            puissance_w=arange(log10(w0)-3,log10(w0)+3,0.01)
        else:
            fig=figure('Zoom Diagrammes Bode')
            puissance_w=arange(log10(w0)-0.1,log10(w0)+0.1,0.01)
    # Les pulsations w
    W=10**puissance_w
    # La phase en degré
    phase = angle(H(W),'deg')
    # Le module en dB
    module = 20*log10(absolute(H(W)))
    #Tracer du diagramme de Bode
    subplot(211) # Perme    t d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
    semilogx(W,module,10,1) # Tracé en semilog du module
    axes = gca()
    axes.set_xlim(w0/100,100*w0)
    axes.set_ylim(-40,5)
    axes.set_ylabel('Gain (dB)')
    axes.set_xscale('log')
    major_ticks_y = np.arange(-40, 10, 20)
    minor_ticks_y = np.arange(-40, 10, 10)
    axes.set_yticks(major_ticks_y)
    axes.set_yticks(minor_ticks_y, minor=True)
    axes.grid(True,which='minor', alpha=0.2)
    axes.grid(True,which='major', alpha=0.5)
    subplot(212)
    semilogx(W,phase,10,1) #Tracé en semilog du module
    axes = gca()
    major_ticks_y = np.arange(0, 91, 30)
    minor_ticks_y = np.arange(0, 91, 10)
    axes.set_yticks(major_ticks_y)
    axes.set_yticks(minor_ticks_y, minor=True)
    axes.set_ylabel('Phase (deg)')
    axes.set_xlabel('Pulsation $(rad.s^{-1})$')
    axes.set_xlim(w0/100,100*w0)
    axes.grid(True,which='minor', alpha=0.2)
    axes.grid(True,which='major', alpha=0.5)
    
ordre=1

if ordre==1:
    trace(False,1,H)
#    trace(False,1,asympt)
else:
    trace(False,2,H)    
    if xi<0.7:
        trace(True,2,H)
    
show()
