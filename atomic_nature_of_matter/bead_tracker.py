import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture

def main():
    # Check command-line arguments
    if len(sys.argv) < 5:
        stdio.writeln("Usage: python bead_tracker.py <p> <tau> <delta> <image1> <image2> ...")
        sys.exit(1)

    # Read command-line arguments
    p = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    # List of image filenames
    filenames = sys.argv[4:]

    # Process the first image to get initial beads
    prev_pic = Picture(filenames[0])
    prev_bf = BlobFinder(prev_pic, tau)
    prev_beads = prev_bf.getBeads(p)

    # Process each subsequent image
    for i in range(1, len(filenames)):
        # Read the next image
        curr_pic = Picture(filenames[i])
        curr_bf = BlobFinder(curr_pic, tau)
        curr_beads = curr_bf.getBeads(p)

        # For each bead in the current image, find the closest bead in the previous image
        for bead2 in curr_beads:
            min_distance = float('inf')
            for bead1 in prev_beads:
                distance = bead2.distanceTo(bead1)
                if distance < min_distance:
                    min_distance = distance
            # If the minimum distance is within delta, output it
            if min_distance <= delta:
                stdio.writef("%.4f\n", min_distance)
        # Add a blank line after processing each pair, except possibly the last one
        if i < len(filenames) - 1:
            stdio.writeln()
        # Update previous beads for the next iteration
        prev_beads = curr_beads

if __name__ == "__main__":
    main()
