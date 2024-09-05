import stdio
import sys

...
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

maximum = (max(x,y,z)) # Find maximum
minimum = (min(x,y,z)) # Find minimum
middle = (x + y + z - minimum - maximum) # Find median

print(minimum, middle, maximum)