# A data type to represent an individual body in the n-body system.

from vector import Vector
import stddraw


class Body:
    # Constructs a body given its initial position and velocity, and mass.
    def __init__(self, r, v, mass):
        self._r = r  # current position of the body
        self._v = v  # current velocity of the body
        self._mass = mass  # mass of the body

    # Updates the velocity and position of this body based on a force acting on it for a time
    # period.
    def move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v += a.scale(dt)
        self._r += self._v.scale(dt)

    # Returns the force on this body due to the other body.
    def forceFrom(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    # Draws this body on standard draw.
    def draw(self):
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0], self._r[1])

    # Returns a string representation of this object.
    def __str__(self):
        return "(" + str(self._r) + ", " + str(self._v) + ", " + str(self._mass) + ")"


# Unit tests the data type.
def _main():
    stddraw.setXscale(-5.0e10, 5.0e10)
    stddraw.setYscale(-5.0e10, 5.0e10)
    aRCoords = [0.0e00, 4.5e10]
    aVCoords = [1.0e04, 0.0e00]
    bRCoords = [0.0e00, -4.5e10]
    bVCoords = [-1.0e04, 0.0e00]
    a = Body(Vector(aRCoords), Vector(aVCoords), 1.5e30)
    b = Body(Vector(bRCoords), Vector(bVCoords), 1.5e30)
    a.draw()
    b.draw()
    stddraw.show(1000)
    fab = a.forceFrom(b)
    fba = b.forceFrom(a)
    a.move(fab, 1000000)
    b.move(fba, 1000000)
    a.draw()
    b.draw()
    stddraw.show()


if __name__ == "__main__":
    _main()
