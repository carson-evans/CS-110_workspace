import stdio
import sys

...

n = int(sys.argv[1])

# check for edge case

if n <= 1:
    stdio.writeln("False")
    sys.exit()
if n == 2:
    stdio.writeln("True")
    sys.exit()

# Since cannot import math,
# Calc approx sqrt of n
i = 1
while i * i <= n:
    i += 1
sqrt_n = i-1 # approx sqrt

# Check for divisibility from 2 to sqrt(n)
is_prime = True
for i in range(2, sqrt_n + 1):
    if n % i == 0:
        is_prime = False
        break

# out
if is_prime:
    stdio.writeln("True")
else:
    stdio.writeln("False")