# Accepts n (int) as command-line argument; and writes n Hellos to standard output.

import stdio
import sys

n = int(sys.argv[1])
i = 1
while i <= n:
    stdio.writeln("Hello # " + str(i))
    i += 1
