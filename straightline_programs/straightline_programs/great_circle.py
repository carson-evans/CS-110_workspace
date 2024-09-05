import math
import stdio
import sys

...

x1 = float(sys.argv[1]) # longitude of point 1
y1 = float(sys.argv[2]) # latitude of point 1
x2 = float(sys.argv[3]) # longitude of point 2
y2 = float(sys.argv[4]) # latitude of point 2

earthRadius = 6359.83 # kilometers

# convert degrees to radians
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

# Formula
d = earthRadius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print(d)