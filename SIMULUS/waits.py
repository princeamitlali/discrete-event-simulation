import simulus
from random import seed, expovariate
seed(12345)

"""
Have to understand this concept.
"""
def waits(x):
    while True:
        sems[x].wait()
        print("p%d wakes up at %g" %(x,sim.now))
        sim.sleep(expovariate(1))
        sems[(x+1)%total_procs].signal()
        
sim = simulus.simulator()

total_procs = 10
sems = [sim.semaphore() for _ in range(total_procs)]
for i in range(10):
    sim.process(waits,i)
sems[0].signal()
sim.run(20)