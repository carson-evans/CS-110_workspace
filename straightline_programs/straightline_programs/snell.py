import math
import stdio
import sys

...

theta_1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# covert theta 1 from deg to rad
theta_1_rad = math.radians(theta_1)

# Snells law to calculate sin theta_2
# Algebra to get sin theta 2 alone is multiply n2/n1 by sin theta 0 and flip the fraction
sin_theta_2 = (n1 / n2) * math.sin(theta_1_rad)

# calculate theta 2 in radians and convert back to degrees
theta_2_rad = math.asin(sin_theta_2)
theta_2 = math.degrees(theta_2_rad)

stdio.writeln(theta_2)