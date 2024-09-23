############## Contexte ##############

import matplotlib.pyplot as plt

def dichotomie(L):
    debut = 0
    fin = len(L) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if L[m] == 0:
            return m
        elif L[m] < 0:
            debut = m + 1
        else:
            fin = m - 1
    return(m)

t=list(range(0,20))
x=[ti**2 for ti in t]

plt.plot(t,x)
plt.show()

############## Réponse ##############

y=[]
for xi in x:
    y.append(xi-100)

print(t[dichotomie(y)])
