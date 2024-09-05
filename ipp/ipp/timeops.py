# Accepts n (int) as command-line argument; computes the sum 1^0.5 + 2^0.5 + ... + n^0.5 using
# math.sqrt(x) and math.pow(x) to calculate the square root of x; and writes to standard output a
# comparison of the performance characteristics of the two functions.

from stopwatch import Stopwatch
import math
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    watch1 = Stopwatch()
    total = 0.0
    for i in range(1, n + 1):
        total += math.sqrt(i)
    time1 = watch1.elapsedTime()
    watch2 = Stopwatch()
    total = 0.0
    for i in range(1, n + 1):
        total += math.pow(i, 0.5)
    time2 = watch2.elapsedTime()
    stdio.writef("math.sqrt() is %.2f times faster than math.pow()\n", time2 / time1)


if __name__ == "__main__":
    main()
