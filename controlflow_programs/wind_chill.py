import stdio
import sys

...

t = float(sys.argv[1]) # Temperature in Fahrenheit
v = float(sys.argv[2]) # Wind speed in miles per hour

# Wind chill formula
# w = 35.74 + 0.6215t + (0.4275t − 35.75)v^0.16

if t > 50 :
    sys.stdout.write("Value of t must be ≤ 50 F")
if v <= 3 :
    sys.stdout.write("Value of v must be > 3 mph")
else :
    w = 35.74 + 0.6214 * t + (0.4275 * t - 35.75) * v ** 0.16
    sys.stdout.write(f"{w}\n")