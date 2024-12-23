import stdio
import sys

...

t = float(sys.argv[1]) # Temperature in Fahrenheit
v = float(sys.argv[2]) # Wind speed in miles per hour

# Wind chill formula
# w = 35.74 + 0.6215t + (0.4275t − 35.75)v^0.16

if t > 50 :
    stdio.writeln("Value of t must be <= 50 F")
    exit()
if v <= 3 :
    stdio.writeln("Value of v must be > 3 mph")
    exit()
else:
    w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * (v ** 0.16)
    stdio.writeln(w)