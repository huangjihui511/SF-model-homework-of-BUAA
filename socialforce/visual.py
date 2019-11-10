import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

global anim

class Visual(object):

    def __init__(self,size,frames,simulator,epoch,ratio,gatewidth):
        self.frames = frames
        self.size = size
        self.simulator = simulator
        self.epoch = epoch
        self.ratio = ratio
        self.gatewidth = gatewidth
        self.hinders = simulator.gethinders()
    
    def makefigure(self):
        fig, ax = plt.subplots() 
        xdata, ydata = [], []
        ln, = ax.plot([], [], 'bo',markersize=8, animated=False)
        def init():
            ax.set_xlim(-1, self.size[0] + 1)
            ax.set_ylim(-1, self.size[1] + 1)
            f = self.frames[0]
            xdata = [f[id][0] for id in f]
            ydata = [f[id][1] for id in f]
            ln.set_data(xdata, ydata)
            return ln,           

        def update(e):
            #print('e:',e)
            while len(self.frames) <= e:
                self.simulator.runOnce(self.ratio)
            f = self.frames[e]
            xdata = [f[id][0] for id in f]
            ydata = [f[id][1] for id in f]
            ln.set_data(xdata, ydata)
            return ln,
        
        x = self.size[0]
        y = self.size[1]
        plt.plot([x,x],[0,y/2 - self.gatewidth/2],'g')
        plt.plot([x,x],[y/2 + self.gatewidth/2,y],'g')
        plt.plot([0,x],[0,0],'g')
        plt.plot([0,x],[y,y],'g')
        plt.plot([0,0],[0,y],'g')
        #plt.plot([self.hinders[l].location[0] for l in self.hinders], [self.hinders[l].location[1] for l in self.hinders], 'go',markersize=12)
        ani = FuncAnimation(fig, update, frames=range(self.epoch),init_func=init, blit=True, repeat = False)
        ani.repeat = False
        plt.show()
        print('end')