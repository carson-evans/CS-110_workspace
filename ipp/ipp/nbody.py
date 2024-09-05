# Accepts filename (String) and dt (float) as command-line arguments; uses the file with that name,
# specifying the number (n) of bodies, their initial positions and velocities, and their masses,
# to create an n-body universe; and simulates the universe using dt as the time step.

from universe import Universe
import stddraw
import sys


# Entry point.
def main():
    filename = sys.argv[1]
    dt = float(sys.argv[2])
    universe = Universe(filename)
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)


if __name__ == "__main__":
    main()
