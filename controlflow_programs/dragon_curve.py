import stdio
import sys

...

# F means "draw a line while moving forward 1 unit"

# L means "turn left"
# R means "turn right"

# curve of order n is a curve of order n-1
# followed by an L
# followed by a curve of order n-1
# traversed in reverse order
# replacing L wth R and R with L

# accept n (int) as cli and write directions for dragon

# Accept n as cli
n = int(sys.argv[1])
dragon = "F"
nogard = "F"

for i in range(n):
    # Create new dragon and nogard for the iteration
    new_dragon = dragon + "L" + nogard
    new_nogard = dragon + "R" + nogard
    # Update dragon and nogard for the next iteration
    dragon = new_dragon
    nogard = new_nogard

stdio.writeln(dragon)