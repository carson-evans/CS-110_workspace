# Accepts filename (str) as command-line argument; reads an image from a file with that name; and
# renders a gray scale version of that image.

from picture import Picture
import stddraw
import sys


# Entry point.
def main():
    filename = sys.argv[1]
    picture = Picture(filename)
    for col in range(picture.width()):
        for row in range(picture.height()):
            pixel = picture.get(col, row)
            gray = pixel.toGray()
            picture.set(col, row, gray)
    stddraw.setCanvasSize(picture.width(), picture.height())
    stddraw.picture(picture)
    stddraw.show()


if __name__ == "__main__":
    main()
