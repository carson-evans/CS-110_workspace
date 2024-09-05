# Accepts n (int) as command-line argument; and writes to standard output the instructions to move n
# Towers of Hanoi disks to the left.

import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    _moves(n, True)


# Writes to standard output the instructions to move n Towers of Hanoi disks to the left (if
# parameter left is True) or to the right (if parameter left is False).
def _moves(n, left):
    if n == 0:
        return
    _moves(n - 1, not left)
    if left:
        stdio.writeln(str(n) + " left")
    else:
        stdio.writeln(str(n) + " right")
    _moves(n - 1, not left)


if __name__ == "__main__":
    main()
