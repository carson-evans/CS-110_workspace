# An iterable data type to represent the First-In-First-Out (FIFO) queue data structure.

import stdio


class Queue:
    # Initializes an empty queue.
    def __init__(self):
        self._first = None  # front of the queue
        self._last = None  # back of the queue
        self._n = 0  # number of items in the queue

    # Returns True if this queue is empty, and False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in this queue.
    def __len__(self):
        return self._n

    # Adds item to the end of this queue.
    def enqueue(self, item):
        oldLast = self._last
        self._last = Queue.Node()
        self._last._item = item
        if self.isEmpty():
            self._first = self._last
        else:
            oldLast._next = self._last
        self._n += 1

    # Returns the item at the front of this queue.
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self._first._item

    # Removes and returns the item at the front of this queue.
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self._first._item
        self._first = self._first._next
        self._n -= 1
        if self.isEmpty():
            self._last = self._first
        return item

    # Returns a string representation of this queue.
    def __str__(self):
        s = ""
        for item in self:
            s += item + ", "
        return s + "[]" if self.isEmpty() else "[" + s[:len(s) - 2] + "]"

    # Returns an iterator that iterates over the items in this queue.
    def __iter__(self):
        return Queue.QueueIterator(self._first)

    # A data type representing a linked-list of nodes. Each node contains an item and a reference
    # to the next node in the list.
    class Node:
        def __init__(self):
            self._item = None
            self._next = None

    # An iterator that iterates over the items in a queue.
    class QueueIterator:
        # Constructs an iterator.
        def __init__(self, first):
            self._current = first

        # Returns the next item in the queue if there is one, and raises StopIteration otherwise.
        def __next__(self):
            if self._current == None:
                raise StopIteration
            item = self._current._item
            self._current = self._current._next
            return item


# Unit tests the data type.
def _main():
    queue = Queue()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != "-":
            queue.enqueue(item)
        elif not queue.isEmpty():
            stdio.write(str(queue.peek()) + " ")
            queue.dequeue()
    stdio.writeln()
    stdio.writeln(str(len(queue)) + " items left in the queue")
    stdio.writeln(queue)


if __name__ == "__main__":
    _main()
