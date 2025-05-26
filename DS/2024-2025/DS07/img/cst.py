from numpy import pi, tan, cos, sin, linspace, arange
from matplotlib.pyplot import plot, legend, grid, show, ylim, figure, MultipleLocator, FormatStrFormatter

fig = figure()
ax = fig.add_subplot(1, 1, 1)

theta=linspace(0,2*pi,100)

ymin=-1.5
ymax=1.5
ylim(ymin,ymax)
major_y_ticks = arange(ymin, ymax, 0.5)
minor_y_ticks = arange(ymin, ymax, 0.1)
ax.set_xticks(arange(0, 2*pi+0.01, pi/8))
labels = [r'$0$', r'$\pi/8$', r'$\pi/4$', r'$3\pi/8$', r'$\pi/2$', r'$5\pi/8$',\
          r'$3\pi/4$', r'$7\pi/8$', r'$\pi$',r'$9\pi/8$', r'$5\pi/4$', r'$11\pi/8$',\
          r'$3\pi/2$', r'$13\pi/8$', r'$7\pi/4$', r'$15\pi/8$', r'$2\pi$']
ax.set_xticklabels(labels)
ax.set_yticks(major_y_ticks)
ax.set_yticks(minor_y_ticks)
plot(theta,cos(theta),'.',label='cos')
plot(theta,sin(theta),'--',label='sin')
plot(theta,tan(theta),label='tan')
legend()
grid('on')
show()
