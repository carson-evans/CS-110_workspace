# An iterable data type to represent the bag data structure.

import stdio


class Bag:
    # Initializes an empty bag.
    def __init__(self):
        self._first = None  # front of the bag
        self._n = 0  # number of items in the bag

    # Returns True if this bag is empty, and False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in this bag.
    def __len__(self):
        return self._n

    # Adds item to this bag.
    def add(self, item):
        oldFirst = self._first
        self._first = Bag.Node()
        self._first._item = item
        self._first._next = oldFirst
        self._n += 1

    # Returns a string representation of this bag.
    def __str__(self):
        s = ""
        for item in self:
            s += item + ", "
        return s + "[]" if self.isEmpty() else "[" + s[:len(s) - 2] + "]"

    # Returns an iterator that iterates over the items in this bag.
    def __iter__(self):
        return Bag.BagIterator(self._first)

    # A data type representing a linked-list of nodes. Each node contains an item and a reference
    # to the next node in the list.
    class Node:
        def __init__(self):
            self._item = None
            self._next = None

    # An iterator that iterates over the items in a bag.
    class BagIterator:
        # Constructs an iterator.
        def __init__(self, first):
            self._current = first

        # Returns the next item in the bag if there is one, and raises StopIteration otherwise.
        def __next__(self):
            if self._current == None:
                raise StopIteration
            item = self._current._item
            self._current = self._current._next
            return item


# Unit tests the data type.
def _main():
    bag = Bag()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != "-":
            bag.add(item)
    stdio.writeln(str(len(bag)) + " items in the bag")
    stdio.writeln(bag)


if __name__ == "__main__":
    _main()
