# Accepts mu (float) and sigma (float) as command-line arguments; and writes to standard output a
# table of the percentage of students scoring below certain scores on the SAT, assuming the test
# scores obey a Gaussian distribution with the given mean and standard deviation.

import gaussian
import stdio
import sys


# Entry point.
def main():
    mu = float(sys.argv[1])
    sigma = float(sys.argv[2])
    for score in range(400, 1600 + 1, 100):
        percentile = gaussian.cdf(score, mu, sigma)
        stdio.writef("%4d  %.4f\n", score, percentile)


if __name__ == "__main__":
    main()
