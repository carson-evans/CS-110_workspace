# An immutable data type that represents a profile of a string, as a d-dimensional unit vector.

from vector import Vector
import stdarray
import stdio
import sys


class Sketch:
    # Constructs a new sketch which is a profile of text, as a d-dimensional unit vector.
    # Component i of the vector indicates how many k-grams in the text hash to i.
    def __init__(self, text, k, d):
        freq = stdarray.create1D(d, 0)
        for i in range(len(text) - k + 1):
            kgram = text[i:i + k]
            h = Sketch._hash(kgram)
            freq[abs(h % d)] += 1
        vector = Vector(freq)
        self._sketch = vector.direction()  # string profile as a d-dimensional unit vector

    # Returns the similarity measure between this and the other sketch, as a number between 0 and 1.
    # The value 0 indicates that the sketches are dissimilar, and 1 indicates that they are similar.
    def similarTo(self, other):
        return self._sketch.dot(other._sketch)

    # Returns a string representation of this sketch.
    def __str__(self):
        return str(self._sketch)

    # Returns a hash of the given string. Unlike Python's hash(), this function is deterministic.
    def _hash(kgram):
        hash = 0
        for c in kgram:
            hash = 31 * hash + ord(c)
        return hash


# Unit tests the data type.
def _main():
    a = sys.argv[1]
    sketchA = Sketch(a, 2, 3)
    b = sys.argv[2]
    sketchB = Sketch(b, 2, 3)
    stdio.writeln("a                          = " + str(a))
    stdio.writeln("sketchA                    = " + str(sketchA))
    stdio.writeln("b                          = " + str(b))
    stdio.writeln("sketchB                    = " + str(sketchB))
    stdio.writeln("sketchA.similarTo(sketchB) = " + str(sketchA.similarTo(sketchB)))


if __name__ == "__main__":
    _main()
