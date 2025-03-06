import numpy as np
import matplotlib.pyplot as plt

#question 1

theta=np.pi/2.
R2=0.15
R1=0.1
fr=0.3

Nt=100
Nr=100
dr=(R2-R1)/Nr
dt=theta/Nt

P0=0.05*10**6
P=P0
a=(0.4*P0)/(R2-R1)
b=0.8*P0-R1*a
C1=0

for i in range(Nr):
     for j in range(Nt):
         P=P0 #cas P=P0
         #P=a*(R1+dr*(i-1/2.))+b #cas P=a*r+b
         ds=(R1+dr*(i+1/2.))*dr*dt
         F=fr*ds*P
         C1=C1+2*F*(R1+dr*(i+1/2.))  
    
print(C1)


C2=2*theta*fr*P*(R2**3-R1**3)/3.
print(C2)

#question 2

def lireFichier(fichier):
    lignes = [line for line in open(fichier,'r')]
    result=[]
    for element in lignes:
        temps,pace = map(float,element.split())
        result.append((temps,pace))
    return result

def convertms(v):
    return v/3.6

vitesse = np.asarray(lireFichier("Course.txt"))
plt.plot(vitesse[:,0],vitesse[:,1],"bo-")

position=np.zeros(len(vitesse[:,0]))

for i in range(len(vitesse[:,0])-1):
    position[i+1] = position[i] + convertms(vitesse[i+1,1])*(vitesse[i+1,0]-vitesse[i,0])    
    
print(position[len(vitesse[:,0])-1]/1000.)

plt.plot(vitesse[:,0],vitesse[:,1],"bo-")
plt.plot(vitesse[:,0],position,"r")