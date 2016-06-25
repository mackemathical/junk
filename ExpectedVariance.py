# The definition of expected variance of a random variable is the expected value of the square of the difference of the variable X
# and the expected value of the variable (or E((X-E(X))^2) written more compactly). This is equivalent to
# the difference between the expected value of the squared variable and the square of the expected value (E(X^2)-(E(X))^2). I 
# couldn't convince myself that this could be the case, so I wrote this quick script. For a die roll, the expected value is 3.5,
# so the variance can be calculated at about 2.917. My code approximates it at 2.916. Now I'm convinced!

import numpy as np

np.random.seed(0)
tot = 0
n = 10000000
for i in range(n):
    r = np.random.random()
    if r < 1/6:
        roll = 1
    elif r < 2/6:
        roll = 2
    elif r < 3/6:
        roll = 3
    elif r < 4/6:
        roll = 4
    elif r < 5/6:
        roll = 5
    else:
        roll = 6
    tot += (roll - 3.5)**2

print(tot/n)
