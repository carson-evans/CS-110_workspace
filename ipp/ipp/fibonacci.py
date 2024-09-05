# Accepts n (int) as command-line argument; and writes the nth Fibonacci number to standard output.

import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    stdio.writeln(_fibonacci(n))


# Returns the nth Fibonacci number computed recursively.
def _fibonacci(n):
    if n < 2:
        return n
    return _fibonacci(n - 1) + _fibonacci(n - 2)


if __name__ == "__main__":
    main()
