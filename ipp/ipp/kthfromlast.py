# Accepts k (int) as command-line argument and a sequence of strings from standard input; and writes
# the kth string from the end to standard output.

from queuex import Queue
import stdio
import sys


# Entry point.
def main():
    k = int(sys.argv[1])
    queue = Queue()
    while not stdio.isEmpty():
        queue.enqueue(stdio.readString())
    n = len(queue)
    for i in range(n - k):
        queue.dequeue()
    stdio.writeln(queue.peek())


if __name__ == "__main__":
    main()
