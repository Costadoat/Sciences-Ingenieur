# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from cmath import phase
from pylab import *

ordre=1

if ordre==1:
    K=0.2
    tau=10
    w0=1/tau
    def H(w):
        return (1+tau*1j*w)/(K*1j*w)
else:
    K=0.2
    w0=500
    xi=1
    def H(w):
        return K/(1+2*xi*1j*w/w0-w**2/w0**2)


fig=figure('Diagrammes Bode')
puissance_w=arange(log10(w0)-3,log10(w0)+3,0.1)
# Les pulsations w
W=10**puissance_w
# La phase en degré
laphase=[(180/pi)*phase(H(wi)) for wi in W]
# Le module en dB
lemodule=[20*log10(abs(H(wi))) for wi in W]
#Tracer du diagramme de Bode
subplot(211) # Perme    t d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod1,diag_mod2=semilogx(W,lemodule,10,1) # Tracé en semilog du module
axes = gca()
axes.set_xlim(min(W),max(W))
delta=(max(lemodule)-min(lemodule))/10
axes.set_ylim(((min(lemodule)-delta)//10)*10, ((max(lemodule)+delta)//10+1)*10)
axes.set_ylabel('Gain (dB)')
axes.set_xscale('log')
major_ticks_y = np.arange(((min(lemodule)-delta)//10-1)*10, ((max(lemodule)+delta)//10+1)*10+1, (((max(lemodule)-min(lemodule))/5)//5)*5)
minor_ticks_y = np.arange(((min(lemodule)-delta)//10-1)*10, ((max(lemodule)+delta)//10+1)*10+1, (((max(lemodule)-min(lemodule))/10)//5)*5)
axes.set_yticks(major_ticks_y)
axes.set_yticks(minor_ticks_y, minor=True)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)
subplot(212)
diag_pha1,diag_pha2=semilogx(W,laphase,10,1) #Tracé en semilog du module
axes = gca()
axes.set_xlim(min(W),max(W))
axes.set_ylim((min(laphase)//30)*30-30, (max(laphase)//30*30)+30)
axes.set_ylabel('Phase (deg)')
axes.set_xlabel('Pulsation $(rad.s^{-1})$')
major_ticks_y = np.arange((min(laphase)//30*30)-30, ((max(laphase)//30+1)*30)+30, 30)
minor_ticks_y = np.arange((min(laphase)//30*30)-30, ((max(laphase)//30+1)*30)+30, 15)
axes.set_yticks(major_ticks_y)
axes.set_yticks(minor_ticks_y, minor=True)
axes.grid(True,which='minor', alpha=0.2)
axes.grid(True,which='major', alpha=0.5)

show()
