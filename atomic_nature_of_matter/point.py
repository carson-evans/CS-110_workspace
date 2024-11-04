import stdio


# A data type to represent a point in 2D space.
class Point:
    # Constructs a new point given its x and y coordinates.
    def __init__(self, x, y):
        ...

    # Returns the Euclidean distance between this point and other.
    def distanceTo(self, other):
        ...

    # Return a string representation of this point.
    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"


# Unit tests the data type [DO NOT EDIT].
def _main():
    p1 = Point(0, 1)
    p2 = Point(1, 0)
    stdio.writeln("p1        = " + str(p1))
    stdio.writeln("p2        = " + str(p2))
    stdio.writeln("d(p1, p2) = " + str(p1.distanceTo(p2)))


if __name__ == "__main__":
    _main()
