# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from matplotlib.ticker import LogFormatter, LogLocator

tau_1=0.006
tau_2=0.1
w0=1/tau_1**(1/2)
xi=0
K=0

def H(w,w0,xi,k):
    return (1-w**2*tau_1)/(1+1j*w*tau_2-w**2*tau_1),w0

fig=figure('Diagrammes Bode')
puissance_w=arange(log10(w0)-0.5,log10(w0)+0.5,0.001)
# Les pulsations w
W=10**puissance_w
module_asymp=[]
phase_asymp=[]
for wi in W:
    if wi<1/tau_2:
        module_asymp.append(0)
        phase_asymp.append(0)
    elif wi<1/tau_1**(1/2):
        module_asymp.append(-20*log10(tau_2*wi))
        phase_asymp.append(-90)
    elif wi<tau_2/tau_1:
        module_asymp.append(20*log10((tau_1/tau_2)*wi))
        phase_asymp.append(90)
    else:
        module_asymp.append(0)
        phase_asymp.append(0)
# La phase en degré
phase = angle(H(W,w0,xi,K)[0],'deg')
# Le module en dB
module = 20*log10(absolute(H(W,w0,xi,K)[0]))
#Tracer du diagramme de Bode
subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
#diag_mod1,diag_mod2=semilogx(W,module,10,1) # Tracé en semilog du module
semilogx(W,module_asymp) # Tracé en semilog du module
axes = gca()
axes.set_ylabel('Gain (dB)')
axes.set_xscale('log')
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
formatter = LogFormatter(labelOnlyBase=False, minor_thresholds=(4, 0.1))
axes.xaxis.set_minor_formatter(formatter)
subplot(212)
#diag_pha1,diag_pha2=semilogx(W,phase,10,1) #Tracé en semilog du module
semilogx(W,phase_asymp) #Tracé en semilog du module
axes = gca()
axes.set_ylabel('Phase (deg)')
axes.set_xlabel('Pulsation $(rad.s^{-1})$')
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
formatter = LogFormatter(labelOnlyBase=False, minor_thresholds=(4, 0.1))
axes.xaxis.set_minor_formatter(formatter)
show()

#savefig("q5.pgf")
