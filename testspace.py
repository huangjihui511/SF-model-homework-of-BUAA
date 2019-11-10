import numpy as np 
from socialforce import space
import random

def getlocation(size):
    x = random.random() * size[0]
    y = random.random() * size[1]
    return np.array([x,y])

def testonce():
    size = np.array([20,20])
    myspace = space.Space(size)
    for i in range(10):
        myspace.createPeople(getlocation(size))

    i = 0
    while not myspace.isend():
        i += 1
        '''if i % 10 == 0:
            myspace.show()'''
        myspace.updateAccele()
        myspace.updateLocation(0.5)
        myspace.checkOutPeople()
    return i
def main():
    times = []
    for i in range(20):
        times.append(testonce())
    print(times)

main()
