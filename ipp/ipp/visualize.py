# Accepts n (int), p (float), and trials (int) as command-line arguments; generates an n-by-n
# random percolation system with vacancy probability p; computes the directed percolation flow;
# and draws the result trials times using standard draw.

import percolation
import percolationio
import stddraw
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    for i in range(trials):
        isOpen = percolationio.random(n, p)
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        percolationio.draw(isOpen, False)
        stddraw.setPenColor(stddraw.BLUE)
        isFull = percolation.flow(isOpen)
        percolationio.draw(isFull, True)
        stddraw.show(1000)
    stddraw.show()


if __name__ == "__main__":
    main()
