# Accepts n (int), p (float), and trials (int) as command-line arguments; performs trials
# experiments, each of which counts the number of heads found when a coin with bias p is
# flipped n times; and draws the results using standard draw.

from histogram import Histogram
import stddraw
import stdrandom
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    histogram = Histogram(n + 1)
    for t in range(trials):
        heads = stdrandom.binomial(n, p)
        histogram.addDataPoint(heads)
    stddraw.setCanvasSize(500, 200)
    histogram.draw()
    stddraw.show()


if __name__ == "__main__":
    main()
