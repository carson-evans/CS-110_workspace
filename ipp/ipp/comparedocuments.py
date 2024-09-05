# Accepts k (int), d (int), and path (str) as command-line arguments; reads a document list
# from standard input; computes d-dimensional profiles based on k-gram frequencies for all those
# documents under the path directory; and writes to standard output a matrix of similarity measures
# between all pairs of documents.

from instream import InStream
from sketch import Sketch
import stdarray
import stdio
import sys


# Entry point.
def main():
    k = int(sys.argv[1])
    d = int(sys.argv[2])
    path = sys.argv[3]
    filenames = stdio.readAllStrings()
    n = len(filenames)
    sketches = stdarray.create1D(n, None)
    for i in range(n):
        inStream = InStream(path + "/" + filenames[i])
        text = inStream.readAll()
        sketches[i] = Sketch(text, k, d)
    stdio.write("    ")
    for filename in filenames:
        stdio.writef("%8.4s", filename)
    stdio.writeln()
    for i in range(n):
        stdio.writef("%.4s", filenames[i])
        for j in range(n):
            stdio.writef("%8.2f", sketches[i].similarTo(sketches[j]))
        stdio.writeln()


if __name__ == "__main__":
    main()
