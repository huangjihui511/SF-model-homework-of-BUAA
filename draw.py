import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
ax1 = plt.subplot()
plt.sca(ax1)
plt.plot(np.linspace(20,200,10),[20,29,40,55,67,74,82,88,90,94],c='r',linestyle='--',marker='o')
plt.xlabel('Number of people')
plt.ylabel('Leaving time')
ax1.set_ylim(0,100)

plt.figure(2)
ax1 = plt.subplot()
plt.sca(ax1)
plt.plot(np.linspace(1,5,5),[123,115,105,90,60],c='r',linestyle='--',marker='o')
plt.xlabel('Width of gate')
plt.ylabel('Leaving time')
ax1.set_ylim(30,150)

plt.figure(3)
ax1 = plt.subplot()
plt.sca(ax1)
plt.plot(np.linspace(1,10,5),[88 / 50,66/ 50,50/ 50,46/ 50,44/ 50],c='r',linestyle='--',marker='o')
plt.xlabel('Expect speed')
plt.ylabel('Leaving dense')
ax1.set_ylim(0.5,2)

plt.show()