# Accepts n (int) as command-line argument; and writes to standard output a table where entry
# (i, j) is a "*" if j divides i or i divides j and a " " otherwise.

import stdio
import sys

n = int(sys.argv[1])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % j == 0 or j % i == 0:
            stdio.write("* ")
        else:
            stdio.write("  ")
    stdio.writeln(i)
