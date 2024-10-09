import math
import stdio
import sys

...

n = int(sys.argv[1])

# create empty list x
x = []

# for each i ∈ [0, n)
#append to x a float read from standard input using stdio.readFloat()
for i in range (0, n):
    x.append(float(stdio.readFloat()))

# create a list y of floats similar to x
y = []
for i in range (0, n):
    y.append(float(stdio.readFloat()))

# set distance to 0.0
distance = 0.0

# for each i ∈ [0, n)
# increment distance by (x[i] - y[i])^2
for i in range(0, n):
    distance += (x[i] - y[i]) ** 2

stdio.write(math.sqrt(distance))