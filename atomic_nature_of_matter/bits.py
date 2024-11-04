import stdio
import sys


# Entry point. [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writef("zeros = %d, ones = %d, total = %d\n", _zeros(s), _ones(s), len(s))


# Return the number of zeros in s.
def _zeros(s):
    ...


# Return the number of ones in s.
def _ones(s):
    ...


if __name__ == "__main__":
    main()
