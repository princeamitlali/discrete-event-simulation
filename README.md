# discrete-event-simulation
Discrete event simulation (DES) is a method used to model real world systems that can be decomposed into a set of logically separate processes that autonomously progress through time. Each event occurs on a specific process, and is assigned a logical time (a timestamp).

Some Famous Models used for Simulation using Python are:-

1. Simpy

2. Simulus

3. CIW 

## Simpy
#### [Simpy Documentation](https://simpy.readthedocs.io/en/latest/contents.html)

SimPy is a process-based discrete-event simulation framework based on standard Python.

Processes in SimPy are defined by Python generator functions and may, for example, be used to model active components like customers, vehicles or agents. SimPy also provides various types of shared resources to model limited capacity congestion points (like servers, checkout counters and tunnels).

Simulations can be performed “as fast as possible”, in real time (wall clock time) or by manually stepping through the events.

Though it is theoretically possible to do continuous simulations with SimPy, it has no features that help you with that. On the other hand, SimPy is overkill for simulations with a fixed step size where your processes don’t interact with each other or with shared resources.



## Simulus 
#### [Simulus Documentation ](https://simulus.readthedocs.io/en/latest/tutorial-howdoesitwork.html)

Simulus is a process-oriented discrete-event simulator written in Python. What it means is that in addition to describing the world as a sequence of events, one can also model it using processes. . Simulus provides the needed support for creating and managing the processes, and having them coordinate with one another, so as to make it easier for you to model the complexed interactions and procedures in this world.


## CIW
#### [CIW Documentation](https://ciw.readthedocs.io/en/latest/index.html)

Ciw is a discrete event simulation library for open queueing networks. Its core features include the capability to simulate networks of queues, multiple customer classes, and implementation of Type I blocking for restricted networks. A number of other features are also implemented, including priorities, baulking, schedules, and deadlock detection.

Ciw is currently supported for and regularly tested on Python versions 3.6, 3.7 and 3.8.

## File Structure
```

```



https://www.flexsim.com/warehousing-simulation/


