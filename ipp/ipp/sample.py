# Accepts m (int) and n (int) as command-line arguments; and writes to standard output a random
# sample of m integers in the range [0, n), with no duplicates.

import stdarray
import stdio
import stdrandom
import sys

m = int(sys.argv[1])
n = int(sys.argv[2])
perm = stdarray.create1D(n, 0)
for i in range(n):
    perm[i] = i
for i in range(m):
    r = stdrandom.uniformInt(i, n)
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp
for i in range(m):
    stdio.write(str(perm[i]) + " ")
stdio.writeln()
