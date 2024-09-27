import math
import stdio
import sys

...

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    sys.stdout.write("Value of a must not be 0\n")
else :
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0: # Check if discriminant is less than 0
        sys.stdout.write("Value of discriminant must not be negative\n")

    else :
        # Quadratic formula
        root1 = (-b + math.sqrt(discriminant)) // (2 * a)
        root2 = (-b - math.sqrt(discriminant)) // (2 * a)
        sys.stdout.write(f"{root1} {root2}\n")