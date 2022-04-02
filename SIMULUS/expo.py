"""
Expovariate method returns a random floating number.
"""

import random

print(random.expovariate(-953))

"""
Seed method - Initialize the random number generator.
"""

random.seed(10)
print(random.random())

"""
Gauss method - returns random floating number with guassian distribution.
"""

mu = 100
sigma = 50

print(random.gauss(mu, sigma))