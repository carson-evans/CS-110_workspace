# A library of percolation support functions.

import stdarray
import stddraw
import stdrandom
import sys


# Returns an n-by-n percolation system with vacancy probability p.
def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a


# Draws the percolation system a to standard draw. Parameter which indicates whether to display
# the entries corresponding to True or to False.
def draw(a, which):
    n = len(a)
    stddraw.setXscale(-1, n)
    stddraw.setYscale(-1, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n - i - 1, 0.5)


# Unit tests the library.
def _main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    isOpen = random(n, p)
    draw(isOpen, False)
    stddraw.show()


if __name__ == "__main__":
    _main()
