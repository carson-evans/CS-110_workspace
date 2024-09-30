import stdio
import sys

...

n = int(sys.argv[1])

factorial = 1 # init

# loop through
for i in range(1, n + 1):
    factorial *= i

stdio.writeln(str(factorial))