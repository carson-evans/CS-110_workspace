import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture

# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        self._blobs = []  # List to store all blobs found
        width = pic.width()
        height = pic.height()
        # Create a 2D boolean array to mark visited pixels
        self._marked = stdarray.create2D(width, height, False)
        # Iterate over each pixel in the picture
        for i in range(width):
            for j in range(height):
                # If pixel (i, j) is unvisited and luminance is >= tau, start a new blob
                if not self._marked[i][j]:
                    if luminance(pic.get(i, j)) >= tau:
                        blob = Blob()
                        self._findBlob(pic, tau, i, j, self._marked, blob)
                        # If the blob has mass (pixels), add it to the list
                        if blob.mass() > 0:
                            self._blobs.append(blob)

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        beads = []
        for blob in self._blobs:
            if blob.mass() >= pixels:
                beads.append(blob)
        return beads

    # Identifies a blob using depth-first search.
    # Parameters: pic (Picture), tau (float), i (int), j (int),
    # marked (2D list of bool), blob (Blob)
    def _findBlob(self, pic, tau, i, j, marked, blob):
        width = pic.width()
        height = pic.height()
        # Check if the pixel is out of bounds
        if i < 0 or i >= width or j < 0 or j >= height:
            return
        # Check if the pixel has already been visited
        if marked[i][j]:
            return
        # Check if the pixel's luminance is below the threshold
        if luminance(pic.get(i, j)) < tau:
            return
        # Mark the pixel as visited
        marked[i][j] = True
        # Add the pixel to the blob
        blob.add(i, j)
        # Recursively search neighboring pixels (N, E, S, W)
        self._findBlob(pic, tau, i, j - 1, marked, blob)  # North
        self._findBlob(pic, tau, i + 1, j, marked, blob)  # East
        self._findBlob(pic, tau, i, j + 1, marked, blob)  # South
        self._findBlob(pic, tau, i - 1, j, marked, blob)  # West

# Function to compute the luminance of a color
def luminance(color):
    r = color.getRed()
    g = color.getGreen()
    b = color.getBlue()
    # Use the standard formula for luminance
    return 0.299 * r + 0.587 * g + 0.114 * b

# Unit tests the data type [DO NOT EDIT].
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef("%d Beads:\n", len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef("%d Blobs:\n", len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))

if __name__ == "__main__":
    _main()
