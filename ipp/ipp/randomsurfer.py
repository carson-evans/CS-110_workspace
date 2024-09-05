# Accepts moves (int) as command-line argument and a transition matrix from standard input;
# performs moves transitions as prescribed by the transition matrix; and writes the relative
# frequency of hitting each page to standard output.

import stdarray
import stdio
import stdrandom
import sys

moves = int(sys.argv[1])
transitionMatrix = stdarray.readFloat2D()
n = len(transitionMatrix)
hits = stdarray.create1D(n, 0)
page = 0
for m in range(moves):
    page = stdrandom.discrete(transitionMatrix[page])
    hits[page] += 1
for hit in hits:
    stdio.writef("%8.5f", hit / moves)
stdio.writeln()
