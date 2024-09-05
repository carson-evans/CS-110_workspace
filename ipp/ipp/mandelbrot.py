# Accepts xc (float), yc (float), and size (float) as command-line arguments; and draws using
# standard draw the size-by-size region of the Mandelbrot set, centered at (xc, yc).

from color import Color
from complex import Complex
from picture import Picture
import stddraw
import sys


# Entry point.
def main():
    xc = float(sys.argv[1])
    yc = float(sys.argv[2])
    size = float(sys.argv[3])
    N = 512
    ITERATIONS = 255
    picture = Picture(N, N)
    for col in range(N):
        for row in range(N):
            x0 = xc - size / 2 + size * col / N
            y0 = yc - size / 2 + size * row / N
            z0 = Complex(x0, y0)
            gray = ITERATIONS - _mandel(z0, ITERATIONS)
            color = Color(gray, gray, gray)
            picture.set(col, N - 1 - row, color)
    stddraw.setCanvasSize(N, N)
    stddraw.picture(picture)
    stddraw.show()


# Returns the number of iterations to check if z0 is in the Mandelbrot set.
def _mandel(z0, iterations):
    z = z0
    for i in range(iterations):
        if abs(z) > 2.0:
            return i
        z = z * z + z0
    return iterations


if __name__ == "__main__":
    main()
