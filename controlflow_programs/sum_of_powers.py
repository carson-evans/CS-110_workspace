import stdio
import sys

...

n = int(sys.argv[1]) # upper limit
k = int(sys.argv[2]) # power to raise

# S(n,k) = 1^k + 2^k + ... + n^k

sum_of_powers = 0 # init

# loop through each number from 1 to n
for i in range(1, n+1):
    sum_of_powers += i ** k

# out
stdio.writeln(sum_of_powers)