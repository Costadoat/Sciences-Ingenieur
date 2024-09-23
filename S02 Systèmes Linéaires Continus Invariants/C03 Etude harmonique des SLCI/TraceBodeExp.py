# On importe les bibliothèques
from matplotlib.pyplot import show, figure, subplot, gca
from numpy import log10, arange, absolute, pi, array
from pylab import angle, semilogx
from matplotlib.widgets import TextBox
from os.path import exists


################ Partie à modifier pour l'identification ##############################

# Exemple de fonction du second ordre

K=1
w0=100
xi=1

def H(w,w0,xi,K):
    return K/(1+2*xi*1j*w/w0-w**2/w0**2)

#######################################################################################


if not exists('data.csv'):
    # Génération du  fichier data.csv pour l'import des données expérimentales

    from random import randrange
    
    def incert_exp():
        return randrange(90,110,1)/100

    K=1
    w0=100
    xi=1

    def H(w,w0,xi,K):
        return K/(1+2*xi*1j*w/w0-w**2/w0**2)

    file_out=open('data.csv','w')
    file_out.write('Période;Amp Entrée;Amp Sortie;Delta T;Pulsation (rad/s);Gain;Gain dB;Phase\n')
    puissances_w=arange(log10(w0)-2,log10(w0)+2,0.1)
    W=10**puissances_w
    # Le module en dB
    module = 20*log10(absolute(H(W,w0,xi,K)))
    # La phase en degré
    phase = angle(H(W,w0,xi,K),'deg')
    for i in range(len(puissances_w)):
        file_out.write('{:.4f};10;{:.4f};{:.4f};0;0;0;0\n'.format(2*pi/10**puissances_w[i],10*10**(module[i]*incert_exp()/20),-phase[i]*incert_exp()/360*(2*pi/10**puissances_w[i])).replace('.',','))
    file_out.close()

else:
    # Ouverture du fichier data.csv présent dans le dossier
    W_exp=[]
    module_exp=[]
    phase_exp=[]
    file_in=open('data.csv','r')
    contenu=file_in.read().replace(',','.').replace('\t',';')
    lignes=contenu.split('\n')
    for ligne in lignes[1:-1]:
        data=ligne.split(';')
        W_exp.append(float(data[4]))
        module_exp.append(float(data[6]))
        phase_exp.append(float(data[7]))
    W_exp=array(W_exp)
    module_exp=array(module_exp)
    phase_exp=array(phase_exp)
    
    


    # Tracé des diagrammes
    fig=figure('Diagrammes Bode')
    # Calcul des valeurs de l'abscisse
    puissances_w=arange(log10(w0)-3,log10(w0)+3,0.1)
    W=10**puissances_w
    # Le module en dB
    module = 20*log10(absolute(H(W,w0,xi,K)))
    # La phase en degré
    phase = angle(H(W,w0,xi,K),'deg')
    #Tracer des diagrammes de Bode
    subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
    diag_mod,val=semilogx(W,module,10,1) # Tracé en semilog du module
    diag_mod,val=semilogx(W_exp,module_exp,10,1) # Tracé en semilog du module
    # Paramétrage de la grille pour le module
    axes_mod = gca()
    axes_mod.grid(True,which='minor', alpha=0.2)
    axes_mod.grid(True,which='major', alpha=0.5)
    axes_mod.set_ylabel('Gain (dB)')
    axes_mod.set_xscale('log')
    subplot(212)
    diag_pha,val=semilogx(W,phase,10,1) #Tracé en semilog de la phase
    diag_pha,val=semilogx(W_exp,phase_exp,10,1) # Tracé en semilog du module
    # Paramétrage de la grille pour le module
    axes_pha = gca()
    axes_pha.set_ylabel('Phase (deg)')
    axes_pha.set_xlabel('Pulsation $(rad.s^{-1})$')
    axes_pha.grid(True,which='minor', alpha=0.2)
    axes_pha.grid(True,which='major', alpha=0.5)

    show()
