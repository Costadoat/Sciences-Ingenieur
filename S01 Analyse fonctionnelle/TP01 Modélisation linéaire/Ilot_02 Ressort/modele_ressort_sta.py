    # -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 17:41:02 2016

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

k=float(input('Raideur du ressort (en N/m) ?'))
m=float(input('Masse suspendue (en kg) ?'))
K0=m*9.81/k

s=K0
print("%4.2f m" % s)

