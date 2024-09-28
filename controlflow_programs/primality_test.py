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

# Check for divisibility from 2 to sqrt(n)
is_prime = True
for i in range(2, n // 2 + 1):
    if n & i == 0:
        is_prime = False
        break

# out
if is_prime:
    stdio.writeln("True")
else:
    stdio.writeln("False")