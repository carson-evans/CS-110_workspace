# A data type that represents histograms of the frequency of occurrence of values in [0, n).

import stdarray
import stddraw
import stdrandom
import stdstats
import sys


class Histogram:
    # Constructs a histogram to store frequency of occurrence of values [0, n).
    def __init__(self, n):
        self._freq = stdarray.create1D(n, 0)  # array of frequencies

    # Adds one occurrence of the value i.
    def addDataPoint(self, i):
        self._freq[i] += 1

    # Draws this histogram to standard draw.
    def draw(self):
        stddraw.setYscale(-1, max(self._freq) + 1)
        stdstats.plotBars(self._freq)


# Unit tests the data type.
def _main():
    trials = int(sys.argv[1])
    histogram = Histogram(6)
    for t in range(trials):
        roll = stdrandom.uniformInt(0, 6)
        histogram.addDataPoint(roll)
    stddraw.setCanvasSize(500, 200)
    histogram.draw()
    stddraw.show()


if __name__ == "__main__":
    _main()
