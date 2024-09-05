# An immutable data type to represent an n-dimensional vector.

import math
import stdarray
import stdio


class Vector:
    # Constructs a vector given its components.
    def __init__(self, a):
        self._n = len(a)  # dimension of vector
        self._coords = a[:]  # defensive copy of array of components

    # Returns the ith component of this vector.
    def __getitem__(self, i):
        return self._coords[i]

    # Returns the sum of this and the other vector.
    def __add__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self[i] + other[i]
        return Vector(result)

    # Returns the difference of this and the other vector.
    def __sub__(self, other):
        return self + other.scale(-1)

    # Returns the dot product of this and the other vector.
    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self[i] * other[i]
        return result

    # Returns a scaled (by factor alpha) copy of this vector.
    def scale(self, alpha):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = alpha * self[i]
        return Vector(result)

    # Returns a unit vector in the direction of this vector.
    def direction(self):
        return self.scale(1.0 / abs(self))

    # Returns the magnitude of this vector.
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Returns the dimension of this vector.
    def dimension(self):
        return self._n

    # Returns a string representation of this vector.
    def __str__(self):
        return str(self._coords)


# Unit tests the data type.
def _main():
    xCoords = [1.0, 2.0, 3.0, 4.0]
    yCoords = [5.0, 2.0, 4.0, 1.0]
    x = Vector(xCoords)
    y = Vector(yCoords)
    stdio.writeln("x       = " + str(x))
    stdio.writeln("y       = " + str(y))
    stdio.writeln("x + y   = " + str(x + y))
    stdio.writeln("x - y   = " + str(x - y))
    stdio.writeln("x dot y = " + str(x.dot(y)))
    stdio.writeln("10x     = " + str(x.scale(10.0)))
    stdio.writeln("xhat    = " + str(x.direction()))
    stdio.writeln("|x|     = " + str(abs(x)))
    stdio.writeln("ydim    = " + str(y.dimension()))


if __name__ == "__main__":
    _main()
