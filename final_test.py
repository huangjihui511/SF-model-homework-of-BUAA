from socialforce.simulator import Simulator
from socialforce.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
multtimes = 5

def mean_list(l):
    sum = 0
    for x in l:
        sum += x
    return sum / len(l)

rs = np.linspace(20,100,10)
#rs = [100]
ss = []
results = {}
for r in rs:
    for i in range(multtimes):
        simu = Simulator(xlength = 50,ylength = 50,population = int(r),deltatime = 0.05, r = 0.2, epoch = 10000,ratio = 1,expV = 2,gatewidth = 1)
        ss.append(simu)
for s in ss:
    s.run(visual = False)
for s in ss:
    print(s.result())
    results.setdefault(s.population,[])
    results[s.population].append(s.result())

plt.figure(1)
ax1 = plt.subplot()
plt.sca(ax1)
plt.plot([r for r in results],[mean_list([x['leaveTime'] for x in results[r]]) for r in results],'g-')
plt.xlabel('Number of people')
plt.ylabel('Leaving time')
ax1.set_ylim(0,30)
gs = np.linspace(1,4,10)
ss = []
results = {}
for g in gs:
    for i in range(multtimes):
        simu = Simulator(xlength = 50,ylength = 50,population = 150,deltatime = 0.05, epoch = 10000,ratio = 1,expV = 3,gatewidth = g)
        ss.append(simu)
for s in ss:
    s.run(visual = False)
for s in ss:
    print(s.result())
    results.setdefault(s.gatewidth,[])
    results[s.gatewidth].append(s.result())

plt.figure(2)
ax1 = plt.subplot()
plt.sca(ax1)
plt.plot([g for g in results],[mean_list([x['leaveTime'] for x in results[g]]) for g in results],'g-')
plt.xlabel('Width of gate')
plt.ylabel('Leaving time')
ax1.set_ylim(0,30)

vs = np.linspace(1,10,10)
ss = []
results = {}
for v in vs:
    for i in range(multtimes):
        simu = Simulator(xlength = 50,ylength = 50,population = 150,deltatime = 0.05, epoch = 10000,ratio = 1,expV = v)
        ss.append(simu)
for s in ss:
    s.run(visual = False)
for s in ss:
    results.setdefault(s.expV,[])
    results[s.expV].append(s.result())

plt.figure(3)
ax1 = plt.subplot()
plt.sca(ax1)
plt.plot([v for v in results],[mean_list([150 / x['leaveTime'] for x in results[v]]) for v in results],'g-')
plt.xlabel('Expect speed')
plt.ylabel('Leaving dense')
#ax.set_ylim(0,15)
plt.show()