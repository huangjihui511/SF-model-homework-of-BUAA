import numpy as np

from .hinder import Hinder
from .people import People

class Space(object):
    def __init__(self, size,r,expV,gatewidth):
        self.size = size
        self.peoples = {}
        self.id = 0
        self.gateLocation = np.zeros(2)
        self.gateLocation[0] = self.size[0]
        self.gateLocation[1] = self.size[1] / 2
        self.gateWidth = gatewidth
        self.r = r
        self.hinders = {}
        self.hinderid = 0
        self.outnum = []
        self.injurednum = []
        self.expV = expV

    def createHinder(self,location):
        self.hinders[self.hinderid] = Hinder(self.hinderid,location)
        self.hinderid += 1

    def createPeople(self, location,r):
        self.peoples[self.id] = People(self.id,location,self.gateLocation,self.gateWidth,self.size,self.r,self.expV)
        self.id += 1

    def updateAccele(self):
        for i in self.peoples:
            if self.peoples[i].state == 'IN':
                self.peoples[i].setMainFornomular()
            else:
                self.peoples[i].removeAccele()
            for j in self.peoples:
                self.peoples[i].addRepulsiveForce(self.peoples[j])
            for k in self.hinders:
                #elf.peoples[i].addHinderForce(self.hinders[k])
                pass
            if self.peoples[i].ishindered() or self.peoples[i].state == 'HINDERED':
                #self.peoples[i].think(self.hinders)
                pass
        return
    
    def updateLocation(self,time):
        for i in self.peoples:
            self.peoples[i].move(time)
        return

    def checkOutPeople(self):
        new_peoples = {}
        out = 0
        injured = 0
        for i in self.peoples:
            if self.peoples[i].state != 'OUT' and self.peoples[i].state != 'INJURED':
                new_peoples[i] = self.peoples[i]
            if self.peoples[i].state == 'OUT':
                out += 1
            if self.peoples[i].state == 'INJURED':
                injured += 1
        self.peoples = new_peoples
        self.outnum.append(out)
        self.injurednum.append(injured)
        
    def show(self):
        frame = {}
        for id in self.peoples:
            print(id,self.peoples[id].location)

    def isend(self):
        return len(self.peoples) == 0

    def getframe(self):
        frame = {id:self.peoples[id].location.copy() for id in self.peoples}
        return frame

    def gethinders(self):
        return self.hinders