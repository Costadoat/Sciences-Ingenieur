# On importe les bibliothèques
from matplotlib.pyplot import show, figure, subplot, gca, legend
from numpy import log10, arange, absolute, ones, zeros, concatenate
from pylab import angle, semilogx
from matplotlib.widgets import TextBox
from matplotlib.ticker import MultipleLocator

K1=10
K2=100
cst=8
a1=0.01*cst
a2=0.01/cst
b1=0.01
b2=0.01

def H(w):
    return K1*(1+b1*1j*w)*(1+b2*1j*w)/(K2*(1+a1*1j*w)*(1+a2*1j*w))


# Calcul des valeurs de l'abscisse
puissances_w=arange(0,4,0.01)
W=10**puissances_w
# Le module en dB
module = 20*log10(absolute(H(W)))
# La phase en degré
phase = angle(H(W),'deg')


# Calcul des valeurs de l'abscisse
puissances_w=arange(0,log10(1/a1),0.01)
W1=10**puissances_w
# Le module en dB
module1 = 20*log10(K1*ones(len(W1)))
# La phase en degré
phase1 = angle(zeros(len(W1)),'deg')
puissances_w=arange(log10(1/a1),log10(1/a2),0.01)
W2=10**puissances_w
# Le module en dB
module2 = 20*log10(K1/(a1*W2))
# La phase en degré
phase2 = angle(K1/(1j*W2),'deg')
puissances_w=arange(log10(1/a2),4,0.01)
W3=10**puissances_w
# Le module en dB
module3 = 20*log10(K1/(a2*a1*W3**2))
# La phase en degré
phase3 = angle(K1/(a2*(1j*W3)**2),'deg')
W=concatenate([W1,W2,W3])
modulea=concatenate([module1,module2,module3])
phasea=concatenate([phase1,phase2,phase3])


fig=figure('Diagrammes Bode')
# Calcul des valeurs de l'abscisse
puissances_w=arange(0,log10(1/b1),0.01)
W1=10**puissances_w
# Le module en dB
module1 = 20*log10(ones(len(W1))/K2)
# La phase en degré
phase1 = angle(zeros(len(W1)),'deg')
puissances_w=arange(log10(1/b1),log10(1/b2),0.01)
W2=10**puissances_w
# Le module en dB
module2 = 20*log10((b1*W2)/K2)
# La phase en degré
phase2 = angle((1j*b1*W2)/K2,'deg')
puissances_w=arange(log10(1/b2),4,0.01)
W3=10**puissances_w
# Le module en dB
module3 = 20*log10((b1*b2*W3**2)/K2)
# La phase en degré
phase3 = angle(-(b2*W3**2)/K2,'deg')
W=concatenate([W1,W2,W3])
moduleb=concatenate([module1,module2,module3])
phaseb=concatenate([phase1,phase2,phase3])

modulea=modulea[:-1]
phasea=phasea[:-1]
moduleas=modulea+moduleb
phaseas=phasea+phaseb

#Tracer des diagrammes de Bode
subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
diag_mod=semilogx(W,module,':',color='black',label='Tracé théorique') # Tracé en semilog du module
diag_mod=semilogx(W,modulea,color='black',label='Asymptote 1') # Tracé en semilog du module
diag_mod=semilogx(W,moduleb,'--',color='black',label='Asymptote 2') # Tracé en semilog du module
diag_mod=semilogx(W,moduleas,'-.',color='black',label='Asymptote') # Tracé en semilog du module
# Paramétrage de la grille pour le module
axes_mod = gca()
axes_mod.legend()
axes_mod.yaxis.set_major_locator(MultipleLocator(5))
axes_mod.grid(True, axis='x',which='minor', alpha=0.2)
axes_mod.grid(True, axis='x',which='minor', alpha=0.5)
axes_mod.grid(True, axis='y', which='major', alpha=0.6)
axes_mod.grid(True, axis='y', which='minor', alpha=0.3)
axes_mod.set_ylabel('Gain (dB)')
axes_mod.set_xscale('log')

subplot(212)
diag_pha=semilogx(W,phase,':',color='black',label='Tracé théorique') #Tracé en semilog de la phase
diag_pha=semilogx(W,phasea,color='black',label='Asymptote 1') #Tracé en semilog de la phase
diag_pha=semilogx(W,phaseb,'--',color='black',label='Asymptote 2') #Tracé en semilog de la phase
diag_pha=semilogx(W,phaseas,'-.',color='black',label='Asymptote') #Tracé en semilog de la phase
# Paramétrage de la grille pour le module
axes_pha = gca()
axes_pha.legend()
axes_pha.set_ylabel('Phase (deg)')
axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
axes_pha.grid(True,which='minor', alpha=0.2)
axes_pha.grid(True,which='major', alpha=0.5)
show()
