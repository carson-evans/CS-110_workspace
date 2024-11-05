import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    n = int(sys.argv[1])
    stdio.writeln(_sumOfInts(n))


# Returns the sum 1 + 2 + ... + n.
def _sumOfInts(n):
    """
    :param n:
    :return sum of integers n - 1:
    """

    # Base case
    if n == 1:
        return 1

    # S(n) = n + S(n - 1)
    if n > 1:
        return n + _sumOfInts(n - 1)

if __name__ == "__main__":
    main()
