# A library of Gaussian functions.

import math
import stdio
import sys


# Returns the value of the Gaussian probability density function with mean mu and standard
# deviation sigma at the given x value.
def pdf(x, mu=0.0, sigma=1.0):
    z = (x - mu) / sigma
    return _pdf(z) / sigma


# Returns the value of the Gaussian cumulative distribution function with mean mu and standard
# deviation sigma at the given x value.
def cdf(x, mu=0.0, sigma=1.0):
    z = (x - mu) / sigma
    return _cdf(z)


# Returns the value of the Gaussian probability density function with mean 0 and standard
# deviation 1 at the given z value.
def _pdf(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


# Returns the value of the Gaussian cumulative distribution function with mean 0 and standard
# deviation 1 at the given z value.
def _cdf(z):
    if z < -8.0:
        return 0.0
    if z > +8.0:
        return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / i
        i += 2
    return 1 / 2 + total * _pdf(z)


# Unit tests the library.
def _main():
    x = float(sys.argv[1])
    mu = float(sys.argv[2])
    sigma = float(sys.argv[3])
    stdio.writeln(pdf(x, mu, sigma))
    stdio.writeln(cdf(x, mu, sigma))


if __name__ == "__main__":
    _main()
