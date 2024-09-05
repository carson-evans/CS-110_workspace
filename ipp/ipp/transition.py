# Accepts links from standard input; and writes the corresponding transition matrix to standard
# output, computed using the 90-10 rule.

import stdarray
import stdio

n = stdio.readInt()
outDegrees = stdarray.create1D(n, 0)
linkCounts = stdarray.create2D(n, n, 0)
while not stdio.isEmpty():
    i = stdio.readInt()
    j = stdio.readInt()
    outDegrees[i] += 1
    linkCounts[i][j] += 1
stdio.writeln(str(n) + " " + str(n))
for i in range(n):
    for j in range(n):
        p = 0.9 * linkCounts[i][j] / outDegrees[i] + 0.1 / n
        stdio.writef("%8.5f", p)
    stdio.writeln()
