import math
import stdio
import sys

...

lmbda = float(sys.argv[1]) # Lambda: avg num of events per unit of time
t = float(sys.argv[2]) # time

# Calc probability using exponent distribution
# p = e^−λt
p = math.exp(-lmbda * t)

print(p)