__author__ = 'tomaton'
import pylab
import matplotlib.pyplot as plt
import numpy as np

def my_legend2(axis = None):
    if axis == None:
        axis = plt.gca()

    Nlines = len(axis.lines)
    #print Nlines

    xmin, xmax = axis.get_xlim()
    ymin, ymax = axis.get_ylim()
    for l in range(Nlines):
        x = axis.lines[l].get_xdata()[950];
        y = axis.lines[l].get_ydata()[950]*1.2;


        axis.text(x, y, axis.lines[l].get_label(),
                  horizontalalignment='right',
                  verticalalignment='center')

def my_legend3(axis = None):
    if axis == None:
        axis = plt.gca()

    Nlines = len(axis.lines)
    #print Nlines

    xmin, xmax = axis.get_xlim()
    ymin, ymax = axis.get_ylim()
    for l in range(Nlines):
        x = axis.lines[l].get_xdata()[38];
        y = axis.lines[l].get_ydata()[37]+1;


        axis.text(x, y, axis.lines[l].get_label(),
                  horizontalalignment='right',
                  verticalalignment='center')
a=[i for i in xrange(1,1001,1)]
a2 = [i for i in xrange(1,61,1)]
a22=[1,10,20,30,40,50,60]

g2 = [i for i in xrange(80,160,2)]
g22= [80,160]

#for alpha in xrange(0.0)
#fig = plt.figure(figsize=(12,6), dpi=180)
f,axis1 = plt.subplots(3,1,squeeze=False, sharex='col', sharey='row')#, gridspec_kw=dict(width_ratios=[2, 1]))#[fig.add_subplot(13),fig.add_subplot(211),fig.add_subplot(311)]
#f,axis1 = plt.subplots(3,2, subplot_kw=dict(polar=True))#[fig.add_subplot(13),fig.add_subplot(211),fig.add_subplot(311)]
#f,axis2 = plt.subplots(3,1,sharey=True,sharex=True)#[fig.add_subplot(13),fig.add_subplot(211),fig.add_subplot(311)]

f.set_size_inches(8,8)
#f = plt.figure(figsize=(12,6), dpi=180)
## alphas [[alpha, descriptiom,measured points,color in graph, axis, overheadfraction]]
alphas = [[0.0144,'Matejak2014',[1,7.5,11.8,12.5,15.4,15.7,14.73],'b',axis1[0][0],0.9072],[0.000494,'Meurs2014',[1,8.7,16.6,24.4,29.6,32.9,38.65],'g',axis1[1][0],0.040488],[0.0000885,'Hummod2013',[1,10,20.4,24.8,35.4,41.8,49.83],'r',axis1[2][0],0.004255]]
#betas = [[0.21,'Matejak2014',[15.7,15.7],'b',axis1[0][1],0],[0.0253,'Meurs2014',[72.7,72.7],'g',axis1[1][1],0],[0.00431,'HumMod2013',[85.2,161.8],'r',axis1[2][1],0]]
#ax = fig.add_subplot(122)
for alpha in alphas:
    b=[(1/(alpha[0]+(1-alpha[0])/i)) for i in xrange(1,1001,1)]
    b2=[(1/(alpha[0]+(1-alpha[0])/i)) for i in xrange(1,61,1)]

    #corS = [((1+alpha[5])/(alpha[0]+(1-alpha[0])/i +alpha[5])) for i in xrange(1,61,1)]
    #ax.plot(a,b, label =r'$\alpha='+str(alpha[0])+'$ '+alpha[1])# $S='+"{:10.2f}".format(1/alpha)+'$')
    alpha[4].plot(a2,b2, label =r'$\alpha='+str(alpha[0])+'$ '+alpha[1],color=alpha[3])# $S_{(40)}='+"{:10.2f}".format(b2[39])+'$')
    #if (alpha[5]>0):
    #    alpha[4].plot(a2,corS, label =r'$o='+str(alpha[5])+'$', color=alpha[3],linestyle='--')# $S_{(40)}='+"{:10.2f}".format(b2[39])+'$')
    alpha[4].plot(a22,alpha[2],marker='o',linestyle='..',color=alpha[3])
#    alpha[4].set_xlabel('P - number of processors')
#    alpha[4].set_ylabel('S(P) - speedup')
    alpha[4].grid(True, which='both')
    alpha[4].legend(loc='best')

#for beta in betas:
    #b=[(1/(alpha[0]+(1-alpha[0])/i)) for i in xrange(1,1001,1)]
#   b2=[((beta[0]+(1-beta[0])*i)) for i in xrange(80,160,2)]

    #corS = [((1+alpha[5])/(alpha[0]+(1-alpha[0])/i +alpha[5])) for i in xrange(1,61,1)]
    #ax.plot(a,b, label =r'$\alpha='+str(alpha[0])+'$ '+alpha[1])# $S='+"{:10.2f}".format(1/alpha)+'$')
    #beta[4].plot(g2,b2, label =r'$\beta='+str(beta[0])+'$ '+beta[1],color=beta[3])# $S_{(40)}='+"{:10.2f}".format(b2[39])+'$')
    #if (alpha[5]>0):
    #    alpha[4].plot(a2,corS, label =r'$o='+str(alpha[5])+'$', color=alpha[3],linestyle='--')# $S_{(40)}='+"{:10.2f}".format(b2[39])+'$')
#    beta[4].plot(g22,beta[2],marker='o',linestyle='..',color=beta[3])
#    alpha[4].set_xlabel('P - number of processors')
#    alpha[4].set_ylabel('S(P) - speedup')
#    beta[4].grid(True, which='major')
    #beta[4].legend(loc='best')

#major_ticks = np.arange(60, 200, 20)
#axis1[2][1].set_xticks(major_ticks)
#axis1[1][1].set_xticks(major_ticks)
#axis1[0][1].set_xticks(major_ticks)
axis1[2][0].set_xlabel('P - number of processors')
#ax.set_yscale('log')
#ax.grid(True, which='both')
#ay.grid(True, which='both')
#ay.legend(loc='best')
#ax.xaxis.set_ticks([10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])
#ax.yaxis.set_ticks([2,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95])
#ax.set_xlabel('P - number of processors')
#ax.set_ylabel('S(P) - speedup')
#ay.set_xlabel('P - number of processors')
#ay.set_ylabel('S(P) - speedup')
#ax.set_yscale('log')
#ax.grid(True, which='both')
#ay.grid(True, which='both')
#ay.legend(loc='best')
#ax.legend(loc='best')

#my_legend2(ax)
#my_legend3(ay)
#pylab.savefig('/home/tomaton/Dropbox/Studium-Dokumenty/Dizertace/chapter7/speedup.png',dpi=150)
plt.show()
__author__ = 'tomaton'
