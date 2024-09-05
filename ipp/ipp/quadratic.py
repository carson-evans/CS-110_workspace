# Accepts a (float), b (float), and c (float) as command-line arguments; and writes the two roots
# of the quadratic equation ax^2 + bx + c = 0 to standard output.

import math
import stdio
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
discriminant = b * b - 4 * a * c
root1 = (-b + math.sqrt(discriminant)) / (2 * a)
root2 = (-b - math.sqrt(discriminant)) / (2 * a)
stdio.writeln("Root # 1 = " + str(root1))
stdio.writeln("Root # 2 = " + str(root2))
