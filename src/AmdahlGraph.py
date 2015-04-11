__author__ = 'tomaton'
import matplotlib.pyplot as plt
import pylab

def my_legend2(axis = None):
    if axis == None:
        axis = plt.gca()

    Nlines = len(axis.lines)
    print Nlines

    xmin, xmax = axis.get_xlim()
    ymin, ymax = axis.get_ylim()
    for l in range(Nlines):
        x = axis.lines[l].get_xdata()[90]-5;
        y = axis.lines[l].get_ydata()[90]+0.7;


        axis.text(x, y, axis.lines[l].get_label(),
                  horizontalalignment='center',
                  verticalalignment='center')
a=[i for i in xrange(1,100,1)]
#for alpha in xrange(0.0)
alphas = [0.01,0.02,0.05,0.1,0.2,0.5]
fig = plt.figure(figsize=(10,8), dpi=150)
ax = fig.add_subplot(111)
for alpha in alphas:
    b=[(1/(alpha+(1-alpha)/i)) for i in xrange(1,100,1)]
    ax.plot(a,b, label =r'$\alpha ='+str(alpha)+'$')
ax.xaxis.set_ticks([10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])
ax.yaxis.set_ticks([2,5,10,15,20,25,30,35,40,45,50,55])
ax.set_xlabel('P - number of processors')
ax.set_ylabel('S(P) - speedup')
ax.grid(True, which='both')
#ax.legend(loc='best')
my_legend2()
pylab.savefig('/home/tomaton/Dropbox/Studium-Dokumenty/Dizertace/chapter2/Amdahl.png')
plt.show()
