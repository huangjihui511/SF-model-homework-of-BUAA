import numpy as np
import matplotlib.pyplot as plt
#创建自变量数组
x= np.linspace(0,2*np.pi,500)
#创建函数值数组
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
#创建图形
plt.figure(1)
 
#第一行第一列图形
ax1 = plt.subplot(2,2,1)
#第一行第二列图形
ax2 = plt.subplot(2,2,2)
plt.figure(2)
#第二行
ax3 = plt.subplot(2,2,1)

#选择ax1
plt.sca(ax1)
plt.plot(x,y1,'r-.')
plt.ylim(-1.5,1.5)  #限定y axis
 
#选择ax2
plt.sca(ax2)
plt.plot(x,y2,'g--')
plt.ylim(-1.5,1.5)
 
#选择ax3
plt.sca(ax3)
plt.plot(x,y3,'b--')
plt.ylim(-1.5,1.5)
#plt.savefig('.//result//3.6.png')
plt.show()

