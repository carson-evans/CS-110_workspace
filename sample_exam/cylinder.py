import math
import stdio
import sys
...

r = float(sys.argv[1]) # radius
h = float(sys.argv[2]) # height

# a = 2πr(r + h) and v = πr2h.

a = 2 * math.pi * r * ( r + h)
v = math.pi * r * 2 * h

stdio.write("Area = ")
stdio.write(a)

stdio.writeln("")

stdio.write("Volume = ")
stdio.write(v)