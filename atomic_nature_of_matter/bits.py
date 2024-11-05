import stdio
import sys


# Entry point. [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writef("zeros = %d, ones = %d, total = %d\n", _zeros(s), _ones(s), len(s))


# Return the number of zeros in s.
def _zeros(s):
    # Base case
    if s == "":
        return 0
    else:
        # If first char of s is a 0,
        if s[0] == "0":
            return 1 + _zeros(s[1 :])
        return _zeros(s[1 :])

# Return the number of ones in s.
def _ones(s):
    # Base case
    if s == "":
        return 0
    else:
        # If first char of s is a 1,
        if s[0] == "1":
            return 1 + _ones(s[1 :])
        else:
            return _ones(s[1 :])

if __name__ == "__main__":
    main()
