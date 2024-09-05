# Accepts n (int) as command-line argument; and writes the prime factors of n to standard output.

import stdio
import sys

n = int(sys.argv[1])
factor = 2
while factor * factor <= n:
    while n % factor == 0:
        stdio.write(str(factor) + " ")
        n //= factor
    factor += 1
if n > 1:
    stdio.write(n)
stdio.writeln()
