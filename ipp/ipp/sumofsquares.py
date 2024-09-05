# Accepts x (int) and y (int) as command-line arguments; and writes the sum of their squares to
# standard output.

import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
result = x * x + y * y
stdio.writeln(result)
