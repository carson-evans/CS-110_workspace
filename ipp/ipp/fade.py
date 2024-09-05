# Accepts sourceFile (str), targetFile (str), and n (int) as command-line arguments; reads images
# from sourceFile and targetFile; over the course of n frames, gradually replaces the image from
# sourceFile with the image from targetFile; and displays each intermediate image using standard
# draw.

from color import Color
from picture import Picture
import stddraw
import sys


# Entry point.
def main():
    sourceFile = sys.argv[1]
    targetFile = sys.argv[2]
    n = int(sys.argv[3])
    source = Picture(sourceFile)
    target = Picture(targetFile)
    width = source.width()
    height = source.height()
    stddraw.setCanvasSize(width, height)
    picture = Picture(width, height)
    for i in range(n + 1):
        for col in range(width):
            for row in range(height):
                c0 = source.get(col, row)
                cn = target.get(col, row)
                alpha = i / n
                c = _blend(c0, cn, alpha)
                picture.set(col, row, c)
        stddraw.picture(picture)
        stddraw.show(1000)
    stddraw.show()


# Returns a new Color object which blends Color objects c1 and c2 using alpha as the blending
# factor.
def _blend(c1, c2, alpha):
    r = (1 - alpha) * c1.getRed() + alpha * c2.getRed()
    g = (1 - alpha) * c1.getGreen() + alpha * c2.getGreen()
    b = (1 - alpha) * c1.getBlue() + alpha * c2.getBlue()
    return Color(int(r), int(g), int(b))


if __name__ == "__main__":
    main()
