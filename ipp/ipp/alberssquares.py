# Accepts r1 (int), g1 (int), b1 (int), r2 (int), g2 (int), and b2 (int) as command-line
# arguments; and draws using standard draw Albers' squares with colors (r1, g1, b1) and (r2, g2,
# b2).

from color import Color
import stddraw
import sys


# Entry point.
def main():
    r1 = int(sys.argv[1])
    g1 = int(sys.argv[2])
    b1 = int(sys.argv[3])
    r2 = int(sys.argv[4])
    g2 = int(sys.argv[5])
    b2 = int(sys.argv[6])
    c1 = Color(r1, g1, b1)
    c2 = Color(r2, g2, b2)
    stddraw.setCanvasSize(512, 256)
    stddraw.setYscale(0.25, 0.75)
    stddraw.setPenColor(c1)
    stddraw.filledSquare(0.25, 0.5, 0.2)
    stddraw.setPenColor(c2)
    stddraw.filledSquare(0.25, 0.5, 0.1)
    stddraw.setPenColor(c2)
    stddraw.filledSquare(0.75, 0.5, 0.2)
    stddraw.setPenColor(c1)
    stddraw.filledSquare(0.75, 0.5, 0.1)
    stddraw.show()


if __name__ == "__main__":
    main()
