# Accepts n (int) as command-line argument, a 1-by-m vector (probabilities) and two m-by-3
# matrices (coefficients for updating x and y, respectively) from standard input; and plots the
# results as a set of n points using standard output.

import matrix
import stdarray
import stddraw
import stdrandom
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    dist = stdarray.readFloat1D()
    cx = stdarray.readFloat2D()
    cy = stdarray.readFloat2D()
    x, y = 0.0, 0.0
    stddraw.setPenRadius(0.0)
    for i in range(n):
        r = stdrandom.discrete(dist)
        col = [x, y, 1]
        x0 = matrix.dot(matrix.row(cx, r), col)
        y0 = matrix.dot(matrix.row(cy, r), col)
        x = x0
        y = y0
        stddraw.point(x, y)
    stddraw.show()


if __name__ == "__main__":
    main()
