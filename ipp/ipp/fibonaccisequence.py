# An iterable data type to iterate over the first n numbers from the Fibonacci sequence.

import stdio
import sys


class FibonacciSequence:
    # Constructs a FibonacciSequence object given the length of the sequence.
    def __init__(self, n):
        self._n = n  # length of the sequence

    # Returns a string representation of this object.
    def __str__(self):
        s = ""
        for v in self:
            s += str(v) + " "
        return s.strip()

    # Returns an iterator that iterates over the numbers in the Fibonacci sequence.
    def __iter__(self):
        return FibonacciSequence.FibonacciIterator(self._n)

    # An iterator that iterates over the numbers in the Fibonacci sequence.
    class FibonacciIterator:
        def __init__(self, n):
            self._n = n  # length of the sequence
            self._a = -1  # previous number in the sequence
            self._b = 1  # current number in the sequence
            self._count = 0  # count of numbers iterated so far

        # Returns the next number in the sequence if there is one, and raises StopIteration
        # otherwise.
        def __next__(self):
            if self._count == self._n:
                raise StopIteration()
            self._count += 1
            temp = self._a
            self._a = self._b
            self._b += temp
            return self._b


# Unit tests the data type.
def _main():
    n = int(sys.argv[1])
    fib = FibonacciSequence(n)
    stdio.writeln(fib)


if __name__ == "__main__":
    _main()
