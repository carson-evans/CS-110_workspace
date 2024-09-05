# Accepts n (int) as command-line argument; and writes the number of primes <= n to standard output.

import stdarray
import stdio
import sys

n = int(sys.argv[1])
isPrime = stdarray.create1D(n + 1, False)
for i in range(2, n + 1):
    isPrime[i] = True
for i in range(2, n):
    if isPrime[i]:
        for j in range(2, n // i + 1):
            isPrime[i * j] = False
count = 0
for i in range(2, n + 1):
    count += 1 if isPrime[i] else 0
stdio.writeln(count)
