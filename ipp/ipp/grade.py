# Accepts a percentage score (float) as command-line argument; and writes the corresponding
# letter grade to standard output.

import stdio
import sys

score = float(sys.argv[1])
if score >= 93:
    stdio.writeln("A")
elif score >= 90:
    stdio.writeln("A-")
elif score >= 87:
    stdio.writeln("B+")
elif score >= 83:
    stdio.writeln("B")
elif score >= 80:
    stdio.writeln("B-")
elif score >= 77:
    stdio.writeln("C+")
elif score >= 73:
    stdio.writeln("C")
elif score >= 70:
    stdio.writeln("C-")
elif score >= 67:
    stdio.writeln("D+")
elif score >= 63:
    stdio.writeln("D")
elif score >= 60:
    stdio.writeln("D-")
else:
    stdio.writeln("F")
