# A data type to represent paths within an undirected symbol graph from a fixed source vertex.

from graph import Graph
from queuex import Queue
from stack import Stack
from symboltable import SymbolTable
import stdio
import sys


class PathFinder:
    # Constructs a path finder given the graph and source vertex.
    def __init__(self, graph, s):
        self._graph = graph  # the graph
        self._s = s  # the source vertex
        self._distTo = SymbolTable()  # maps a vertex to its distance from source
        self._edgeTo = SymbolTable()  # maps a vertex to previous vertex on path
        queue = Queue()
        queue.enqueue(s)
        self._distTo[s] = 0
        while not queue.isEmpty():
            v = queue.dequeue()
            for w in graph.adjacentTo(v):
                if w not in self._distTo:
                    queue.enqueue(w)
                    self._distTo[w] = 1 + self._distTo[v]
                    self._edgeTo[w] = v

    # Returns the distance of vertex v from the source vertex.
    def distanceTo(self, v):
        return self._distTo[v]

    # Returns True if there is a path to vertex v from the source vertex, and False otherwise.
    def hasPathTo(self, v):
        return v in self._distTo

    # Returns the path to vertex v from the source vertex.
    def pathTo(self, v):
        path = Stack()
        while v != None:
            path.push(v)
            v = self._edgeTo[v]
        return path

    # Returns a string representation of this object.
    def __str__(self):
        s = ""
        for t in self._graph.vertices():
            if self.hasPathTo(t):
                s += self._s + " -> " + t + ": "
                for v in self.pathTo(t):
                    s += v + " "
                s += "(" + str(self.distanceTo(t)) + ")\n"
        return s.strip()


# Unit tests the data type.
def _main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    s = sys.argv[3]
    graph = Graph(filename, delimiter)
    pf = PathFinder(graph, s)
    stdio.writeln(pf)


if __name__ == "__main__":
    _main()
