import stdio
import sys

...

p = int(sys.argv[1])
q = int(sys.argv[1])

while q:
    temp = q
    q = p % q
    p = temp

stdio.write(f"{p}\n")