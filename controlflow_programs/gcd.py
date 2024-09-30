import stdio
import sys

...

p = int(sys.argv[1])
q = int(sys.argv[2])

# Euclid's
while q != 0:
    p, q = q, p % q

stdio.writeln(p)