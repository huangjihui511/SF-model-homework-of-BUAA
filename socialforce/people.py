import numpy as np 
from .tactics import Tactics

class People(object):
    def __init__(self,id,location,gateLocation,gateWidth,spaceSize,r,expV):
        self.id = id
        self.location = location
        self.speed = np.zeros(2)
        self.accele = np.zeros(2)
        self.gateLocation = gateLocation
        self.gateWidth = gateWidth
        self.expV = expV
        self.A = 2000
        self.B = 0.08
        self.k1 = 120000
        self.k2 = 240000
        self.r = r
        self.m = 60
        self.spaceSize = spaceSize
        self.state = 'IN'
        self.error = []
        self.clever = 10

    def removeAccele(self):
        self.accele = 0

    def getDirect(self):
        newlocation = self.gateLocation.copy()
        newlocation[0] += 0.5
        data = - self.location + newlocation
        return People.getVector(data)

    def setMainFornomular(self):
        '''if np.sqrt(np.dot(self.expV,self.expV)) > 100:
            self.expV = 0'''
        mf = (self.expV * self.getDirect() - self.speed) / 0.5
        self.accele = mf
        self.error = [self.getDirect(),mf]
        '''if np.linalg.norm(mf) > 100:
            print('mf')'''
    
    def addRepulsiveForce(self,p):
        if self.id == p.id:
            return
        rij = self.r + p.r
        dLocation = self.location - p.location
        dij = np.linalg.norm(dLocation)
        g = rij - dij
        if g < 0:
            g = 0
        '''if g > 0:
            print('f')'''
        f = (self.A * np.exp((rij - dij) / self.B) + \
            self.k1 * g )* People.getVector(dLocation) \
            + self.k2 * g * np.dot(np.array([-dLocation[1],dLocation[0]]),(p.speed - self.speed) ) \
            * np.array([-dLocation[1],dLocation[0]])
        a = f / self.m
        '''if np.linalg.norm(a) > 100:
            print(self.id,p.id,np.linalg.norm(a),dij)'''
        self.accele += a
        self.error.append(a)
        return

    def addHinderForce(self,h):
        ri = self.r
        dLocation = self.location - h.location
        diw = np.linalg.norm(dLocation)
        g = ri - diw
        if g < 0:
            g = 0
        f = (self.A * np.exp((ri - diw) / self.B) + \
            self.k1 * g )* People.getVector(dLocation) \
            + self.k2 * g * np.dot(self.speed,np.array([-dLocation[1],dLocation[0]]) ) \
            * np.array([-dLocation[1],dLocation[0]])
        a = f / self.m
        self.accele += a
        self.error.append(a)
        return

    def think(self,hinders):
        tactics = Tactics(hinders,self.gateLocation,self.spaceSize)
        direction = np.array(tactics.think(self.location,self.r))
        #print(direction - self.location)
        deltA = (direction - self.location) * self.clever
        deltM = self.gateLocation - self.location
        Lx=np.sqrt(np.dot(deltA,deltA))
        Ly=np.sqrt(np.dot(deltM,deltM))
        cos_angle=np.dot(deltA,deltM)/(Lx*Ly)
        angle=np.arccos(cos_angle)
        angle2=angle*360/2/np.pi
        print(angle2)
        if angle2 > 30:
            self.state = 'HINDERED'
            print(self.id,'hindered')
            self.speed = deltA
            print(deltA)
        else:
            self.state = 'IN'
            print(self.id,'in')
            self.speed = np.zeros(2)
        

    def move(self,time):
        move = self.speed * time + self.accele * time * time * 0.5
        if np.sqrt(np.dot(move,move)) > 5:
            self.state = 'INJURED'
            print(self.id,'injured')
            return
        dmove = np.linalg.norm(move)
        self.location += move
        self.speed += self.accele
        self.whatIfOut()
        return

    def whatIfOut(self):
        x = self.location[0]
        y = self.location[1]
        if x >= 0 + self.r and y >=0 + self.r and x <= self.spaceSize[0] - self.r  and y <= self.spaceSize[1] - self.r :
            return False
        if np.linalg.norm(self.location - self.gateLocation) < self.gateWidth / 2:
            self.state = 'OUT'
            print(self.id,'is out')
            return True
        if x < 0 + self.r :
            self.location[0] = 0 + self.r
            self.speed[0] = 0
        if x > self.spaceSize[0] - self.r :
            self.location[0] = self.spaceSize[0] -self.r
            self.speed[0] = 0
        if y < 0 + self.r :
            self.location[1] = self.r
            self.speed[1] = 0
        if y > self.spaceSize[1] - self.r :
            self.location[1] = self.spaceSize[1] - self.r
            self.speed[1] = 0
        return True

    def ishindered(self):
        return np.linalg.norm(self.speed) < 0.1 and np.linalg.norm(self.accele) < 0.1

    @staticmethod
    def getVector(data):
        d = np.linalg.norm(data) + 0.01
        result = data / d
        return result
    