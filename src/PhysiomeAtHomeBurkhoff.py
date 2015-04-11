__author__ = 'tomaton'

#import json
import json
import matplotlib.pyplot as plt
import numpy
import pylab

with open('test1.txt') as json_data:
    d = json.load(json_data)
    json_data.close()

fig = plt.figure(figsize=(10,6), dpi=80)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

for i in range(d.__len__()):
    try:
        e = numpy.array(d[i]["VariableValues"])
        ax1.plot(e[:,1])
        ax2.plot(e[:,2])
        ax3.plot(e[:,3])
        ax4.plot(e[:,4])
    except:
        pass

    #pylab.savefig('/home/tomaton/Dropbox/Studium-Dokumenty/Dizertace/chapter7/physiomeathome.png')
plt.show()
