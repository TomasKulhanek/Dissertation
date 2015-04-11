__author__ = 'tomaton'
import matplotlib.pyplot as plt
import pylab
from pandas import Series, DataFrame
countries = ['Armenia','Belarus','Bosnia & Herz.','Bulgaria','CERN','Croatia','Cyprus','Czech Republic',
             'Finland','France','Georgia','Germany','Greece','Hungary','Israel','Italy','Lithuania','Macedonia','Moldova',
             'Montenegro','Netherlands','NGI_IBERGRID','NGI_NDGF','Poland','Romania','Russia','Serbia',
             'Slovakia','Slovenia','Switzerland','Turkey','Ukraine','United Kingdom']

cpus = [93,139,16,983,28867,560,132,4244,1512,30878,12,44380,1749,1733,1607,43258,700,2056,72,40,29627,19009,43503,31840,7086,4721,1097,720,3844,2753,6019,794,36448]
data = Series(cpus,index=countries)

fig = plt.figure(figsize=(10,7), dpi=80)
axis = fig.add_subplot(111)

#axis.annotate()
#axis.ylabel('Logical CPUs')
index = len(cpus)
axis.set_yscale('log')
axis.bar(range(index),cpus,log=True)
axis.set_xticks(range(index))
axis.set_xticklabels(countries)
axis.yaxis.set_ticks([10,20,40,100,200,400,1000,2000,4000,10000,20000,40000])
axis.yaxis.set_ticklabels([10,20,40,100,200,400,1000,2000,4000,10000,20000,40000])


axis.grid(True)
fig.autofmt_xdate(bottom=0.2, rotation=90, ha='left')
#data.plot(kind='bar',ax = axis,logy=True)
plt.ylabel('Logical CPUs')
pylab.savefig('/home/tomaton/Dropbox/Studium-Dokumenty/Dizertace/chapter2/egicpus.png')
plt.show()