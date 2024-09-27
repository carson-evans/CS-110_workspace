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

n = int(sys.argv[1])

if n == 0:
    sys.stdout.write("F\n")
else:
    results = "F"
    for _ in range(n):
        result = result + "L" + result.replace("L", "X").replace("R", "L").replace("X", "R")
    sys.stdout.write(result + "\n")