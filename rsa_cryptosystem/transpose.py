from array import array

import stdarray
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    a = stdarray.create2D(m, n)
    for i in range(m):
        for j in range(n):
            a[i][j] = stdio.readFloat()
    c = _transpose(a)
    for row in c:
        for v in row:
            stdio.write(str(v) + " ")
        stdio.writeln()


# Returns the transpose of a.
def _transpose(a):
    ...

    # creates and returns a new matrix
    # that is the transpose of the matrix represented by arg a

    # note that a need not have the same num of row and col
    # recall transpose of m by n matrix a is an n by m matrix b
    # such that B[i][j] = A[j][i]
    # where 0 <= i < n and 0 <= j < m

    # set m to the num of rows in a and n to num of col in a
    m, n = len(a), len(a[0])

    # set c to a 2d list of dimensions x by m
    c = stdarray.create2D(n, m, 0.0)

    # for each i in [0, n)
        # for each j in [0, m)
            # set c[i][j] to a[j][i] # CR for correct transpose
    # return c

    for i in range (n):
        for j in range (m):
            c[i][j] = a[j][i]
    return c

if __name__ == "__main__":
    main()
