'''imports simulus for simulation and gmt and strftime for representing time for diffrent scenerios'''
import simulus
from time import gmtime, strftime
import random



def strnow():
    return strftime("%H:%M:%S", gmtime(sim.now))

def wake_up():
    print("professor wakes up at "+strnow())
    sim.sched(start_coffee, offset=5*60) # 5 minutes from now
    sim.sched(breakfast, offset=2*3600+30*60) # 2 hours and 30 minutes from now
    sim.sched(shower, offset=2*3600+50*60) # 2 hours and 50 minutes from now
    sim.sched(leave, offset=3*3600+30*60) # 3 hours and 30 minutes from now

def start_coffee():
    print("professor starts drinking coffee at "+strnow())
    sim.sched(finish_coffee, offset=15*60) # 15 minutes from now
    sim.sched(start_read, offset=5*60) # 5 minutes from now

def finish_coffee():
    print("professor finishes drinking coffee at "+strnow())

def start_read():
    print("professor starts reading at "+strnow())
    sim.sched(finish_read, offset=2*3600) # 2 hours from now

def finish_read():
    print("professor finishes reading at "+strnow())

def breakfast():
    print("professor breakfasts at "+strnow())

def shower():
    print("professor showers at "+strnow())


def leave():
    print("professor leaves home and drives to school at "+strnow())
    # e1 = sim.sched(meeting1, until=9*3600, repeat_intv=24*3600) # 9:00
    # e2 = sim.sched(meeting2, until=10*3600, repeat_intv=24*3600) # 10:00
    # cl = sim.sched(classes, until=11*3600, repeat_intv=24*3600)
    if bool(random.getrandbits(1)):
        print("true")
        sim.sched(arrive, offset=2*3600+45*60) # 2 hours and 45 minutes from now
        sim.cancel(e1)
        sim.resched(e2, offset= 3.5*3600) # 11:00
        sim.resched(cl, offset= 4.5*3600)
    else:
        print("false")
        sim.sched(arrive, offset=45*60) # 45 minutes from now
        sim.sched(meeting1,offset=90*60)
        sim.resched(e2,offset=150*60)
        sim.resched(cl,offset=210*60 )

def arrive():
    print("professor arrives at school at "+strnow())

def meeting1():
    print("professor has first meeting at "+strnow())

def meeting2():
    print("professor has second meeting at "+strnow())
    
def classes_start(num):
    print("professor started {} clss at {} ".format(num+1,strnow()))
    sim.sched(classes_end,offset=45*60)

def classes_end():
    print("Professor ended the class at "+strnow())
    
def lunch_break():
    print("professor is taking lunch at "+strnow())
    
def classes():
    for i in range(5):
        if i < 2:
            sim.sched(classes_start,i,offset=i*3600+10*60)
        if i ==2:
            sim.sched(lunch_break,offset=i*3600+10*60)
            sim.sched(classes_start,i,offset=i*3600+40*60)
        if i >2:
            sim.sched(classes_start,i,offset=i*3600+50*60)


sim = simulus.simulator()
sim.sched(wake_up, until=4*3600, repeat_intv=24*3600) # 4:00
e1 = sim.sched(meeting1, until=9*3600, repeat_intv=24*3600) # 9:00
e2 = sim.sched(meeting2, until=10*3600, repeat_intv=24*3600) # 10:00
cl = sim.sched(classes, until=11*3600, repeat_intv=24*3600)
sim.run(until=288*3600)