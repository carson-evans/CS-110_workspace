import math
import stdio
import sys

...

r = float(sys.argv[1]) # radius
theta_degrees = float(sys.argv[2]) # theta (angle in radians)

# Convert degrees to radians
theta_radians = math.radians(theta_degrees)

# x = r (cos(theta))
# y = r (sin(theta))

x = r * math.cos(theta_radians)
y = r * math.sin(theta_radians)

stdio.write(x)
stdio.write(" ")
stdio.write(y)