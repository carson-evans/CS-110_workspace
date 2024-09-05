# Accepts k (int) as command-line argument and words from standard input; computes the number of
# times each word appears; writes to standard output the k most frequent words in reverse
# order of their frequencies; and draws using standard draw the corresponding histogram
# demonstrating Zipf's law (ie, the power-law relationship between word frequencies and their
# ranks).

from counter import Counter
from histogram import Histogram
import merge
import stddraw
import stdio
import sys


# Entry point.
def main():
    k = int(sys.argv[1])
    words = stdio.readAllStrings()
    merge.sort(words)
    counters = []
    for i in range(len(words)):
        if (i == 0) or (words[i] != words[i - 1]):
            entry = Counter(words[i])
            counters += [entry]
        counters[len(counters) - 1].increment()
    merge.sort(counters)
    histogram = Histogram(k)
    for i in range(k):
        counter = counters[len(counters) - i - 1]
        stdio.writeln(counter)
        for j in range(counter.tally()):
            histogram.addDataPoint(i)
    histogram.draw()
    stddraw.show()


if __name__ == "__main__":
    main()
