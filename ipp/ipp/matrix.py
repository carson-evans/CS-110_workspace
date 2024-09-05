# A library of matrix functions.

import stdarray
import stdio


# Returns the ith row of matrix a.
def row(a, i):
    return a[i]


# Returns the jth column of matrix a.
def col(a, j):
    c = []
    for row in a:
        c += [row[j]]
    return c


# Returns the sum of the matrices a and b.
def add(a, b):
    m, n = len(a), len(a[0])
    c = stdarray.create2D(m, n, 0.0)
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c


# Returns the difference of matrices a and b.
def subtract(a, b):
    m, n = len(a), len(a[0])
    c = stdarray.create2D(m, n, 0.0)
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c


# Returns the product of matrices a and b.
def multiply(a, b):
    m, n = len(a), len(b[0])
    c = stdarray.create2D(m, n, 0.0)
    for i in range(m):
        for j in range(n):
            c[i][j] = dot(row(a, i), col(b, j))
    return c


# Returns the transpose of matrix a.
def transpose(a):
    m, n = len(a), len(a[0])
    c = stdarray.create2D(n, m, 0.0)
    for i in range(m):
        for j in range(n):
            c[j][i] = a[i][j]
    return c


# Returns the dot product of the 1-by-n matrices a and b.
def dot(a, b):
    total = 0.0
    for x, y in zip(a, b):
        total += x * y
    return total


# Unit tests the library.
def _main():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1], [2], [3]]
    stdio.writeln("a              = " + str(a))
    stdio.writeln("b              = " + str(b))
    stdio.writeln("row(a, 1)      = " + str(row(a, 1)))
    stdio.writeln("col(a, 1)      = " + str(col(a, 1)))
    stdio.writeln("add(a, a)      = " + str(add(a, a)))
    stdio.writeln("subtract(a, a) = " + str(subtract(a, a)))
    stdio.writeln("multiply(a, b) = " + str(multiply(a, b)))
    stdio.writeln("transpose(b)   = " + str(transpose(b)))


if __name__ == "__main__":
    _main()
