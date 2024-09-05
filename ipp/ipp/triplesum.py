# Accepts a filename as command-line argument; reads the integers in the file; and writes to
# standard output the number of unordered triples (x, y, z) such that x + y + z = 0.

from instream import InStream
import stdio
import sys


# Entry point.
def main():
    inStream = InStream(sys.argv[1])
    a = inStream.readAllInts()
    stdio.writeln(_count(a))


# Returns the number of triples(i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0.
def _count(a):
    n = len(a)
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] == 0:
                    count += 1
    return count


if __name__ == "__main__":
    main()
