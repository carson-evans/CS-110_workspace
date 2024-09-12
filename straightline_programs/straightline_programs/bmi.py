import stdio
import sys

...

weight = float(sys.argv[1]) # Unit of measure is kg
height = float(sys.argv[2]) # Unit of measure is m

bmi = weight / (height ** 2) # Ratio of weight to square of the height

stdio.writeln(bmi)