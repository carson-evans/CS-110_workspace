# An immutable data type to represent a complex number using cartesian coordinates.

import math
import stdio


class Complex:
    # Constructs a complex number given its cartesian coordinates.
    def __init__(self, x=0.0, y=0.0):
        self._x = x  # the real part
        self._y = y  # the imaginary part

    # Returns the conjugate of this complex number.
    def conjugate(self):
        return Complex(self._x, -self._y)

    # Returns the sum of this and the other complex number.
    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Complex(x, y)

    # Returns the difference of this and the other complex number.
    def __sub__(self, other):
        x = self._x - other._x
        y = self._y - other._y
        return Complex(x, y)

    # Returns the product of this and the other complex number.
    def __mul__(self, other):
        x = self._x * other._x - self._y * other._y
        y = self._x * other._y + self._y * other._x
        return Complex(x, y)

    # Returns the magnitude of this complex number.
    def __abs__(self):
        return math.sqrt(self._x * self._x + self._y * self._y)

    # Returns True if this and other denote the same complex number, and False otherwise.
    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    # Returns a string representation of this complex number.
    def __str__(self):
        SUFFIX = "i"
        if self._y == 0:
            return str(self._x)
        elif self._x == 0:
            return str(self._y) + SUFFIX
        elif self._y < 0:
            return str(self._x) + " - " + str(-self._y) + SUFFIX
        else:
            return str(self._x) + " + " + str(self._y) + SUFFIX


# Unit tests the data type.
def _main():
    a = Complex(5.0, -6.0)
    b = Complex(3.0, 4.0)
    stdio.writeln("a       = " + str(a))
    stdio.writeln("b       = " + str(b))
    stdio.writeln("conj(a) = " + str((a.conjugate())))
    stdio.writeln("a + b   = " + str(a + b))
    stdio.writeln("a - b   = " + str(a - b))
    stdio.writeln("a * b   = " + str(a * b))
    stdio.writeln("|b|     = " + str(abs(b)))
    stdio.writeln("a == b  = " + str(a == b))


if __name__ == "__main__":
    _main()
