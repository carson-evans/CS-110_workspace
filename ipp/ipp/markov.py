# Accepts moves (int) as command-line argument and a transition matrix from standard input;
# computes the probabilities that a random surfer lands on each page (page ranks) after moves
# matrix-vector multiplications; and writes the page ranks to standard output.

import stdarray
import stdio
import sys

moves = int(sys.argv[1])
transitionMatrix = stdarray.readFloat2D()
n = len(transitionMatrix)
ranks = stdarray.create1D(n, 0.0)
ranks[0] = 1.0
for m in range(moves):
    newRanks = stdarray.create1D(n, 0.0)
    for j in range(n):
        for i in range(n):
            newRanks[j] += ranks[i] * transitionMatrix[i][j]
    ranks = newRanks
for rank in ranks:
    stdio.writef("%8.5f", rank)
stdio.writeln()
