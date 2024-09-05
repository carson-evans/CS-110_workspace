# Accepts a sequence of strings from standard input; and writes the strings in reverse order to
# standard output.

from stack import Stack
import stdio


# Entry point.
def main():
    stack = Stack()
    while not stdio.isEmpty():
        stack.push(stdio.readString())
    for s in stack:
        stdio.write(s + " ")
    stdio.writeln()


if __name__ == "__main__":
    main()
