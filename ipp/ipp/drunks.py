# Accepts n (int), steps (int), and stepSize (float) as command-line arguments; creates n Turtle
# objects; and has the turtles take steps random steps, each of size stepSize.

from turtle import Turtle
import stdarray
import stddraw
import stdrandom
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    steps = int(sys.argv[2])
    stepSize = float(sys.argv[3])
    turtles = stdarray.create1D(n, None)
    for i in range(n):
        x = stdrandom.uniformFloat(0.0, 1.0)
        y = stdrandom.uniformFloat(0.0, 1.0)
        theta = stdrandom.uniformFloat(0.0, 360.0)
        turtles[i] = Turtle(x, y, theta)
    stddraw.setPenRadius(0.0)
    for i in range(steps):
        for turtle in turtles:
            theta = stdrandom.uniformFloat(0.0, 360.0)
            turtle.turnLeft(theta)
            turtle.goForward(stepSize)
            stddraw.show(0.0)
    stddraw.show()


if __name__ == "__main__":
    main()
