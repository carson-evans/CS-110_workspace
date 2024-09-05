# Accepts n (int) as command-line argument; and writes n! to standard output.

import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    stdio.writeln(_factorial(n))


# Returns n! computed recursively.
def _factorial(n):
    if n == 0:
        return 1
    return n * _factorial(n - 1)


if __name__ == "__main__":
    main()
