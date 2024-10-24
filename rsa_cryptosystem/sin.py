import math
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    x = float(sys.argv[1])
    stdio.writeln(_sin(math.radians(x)))


# Returns sin(x) calculated using the formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def _sin(x):
    ...

    # set total to 0.0, term to 1.0, sign to 1, and i to 1
    total = 0.0
    term = 1.0
    sign = 1
    i = 1

    # As long as total is different from total + term
    while total != (total + term):
        # add x/i to term
        # if i is off, increment total by sign * term and
        # toggle sign
        # set to -1 if positive and +1 if negative
        # then increment i by 1

        term *= x/i

        if i % 2 != 0:
            total += sign * term
            sign *= -1

        i += 1

    return total


if __name__ == "__main__":
    main()
