# Accepts filename (str) and n (int) as command-line arguments; and splits the file whose name is
# filename.csv, by field, into n files named filename1.txt, filename2.txt, etc.

from instream import InStream
from outstream import OutStream
import stdarray
import sys


# Entry point.
def main():
    filename = sys.argv[1]
    n = int(sys.argv[2])
    outStreams = stdarray.create1D(n, None)
    for i in range(n):
        outStreams[i] = OutStream(filename + str(i + 1) + ".txt")
    inStream = InStream(filename + ".csv")
    while inStream.hasNextLine():
        line = inStream.readLine()
        fields = line.split(",")
        for i in range(n):
            outStreams[i].writeln(fields[i])


if __name__ == "__main__":
    main()
