import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 3))
plt.plot([0,2,2,5],[4,4,0,0])
plt.xlabel(r't (s)')
plt.ylabel(r'$V_{R_s}\ (V)$')
plt.grid('on')
plt.show()
