# Accepts n (int), lo (float), and hi (float) as command-line arguments; and writes to standard
# output n random floats in the range [lo, hi), each up to 2 decimal places.

import stdio
import stdrandom
import sys

n = int(sys.argv[1])
lo = float(sys.argv[2])
hi = float(sys.argv[3])
for i in range(n):
    r = stdrandom.uniformFloat(lo, hi)
    stdio.writef("%.2f\n", r)
