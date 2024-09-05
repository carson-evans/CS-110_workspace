# A data type to represent an undirected symbol graph.

from bag import Bag
from instream import InStream
from symboltable import SymbolTable
import stdio
import sys


class Graph:
    # Constructs a graph from the given file using the specified delimiter.
    def __init__(self, filename, delimiter=None):
        self._adj = SymbolTable()  # maps each vertex to its neighbors
        self._e = 0  # number of edges in graph
        inStream = InStream(filename)
        while inStream.hasNextLine():
            line = inStream.readLine()
            names = line.split(delimiter)
            for i in range(1, len(names)):
                self.addEdge(names[0], names[i])

    # Adds an undirected edge between vertices v and w in this graph.
    def addEdge(self, v, w):
        if v not in self._adj:
            self._adj[v] = Bag()
        self._adj[v].add(w)
        if w not in self._adj:
            self._adj[w] = Bag()
        self._adj[w].add(v)
        self._e += 1

    # Returns the number of vertices in this graph.
    def countV(self):
        return len(self._adj)

    # Returns the number of edges in this graph.
    def countE(self):
        return self._e

    # Returns the degree of vertex v in this graph.
    def degree(self, v):
        return len(self._adj[v])

    # Returns the vertices adjacent to vertex v in this graph, as an iterable object.
    def adjacentTo(self, v):
        return self._adj[v]

    # Returns all the vertices in this graph, as an iterable object.
    def vertices(self):
        return self._adj.keys()


# Unit tests the data type.
def _main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    v = sys.argv[3]
    graph = Graph(filename, delimiter)
    stdio.writeln("V: " + str(graph.countV()))
    stdio.writeln("E: " + str(graph.countE()))
    stdio.write("adj(" + v + "): ")
    for w in graph.adjacentTo(v):
        stdio.write(w + " ")
    stdio.writeln()


if __name__ == "__main__":
    _main()
