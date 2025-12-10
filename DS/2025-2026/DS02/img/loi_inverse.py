L = 0.03
P = 0.088
Qx = 0.012
Qy = 0.03
M = 0.1
N = 0.007
import numpy as np
from sklearn import neighbors
# nombre de voisins
knn_parametre = 5
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## Définition de la loi directe
def loi_directe(alpha,theta4,thetaR):
    AHx = L*np.sin(alpha) + P*np.cos(theta4) + Qx*np.cos(thetaR) - Qy*np.sin(thetaR)
    AHy = -L*np.cos(alpha) + P*np.sin(theta4) + Qx*np.sin(thetaR) + Qy*np.cos(thetaR)
    return np.array((AHx,AHy))


## Génération des données d'entrainement
# Valeurs d'angles
vect_alpha=np.linspace(-30*np.pi/180,30*np.pi/180,100)
vect_theta4=np.linspace(-60*np.pi/180,60*np.pi/180,100)
vect_thetaR=np.linspace(-60*np.pi/180,60*np.pi/180,100)

vect_theta4_out=[]
vect_thetaR_out=[]

for alpha in vect_alpha:

	# Mise en forme des données
	D1,D2=np.meshgrid(vect_theta4,vect_thetaR)
	Data=np.concatenate((D1.reshape(-1,1),D2.reshape(-1,1)),axis=1)

	# Calcul des positions
	Y=loi_directe(alpha,Data[:,0],Data[:,1]).transpose()


	## Algorithme des k plus proches voisins (KNN)

	knn=neighbors.KNeighborsRegressor(knn_parametre)

	# Stockage des données d'entrainement
#	print("fit Knn")
	knn.fit(Y,Data)

	# Coefficient de corrélation
	score_knn=knn.score(Y,Data)
#	print("Coefficient R^2 de knn",score_knn)



	## Calcul de la loi inverse
	# Choix du déplacement
	position_finale=np.array((M,N))
	#print(position_finale)

	# Prédiction via l'algo knn
	prediction_knn=knn.predict(position_finale.reshape(1, -1))[0]
	#print("Angle servomoteur :",prediction_knn*180/np.pi)
	vect_theta4_out.append(prediction_knn[0])
	vect_thetaR_out.append(prediction_knn[1])

	## Vérification
	position_finale_knn=loi_directe(alpha,prediction_knn[0],prediction_knn[1])
	#print(position_finale_knn)

	# Calcul de l'écart
	Ecart_knn=position_finale-position_finale_knn
	Ecart_knn[0:2]=np.abs(Ecart_knn[0:2]/np.abs(position_finale[0:2]))*100
	#print("Ecart obtenue avec knn:",Ecart_knn)
	

nbx = 2*len(vect_alpha)
fig = plt.figure() # initialise la figure
line, = plt.plot([], []) 
plt.xlim(-0.1,0.2)
plt.ylim(-0.04, 0.02)

def animate(i):
    if i>=nbx/2:
        i=nbx-i-1
    alpha=vect_alpha[i]
    theta4=vect_theta4_out[i]
    thetaR=vect_thetaR_out[i]
    x=[0,L*np.sin(alpha),L*np.sin(alpha) + P*np.cos(theta4),L*np.sin(alpha) + P*np.cos(theta4) + Qx*np.cos(thetaR) - Qy*np.sin(thetaR)]
    y=[0,-L*np.cos(alpha),-L*np.cos(alpha) + P*np.sin(theta4),-L*np.cos(alpha) + P*np.sin(theta4) + Qx*np.sin(thetaR) + Qy*np.cos(thetaR)]
    line.set_data(x, y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, frames=nbx,
                              interval=1, blit=True, repeat=True)
ani = animation.FuncAnimation(fig, animate, frames=nbx,
                              interval=1, blit=True, repeat=True)

fig = plt.figure() # initialise la figure
plt.plot(vect_alpha,vect_theta4_out,label=r'$\theta_4$')
plt.plot(vect_alpha,vect_thetaR_out,label=r'$\theta_R$')
plt.xlabel(r'$\alpha$')
plt.legend()
plt.show()	

dalpha=(40*np.pi/180)/10
vect_omegaR=[]
for i in range(len(vect_alpha)):
    alpha=vect_alpha[i]
    theta4=vect_theta4_out[i]
    thetaR=vect_thetaR_out[i]
    vect_omegaR.append(L*dalpha*np.cos(theta4-alpha)/(Qx*np.sin(thetaR-theta4)+Qy*np.cos(thetaR-theta4)))


plt.plot(vect_alpha,vect_omegaR)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\omega_R$')
plt.show()
