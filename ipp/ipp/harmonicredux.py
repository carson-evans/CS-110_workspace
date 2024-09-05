# Accepts n (int) as command-line argument; and writes the nth harmonic number (1 + 1/2 + ... +
# 1/n) to standard output.

import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    stdio.writeln(_harmonic(n))


# Returns the nth harmonic number.
def _harmonic(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1 / i
    return total


if __name__ == "__main__":
    main()
