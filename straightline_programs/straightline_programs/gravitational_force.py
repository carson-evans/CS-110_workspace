import stdio
import sys

...

# init vars
m1 = float(sys.argv[1]) # Mass in kg of obj 1
m2 = float(sys.argv[2]) # Mass in kg of obj 2
r = float(sys.argv[3]) # Distance in m between m1 and m2's centers
G = 6.674 * (10 ** -11) # (in m^3 kg^−1 s^−2) is the gravitational constant.

# Formula
f = G * ((m1 * m2)//(r ** 2)) # Gravitational force acting between two objs in newtons

print (f)