import math
import stdio
import sys

...

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

discriminant = float(b ** 2) - (4 * a * c)

if a == 0:
    stdio.writeln("Value of a must not be 0")
    sys.exit()

if discriminant < 0: # Check if discriminant is less than 0
    stdio.writeln("Value of discriminant must not be negative")
    sys.exit()

else:
    # Quadratic formula
    root1 = float((-b + math.sqrt(discriminant))) // (2 * a)
    root2 = float((-b - math.sqrt(discriminant))) // (2 * a)
    stdio.write(root1)
    stdio.write(" ")
    stdio.write(root2)