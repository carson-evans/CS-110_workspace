# Accepts n (int) as command-line argument; and writes to standard output a table of powers of 2
# that are less than or equal to 2^n.

import stdio
import sys

n = int(sys.argv[1])
power = 1
for i in range(n + 1):
    stdio.writeln(str(i) + " " + str(power))
    power *= 2
