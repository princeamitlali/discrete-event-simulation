import simulus

"""
This concept needs some understanding with a real time example
"""
def traps(x):
    if x > 0:
        print("p%d starts at %g and waits on trap" %(x,sim.now))
        t.wait()
        print("p%d resumes at %g" %(x,sim.now))
    else:
        print("p%d starts at %g" %(x,sim.now))
        sim.sleep(5)
        print("p%d triggers the trap at %g" %(x,sim.now))
        t.trigger()

sim = simulus.simulator()
t = sim.trap()
for i in range(5):
    sim.process(traps, i, offset=1+i)
sim.run()