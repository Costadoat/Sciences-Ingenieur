# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *


K=10
w1=1/0.025
w2=1/0.0025
print(w1,w2)
w0=(w1*w2)**(1/2)
xi=1

def H(w,w0,xi,k):
    return K/((1+1j*w/w1)*(1+1j*w/w2)),w0

fig=figure('Diagrammes Bode')
puissance_w=arange(log10(w0)-3,log10(w0)+3,0.01)
# Les pulsations w
W=10**puissance_w
module_asymp=[]
phase_asymp=[]
for wi in W:
    if wi<w1:
        module_asymp.append(20*log10(K))
        phase_asymp.append(0)
    elif wi<w2:
        module_asymp.append(20*log10(K)-20*log10(wi/w1))
        phase_asymp.append(-90)
    else:
        module_asymp.append(20*log10(K)-20*log10(wi/w1)-20*log10(wi/w2))
        phase_asymp.append(-180)
# La phase en degré
phase = angle(H(W,w0,xi,K)[0],'deg')
# Le module en dB
module = 20*log10(absolute(H(W,w0,xi,K)[0]))
#Tracer du diagramme de Bode
subplot(211) # Perme    t d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod1,diag_mod2=semilogx(W,module,10,1) # Tracé en semilog du module
diag_mod1,diag_mod2=semilogx(W,module_asymp,10,1) # Tracé en semilog du module
axes = gca()
axes.set_ylabel('Gain (dB)')
axes.set_xscale('log')
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
subplot(212)
diag_pha1,diag_pha2=semilogx(W,phase,10,1) #Tracé en semilog du module
diag_pha1,diag_pha2=semilogx(W,phase_asymp,10,1) #Tracé en semilog du module
axes = gca()
axes.set_ylabel('Phase (deg)')
axes.set_xlabel('Pulsation $(rad.s^{-1})$')
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)

plt.savefig("q4.pgf")

#show()
