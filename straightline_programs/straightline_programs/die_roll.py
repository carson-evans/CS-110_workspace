import stdio
import stdrandom
import sys

...

n = int(sys.argv[1]) # Get number of sides of die

# Roll twice using stdrandom, generate random ints between 1 and n
roll1 = stdrandom.uniformInt(1, n+1)
roll2 = stdrandom.uniformInt(1, n+1)

# Compute sum of the two
total = roll1 + roll2

stdio.writeln(total)