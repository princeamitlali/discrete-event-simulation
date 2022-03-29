import simulus

from random import seed, expovariate, gauss
seed(12345)

bufsiz = 5
items_produced = 0
items_consumed = 0
num_producers = 2
num_consumers = 3

def producer(x):
    global items_produced
    while True:
        sim.sleep(expovariate(1))
        num = items_produced
        items_produced += 1
        print("%f: p[%d] produces item [%d]" % (sim.now, x, num))
        sem_avail.wait()
        sem_occupy.signal()
        print("%f: p[%d] stores item [%d] in buffer" %(sim.now, x, num))

def consumer(x):
    global items_consumed
    while True:
        sem_occupy.wait()
        sem_avail.signal()
        num = items_consumed
        items_consumed += 1
        print("%f: c[%d] retrieves item [%d] from buffer" %(sim.now, x, num))
        sim.sleep(gauss(0.8,0.2))
        print("%f: c[%d] consumes item[%d]" %(sim.now, x, num))

sim = simulus.simulator()
sem_avail = sim.semaphore(bufsiz)
sem_occupy = sim.semaphore(0)
for i in range(num_producers):
    sim.process(producer, i)
for i in range(num_consumers):
    sim.process(consumer,i)
sim.run(5)