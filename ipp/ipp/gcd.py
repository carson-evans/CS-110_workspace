# Accepts p (int) and q (int) as command-line arguments; and writes gcd(p, q) to standard output.

import stdio
import sys


# Entry point.
def main():
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    stdio.writeln(_gcd(p, q))


# Returns the gcd of p and q computed recursively using Euclid's algorithm.
def _gcd(p, q):
    if q == 0:
        return p
    return _gcd(q, p % q)


if __name__ == "__main__":
    main()
