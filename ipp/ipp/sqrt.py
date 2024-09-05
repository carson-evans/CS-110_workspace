# Accepts c (float) as command-line argument; and writes the square root of c to standard output,
# computed using Newton's method.

import stdio
import sys

c = float(sys.argv[1])
EPSILON = 1e-15
t = c
while abs(1 - c / (t * t)) > EPSILON:
    t = (c / t + t) / 2
stdio.writeln(t)
