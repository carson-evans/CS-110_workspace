import stdio
import sys

...

n = int(sys.argv[1])

for k in range(2, n+1):
    sum_divisors = 0
    # Find all proper divisors of k
    for i in range(1, k // 2 + 1):
        if k % i == 0:
            sum_divisors += i
    # Check if k is perfect
    if sum_divisors == k:
        stdio.writeln(k)