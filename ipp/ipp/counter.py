# A comparable data type to represent a counter.

import stdarray
import stdio
import stdrandom
import sys


class Counter:
    # Initializes a new counter with the given id.
    def __init__(self, id):
        self._id = id  # counter name
        self._count = 0  # current value

    # Increments this counter by 1.
    def increment(self):
        self._count += 1

    # Returns the current value of this counter.
    def tally(self):
        return self._count

    # Resets this counter to zero.
    def reset(self):
        self._count = 0

    # Returns True if this counter is less than the other counter by count, and False otherwise.
    def __lt__(self, other):
        return self.tally() < other.tally()

    # Returns True if this and the other counter have the same count, and False otherwise.
    def __eq__(self, other):
        return self.tally() == other.tally()

    # Returns a string representation of this counter.
    def __str__(self):
        return str(self.tally()) + " " + self._id


# Unit tests the data type.
def _main():
    n = int(sys.argv[1])
    trials = int(sys.argv[2])
    counters = stdarray.create1D(n, None)
    for i in range(n):
        counters[i] = Counter("counter " + str(i))
    for i in range(trials):
        counters[stdrandom.uniformInt(0, n)].increment()
    for counter in sorted(counters):
        stdio.writeln(counter)


if __name__ == "__main__":
    _main()
