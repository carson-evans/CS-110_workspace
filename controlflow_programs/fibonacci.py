import stdio
import sys

...

n = int(sys.argv[1])
result = 1

for i in range(1, n+1):
    result *= i

sys.stdout.write(f"{result}\n")