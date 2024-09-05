#  Accepts filename (str), delimiter (str), and s (str) as command-line arguments; and query
#  vertices from standard input; constructs a graph using filename, delimiter, and s; and
#  for each query vertex, writes to standard output the shortest path between the source vertex s
#  and the query vertex, and the distance between the two.

from graph import Graph
from pathfinder import PathFinder
import stdio
import sys


def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    s = sys.argv[3]
    graph = Graph(filename, delimiter)
    pf = PathFinder(graph, s)
    while stdio.hasNextLine():
        t = stdio.readLine()
        if pf.hasPathTo(t):
            distance = pf.distanceTo(t)
            for v in pf.pathTo(t):
                stdio.writeln("   " + v)
            stdio.writeln("distance: " + str(distance))
        else:
            stdio.writeln("\"" + s + "\" is not connected to \"" + t + "\"")


if __name__ == "__main__":
    main()
