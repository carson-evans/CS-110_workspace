import stdio
import sys

from ipp.ipp.factors import factor

...

n = int(sys.argv[1])

# n! = 1 * 2 * ... (n-1) * n
# where n != 1

factorial = 1 # init

# loop through
for i in range(1, n+1):
    factorial *= i

stdio.writeln(factorial)