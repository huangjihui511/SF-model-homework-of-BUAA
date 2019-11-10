import numpy as np
import matplotlib.pyplot as plt

class Figure():
    def __init__(self,results):
        self.results = results
        self.xs = [x for x in results]
        self.leavingtimes = [results[e]['leaveTime'] for e in results]
        self.flow = [1/(t/100) for t in self.leavingtimes]
        leavingPairs = []
        injuredPairs = []
        for e in results:
            result = results[e]
            timeLine = result['timeLine']
            outnum = result['outnum']
            injurednum = result['injurednum']
            for i in range(len(timeLine)):
                if outnum[i] != 0:
                    leavingPairs.append((e,timeLine[i]))
                if injurednum[i] != 0:
                    leavingPairs.append((e,timeLine[i]))
        self.leavingtimes2 = []
        self.xsleaving = []
        self.xsinjured = []
        self.injuredtime = []
        for p in leavingPairs:
            self.xsleaving.append(p[0])
            self.leavingtimes2.append(p[1])
        for p in injuredPairs:
            self.xsinjured.append(p[0])
            self.injuredtime.append(p[1])
        self.injurednum = []
        for e in results:
            injurednum = 0
            result_injured = results[e]['injurednum']
            for n in result_injured:
                injurednum += n
            self.injurednum.append(injurednum)

        

    def show(self):
        plt.figure(1)
        ax1 = plt.subplot()
        plt.sca(ax1)
        plt.plot(self.xs,self.leavingtimes,'g-',label = 'Leaving time for 200 poeple')
        plt.plot(self.xs,self.injurednum,'r-' , label = 'Number of injured people')
        plt.xlabel('Desired Velocity V_0')
        plt.legend()
        plt.figure(2)
        ax2 = plt.subplot()
        plt.legend()
        plt.sca(ax2)
        plt.plot(self.xs,self.flow,'g-' , label = 'flow')
        plt.xlabel('Desired Velocity V_0')
        plt.figure(3)
        ax3 = plt.subplot()
        plt.legend()
        plt.sca(ax3)
        plt.plot(self.xsleaving,self.leavingtimes2,'g+')
        plt.plot(self.xsinjured,self.injuredtime,'r+')
        plt.xlabel('Desired Velocity V_0')
        plt.ylabel('Leaving time & Injured time')
        plt.legend()
        plt.show()


