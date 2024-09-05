# Accepts d (str), m (str), and y (str) representing a date as command-line arguments; and writes
# the date in different formats to standard output.

import stdio
import sys

d = sys.argv[1]
m = sys.argv[2]
y = sys.argv[3]
dmy = d + "/" + m + "/" + y
mdy = m + "/" + d + "/" + y
ymd = y + "/" + m + "/" + d
stdio.writeln(dmy)
stdio.writeln(mdy)
stdio.writeln(ymd)
