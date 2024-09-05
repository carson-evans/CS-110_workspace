# Accepts n (int) as a command-line argument; and writes to standard output the number of coupons
# you collect before obtaining one of each of n types.

import stdarray
import stdio
import stdrandom
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    stdio.writeln(_collect(n))


# Collects coupons until getting one of each value in the range 0 to n - 1, and returns the
# number of coupons collected.
def _collect(n):
    count = 0
    collectedCount = 0
    isCollected = stdarray.create1D(n, False)
    while collectedCount < n:
        value = _getCoupon(n)
        count += 1
        if not isCollected[value]:
            collectedCount += 1
            isCollected[value] = True
    return count


# Returns a random coupon between 0 and n - 1.
def _getCoupon(n):
    return stdrandom.uniformInt(0, n)


if __name__ == "__main__":
    main()
