# The types defined in this program provide a demonstration of subclassing inheritance in Python.

import math
import stdio


# Representation of an abstract shape.
class Shape:
    # Returns the area of this shape.
    def area(self):
        return math.nan


# Representation of a rectangle.
class Rectangle(Shape):
    # Constructs a rectangle given its width and height.
    def __init__(self, width, height):
        self._width = width  # width of the rectangle
        self._height = height  # height of the rectangle

    # Returns the area of this rectangle.
    def area(self):
        return self._width * self._height

    # Returns a string representation of this rectangle.
    def __str__(self):
        return "Rectangle(w = " + str(self._width) + ", h = " + str(self._height) + ")"


# Representation of a circle.
class Circle(Shape):
    # Constructs a circle given its radius.
    def __init__(self, radius):
        self._radius = radius  # radius of the circle

    # Returns the area of this circle.
    def area(self):
        return math.pi * self._radius ** 2

    # Returns a string representation of this circle.
    def __str__(self):
        return "Circle(r = " + str(self._radius) + ")"


# Unit tests the data types.
def _main():
    r = Rectangle(3, 4)
    c = Circle(5)
    stdio.writeln("r        = " + str(r))
    stdio.writeln("r.area() = " + str(r.area()))
    stdio.writeln("c        = " + str(c))
    stdio.writeln("c.area() = " + str(c.area()))


if __name__ == "__main__":
    _main()
