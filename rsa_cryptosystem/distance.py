import math
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    n = int(sys.argv[1])
    x, y = [], []
    for i in range(n):
        x += [stdio.readFloat()]
    for i in range(n):
        y += [stdio.readFloat()]
    stdio.writeln(_distance(x, y))


def _distance(x, y):
    ...
    # returns the euclidean distance between the vectors x and y
    # represented as one dimensional list of floats

    # calculated as square root of the sum of squares of the differences
    # between the corresponding entries

    n = len(x) # set n to num of elements in x
    d = 0.0 # distance

    # for each i in [0,n):
        # increment d by (x[i] - y[i])^2
    for i in range (n):
        d += (x[i] - y[i]) ** 2

    return math.sqrt(d)


if __name__ == "__main__":
    main()
