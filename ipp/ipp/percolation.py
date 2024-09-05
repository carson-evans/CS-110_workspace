# A library of percolation functions.

import stdio
import stdarray


# Computes and returns the full sites of the given percolation system.
def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    return isFull


# Given the full sites of a percolation system, returns True if the system percolates, and False
# otherwise.
def percolates(isFull):
    n = len(isFull)
    for j in range(n):
        if isFull[n - 1][j]:
            return True
    return False


# Given the open and full sites of a percolation system, updates the full sites by marking every
# site of that system that is open and reachable from site (i, j).
def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    if i < 0 or i >= n or j < 0 or j >= n or not isOpen[i][j] or isFull[i][j]:
        return
    isFull[i][j] = True
    _flow(isOpen, isFull, i + 1, j)
    _flow(isOpen, isFull, i, j + 1)
    _flow(isOpen, isFull, i, j - 1)
    _flow(isOpen, isFull, i - 1, j)


# Unit tests the library.
def _main():
    isOpen = stdarray.readBool2D()
    isFull = flow(isOpen)
    stdarray.write2D(isFull)
    stdio.writeln(percolates(isFull))


if __name__ == "__main__":
    _main()
