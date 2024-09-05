import math
import stdio
import stdrandom
import random
import sys

...

a = int(sys.argv[1])
b = int(sys.argv[2])

# Generate 3 random floats x1, x2, x3
# Each from interval [a, b)
x1 = random.uniform(a, b)
x2 = random.uniform(a, b)
x3 = random.uniform(a, b)

# Compute their mean
# mew = (x1 + x2 + x3) / 3
mew = (x1 + x2 + x3) / 3

# Variance
# var = ((x1 - mew)^2 + (x2 - mew)^2 + (x3 - mew)^2) / 3
var = ((x1 - mew) ** 2 + (x2 - mew) ** 2 + (x3 - mew) ** 2) / 3

# Standard deviation
std = math.sqrt(var)

print(f"{mew}, {var}, {std}")