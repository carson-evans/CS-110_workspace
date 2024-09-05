# Accepts y (int) as command-line argument representing a year; and writes to standard output
# whether the year is a leap year or not.

import stdio
import sys

y = int(sys.argv[1])
result = y % 4 == 0 and y % 100 != 0 or y % 400 == 0
stdio.writeln(result)
