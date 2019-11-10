import numpy as np 
from .space import Space
from .visual import Visual
import random

class Simulator(object):
    def __init__(self,xlength = 20,ylength = 20,population = 20,deltatime = 0.1, epoch = 200, ratio = 20,r = 0.2,expV = 3,gatewidth = 1):

        located = []
        def getlocation(size,l):
            #x = random.random() * size[0]
            #y = random.random() * size[1]
            x = random.randint(0,size[0]-1)
            y = random.randint(0,size[1]-1)
            while (x,y) in l:
                x = random.randint(0,size[0]-1)
                y = random.randint(0,size[1]-1)
            l.append((x,y))
            l.append((x,y+1))
            l.append((x+1,y))
            l.append((x+1,y+1))
            '''l.append((x,y-1))
            l.append((x-1,y))
            l.append((x-1,y-1))
            l.append((x-1,y+1))
            l.append((x+1,y-1))'''
            return np.array([x + random.random() , y+random.random()])
        xlength = xlength
        ylength = ylength
        self.gatewidth = gatewidth
        self.r = r
        self.population = population
        self.epoch = epoch
        self.size = np.array([xlength,ylength])
        self.myspace = Space(self.size,r,expV,gatewidth)
        self.deltatime = deltatime
        self.frames = []
        self.ratio = ratio
        self.timeslist = []
        self.expV = expV

        for i in range(10):
            l = (xlength/2,ylength/2 - 5 + i)
            located.append(l)
            
            self.myspace.createHinder(np.array(l))

        for i in range(self.population):
            self.myspace.createPeople(getlocation(self.size,located),r=0.5)
        self.times = 0
        self.visual = Visual(self.size,self.frames,self,self.epoch,self.ratio,self.myspace.gateWidth)
        self.frames.append(self.myspace.getframe())
        self.leaveTime = None

    def runOnce(self,runTimes):
        times = 0
        while not self.myspace.isend() and times < runTimes and self.times * runTimes < self.epoch:
            times += 1
            self.times += 1
            self.myspace.updateAccele()
            self.myspace.updateLocation(self.deltatime)
            self.myspace.checkOutPeople()
            self.timeslist.append(self.times * self.deltatime)
            if len(self.myspace.peoples) == 0:
                self.leaveTime = self.times * self.deltatime
        self.frames.append(self.myspace.getframe())
        if self.times % 100 == 0:
            print('times:',self.times,'\tremain:',len(self.myspace.peoples))
       

    def run(self,visual = False):
        if visual == False:
            for i in range(self.epoch):
                self.runOnce(1)
        else:
            self.visualize()

    def visualize(self):
        self.visual.makefigure()

    def gethinders(self):
        return self.myspace.gethinders()

    def result(self):
        result = {}
        if self.leaveTime == None:
            self.leaveTime = self.times * self.deltatime
        result['leaveTime'] = self.leaveTime
        result['timeLine'] = self.timeslist
        result['injurednum'] = self.myspace.injurednum
        result['outnum'] = self.myspace.outnum
        return result