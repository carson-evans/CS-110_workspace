import stdio
import sys

...

n = int(sys.argv[1])

a, b = 0, 1

# iterate
for i in range(2, n + 1):
    a, b = b, a + b

stdio.writeln(b)