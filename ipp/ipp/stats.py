# Accepts a sequence of floats from standard input; and writes their mean and standard deviation
# to standard output.

from bag import Bag
import math
import stdio


# Entry point.
def main():
    bag = Bag()
    while not stdio.isEmpty():
        bag.add(stdio.readFloat())
    n = len(bag)
    sum = 0.0
    for x in bag:
        sum += x
    mean = sum / n
    sum = 0.0
    for x in bag:
        sum += (x - mean) * (x - mean)
    stddev = math.sqrt(sum / (n - 1))
    stdio.writef("Mean:    %.2f\n", mean)
    stdio.writef("Std dev: %.2f\n", stddev)


if __name__ == "__main__":
    main()
