import stdio

# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    def __init__(self):
        self._pixels = 0
        self._x_total = 0.0
        self._y_total = 0.0

    # Adds pixel (x, y) to this blob.
    def add(self, x, y):
        self._x_total += x
        self._y_total += y
        self._pixels += 1

    # Returns the mass of this blob, ie, the number of pixels in it.
    def mass(self):
        return self._pixels

    # Returns the Euclidean distance between the center of mass of this blob and the center of
    # mass of the other blob.
    def distanceTo(self, other):
        if self._pixels == 0 or other._pixels == 0:
            return float('inf')
        x1 = self._x_total / self._pixels
        y1 = self._y_total / self._pixels
        x2 = other._x_total / other._pixels
        y2 = other._y_total / other._pixels
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # Returns a string representation of this blob.
    def __str__(self):
        if self._pixels == 0:
            center_x = 0.0
            center_y = 0.0
        else:
            center_x = self._x_total / self._pixels
            center_y = self._y_total / self._pixels
        return "%d (%.4f, %.4f)" % (self._pixels, center_x, center_y)

# Unit tests the data type [DO NOT EDIT].
def _main():
    a = Blob()
    a.add(0, 0)
    b = Blob()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        b.add(x, y)
    stdio.writeln("a          = " + str(a))
    stdio.writeln("b          = " + str(b))
    stdio.writeln("dist(a, b) = " + str(a.distanceTo(b)))

if __name__ == "__main__":
    _main()
