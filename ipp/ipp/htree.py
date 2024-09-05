# Accepts n (int) as a command-line argument; and draws using standard draw a level n H-tree
# centered at (0.5, 0.5) with lines of length 0.5.

import stddraw
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    stddraw.setPenRadius(0.0)
    _draw(n, 0.5, 0.5, 0.5)
    stddraw.show()


# Draws to standard draw a level n H-tree centered at (x, y) with lines of length lineLength.
def _draw(n, lineLength, x, y):
    if n == 0:
        return
    x0 = x - lineLength / 2
    x1 = x + lineLength / 2
    y0 = y - lineLength / 2
    y1 = y + lineLength / 2
    stddraw.line(x0, y, x1, y)
    stddraw.line(x0, y0, x0, y1)
    stddraw.line(x1, y0, x1, y1)
    _draw(n - 1, lineLength / 2, x0, y0)
    _draw(n - 1, lineLength / 2, x0, y1)
    _draw(n - 1, lineLength / 2, x1, y0)
    _draw(n - 1, lineLength / 2, x1, y1)


if __name__ == "__main__":
    main()
