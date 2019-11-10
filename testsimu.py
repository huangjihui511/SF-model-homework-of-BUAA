from socialforce import simulator
simu = simulator.Simulator(xlength = 20,ylength = 20,population = 10,deltatime = 0.01, epoch = 200000000,ratio = 1,expV = 1)
simu.visualize()