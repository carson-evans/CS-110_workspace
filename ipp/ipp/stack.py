# An iterable data type to represent the Last-In-First-Out (LIFO) stack data structure.

import stdio


class Stack:
    # Initializes an empty stack.
    def __init__(self):
        self._first = None  # top of the stack
        self._n = 0  # number of items in the stack

    # Returns True if this stack is empty, and False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in this stack.
    def __len__(self):
        return self._n

    # Adds item to the top of this stack.
    def push(self, item):
        oldFirst = self._first
        self._first = Stack.Node()
        self._first._item = item
        self._first._next = oldFirst
        self._n += 1

    # Returns the item at the top of this stack.
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self._first._item

    # Removes and returns the item at the top of this stack.
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        item = self._first._item
        self._first = self._first._next
        self._n -= 1
        return item

    # Returns a string representation of this stack.
    def __str__(self):
        s = ""
        for item in self:
            s += item + ", "
        return s + "[]" if self.isEmpty() else "[" + s[:len(s) - 2] + "]"

    # Returns an iterator that iterates over the items in this stack.
    def __iter__(self):
        return Stack.StackIterator(self._first)

    # A data type representing a linked-list of nodes. Each node contains an item and a reference
    # to the next node in the list.
    class Node:
        def __init__(self):
            self._item = None
            self._next = None

    # An iterator that iterates over the items in a stack.
    class StackIterator:
        # Constructs an iterator.
        def __init__(self, first):
            self._current = first

        # Returns the next item in the stack if there is one, and raises StopIteration otherwise.
        def __next__(self):
            if self._current == None:
                raise StopIteration
            item = self._current._item
            self._current = self._current._next
            return item


# Unit tests the data type.
def _main():
    stack = Stack()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != "-":
            stack.push(item)
        elif not stack.isEmpty():
            stdio.write(str(stack.peek()) + " ")
            stack.pop()
    stdio.writeln()
    stdio.writeln(str(len(stack)) + " items left in the stack")
    stdio.writeln(stack)


if __name__ == "__main__":
    _main()
