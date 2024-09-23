import numpy as np
import matplotlib.pyplot as plt

from IPython.display import display 
import pandas as pd 
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
  
t=np.linspace(0,5,51)
dot_y=1.5-0.5*t
vg2=5-t/2
theta=-np.linspace(1,2,51)**2-2
deltaF=np.linspace(3,4,51)**3/7.5

tbeta=[]
betaF=[]
for i in range(0,51,10):
    tbeta.append(t[i])
    betaF.append((dot_y[i]/vg2[i])+theta[i]+deltaF[i])

# creating a DataFrame 
dict = {r'$\dot{y}_F$' : [dot_y[i] for i in range(0,51,10)], 
        r'$V_{G_2}$' : [vg2[i] for i in range(0,51,10)],
        r'$\theta$' : [theta[i] for i in range(0,51,10)],
        r'$\delta_F$' : [deltaF[i] for i in range(0,51,10)],
        r'$\widehat{\beta}_F$' : betaF
        } 
df = pd.DataFrame(dict) 
  
# displaying the DataFrame 
display(df)


print(betaF)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(t,dot_y,'--',label=r'$\dot{y}_F$')
plt.plot(t,vg2,'.',label=r'$V_{G_2}$')
plt.plot(t,theta,'+',label=r'$\theta$')
plt.plot(t,deltaF,':',label=r'$\delta_F$')
plt.plot(tbeta,betaF,'.-',label=r'$\widehat{\beta}_F$')
plt.legend()


# Major ticks every 20, minor ticks every 5
major_ticks_x = np.arange(0, 5.1, 1)
minor_ticks_x = np.arange(0, 5.1, 1)
major_ticks_y = np.arange(-10, 10.1, 1)
minor_ticks_y = np.arange(-10, 10.1, 0.25)

ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x, minor=False)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y, minor=True)

# And a corresponding grid
ax.grid(which='both')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.show()
