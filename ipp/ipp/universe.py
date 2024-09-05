# A data type to represent a universe.

from body import Body
from instream import InStream
from vector import Vector
import stdarray
import stddraw
import sys


class Universe:
    # Constructs an n-body universe from the given file containing the number (n) of bodies,
    # their initial positions and velocities, and their masses.
    def __init__(self, filename):
        inStream = InStream(filename)
        n = inStream.readInt()
        radius = inStream.readFloat()
        stddraw.setXscale(-radius, +radius)
        stddraw.setYscale(-radius, +radius)
        self.bodies = stdarray.create1D(n, None)  # list of n bodies
        for i in range(n):
            rx = inStream.readFloat()
            ry = inStream.readFloat()
            vx = inStream.readFloat()
            vy = inStream.readFloat()
            mass = inStream.readFloat()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self.bodies[i] = Body(r, v, mass)

    # Updates the state of this universe to what it would be after the given time period.
    def increaseTime(self, dt):
        n = len(self.bodies)
        f = stdarray.create1D(n, Vector([0, 0]))
        for i in range(n):
            for j in range(n):
                if i != j:
                    f[i] += self.bodies[i].forceFrom(self.bodies[j])
        for i in range(n):
            self.bodies[i].move(f[i], dt)

    # Draws this universe to standard draw.
    def draw(self):
        for body in self.bodies:
            body.draw()

    # Returns a string representation of this object.
    def __str__(self):
        s = ""
        for body in self.bodies:
            s += str(body) + ", "
        s = "[" + s[:-2] + "]" if len(self.bodies) > 0 else "[]"
        return s


# Unit tests the data type.
def _main():
    filename = sys.argv[1]
    universe = Universe(filename)
    universe.draw()
    stddraw.show(1000)
    universe.increaseTime(1000000)
    universe.draw()
    stddraw.show()


if __name__ == "__main__":
    _main()
