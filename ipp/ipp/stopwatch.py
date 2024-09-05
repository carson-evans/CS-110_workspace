# An immutable data type to measure the running (wall clock) time of a program.

import stdio
import sys
import time


class Stopwatch:
    # Constructs a new stopwatch.
    def __init__(self):
        self._creationTime = time.time()  # creation time of stopwatch

    # Returns the elapsed time (in seconds) since creation.
    def elapsedTime(self):
        return time.time() - self._creationTime

    # Returns a string representation of this stopwatch.
    def __str__(self):
        return str(self._creationTime)


# Unit tests the data type.
def _main():
    n = int(sys.argv[1])
    watch = Stopwatch()
    primes = 0
    for i in range(2, n + 1):
        j = 2
        while j <= i / j:
            if i % j == 0:
                break
            j += 1
        if j > i / j:
            primes += 1
    t = watch.elapsedTime()
    stdio.writef("pi(%d) = %d computed in %.5f seconds\n", n, primes, t)


if __name__ == "__main__":
    _main()
