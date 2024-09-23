from matplotlib import rcParams
import numpy as np
import matplotlib.pyplot as plt

#set plot attributes
fig_width = 7  # width in inches
fig_height = 4.2  # height in inches
fig_size =  [fig_width,fig_height]
params = {'axes.labelsize': 14,
          'axes.titlesize': 14,
          'font.size': 10,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'figure.figsize': fig_size,
          'savefig.dpi' : 600,
          'axes.linewidth' : 1.3,
          'ytick.major.size' : 6,      # major tick size in points
          'xtick.major.size' : 6      # major tick size in points
          #'xtick.major.size' : 2,
          #'ytick.major.size' : 2,
          }
rcParams.update(params)

# set sans-serif font to Arial
rcParams['font.sans-serif'] = 'Arial'


def sigmoid(x):
    return 1./(1+np.exp(-(x-5)))+1

# data to be displayed
np.random.seed(1234)
t = np.arange(0.1, 9.2, 0.15)
y = sigmoid(t) + 0.2*np.random.randn(len(t))
residuals = y - sigmoid(t)

t_fitted = np.linspace(0, 10, 100)

###########################
#adjust plots position
###########################
fig = plt.figure()

ax1 = plt.axes((0.14, 0.12, 0.65, 0.8))
plt.plot(t, y, 'b.', ms=5., clip_on=False)
plt.plot(t_fitted, sigmoid(t_fitted), 'r-', lw=3)

plt.text(5, 1.0, r"$L = \frac{1}{1+\exp(-V+5)}+10$",
                   fontsize=14,
                   transform=ax1.transData, clip_on=False,
                   va='top', ha='left')

#set axis limits
ax1.set_xlim((0, t.max()))
ax1.set_ylim((0.5, y.max()))

#hide right and top axes
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_position(('outward', 10))
ax1.spines['left'].set_position(('outward', 10))
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

#set labels
plt.xlabel(r'voltage (V, $\mu$V)')
plt.ylabel('luminescence (L)')

#make inset
ax_inset = plt.axes((0.25, 0.74, 0.2, 0.2), frameon=False)
plt.hist(residuals, fc='0.8',ec='w', lw=2)
plt.xticks([-0.5, 0, 0.5],[-0.5, 0, 0.5], size=6)
plt.xlim((-0.5, 0.5))
plt.yticks([5, 10], size=6)
plt.xlabel("residuals", size=8)
ax_inset.xaxis.set_ticks_position("none")
ax_inset.yaxis.set_ticks_position("left")
# change ticks for inset
for line in ax_inset.get_yticklines():
    line.set_markersize(4)
    line.set_markeredgewidth(0.5)
ax_inset.yaxis.grid(lw=1, color='w', ls='-')
plt.text(0, 0.9, "frequency", transform=ax_inset.transAxes,
        va='center', ha='right', size=8)
        
#export to svg and png
plt.savefig('sigmoid_fit.png')
plt.savefig('sigmoid_fit.svg')